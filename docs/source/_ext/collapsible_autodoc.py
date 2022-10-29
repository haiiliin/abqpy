from sphinx.application import Sphinx
from sphinx.ext.autodoc import ClassDocumenter, ALL


class AutoCollapsibleClassDocumenter(ClassDocumenter):
    objtype = 'class'
    directivetype = ClassDocumenter.objtype
    priority = 10 + ClassDocumenter.priority
    option_spec = dict(ClassDocumenter.option_spec)

    def document_members(self, all_members: bool = False) -> None:
        # find out all the members that are documented
        want_all = all_members or self.options.inherited_members or self.options.members is ALL
        _, members = self.get_object_members(want_all)
        if members:
            sourcename = self.get_sourcename()
            self.add_line('', sourcename)
            self.add_line('.. rubric:: Member Details', sourcename)
            self.add_line('', sourcename)
            self.add_line('.. collapse:: Click here to Expand', sourcename)
            self.indent += ' ' * 3
        super().document_members(all_members)


def setup(app: Sphinx) -> None:
    app.setup_extension('sphinx.ext.autodoc')  # Require autodoc extension
    app.setup_extension('sphinx_toolbox.collapse')  # Require sphinx_toolbox.collapse extension
    app.add_autodocumenter(AutoCollapsibleClassDocumenter)
