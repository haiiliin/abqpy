from pathlib import Path

from .template import *

try:
    from ._version import version as _default_version
except ImportError:
    _default_version = '2023.0.0-dev'


def _get_version():
    """Return the version string used for __version__."""
    # Only shell out to a git subprocess if really needed, and not on a
    # shallow clone, such as those used by CI, as the latter would trigger
    # a warning from setuptools_scm.
    root = Path(__file__).resolve().parents[2]
    if (root / ".git").exists() and not (root / ".git/shallow").exists():
        import setuptools_scm
        try:
            return setuptools_scm.get_version(
                root=str(root),
                version_scheme="release-branch-semver",
                local_scheme="node-and-date",
                fallback_version=_default_version,
            )
        except Exception:
            return _default_version
    else:  # Get the version from the _version.py setuptools_scm file.
        return _default_version


__version__ = _get_version()
__semver__ = __version__.split("+")[0]
