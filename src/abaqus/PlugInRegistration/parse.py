from __future__ import annotations

import re
import textwrap
from pathlib import Path
from typing import Any, Callable, Type

from pydantic import BaseModel

python_types = {
    "String": str,
    "Int": int,
    "Float": float,
    "Bool": bool,
    "Function": Callable,
    "Any": Any,
    "void*": Any,
    "AFXTransition::Operator": "Operator",
    "Type": Type,
}


class_templates = '''\
{imports}


class {class_name}:
    """{description}"""
    
{methods}
'''


signature_templates = """def {method_name}({arguments}):"""


method_templates = '''\
def {method_name}({arguments}):
    """{description}
    
    Parameters
    ----------
{parameters}
    """
'''


method_no_arguments_templates = '''\
def {method_name}({arguments}):
    """{description}"""
'''


parameter_templates = """\
{parameter_name} : {parameter_type}
    {parameter_description}\
"""


class Argument(BaseModel):
    name: str
    type: str
    description: str
    required: bool
    default: str | None = None

    def render_parameter(self) -> str:
        return parameter_templates.format(
            parameter_name=self.name,
            parameter_type=self.type,
            parameter_description=self.description,
        )


class Method(BaseModel):
    name: str
    description: str
    arguments: dict[str, Argument]

    def render_parameters(self) -> str:
        return "\n".join([argument.render_parameter() for argument in self.arguments.values()])

    def render_arguments(self) -> str:
        arguments = [
            "self",
            ", ".join(
                [
                    f"{name}: {argument.type}"
                    if argument.default is None
                    else f"{name}: {argument.type} = {argument.default}"
                    for name, argument in self.arguments.items()
                ]
            ),
        ]
        if "" in arguments:
            arguments.remove("")
        return ", ".join(arguments)

    def render_method(self) -> str:
        if not self.arguments:
            return textwrap.indent(
                method_no_arguments_templates.format(
                    method_name=self.name,
                    arguments=self.render_arguments(),
                    description=self.description,
                ),
                " " * 4,
            )
        else:
            return textwrap.indent(
                method_templates.format(
                    method_name=self.name,
                    arguments=self.render_arguments(),
                    description=self.description,
                    parameters=textwrap.indent(self.render_parameters(), " " * 4),
                ),
                " " * 4,
            )


class Flag(BaseModel):
    pass


class Class(BaseModel):
    imports: list[str] = []
    name: str
    description: str
    methods: dict[str, Method]
    flags: list[Flag] = []

    def render_methods(self) -> str:
        return "\n".join([method.render_method() for method in self.methods.values()])

    def render_class(self) -> str:
        return class_templates.format(
            imports="\n".join(self.imports),
            class_name=self.name,
            description=self.description,
            methods=self.render_methods(),
        )

    def render(self, file: str | Path):
        with open(file, "w", encoding="utf-8") as file:
            file.write(self.render_class())


missing_classes = [
    "SOCKET",
    "FXRGB",
]
constants = {"FONT_PROPORTIONAL": 0}
method_pattern = re.compile(r"(\w+)\((.*)\)")
flag_pattern = re.compile(r".*\*\*(\w+)\*\*.*")
for md in Path(".").glob("*.md"):
    class_name = md.stem
    if " " in class_name:
        continue

    with md.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    sections, current_section = [], []
    for line in lines:
        line = re.sub(r"!\[.*]\(.*\)", "", line)
        if not line.strip():
            continue
        if line.startswith("#"):
            sections.append(current_section)
            current_section = [line.lstrip("#").strip()]
        else:
            current_section.append(line.strip())
    sections.append(current_section)

    heading: str
    paragraphs: list[str]
    data = {
        "description": sections[0][0],
        "name": class_name,
        "methods": {},
        "imports": ["from __future__ import annotations"],
    }
    for heading, *paragraphs in sections[1:]:
        if method_pattern.match(heading):
            # Parse heading
            method_name = method_pattern.match(heading).group(1)
            if method_name == class_name:
                method_name = "__init__"
            data["methods"][method_name] = {"name": method_name}

            # Parse description and parameters
            descriptions, parameters, current_is_description = [], [], True
            for paragraph in paragraphs:
                paragraph = paragraph.replace("\\", "")
                if paragraph.startswith("|"):
                    current_is_description = False
                    parameters.append(paragraph)
                    continue
                elif current_is_description:
                    descriptions.append(paragraph)
            data["methods"][method_name]["description"] = " ".join(descriptions)
            data["methods"][method_name]["arguments"] = {}
            for parameter in parameters[1:]:
                try:
                    name, type, default, description = parameter.strip("|").split("|")
                except ValueError as e:
                    print(f"Error parsing {class_name} {method_name} {parameter}")
                    continue
                name, type, default, description = name.strip(), type.strip(), default.strip(), description.strip()
                default = default.replace("\\", "") if default != "" else None
                required = default is None
                python_type = type
                if isinstance(default, str) and default.isupper() and default.isidentifier() and default != "SIMULIA":
                    constants[default] = 0
                    data["imports"].append(f"from .constants import {default}")
                if "SOCKET" in type:
                    data["imports"].append("from .SOCKET import SOCKET")
                elif "FXRGB" in type:
                    data["imports"].append("from .FXRGB import FXRGB")
                if type in python_types:
                    python_type = python_types[type]
                    python_type = getattr(python_type, "__name__", python_type)
                    if python_type == "Callable":
                        data["imports"].append("from typing import Callable")
                    elif python_type == "Any":
                        data["imports"].append("from typing import Any")
                    elif python_type == "Type":
                        data["imports"].append("from typing import Type")
                    elif python_type == "str" and default is not None:
                        default = f'"{default}"'
                elif type.startswith(("AFX", "FX")):
                    if type == class_name:
                        python_type = "Self"
                        data["imports"].append(f"from typing_extensions import Self")
                    else:
                        data["imports"].append(f"from .{type} import {type}")
                        if not Path(f"{type}.py").exists():
                            missing_classes.append(type)
                # else:
                #     python_type = f'"{type}"'
                if default == "None":
                    python_type = f"{python_type} | None"
                data["methods"][method_name]["arguments"][name] = {
                    "name": name,
                    "type": python_type,
                    "description": description,
                    "required": required,
                    "default": default,
                }
        else:
            for paragraph in paragraphs:
                if flag_pattern.match(paragraph):
                    name = flag_pattern.match(paragraph).group(1)
                    constants[name] = 0
    data["imports"] = list(set(data["imports"]))
    if "from __future__ import annotations" in data["imports"]:
        data["imports"].remove("from __future__ import annotations")
        data["imports"].insert(0, "from __future__ import annotations")
    cls = Class(**data)
    cls.render(f"{class_name}.py")

constants = {key: constants[key] for key in sorted(constants)}
with open("constants.py", "w", encoding="utf-8") as f:
    for name, value in constants.items():
        f.write(f"{name} = {value}\n")

for cls in missing_classes:
    with open(f"{cls}.py", "w", encoding="utf-8") as f:
        f.write(f"class {cls}:\n    ...")
