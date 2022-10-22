import re
from typing import Tuple

from . import __version__ as version

version = version[:4]


class AbaqusDoc:

    @classmethod
    def _class_or_module_link(
        cls,
        type: str,
        class_or_module_name: str,
        prefix='',
        suffix='',
        label=None,
    ) -> Tuple[str, str]:
        """Generate a link to the Abaqus class documentation.

        Parameters
        ----------
        type : 'class' or 'module'
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
        link = (f"https://help.3ds.com/{version}/English/DSSIMULIA_Established/SIMACAEKERRefMap/"
                f"simaker-c-{prefix}{module_name}{suffix}pyc.htm?contextscope=all")
        return link, f"Check `{label} on help.3ds.com/{version} <{link}>`__."

    @classmethod
    def _method_or_function_link(
        cls,
        type: str,
        class_or_module_name: str,
        method_or_function_name: str,
        prefix='',
        suffix='',
        label=None,
    ) -> Tuple[str, str]:
        """Generate a link to the Abaqus function documentation.

        Parameters
        ----------
        type : 'method' or 'function'
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
            return cls._class_or_module_link('class', method_or_function_name, prefix, suffix, method_or_function_name)
        class_name = f"{type if type == 'function' else ''}{class_or_module_name.lower()}"
        function_prefix = prefix if type == 'function' else ''
        if type == 'class' and method_or_function_name == '__init__':
            method_or_function_name = class_or_module_name
        link = (f"https://help.3ds.com/{version}/English/DSSIMULIA_Established/SIMACAEKERRefMap/"
                f"simaker-c-{prefix}{class_name}{suffix}pyc.htm?contextscope=all"
                f"#simaker-{function_prefix}{class_name}{method_or_function_name.lower()}pyc")
        if method_or_function_name == class_or_module_name and type == 'class':
            signature = f"{class_or_module_name}()"
        else:
            signature = f"{class_or_module_name}.{method_or_function_name}()"
        if label is None:
            label = signature
        return link, f"Check `{label} on help.3ds.com/{version} <{link}>`__."

    @classmethod
    def _add_link_in_class_or_module_docstring(
        cls,
        type: str,
        class_or_module_name: str,
        docstring: str,
        prefix='',
        suffix='',
        label=None,
    ) -> str:
        """Add a link to the Abaqus documentation to the docstring for classes or modules.

        Parameters
        ----------
        type : 'class' or 'module'
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
        link, link_with_label = cls._class_or_module_link(type, class_or_module_name, prefix, suffix, label)
        return (docstring.rstrip() + '\n\n' + ' ' * (0 if type == 'module' else 4) +
                '.. note::\n' + ' ' * (4 if type == 'module' else 8) + link_with_label)

    @classmethod
    def _add_link_in_method_or_function_docstring(
        cls,
        type: str,
        class_or_module_name: str,
        method_or_function_name: str,
        docstring: str,
        prefix='',
        suffix='',
        label=None,
    ) -> str:
        """Add a link to the Abaqus documentation to the docstring for methods or functions.

        Parameters
        ----------
        type : 'method' or 'function'
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
        link, link_with_label = cls._method_or_function_link(type, class_or_module_name,
                                                             method_or_function_name, prefix, suffix, label)
        return re.sub(r'(\n\s+?)(Parameters\n\s+----------)',
                      r'\1' + '.. note::\n' + ' ' * (8 if type == 'function' else 12) + link_with_label + r'\1\2',
                      docstring)

    @classmethod
    def add_link_in_class_docstring(
        cls,
        class_name: str,
        docstring: str,
        prefix='',
        suffix='',
        label=None,
    ) -> str:
        """Add a link to the Abaqus documentation to the docstring for classes.

        Parameters
        ----------
        class_name : str
            The name of the class.
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
        return cls._add_link_in_class_or_module_docstring(
            'class', class_name, docstring, prefix, suffix, label
        )

    @classmethod
    def add_link_in_module_docstring(
        cls,
        module_name: str,
        docstring: str,
        prefix='',
        suffix='',
        label=None,
    ) -> str:
        """Add a link to the Abaqus documentation to the docstring for modules.

        Parameters
        ----------
        module_name : str
            The name of the module.
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
        return cls._add_link_in_class_or_module_docstring(
            'module', module_name, docstring, prefix, suffix, label
        )

    @classmethod
    def add_link_in_function_docstring(
        cls,
        module_name: str,
        function_name: str,
        docstring: str,
        prefix='',
        suffix='',
        label=None,
    ) -> str:
        """Add a link to the Abaqus documentation to the docstring for functions.

        Parameters
        ----------
        module_name : str
            The name of the module.
        function_name : str
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
        return cls._add_link_in_method_or_function_docstring(
            'function', module_name, function_name, docstring, prefix, suffix, label
        )

    @classmethod
    def add_link_in_method_docstring(
        cls,
        class_name: str,
        method_name: str,
        docstring: str,
        prefix='',
        suffix='',
        label=None,
    ) -> str:
        """Add a link to the Abaqus documentation to the docstring for methods.

        Parameters
        ----------
        class_name : str
            The name of the class.
        method_name : str
            The name of the method.
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
        return cls._add_link_in_method_or_function_docstring(
            'method', class_name, method_name, docstring, prefix, suffix, label
        )


doc = AbaqusDoc


def abaqus_function_doc(func):
    """Add a link to the Abaqus documentation to the docstring of the function.
    """
    module_name = func.__module__.split('.')[-1]
    func.__doc__ = doc.add_link_in_function_docstring(
        module_name=module_name,
        function_name=func.__name__,
        docstring=func.__doc__,
        prefix='gpr' if module_name.lower().startswith('cae') else '',
        label=f'{module_name}.{func.__name__}',
    )
    return func


def _process_class_name(class_name: str) -> str:
    """Process the class name.
    """
    # Handle the base class case.
    if class_name.endswith('Base'):
        class_name = class_name[:-4]
    # Handle the class with a suffix.
    if class_name.endswith('Mdb'):
        class_name = 'Mdb'
    if class_name.endswith('Model'):
        class_name = 'Model'
    if class_name.endswith('Step'):
        class_name = 'Step'
    if class_name.endswith('Assembly'):
        class_name = 'Assembly'
    if class_name.endswith('Step'):
        class_name = 'Step'
    if class_name.endswith('Odb'):
        class_name = 'Odb'
    if class_name.endswith('Part'):
        class_name = 'Part'
    return class_name


class_suffix = {
    'AdaptivityModel': 'kar',
    'AssemblyModel': 'asm',
    'EditMeshAssembly': 'edt',
    'EditMeshPart': 'edt',
    'InteractionModel': 'itn',
    'MeshAssembly': 'mgn',
    'MeshPart': 'mgn',
    'RegionAssembly': 'reg',
    'RegionPart': 'reg',
}


def abaqus_method_doc(method):
    """Add a link to the Abaqus documentation to the docstring of the method.
    """
    class_name = method.__qualname__.split('.')[0]
    method.__doc__ = doc.add_link_in_method_docstring(
        class_name=_process_class_name(class_name),
        method_name=method.__name__,
        docstring=method.__doc__,
        prefix='gpr' if class_name.lower().startswith('cae') else '',
        suffix=class_suffix.get(class_name, ''),
        label=f'{class_name}.{method.__name__}',
    )
    return method


def abaqus_class_doc(cls):
    """Add a link to the Abaqus documentation to the docstring of the class.
    """
    class_name = cls.__name__
    processed_class_name = _process_class_name(class_name)
    cls.__doc__ = doc.add_link_in_class_docstring(
        class_name=processed_class_name,
        docstring=cls.__doc__,
        prefix='gpr' if class_name.lower().startswith('cae') else '',
        suffix=class_suffix.get(class_name, ''),
        label=class_name,
    )
    return cls


@abaqus_function_doc
def foo(a, b):
    """This is a test function.

    Parameters
    ----------
    a : int
        The first parameter.
    b : int
        The second parameter.
    """
    return a + b


@abaqus_class_doc
class Bar:
    """This is a test class.
    """

    @abaqus_method_doc
    def foo(self, a, b):
        """This is a test method.

        Parameters
        ----------
        a : int
            The first parameter.
        b : int
            The second parameter.
        """
        pass


def test_foo_bar():
    """
    Test the foo function.
    """
    # foo
    print('\n')
    print(foo.__name__)
    print(foo.__doc__)

    # Bar
    print(Bar.__name__)
    print(Bar.__doc__)

    # Bar.foo
    print(Bar.foo.__name__)
    print(Bar.foo.__doc__)
