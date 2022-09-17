import importlib.util
import os
import typing

from jinja2 import Template


def available_templates() -> typing.List[str]:
    """Return a list of available templates.

    Returns
    -------
    List[str]
        A list of existing templates.
    """
    return [file[:-3]for file in os.listdir(os.path.join(os.path.dirname(__file__), 'templates'))
            if file.endswith('.py')]


class ScriptTemplate(Template):
    _vars: typing.Dict[str, typing.Any]

    def __new__(cls, tmp: typing.Union[os.PathLike, str, Template], **kwargs):
        _vars = {}
        if os.path.exists(tmp):
            obj = super().__new__(cls, open(tmp, 'r', encoding='utf-8').read())
        elif tmp in available_templates():
            module = importlib.import_module(f'abqpy.templates.{tmp}')
            obj = super().__new__(cls, module.template)
            _vars.update(module.defaults)
        else:
            obj = super().__new__(cls, tmp)
        obj._vars = _vars
        obj._vars.update(kwargs)
        return obj

    def __init__(self, tmp: typing.Union[os.PathLike, str, Template], **kwargs):
        """Get a template object.

        Parameters
        ----------
        tmp : str or PathLike
            The name of the template to use, or the path to the template file, or a string of the template,
            or a Template object.
        **kwargs
            The parameters to render the template.

        Returns
        -------
        Template
            The template object.
        """
        if tmp in available_templates():
            module = importlib.import_module(f'abqpy.templates.{tmp}')
            self._vars.update(module.defaults)
        self._vars.update(kwargs)

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
        self._vars.update(kwargs)
        return super().render(**self._vars)

    def write(self, file: typing.Union[os.PathLike, str], **kwargs):
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
    print(ScriptTemplate('COMPRESSION', width=2, length=2, height=2).render())
