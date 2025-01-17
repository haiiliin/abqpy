from __future__ import annotations

from pathlib import Path
from re import error as RegexError

from .cli import AbqpyCLI, abaqus
from .run import run

try:
    from ._version import version as _default_version
except ImportError:
    _default_version = "2018.0.0-dev"


def _get_version():
    root = Path(__file__).resolve().parents[2]
    if (root / ".git").exists() and not (root / ".git/shallow").exists():
        try:
            import setuptools_scm

            return setuptools_scm.get_version(root=str(root))
        except (ImportError, RegexError, LookupError):
            return _default_version
    else:
        return _default_version


__version__ = _get_version()
__semver__ = __version__.split("+")[0]
version_info = __semver__.split(".")

__all__ = [
    "run",
    "abaqus",
    "AbqpyCLI",
    "version_info",
    "__version__",
    "__semver__",
]
