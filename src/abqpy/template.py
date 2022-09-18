"""
Templates to generate python scripts.

API Reference
-------------
"""
import os
from typing import Dict, Union, Type
import textwrap

import toml
from jinja2 import Template

__all__ = [
    'CompressionTemplate',
    'ScriptTemplate',
]


class ScriptTemplate(Template):
    """A template class for Abaqus script.
    """
    _params: Dict[str, Dict[str, Union[str, int, float, bool]]]
    #: A list of parameters required by the template.
    parameters = property(lambda self: list(self._params))
    #: The default parameters.
    defaults = property(lambda self: {name: param['default'] for name, param in self._params.items()})
    #: The types of the parameters.
    types = property(lambda self: {name: param['type'] for name, param in self._params.items()})
    #: The descriptions of the parameters.
    descriptions = property(lambda self: {name: param['description'] for name, param in self._params.items()})

    def __new__(
        cls,
        source: Union[os.PathLike, str, Template],
        config: Union[
            Dict[str, Dict[str, Union[str, int, float, bool]]],
            os.PathLike, str,
        ] = None,
    ):
        """Create a new template.

        Parameters
        ----------
        source : str or PathLike or Template
            The template source.
        config : str or PathLike or dict, optional
            The config file or dict, by default None
        """
        if os.path.exists(source) and os.path.isfile(config):
            source = open(source, 'r', encoding='utf-8').read()
        obj = super().__new__(cls, source)
        if os.path.exists(config) and os.path.isfile(config):
            if config.endswith('.toml'):
                config = toml.load(config)
            elif config.endswith('.json'):
                import json
                with open(config, 'r', encoding='utf-8') as f:
                    config = json.load(f)
        obj._params = {}
        if isinstance(config, dict):
            for name, param in config.items():
                if isinstance(param, Dict):
                    obj._params[name] = dict(name=name, **param)
                else:
                    raise TypeError(f'Invalid parameter type: {type(param)}')
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
            if name not in self._params:
                raise ValueError(f'Invalid parameter: {name}')
            if 'min' in self._params[name] and param < self._params[name]['min']:
                if correct_bounds:
                    kwargs[name] = self._params[name]['min']
                else:
                    raise ValueError(f'Parameter {name} is too small: {param}')
            if 'max' in self._params[name] and param > self._params[name]['max']:
                if correct_bounds:
                    kwargs[name] = self._params[name]['max']
                else:
                    raise ValueError(f'Parameter {name} is too large: {param}')
        params = self.defaults
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
This is a template for {cls.name}.

.. warning::
    This is a template class just for documentation, do not use it directly.

.. note::
    Details of the parameters requirements to render the template:

{textwrap.indent(attrs_docstring, ' ' * 4)}

    The source code of the template is::
    
{textwrap.indent(obj.source, ' ' * 8)}
"""
    cls.__doc__ = docstring
    return cls


class _DocumentTemplate(ScriptTemplate):
    name = 'template'

    def __new__(cls):
        dirname = os.path.dirname(__file__)
        source = os.path.join(dirname, 'templates', f'{cls.name}.tmpl')
        config = os.path.join(dirname, 'templates', f'{cls.name}.toml')
        obj = super().__new__(cls, source, config)
        obj.source = open(source, 'r', encoding='utf-8').read()
        return obj


@template_doc
class CompressionTemplate(_DocumentTemplate):
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
