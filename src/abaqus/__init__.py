import sys
import abqpy.abaqus
from abqpy.python2funcs import *
from .Canvas.Highlight import *
from .Mdb.Mdb import Mdb
from .Odb.Odb import Odb
from .Session.Session import Session
from .UtilityAndView.BackwardCompatibility import BackwardCompatibility
from .UtilityAndView.SymbolicConstant import SymbolicConstant
from .UtilityAndView.abaqusConstants import Boolean, OFF
from .UtilityAndView.User import *

session = Session()
mdb = Mdb()

backwardCompatibility = BackwardCompatibility()

YES = SymbolicConstant.YES
NO = SymbolicConstant.NO

abqpy.abaqus.run(cae=True)

__main__ = sys.modules['__main__']
