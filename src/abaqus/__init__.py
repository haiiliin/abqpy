from .Canvas.Highlight import *
from .Mdb.Mdb import Mdb as AbaqusMdb
from .Odb.Odb import Odb
from .Session.Session import Session as AbaqusSession
from .UtilityAndView.BackwardCompatibility import BackwardCompatibility
from .UtilityAndView.SymbolicConstant import SymbolicConstant
from .UtilityAndView.User import *


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
        args = " ".join(sys.argv[1:])

        try:  # If it is a jupyter notebook
            import ipynbname
            filePath = ipynbname.path()
            os.system(f"jupyter nbconvert --to python {filePath}")
            filePath = filePath.replace(".ipynb", ".py")
        except:
            pass
        os.system(f"{abaqus} cae noGUI={filePath} -- {args}")


class Session(AbaqusSession):

    def openOdb(self, name: str, *args, **kwargs) -> Odb:
        self.odbs[name] = odb = Odb(name, *args, **kwargs)

        abaqus = "abaqus"
        if "ABAQUS_BAT_PATH" in os.environ.keys():
            abaqus = os.environ["ABAQUS_BAT_PATH"]

        filePath = os.path.abspath(sys.argv[0])
        args = " ".join(sys.argv[1:])

        try:  # If it is a jupyter notebook
            import ipynbname

            filePath = ipynbname.path()
            os.system(f"jupyter nbconvert --to python {filePath}")
            filePath = filePath.replace(".ipynb", ".py")
        except:
            pass
        os.system(f"{abaqus} cae noGUI={filePath} -- {args}")

        self.exit()
        return odb


session = Session()
mdb = Mdb()

backwardCompatibility = BackwardCompatibility()

YES = SymbolicConstant('YES')
NO = SymbolicConstant('NO')
