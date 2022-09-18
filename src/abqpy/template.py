"""
Templates to generate python scripts.

User's Guide
------------

The :py:class:`~abqpy.template.ScriptTemplate` class provides a simple interface to generate python scripts from
templates.

API Reference
-------------
"""
import json
import os
from typing import Dict, Union, Type
import textwrap

import toml
from jinja2 import Template

__all__ = [
    'CompressionTemplate',
    'ScriptTemplate',
]


def load_json_or_toml(path: Union[str, Dict]) -> Dict:
    """Load a json or toml file."""
    if isinstance(path, dict):
        return path
    if not os.path.exists(path):
        raise FileNotFoundError(f'File {path} does not exist.')
    if path.endswith('.json'):
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    elif path.endswith('.toml'):
        with open(path, encoding='utf-8') as f:
            return toml.load(f)
    else:
        raise ValueError(f'Unknown file type: {path}')


class ScriptTemplate(Template):
    """A template class for Abaqus script.

    Examples
    --------
    >>> from abqpy.template import ScriptTemplate
    >>>
    >>> template = ScriptTemplate(template='template.py', config='config.toml', user='user.toml')
    >>> template.write('script.py')
    >>>
    >>> template = ScriptTemplate(template='template.py', config='config.toml')
    >>> template.write('script.py', param1=1, param2=2)
    """
    #: Parameter config
    _config: Dict[str, Dict[str, Union[str, int, float, bool]]]
    #: User config
    _user: Dict[str, Union[str, int, float, bool]]
    #: Template source
    _template_source: str
    #: Parameter config source
    _config_source: str
    #: User config source
    _user_source: str
    #: A list of parameters required by the template.
    parameters = property(lambda self: list(self._config))
    #: The default parameters.
    defaults = property(lambda self: {name: param['default'] for name, param in self._config.items()})
    #: The types of the parameters.
    types = property(lambda self: {name: param['type'] for name, param in self._config.items()})
    #: The descriptions of the parameters.
    descriptions = property(lambda self: {name: param['description'] for name, param in self._config.items()})
    #: Template source
    template_source = property(lambda self: self._template_source)
    #: Parameter config source
    config_source = property(lambda self: self._config_source)
    #: User config source
    user_source = property(lambda self: self._user_source)

    def __new__(
        cls,
        template: Union[
            os.PathLike, str,
        ],
        config: Union[
            Dict[str, Dict[str, Union[str, int, float, bool]]],
            os.PathLike, str,
        ] = None,
        user: Union[
            Dict[str, Dict[str, Union[str, int, float, bool]]],
            os.PathLike, str,
        ] = None,
    ):
        """Create a new template.
        """
        if os.path.exists(template) and os.path.isfile(config):
            template = open(template, 'r', encoding='utf-8').read()
        obj = super().__new__(cls, template)
        obj._template_source = template

        # Read the config file
        if os.path.exists(config) and os.path.isfile(config):
            obj._config_source = open(config, 'r', encoding='utf-8').read()
        obj._config = load_json_or_toml(config) if config else {}
        for name in obj._config.keys():
            obj._config[name]['name'] = name

        # Read the user config file
        if os.path.exists(user) and os.path.isfile(user):
            obj._user_source = open(user, 'r', encoding='utf-8').read()
        obj._user = load_json_or_toml(user) if user else {}
        return obj

    def check(self, correct_bounds=True, **kwargs):
        """Check if the parameters are valid, if valid, return the processed parameters as a dict.

        Parameters
        ----------
        correct_bounds : bool, optional
            Whether to correct the parameters to the bounds, by default True
        **kwargs
            The parameters to check.

        Returns
        -------
        Dict
            The original or corrected parameters.

        Raises
        ------
        ValueError
            If the parameters are invalid.
        """
        for name, param in kwargs.items():
            if name not in self._config:
                raise ValueError(f'Invalid parameter: {name}')
            if 'min' in self._config[name] and param < self._config[name]['min']:
                if correct_bounds:
                    kwargs[name] = self._config[name]['min']
                else:
                    raise ValueError(f'Parameter {name} is too small: {param}')
            if 'max' in self._config[name] and param > self._config[name]['max']:
                if correct_bounds:
                    kwargs[name] = self._config[name]['max']
                else:
                    raise ValueError(f'Parameter {name} is too large: {param}')
        params = self.defaults
        params.update(self._user)
        params.update(kwargs)
        return params

    def render(self, **kwargs) -> str:
        """Render the template.

        Parameters
        ----------
        **kwargs
            The parameters to render the template.

        Returns
        -------
        str
            The rendered template.
        """
        return super().render(**self.check(**kwargs))

    def write(self, file: Union[os.PathLike, str], **kwargs):
        """Write the rendered template to a file.

        Parameters
        ----------
        file : str or PathLike
            The file to write to.
        **kwargs
            The parameters to render the template.
        """
        with open(file, 'w', encoding='utf-8') as f:
            f.write(self.render(**kwargs))


def template_doc(cls: Type['CompressionTemplate']):
    """Generate the docstring for the template class."""
    obj = cls()
    attr_docstrings = []
    parameters, types, defaults, descriptions = obj.parameters, obj.types, obj.defaults, obj.descriptions
    for var in parameters:
        attr_docstrings.append(f'.. confval:: {var}\n'
                               f'    :type: {types[var]}, defaults to {defaults[var]}\n\n'
                               f'    {descriptions[var]}')
    attrs_docstring = '\n\n'.join(attr_docstrings)
    docstring = f"""
This is a template for {cls.name}. Example usage::
    
    from abqpy.template import {cls.__name__}
    
    template = {cls.__name__}()
    template.write('script.py')

.. admonition:: Details of required parameters

{textwrap.indent(attrs_docstring, ' ' * 4)}

.. admonition:: User config file (A `toml <https://toml.io/>`_ or `json <https://www.json.org/>`_ file)
    
    .. code-block:: toml
    
{textwrap.indent(obj.user_source, ' ' * 8)}

.. admonition:: The template source code

    .. code-block:: python
    
{textwrap.indent(obj.template_source, ' ' * 8)}

.. admonition:: The template config file  (A `toml <https://toml.io/>`_ or `json <https://www.json.org/>`_ file)
    
    .. code-block:: toml
    
{textwrap.indent(obj.config_source, ' ' * 8)}
"""
    cls.__doc__ = docstring
    return cls


class _DocumentTemplate(ScriptTemplate):
    #: The name of the template, the corresponding template filename must be `name.tmpl`, and the corresponding config
    #: filename must be `name.toml`.
    name = 'template'

    def __new__(
        cls,
        user: Union[
            Dict[str, Dict[str, Union[str, int, float, bool]]],
            os.PathLike, str,
        ] = None,
    ):
        dirname = os.path.dirname(__file__)
        template = os.path.join(dirname, 'templates', f'{cls.name}.tmpl')
        config = os.path.join(dirname, 'templates', f'{cls.name}.toml')
        if user is None:
            user = os.path.join(dirname, 'templates', f'{cls.name}.conf.toml')
        return super().__new__(cls, template, config, user)


@template_doc
class CompressionTemplate(_DocumentTemplate):
    """A template for compression analysis.

    Examples
    --------
    >>> from abqpy.template import CompressionTemplate
    >>>
    >>> template = CompressionTemplate(user='user.toml')
    >>> template.write('script.py')
    >>>
    >>> template = CompressionTemplate()
    >>> template.write('script.py', width=10.0, height=10.0)
    """
    name = 'compression'


def test_render():
    """Test the render function."""
    os.chdir(os.path.dirname(__file__))
    os.chdir('../../')
    template = ScriptTemplate('templates/compression.tmpl', 'templates/compression.toml')
    print(template.render(width=2, length=2, height=2))


def test_decorator():
    """Test the decorator."""
    print(CompressionTemplate.__doc__)
