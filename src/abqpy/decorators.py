import re
from functools import partial
from typing import Tuple

from . import __version__ as version


def class_or_module_link(
    type: str,
    class_or_module_name: str,
    prefix="",
    suffix="",
    label=None,
) -> Tuple[str, str]:
    """Generate a link to the Abaqus class documentation.

    Parameters
    ----------
    type : str
        Type of the object, 'class' or 'module'.
    class_or_module_name : str
        The name of the class or module.
    prefix : str
        The prefix to the class or module name.
    suffix : str
        The suffix to the class name.
    label : str
        The label to use for the link.

    Returns
    -------
    str
        The link to the documentation.
    str
        The link with label.
    """
    if label is None:
        label = class_or_module_name
    module_name = f"{type if type == 'module' else ''}{class_or_module_name.lower()}"
    link = (
        f"https://help.3ds.com/{version[:4]}/English/DSSIMULIA_Established/SIMACAEKERRefMap/"
        f"simaker-c-{prefix}{module_name}{suffix}pyc.htm?contextscope=all"
    )
    return link, f"Check `{label} on help.3ds.com/{version[:4]} <{link}>`__."


def method_or_function_link(
    type: str,
    class_or_module_name: str,
    method_or_function_name: str,
    prefix="",
    suffix="",
    label=None,
) -> Tuple[str, str]:
    """Generate a link to the Abaqus function documentation.

    Parameters
    ----------
    type : str
        Type of the object, 'method' or 'function'.
    class_or_module_name : str
        The name of the module.
    method_or_function_name : str
        The name of the function.
    prefix : str
        The prefix to the class or module name.
    suffix : str
        The suffix to the class name.
    label : str
        The label to use for the link.

    Returns
    -------
    str
        The link to the documentation.
    str
        The link with label.
    """
    # For methods that start with a capital letter, the link is to the corresponding class documentation.
    if method_or_function_name[0].isupper():
        return class_or_module_link("class", method_or_function_name, prefix, suffix, method_or_function_name)
    class_name = f"{type if type == 'function' else ''}{class_or_module_name.lower()}"
    function_prefix = prefix if type == "function" else ""
    if type == "class" and method_or_function_name == "__init__":
        method_or_function_name = class_or_module_name
    link = (
        f"https://help.3ds.com/{version[:4]}/English/DSSIMULIA_Established/SIMACAEKERRefMap/"
        f"simaker-c-{prefix}{class_name}{suffix}pyc.htm?contextscope=all"
        f"#simaker-{function_prefix}{class_name}{method_or_function_name.lower()}pyc"
    )
    if method_or_function_name == class_or_module_name and type == "class":
        signature = f"{class_or_module_name}()"
    else:
        signature = f"{class_or_module_name}.{method_or_function_name}()"
    if label is None:
        label = signature
    return link, f"Check `{label} on help.3ds.com/{version[:4]} <{link}>`__."


def add_link_in_class_or_module_docstring(
    type: str,
    class_or_module_name: str,
    docstring: str,
    prefix="",
    suffix="",
    label=None,
) -> str:
    """Add a link to the Abaqus documentation to the docstring for classes or modules.

    Parameters
    ----------
    type : str
        Type of the object, 'class' or 'module'.
    class_or_module_name : str
        The name of the class or module.
    docstring : str
        The docstring.
    prefix : str
        The prefix to the class or module name.
    suffix : str
        The suffix to the class name.
    label : str
        The label to use for the link.

    Returns
    -------
    str
        The docstring with the link to the Abaqus documentation.
    """
    if not docstring:
        return docstring
    link, link_with_label = class_or_module_link(type, class_or_module_name, prefix, suffix, label)
    return (
        docstring.rstrip()
        + "\n\n"
        + " " * (0 if type == "module" else 4)
        + ".. note::\n"
        + " " * (4 if type == "module" else 8)
        + link_with_label
    )


add_link_in_class_docstring = partial(add_link_in_class_or_module_docstring, "class")
add_link_in_module_docstring = partial(add_link_in_class_or_module_docstring, "module")


def add_link_in_method_or_function_docstring(
    type: str,
    class_or_module_name: str,
    method_or_function_name: str,
    docstring: str,
    prefix="",
    suffix="",
    label=None,
) -> str:
    """Add a link to the Abaqus documentation to the docstring for methods or functions.

    Parameters
    ----------
    type : str
        Type of the object, 'method' or 'function'.
    class_or_module_name : str
        The name of the module.
    method_or_function_name : str
        The name of the function.
    docstring : str
        The docstring.
    prefix : str
        The prefix to the class or module name.
    suffix : str
        The suffix to the class name.
    label : str
        The label to use for the link.

    Returns
    -------
    str
        The docstring with the link to the Abaqus documentation.
    """
    if not docstring:
        return docstring
    link, link_with_label = method_or_function_link(
        type, class_or_module_name, method_or_function_name, prefix, suffix, label
    )
    return re.sub(
        r"(\n\s+?)(Parameters\n\s+----------)",
        r"\1" + ".. note::\n" + " " * (8 if type == "function" else 12) + link_with_label + r"\1\2",
        docstring,
    )


add_link_in_method_docstring = partial(add_link_in_method_or_function_docstring, "method")
add_link_in_function_docstring = partial(add_link_in_method_or_function_docstring, "function")


def abaqus_function_doc(func):
    """Add a link to the Abaqus documentation to the docstring of the function."""
    module_name = func.__module__.split(".")[-1]
    func.__doc__ = add_link_in_function_docstring(
        class_or_module_name=module_name,
        method_or_function_name=func.__name__,
        docstring=func.__doc__,
        prefix="gpr" if module_name.lower().startswith("cae") else "",
        label=f"{module_name}.{func.__name__}",
    )
    return func


def _process_class_name(class_name: str) -> str:
    """Process the class name."""
    # Handle the base class case.
    if class_name.endswith("Base"):
        class_name = class_name[:-4]
    # Handle the class with a suffix.
    if class_name.endswith("Mdb"):
        class_name = "Mdb"
    if class_name.endswith("Model"):
        class_name = "Model"
    if class_name.endswith("Step"):
        class_name = "Step"
    if class_name.endswith("Assembly"):
        class_name = "Assembly"
    if class_name.endswith("Step"):
        class_name = "Step"
    if class_name.endswith("Odb"):
        class_name = "Odb"
    if class_name.endswith("Part"):
        class_name = "Part"
    return class_name


class_suffix = {
    "AdaptivityModel": "kar",
    "AssemblyModel": "asm",
    "EditMeshAssembly": "edt",
    "EditMeshPart": "edt",
    "InteractionModel": "itn",
    "MeshAssembly": "mgn",
    "MeshPart": "mgn",
    "RegionAssembly": "reg",
    "RegionPart": "reg",
}


def abaqus_method_doc(method):
    """Add a link to the Abaqus documentation to the docstring of the method."""
    if method.__name__ == "__init__":
        return method
    class_name = method.__qualname__.split(".")[0]
    method.__doc__ = add_link_in_method_docstring(
        class_or_module_name=_process_class_name(class_name),
        method_or_function_name=method.__name__,
        docstring=method.__doc__,
        prefix="gpr" if class_name.lower().startswith("cae") else "",
        suffix=class_suffix.get(class_name, ""),
        label=f"{class_name}.{method.__name__}",
    )
    return method


def abaqus_class_doc(cls):
    """Add a link to the Abaqus documentation to the docstring of the class."""
    class_name = cls.__name__
    processed_class_name = _process_class_name(class_name)
    cls.__doc__ = add_link_in_class_docstring(
        class_or_module_name=processed_class_name,
        docstring=cls.__doc__,
        prefix="gpr" if class_name.lower().startswith("cae") else "",
        suffix=class_suffix.get(class_name, ""),
        label=class_name,
    )
    return cls
