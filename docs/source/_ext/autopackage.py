import inspect
from types import ModuleType, FunctionType
from typing import List, Tuple, Union

from sphinx.application import Sphinx
from sphinx.ext.autodoc import ModuleDocumenter


class AutoPackageDocumenter(ModuleDocumenter):
    objtype = 'package'
    directivetype = ModuleDocumenter.objtype
    priority = 10 + ModuleDocumenter.priority
    option_spec = dict(ModuleDocumenter.option_spec)

    @classmethod
    def get_submembers(
        cls,
        module: ModuleType,
        current_members: bool = False,
    ) -> List[Tuple[str, Union[FunctionType, type]]]:
        modules = inspect.getmembers(module, inspect.ismodule)  # type: List[Tuple[str, ModuleType]]
        members = []  # type: List[Tuple[str, Union[FunctionType, type]]]
        if current_members:
            members.extend(inspect.getmembers(module, inspect.isclass))
            members.extend(inspect.getmembers(module, inspect.isfunction))
        return members + [member for _, module in modules for member in cls.get_submembers(module, True)]

    def document_members(self, all_members: bool = False) -> None:
        super().document_members(all_members)
        submembers = self.get_submembers(self.module)
        if submembers:
            sourcename = self.get_sourcename()
            self.add_line('', sourcename)
            self.add_line('.. rubric:: All Members:', sourcename)
            self.add_line('', sourcename)
            self.add_line('.. collapse:: Click here to Expand', sourcename)
            self.add_line('', sourcename)
            self.indent += ' ' * 3
            for name, member in submembers:
                if not member.__module__.startswith(self.module.__name__):
                    continue
                self.add_line('', sourcename)
                if inspect.isclass(member):
                    self.add_line(f'.. currentmodule:: {member.__module__}', sourcename)
                    self.add_line(f'.. autoclass:: {member.__qualname__}', sourcename)
                    self.add_line('    :members:', sourcename)
                    self.add_line('    :special-members: __init__', sourcename)
                    self.add_line('    :show-inheritance:', sourcename)
                    self.add_line('', sourcename)
                    self.add_line('    .. autoclasstoc::', sourcename)
                    self.add_line('', sourcename)
                elif inspect.isfunction(member):
                    self.add_line(f'.. currentmodule:: {member.__module__}', sourcename)
                    self.add_line(f'.. autofunction:: {member.__qualname__}', sourcename)
                    self.add_line('', sourcename)


def setup(app: Sphinx) -> None:
    app.setup_extension('sphinx.ext.autodoc')  # Require autodoc extension
    app.setup_extension('sphinx.ext.autosummary')  # Require autosummary extension
    app.setup_extension('sphinx_toolbox.collapse')  # Require sphinx_toolbox.collapse extension
    app.add_autodocumenter(AutoPackageDocumenter)
