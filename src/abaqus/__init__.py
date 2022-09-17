import abqpy.abaqus
from .Canvas.Highlight import *
from .Mdb.Mdb import Mdb
from .Odb.Odb import Odb
from .Session.Session import Session
from .UtilityAndView.BackwardCompatibility import BackwardCompatibility
from .UtilityAndView.SymbolicConstant import SymbolicConstant
from .UtilityAndView.abaqusConstants import Boolean, OFF
from .UtilityAndView.User import *

<<<<<<< HEAD

class Mdb(AbaqusMdb):

    def __init__(self, pathName: str = ""):
        super().__init__(pathName)

    def save(self):
        super().save()

    def saveAs(self, pathName: str):
        abqpy.abaqus.run()


class Session(AbaqusSession):

    def openOdb(self, name: str, path: str = "", readOnly: Boolean = OFF) -> Odb:
        self.odbs[name] = odb = Odb(name)
        abqpy.abaqus.run()
        return odb


=======
>>>>>>> a2cd44cc (Do not run the abaqus command in debug mode (#1501))
session = Session()
mdb = Mdb()

backwardCompatibility = BackwardCompatibility()

YES = SymbolicConstant('YES')
NO = SymbolicConstant('NO')

abqpy.abaqus.run(cae=True)
