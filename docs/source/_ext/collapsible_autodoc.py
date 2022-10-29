from sphinx.application import Sphinx
from sphinx.ext.autodoc import ClassDocumenter


class AutoCollapsibleClassDocumenter(ClassDocumenter):
    objtype = 'collapsibleclass'
    directivetype = ClassDocumenter.objtype
    priority = 10 + ClassDocumenter.priority
    option_spec = dict(ClassDocumenter.option_spec)

    def document_members(self, all_members: bool = False) -> None:
        self.add_line('.. collapse:: Click here to Expand', self.get_sourcename())
        self.indent += ' ' * 3
        super().document_members(all_members)


def setup(app: Sphinx) -> None:
    app.setup_extension('sphinx.ext.autodoc')  # Require autodoc extension
    app.setup_extension('sphinx_toolbox.collapse')  # Require sphinx_toolbox.collapse extension
    app.add_autodocumenter(AutoCollapsibleClassDocumenter)
