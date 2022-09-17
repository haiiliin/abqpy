import os
from typing import Any, Dict, Union

import toml
from jinja2 import Template


class ScriptTemplate(Template):
    _params: Dict[str, Dict[str, Any]]
    parameters = property(lambda self: list(self._params))
    defaults = property(lambda self: {name: param['default'] for name, param in self._params.items()})

    def __new__(
        cls,
        source: Union[os.PathLike, str, Template],
        config: Union[
            Dict[str, Union[Dict[str, Any]]],
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
        params = self.defaults.copy()
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


def test_render():
    """Test the render function."""
    os.chdir(os.path.dirname(__file__))
    os.chdir('../../')
    template = ScriptTemplate('templates/compression.tmp', 'templates/compression.toml')
    print(template.render(width=2, length=2, height=2))
