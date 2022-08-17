import os
import re
import typing

import parso

from abaqus.AbaqusCAEDisplayPreferences.CaeGuiPrefs import CaeGuiPrefs


class AbaqusDocumentationLink:

    @classmethod
    def _class_or_module_link(
        cls,
        version: typing.Literal['2016', '2017', '2018', '2019', '2020', '2020', '2021', '2022'],
        type: typing.Literal['class', 'module'],
        class_or_module_name: str,
    ) -> tuple[str, str]:
        """Generate a link to the Abaqus class documentation.

        Parameters
        ----------
        version : str
            The Abaqus version.
        type : 'class' or 'module'
            Type of the object, class or module.
        class_or_module_name : str
            The name of the class or module.

        Returns
        -------
        str
            The link to the documentation.
        str
            The link with label.
        """
        name = f"{type if type == 'gprmodule' else ''}{class_or_module_name.lower()}"
        link = (f"https://help.3ds.com/{version}/English/DSSIMULIA_Established/SIMACAEKERRefMap/"
                f"simaker-c-{name}pyc.htm?contextscope=all")
        return link, f"Check `{class_or_module_name} on help.3ds.com/{version} <{link}>`_."

    @classmethod
    def _method_or_function_link(
        cls,
        version: typing.Literal['2016', '2017', '2018', '2019', '2020', '2020', '2021', '2022'],
        type: typing.Literal['class', 'module'],
        class_or_module_name: str,
        method_or_function_name: str,
    ) -> tuple[str, str]:
        """Generate a link to the Abaqus function documentation.

        Parameters
        ----------
        version : str
            The Abaqus version.
        type : 'class' or 'module'
            Type of the object, class or module.
        class_or_module_name : str
            The name of the module.
        method_or_function_name : str
            The name of the function.

        Returns
        -------
        str
            The link to the documentation.
        str
            The link with label.
        """
        name = f"{type if type == 'gprmodule' else ''}{class_or_module_name.lower()}"
        if type == 'class' and method_or_function_name == '__init__':
            method_or_function_name = class_or_module_name
        link = (f"https://help.3ds.com/{version}/English/DSSIMULIA_Established/SIMACAEKERRefMap/"
                f"simaker-c-{name}pyc.htm?contextscope=all"
                f"#simaker-{name}{method_or_function_name.lower()}pyc")
        if method_or_function_name == class_or_module_name and type == 'class':
            signature = f"{class_or_module_name}()"
        else:
            signature = f"{class_or_module_name}.{method_or_function_name}()"
        return link, f"Check `{signature} on help.3ds.com/{version} <{link}>`_."

    @classmethod
    def _add_link_in_class_or_module_docstring(
        cls,
        version: typing.Literal['2016', '2017', '2018', '2019', '2020', '2020', '2021', '2022'],
        type: typing.Literal['class', 'module'],
        class_or_module_name: str,
        docstring: str,
    ) -> str:
        """Add a link to the Abaqus documentation to the docstring for classes or modules.

        Parameters
        ----------
        version : str
            The Abaqus version.
        type : 'class' or 'module'
            Type of the object, class or module.
        class_or_module_name : str
            The name of the class or module.
        docstring : str
            The docstring.

        Returns
        -------
        str
            The docstring with the link to the Abaqus documentation.
        """
        link, link_with_label = cls._class_or_module_link(version, type, class_or_module_name)
        return docstring.rstrip() + '\n\n' + ' ' * (0 if type == 'module' else 4) + link_with_label

    @classmethod
    def _add_link_in_method_or_function_docstring(
        cls,
        version: typing.Literal['2016', '2017', '2018', '2019', '2020', '2020', '2021', '2022'],
        type: typing.Literal['class', 'module'],
        class_or_module_name: str,
        method_or_function_name: str,
        docstring: str,
    ) -> str:
        """Add a link to the Abaqus documentation to the docstring for methods or functions.

        Parameters
        ----------
        version : str
            The Abaqus version.
        type : 'class' or 'module'
            Type of the object, class or module.
        class_or_module_name : str
            The name of the module.
        method_or_function_name : str
            The name of the function.
        docstring : str
            The docstring.

        Returns
        -------
        str
            The docstring with the link to the Abaqus documentation.
        """
        link, link_with_label = cls._method_or_function_link(version, type, class_or_module_name,
                                                             method_or_function_name)
        return re.sub(r'(\n\s+?)(Parameters\n\s+----------)', r'\1' + link_with_label + r'\1\2', docstring)

    @classmethod
    def class_link(
        cls,
        version: typing.Literal['2016', '2017', '2018', '2019', '2020', '2020', '2021', '2022'],
        class_name: str,
    ) -> str:
        """Generate a link to the Abaqus class documentation.

        Parameters
        ----------
        version : str
            The Abaqus version.
        class_name : str
            The name of the class.

        Returns
        -------
        str
            The link with label.
        """
        return cls._class_or_module_link(version, 'class', class_name)[1]

    @classmethod
    def module_link(
        cls,
        version: typing.Literal['2016', '2017', '2018', '2019', '2020', '2020', '2021', '2022'],
        module_name: str,
    ) -> str:
        """Generate a link to the Abaqus module documentation.

        Parameters
        ----------
        version : str
            The Abaqus version.
        module_name : str
            The name of the module.

        Returns
        -------
        str
            The link with label.
        """
        return cls._class_or_module_link(version, 'module', module_name)[1]

    @classmethod
    def method_link(
        cls, version: typing.Literal['2016', '2017', '2018', '2019', '2020', '2020', '2021', '2022'],
        class_name: str,
        method_name: str,
    ) -> str:
        """Generate a link to the Abaqus method documentation.

        Parameters
        ----------
        version : str
            The Abaqus version.
        class_name : str
            The name of the class.
        method_name : str
            The name of the method.

        Returns
        -------
        str
            The link with label.
        """
        return cls._method_or_function_link(version, 'class', class_name, method_name)[1]

    @classmethod
    def function_link(
        cls,
        version: typing.Literal['2016', '2017', '2018', '2019', '2020', '2020', '2021', '2022'],
        module_name: str,
        function_name: str
    ) -> str:
        """Generate a link to the Abaqus function documentation.

        Parameters
        ----------
        version : str
            The Abaqus version.
        module_name : str
            The name of the module.
        function_name : str
            The name of the function.

        Returns
        -------
        str
            The link with label.
        """
        return cls._method_or_function_link(version, 'module', module_name, function_name)[1]

    @classmethod
    def add_link_in_class_docstring(
        cls,
        version: typing.Literal['2016', '2017', '2018', '2019', '2020', '2020', '2021', '2022'],
        class_name: str,
        docstring: str,
    ) -> str:
        """Add a link to the Abaqus documentation to the docstring for classes.

        Parameters
        ----------
        version : str
            The Abaqus version.
        class_name : str
            The name of the class.
        docstring : str
            The docstring.

        Returns
        -------
        str
            The docstring with the link to the Abaqus documentation.
        """
        return cls._add_link_in_class_or_module_docstring(version, 'class', class_name, docstring)

    @classmethod
    def add_link_in_module_docstring(
        cls,
        version: typing.Literal['2016', '2017', '2018', '2019', '2020', '2020', '2021', '2022'],
        module_name: str,
        docstring: str,
    ) -> str:
        """Add a link to the Abaqus documentation to the docstring for modules.

        Parameters
        ----------
        version : str
            The Abaqus version.
        module_name : str
            The name of the module.
        docstring : str
            The docstring.

        Returns
        -------
        str
            The docstring with the link to the Abaqus documentation.
        """
        return cls._add_link_in_class_or_module_docstring(version, 'module', module_name, docstring)

    @classmethod
    def add_link_in_method_docstring(
        cls,
        version: typing.Literal['2016', '2017', '2018', '2019', '2020', '2020', '2021', '2022'],
        class_name: str,
        method_name: str,
        docstring: str,
    ) -> str:
        """Add a link to the Abaqus documentation to the docstring for methods.

        Parameters
        ----------
        version : str
            The Abaqus version.
        class_name : str
            The name of the class.
        method_name : str
            The name of the method.
        docstring : str
            The docstring.

        Returns
        -------
        str
            The docstring with the link to the Abaqus documentation.
        """
        return cls._add_link_in_method_or_function_docstring(version, 'class', class_name, method_name, docstring)

    @classmethod
    def add_link_in_function_docstring(
        cls,
        version: typing.Literal['2016', '2017', '2018', '2019', '2020', '2020', '2021', '2022'],
        module_name: str,
        function_name: str,
        docstring: str,
    ) -> str:
        """Add a link to the Abaqus documentation to the docstring for functions.

        Parameters
        ----------
        version : str
            The Abaqus version.
        module_name : str
            The name of the module.
        function_name : str
            The name of the function.
        docstring : str
            The docstring.

        Returns
        -------
        str
            The docstring with the link to the Abaqus documentation.
        """
        return cls._add_link_in_method_or_function_docstring(version, 'module', module_name, function_name, docstring)

    @classmethod
    def add_link_to_source_code(
        cls,
        version: typing.Literal['2016', '2017', '2018', '2019', '2020', '2020', '2021', '2022'],
        source: str,
        module_name: str,
        force_link: bool = False,
    ) -> str:
        """Add a link to the Abaqus source code for classes.

        Parameters
        ----------
        version : str
            The Abaqus version.
        source : str
            The source code.
        module_name : str
            The name of the module.
        force_link : bool
            If True, the link will be added even if a link already exists.

        Returns
        -------
        str
            The source code with the link to the Abaqus source code.
        """
        if force_link:
            for line in re.findall(r'\n(\n\s+?Check `[\w\W]+? on help.3ds.com[\w\W]+?\n)', source):
                source = source.replace(line, '')
        tree = parso.parse(source)
        if tree:
            for child in tree.children:
                if child.type == 'classdef':
                    try:
                        docstring = re.findall(r'class \w+[\w\W]+?"""([\w\W]+?)\n\s*"""', child.get_code())[0]
                        docstring_with_link = cls.add_link_in_class_docstring(
                            version=version,
                            class_name=child.name.value,
                            docstring=docstring,
                        )
                        source = source.replace(docstring, docstring_with_link)
                    except IndexError:
                        continue
                    for cchild in child.children[-1].children:
                        if cchild.type == 'funcdef':
                            try:
                                docstring = re.findall(r'(?<=def )\w+[\w\W]+?"""([\w\W]+?)\n\s*"""',
                                                       cchild.get_code())[0]
                                if cchild.name.value.istitle():
                                    class_name = cchild.name.value
                                    docstring_with_link = cls.add_link_in_class_docstring(
                                        version=version,
                                        class_name=class_name,
                                        docstring=docstring,
                                    )
                                else:
                                    method_name = cchild.name.value
                                    docstring_with_link = cls.add_link_in_method_docstring(
                                        version=version,
                                        class_name=child.name.value,
                                        method_name=method_name,
                                        docstring=docstring,
                                    )
                                source = source.replace(docstring, docstring_with_link)
                            except IndexError:
                                continue
                elif child.type == 'funcdef':
                    try:
                        docstring = re.findall(r'(?<=def )\w+[\w\W]+?"""([\w\W]+?)\n\s*"""', child.get_code())[0]
                        func_name = child.name.value
                        docstring_with_link = cls.add_link_in_function_docstring(
                            version=version,
                            module_name=module_name,
                            function_name=func_name,
                            docstring=docstring,
                        )
                        source = source.replace(docstring, docstring_with_link)
                    except IndexError:
                        continue
        return source

    @classmethod
    def add_link_to_file(
        cls,
        version: typing.Literal['2016', '2017', '2018', '2019', '2020', '2020', '2021', '2022'],
        file_name: str,
        force_link: bool = False,
        write_to_file: bool = False,
    ) -> str:
        """Add a link to the Abaqus source code for classes.

        Parameters
        ----------
        version : str
            The Abaqus version.
        file_name : str
            The name of the file.
        force_link : bool
            If True, the link will be added even if a link already exists.
        write_to_file : bool, optional
            Write the source code to a file. The default is False.

        Returns
        -------
        str
            The source code with the link to the Abaqus source code.
        """
        file_name = file_name.replace('\\', '/')
        if not os.path.exists(file_name) or not os.path.isfile(file_name) or not file_name.endswith('.py'):
            return ''
        with open(file_name, 'r', encoding='utf-8') as f:
            source = f.read()
        source_with_link = cls.add_link_to_source_code(version, source, file_name[:-3].split('/')[-1], force_link)
        if write_to_file:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(source_with_link)
        return source_with_link


cls = AbaqusDocumentationLink


def test_docstring():
    print('\n')
    print(cls.module_link(version='2020',
                          module_name='caePrefsAccess'))
    print(cls.class_link(version='2020',
                         class_name='caeGuiPrefs'))
    print(cls.function_link(version='2020',
                            module_name='caePrefsAccess',
                            function_name='printValuesList'))
    print(cls.method_link(version='2020',
                          class_name='caeGuiPrefs',
                          method_name='saveAs'))


def test_add_docstring_to_class_or_module():
    print('\n')
    print(cls.add_link_in_class_docstring(
        version='2020',
        class_name='caeGuiPrefs',
        docstring=CaeGuiPrefs.__doc__,
    ))
    print(cls.add_link_in_method_docstring(
        version='2020',
        class_name='caeGuiPrefs',
        method_name='saveAs',
        docstring=CaeGuiPrefs.saveAs.__doc__,
    ))


def test_add_docstring_to_module():
    print('\n')
    print(cls.add_link_to_file(
        version='2022',
        file_name='src/abaqus/AbaqusCAEDisplayPreferences/caePrefsAccess.py',
    ))
    print(cls.add_link_to_file(
        version='2022',
        file_name='src/abaqus/AbaqusCAEDisplayPreferences/caeGuiPrefs.py',
    ))


def generate_docstrings():
    def add_docstrings_to_folder(version, folder_name, force_link=False, write_to_file=False):
        print('# Adding docstrings to {}'.format(folder_name))
        for folder_or_file_name in os.listdir(folder_name):
            if folder_or_file_name.startswith('_'):
                continue
            if (os.path.isfile(os.path.join(folder_name, folder_or_file_name)) and folder_or_file_name.endswith('.py')
                    and not folder_or_file_name.startswith('_') and not folder_or_file_name.endswith('_.py')):
                cls.add_link_to_file(
                    version=version,
                    file_name=os.path.join(folder_name, folder_or_file_name),
                    force_link=force_link,
                    write_to_file=write_to_file,
                )
            elif os.path.isdir(os.path.join(folder_name, folder_or_file_name)):
                add_docstrings_to_folder(
                    version=version,
                    folder_name=os.path.join(folder_name, folder_or_file_name),
                    force_link=force_link,
                    write_to_file=write_to_file,
                )

    base = 'src/abaqus'
    add_docstrings_to_folder(
        version='2022',
        folder_name=base,
        force_link=True,
        write_to_file=True,
    )


generate_docstrings()
