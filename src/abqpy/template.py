import numbers
import os
from typing import Any, Dict, Optional, Union, Type

import toml
from jinja2 import Template


class Parameter(dict):
    """A parameter for a template."""
    #: The name of the parameter.
    name: str
    #: The type of the parameter.
    type: Type = str
    #: The default value of the parameter.
    default: Any = None
    #: The description of the parameter.
    description: str = ''
    #: The minimum value of the parameter.
    min: Optional[numbers.Number] = None
    #: The maximum value of the parameter.
    max: Optional[numbers.Number] = None


class ScriptTemplate(Template):
    _params: Dict[str, Parameter]
    parameters = property(lambda self: list(self._params))
    defaults = property(lambda self: {name: param['default'] for name, param in self._params.items()})

    def __new__(
        cls,
        source: Union[os.PathLike, str, Template],
        config: Union[
            Dict[str, Union[Parameter, Dict[str, Any]]],
            os.PathLike, str,
        ] = None,
    ):
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
                if isinstance(param, Parameter):
                    obj._params[name] = param
                elif isinstance(param, dict):
                    obj._params[name] = Parameter(name=name, **param)
                else:
                    raise TypeError(f'Invalid parameter type: {type(param)}')
        return obj

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
        params = self.defaults.copy()
        params.update(kwargs)
        return super().render(**params)

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


def test_render():
    """Test the render function."""
    os.chdir(os.path.dirname(__file__))
    os.chdir('../../')
    template = ScriptTemplate('templates/compression.tmp', 'templates/compression.toml')
    print(template.render(width=2, length=2, height=2))
