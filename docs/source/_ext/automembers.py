from __future__ import annotations

import importlib
import inspect
import pkgutil
from types import ModuleType

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.statemachine import StringList
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective


class AutoMembers(SphinxDirective):
    required_arguments = 1
    option_spec = {
        "recursive": directives.flag,
        "exclude": directives.unchanged,
    }
    _excluded_members: list[str] = None

    @property
    def module_name(self) -> str:
        return self.arguments[0]

    @property
    def excluded_members(self) -> list[str]:
        if self._excluded_members is None:
            self._excluded_members = [member.strip() for member in self.options.get("exclude", "").split(",")]
        return self._excluded_members

    def run(self):
        return [node for member in self.get_members(self.module_name).values() for node in self.nodes_from_rst(member)]

    def nodes_from_rst(self, rst: list[str]) -> list[nodes.Node]:
        wrapper = nodes.paragraph()
        self.state.nested_parse(StringList(rst), 0, wrapper)
        return wrapper.children

    def should_include(self, obj: object) -> bool:
        module_or_name = getattr(obj, "__module__", obj.__name__)
        return (
            self.module_name == module_or_name
            or f"{self.module_name}." in module_or_name
            and obj.__name__ not in self.excluded_members
        )

    def get_members(self, module: str | ModuleType) -> dict[str, list[str]]:
        autodoc_options = self.env.config.automembers_autodoc_options
        members = {}
        try:
            # If the module is already imported, use it directly
            module = importlib.import_module(module)
            # Class members
            classes = [
                member for member in inspect.getmembers(module, inspect.isclass) if self.should_include(member[1])
            ]
            class_members = {
                cls.__qualname__: [f".. currentmodule:: {module.__name__}"]
                + [f".. autoclass:: {cls.__qualname__}"]
                + [f"    {option}" for option in autodoc_options]
                for name, cls in classes
                if cls.__qualname__ not in members
            }
            members.update(class_members)
            # Function members
            functions = [
                member for member in inspect.getmembers(module, inspect.isfunction) if self.should_include(member[1])
            ]
            function_members = {
                func.__qualname__: [f".. currentmodule:: {module.__name__}"]
                + [f".. autofunction:: {func.__qualname__}"]
                for name, func in functions
                if func.__qualname__ not in members
            }
            members.update(function_members)
            # submodule members
            if "recursive" in self.options and "__path__" in dir(module):
                for moduleinfo in pkgutil.iter_modules(module.__path__):
                    fullname = f"{module.__name__}.{moduleinfo.name}"
                    if self.module_name not in fullname or fullname == self.module_name:
                        continue
                    members.update(self.get_members(fullname))
            return members
        except ImportError:
            return members


def setup(app: Sphinx) -> dict:
    app.add_directive("automembers", AutoMembers)
    app.add_config_value("automembers_recursive", False, "env")
    app.add_config_value("automembers_autodoc_options", [], "env")

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
