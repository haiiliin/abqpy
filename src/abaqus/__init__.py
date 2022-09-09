import os
import sys
from pathlib import Path

from .Canvas.Highlight import *
from .Mdb.Mdb import Mdb as AbaqusMdb
from .Odb.Odb import Odb
from .Session.Session import Session as AbaqusSession
from .UtilityAndView.BackwardCompatibility import BackwardCompatibility
from .UtilityAndView.User import *
from .UtilityAndView.SymbolicConstant import SymbolicConstant

try:
    from ._version import version as _default_version
except ImportError:
    _default_version = '2022.0.0-unknown'


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
                root=root,
                version_scheme="release-branch-semver",
                local_scheme="node-and-date",
                fallback_version=_default_version,
            )
        except ValueError:
            return _default_version
    else:  # Get the version from the _version.py setuptools_scm file.
        return _default_version


__version__ = _get_version()


class Mdb(AbaqusMdb):

    def __init__(self, pathName: str = ""):
        super().__init__(pathName)

    def save(self):
        super().save()

    def saveAs(self, pathName: str):
        abaqus = "abaqus"
        if "ABAQUS_BAT_PATH" in os.environ.keys():
            abaqus = os.environ["ABAQUS_BAT_PATH"]

        filePath = os.path.abspath(sys.argv[0])

        try:  # If it is a jupyter notebook
            import ipynbname
            filePath = ipynbname.path()
            os.system(f"jupyter nbconvert --to python {filePath}")
            filePath = filePath.replace(".ipynb", ".py")
        except:
            pass
        os.system(f"{abaqus} cae -noGUI {filePath}")


class Session(AbaqusSession):

    def openOdb(self, name: str, *args, **kwargs) -> Odb:
        self.odbs[name] = odb = Odb(name, *args, **kwargs)

        abaqus = "abaqus"
        if "ABAQUS_BAT_PATH" in os.environ.keys():
            abaqus = os.environ["ABAQUS_BAT_PATH"]

        filePath = os.path.abspath(sys.argv[0])

        try:  # If it is a jupyter notebook
            import ipynbname

            filePath = ipynbname.path()
            os.system(f"jupyter nbconvert --to python {filePath}")
            filePath = filePath.replace(".ipynb", ".py")
        except:
            pass
        os.system(f"{abaqus} cae script={filePath}")

        self.exit()
        return odb


session = Session()
mdb = Mdb()

backwardCompatibility = BackwardCompatibility()

YES = SymbolicConstant('YES')
NO = SymbolicConstant('NO')
