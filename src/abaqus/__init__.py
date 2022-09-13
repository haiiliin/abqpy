import abqpy.abaqus
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
        abqpy.abaqus.run()


class Session(AbaqusSession):

    def openOdb(self, name: str, *args, **kwargs) -> Odb:
        self.odbs[name] = odb = Odb(name, *args, **kwargs)
        abqpy.abaqus.run(exit_after=True)
        return odb


session = Session()
mdb = Mdb()

backwardCompatibility = BackwardCompatibility()

YES = SymbolicConstant('YES')
NO = SymbolicConstant('NO')
