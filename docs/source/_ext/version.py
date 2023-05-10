from importlib import metadata

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxRole


class VersionRole(SphinxRole):
    """Role for inserting the version of a package. For example:

    .. code-block:: rst

        :version:`numpy`
        :version-major:`numpy`
        :version-minor:`numpy`
        :version-patch:`numpy`
        :version:`prefix text |numpy| suffix text`
    """

    type = "version"

    def run(self):
        prefix, suffix, package = "", "", ""
        elements = self.text.split("|", 3)
        if len(elements) == 1:
            package = elements[0]
        elif len(elements) == 2:
            prefix, package = elements
        elif len(elements) == 3:
            prefix, package, suffix = elements
        else:
            raise ValueError("Invalid version role syntax")

        major, minor, patch = metadata.version(package).split(".")[:3]
        version = (
            major
            if self.type == "major"
            else minor
            if self.type == "minor"
            else patch
            if self.type == "patch"
            else f"{major}.{minor}.{patch}"
        )
        text = f"{prefix}{version}{suffix}"
        return [nodes.Text(text, text)], []


class MajorVersionRole(VersionRole):
    type = "major"


class MinorVersionRole(VersionRole):
    type = "minor"


class PatchVersionRole(VersionRole):
    type = "patch"


def setup(app: Sphinx):
    app.add_role("version", VersionRole())
    app.add_role("version-major", MajorVersionRole())
    app.add_role("version-minor", MinorVersionRole())
    app.add_role("version-patch", PatchVersionRole())
    return {"version": "0.0.1", "parallel_read_safe": True}
