import sys
import abqpy.abaqus
from .Canvas.Highlight import *
from .Mdb.Mdb import Mdb as AbaqusMdb
from .Odb.Odb import Odb
from .Session.Session import Session as AbaqusSession
from .UtilityAndView.BackwardCompatibility import BackwardCompatibility
from .UtilityAndView.SymbolicConstant import SymbolicConstant
from .UtilityAndView.abaqusConstants import Boolean, OFF
from .UtilityAndView.User import *


class Mdb(AbaqusMdb):

    def __init__(self, pathName: str = ""):
        super().__init__(pathName)

    def save(self):
        abqpy.abaqus.run()

    def saveAs(self, pathName: str):
        abqpy.abaqus.run()


class Session(AbaqusSession):

    def openOdb(self, name: str, path: str = "", readOnly: Boolean = OFF) -> Odb:
        self.odbs[name] = odb = Odb(name)
        abqpy.abaqus.run()
        return odb


session = Session()
mdb = Mdb()

backwardCompatibility = BackwardCompatibility()

YES = SymbolicConstant('YES')
NO = SymbolicConstant('NO')

# check if in debug mode and run
gettrace = getattr(sys, 'gettrace', None)
exit_after = False
if gettrace is None or not gettrace():
    exit_after = True

abqpy.abaqus.run(cae=True, exit_after=exit_after)