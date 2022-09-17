import importlib.util
import numbers
import os

import toml
from typing import Any, Dict, List, Optional, Union, Type, NamedTuple

from jinja2 import Template


class Parameter(NamedTuple):
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


class StringParameter(Parameter):
    """A string parameter for a template."""
    type = str
    default = ''


class NumberParameter(Parameter):
    """A number parameter for a template."""
    type = numbers.Number
    #: The default value of the parameter.
    default: numbers.Number
    #: The minimum value of the parameter.
    min: Optional[numbers.Number] = None
    #: The maximum value of the parameter.
    max: Optional[numbers.Number] = None


class IntegerParameter(NumberParameter):
    """An integer parameter for a template."""
    type = int
    #: The default value of the parameter.
    default: int = 0
    #: The minimum value of the parameter.
    min: Optional[int] = None
    #: The maximum value of the parameter.
    max: Optional[int] = None


class BooleanParameter(Parameter):
    """A boolean parameter for a template."""
    type = bool
    #: The default value of the parameter.
    default: bool = False
    min = False
    max = True


class FloatParameter(NumberParameter):
    """A float parameter for a template."""
    type = float
    #: The default value of the parameter.
    default: float = 0.0
    #: The minimum value of the parameter.
    min: Optional[float] = None
    #: The maximum value of the parameter.
    max: Optional[float] = None


def available_templates() -> List[str]:
    """Return a list of available templates.

    Returns
    -------
    List[str]
        A list of existing templates.
    """
    return [file[:-3]for file in os.listdir(os.path.join(os.path.dirname(__file__), 'templates'))
            if file.endswith('.py')]


class ScriptTemplate(Template):
    params: List[Parameter] = []

    def __new__(
        cls,
        source: Union[os.PathLike, str, Template],
        config: Union[
            List[Parameter],
            Dict[str, Union[Template, Dict[str, Any]]],
            os.PathLike, str,
        ] = None,
    ):
        if os.path.exists(source):
            source = open(source, 'r', encoding='utf-8').read()
        elif source in available_templates():
            source = importlib.import_module(f'abqpy.templates.{source}').template
        obj = super().__new__(cls, source)
        if os.path.exists(config) and os.path.isfile(config):
            if config.endswith('.toml'):
                config = toml.load(config)
            elif config.endswith('.json'):
                import json
                with open(config, 'r', encoding='utf-8') as f:
                    config = json.load(f)
        if isinstance(config, list):
            obj.params = config
        elif isinstance(config, dict):
            obj.params = []
            for name, param in config.items():
                if isinstance(param, Parameter):
                    obj.params.append(param)
                elif isinstance(param, dict):
                    obj.params.append(Parameter(name, **param))
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
        return super().render(**kwargs)

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


def test_existing_templates():
    """Test the existing_templates function."""
    print(available_templates())


def test_render():
    """Test the render function."""
    template = ScriptTemplate('compression', 'templates/compression.toml')
    print(template.render(width=2, length=2, height=2))
