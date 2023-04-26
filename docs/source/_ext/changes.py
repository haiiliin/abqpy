from pathlib import Path
from typing import cast, Dict, List

from sphinx.application import Sphinx
from sphinx.builders.changes import ChangesBuilder
from sphinx.domains.changeset import ChangeSetDomain
from sphinx.locale import _


class AbqpyChangesBuilder(ChangesBuilder):

    def write(self, *ignored) -> None:
        libchanges: Dict[str, List[str]] = {}

        domain = cast(ChangeSetDomain, self.env.get_domain('changeset'))
        for changeset in domain.get_changesets_for(self.config.version):
            descname = changeset.descname[0] if isinstance(changeset.descname, tuple) else changeset.descname
            ttext = self.typemap[changeset.type]
            context = changeset.content.replace('\n', ' ')
            if descname or changeset.module:
                module = changeset.module or _('Builtins')
                descname = f"{{py:obj}}`~{module}.{descname}`" or _('**Module level**')
                entry = f"{descname}: *{ttext}*: {context}" if context else f"{descname}: *{ttext}*"
                libchanges.setdefault(module, []).append(entry)

        document = f"# Changes in Abaqus {self.config.version}\n\n"
        document += f"## Library changes\n\n"
        for module, changes in libchanges.items():
            document += f"### {{py:mod}}`{module}`\n\n"
            for change in changes:
                document += f"- {change}\n"
            document += "\n"

        (Path(self.confdir) / self.config.changes_write_to).write_text(document, encoding='utf-8')


def setup(app: Sphinx):
    app.add_config_value("changes_write_to", "CHANGES.md", "env")
    app.add_builder(AbqpyChangesBuilder, override=True)
    return dict(
        version='0.0.1',
        parallel_read_safe=True,
        parallel_write_safe=True,
    )
