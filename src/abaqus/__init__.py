import os
import sys

from .Canvas.Highlight import *
from .Mdb.Mdb import Mdb as AbaqusMdb
from .Odb.Odb import Odb
from .Session.Session import Session as AbaqusSession
from .UtilityAndView.BackwardCompatibility import BackwardCompatibility


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
        fileDir = os.path.dirname(filePath)
        fileName = os.path.basename(filePath)

        os.system(f"cd {fileDir}")
        try:  # If it is a jupyter notebook
            import ipynbname

            fileName = os.path.basename(ipynbname.path())
            fileDir = os.path.dirname(ipynbname.path())
            os.system(f"cd {fileDir}")
            os.system(f"jupyter nbconvert --to python {fileName}")
            fileName = fileName.replace(".ipynb", ".py")
        except:
            pass
        os.system(f"{abaqus} cae -noGUI {fileName}")


class Session(AbaqusSession):

    def openOdb(self, name: str, *args, **kwargs) -> Odb:
        self.odbs[name] = odb = Odb(name, *args, **kwargs)

        abaqus = "abaqus"
        if "ABAQUS_BAT_PATH" in os.environ.keys():
            abaqus = os.environ["ABAQUS_BAT_PATH"]

        filePath = os.path.abspath(sys.argv[0])
        fileDir = os.path.dirname(filePath)
        fileName = os.path.basename(filePath)
        odbName = os.path.basename(os.path.abspath(name))

        os.system(f"cd {fileDir}")
        try:  # If it is a jupyter notebook
            import ipynbname

            fileName = os.path.basename(ipynbname.path())
            os.system(f"jupyter nbconvert --to python {fileName}")
            fileName = fileName.replace(".ipynb", ".py")
        except:
            pass
        os.system(f"{abaqus} cae database={odbName} script={fileName}")

        self.exit()
        return odb


session = Session()
mdb = Mdb()

backwardCompatibility = BackwardCompatibility()
