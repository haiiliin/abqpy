from pathlib import Path
from typing import Dict, List, cast

from sphinx.application import Sphinx
from sphinx.builders.changes import ChangesBuilder
from sphinx.domains.changeset import ChangeSetDomain
from sphinx.locale import _


class AbqpyChangesBuilder(ChangesBuilder):
    def write(self, *ignored) -> None:
        domain = cast(ChangeSetDomain, self.env.get_domain("changeset"))

        def get_libchanges(v: str):
            libchanges: Dict[str, List[str]] = {}
            for changeset in domain.get_changesets_for(v):
                descname = changeset.descname[0] if isinstance(changeset.descname, tuple) else changeset.descname
                ttext = self.typemap[changeset.type]
                context = changeset.content.replace("\n", " ")
                if descname or changeset.module:
                    module = changeset.module or _("Builtins")
                    descname = f"{{py:obj}}`{module}.{descname}`" or _("**Module level**")
                    entry = f"{descname}: *{ttext}*: {context}" if context else f"{descname}: *{ttext}*"
                    libchanges.setdefault(module, []).append(entry)
            return libchanges

        document = f"# Abaqus API Changes\n\n"
        for version in self.config.changes_versions or [self.config.version]:
            libchanges = get_libchanges(version)
            if not libchanges:
                continue
            document += f"## Abaqus {version}\n\n"
            for mod, changes in libchanges.items():
                document += f"### {{py:obj}}`{mod}`\n\n"
                for change in changes:
                    document += f"- {change}\n"
                document += "\n"
            document += "\n"

        (Path(self.confdir) / self.config.changes_write_to).write_text(document, encoding="utf-8")


def setup(app: Sphinx):
    app.add_config_value("changes_write_to", "CHANGES.md", "env")
    app.add_config_value("changes_versions", None, "env")
    app.add_builder(AbqpyChangesBuilder, override=True)
    return dict(
        version="0.0.1",
        parallel_read_safe=True,
        parallel_write_safe=True,
    )
