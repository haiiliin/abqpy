import sys
from math import *

from abqpy import run

from .builtin import *
from .Canvas.Highlight import *
from .Mdb.Mdb import Mdb
from .Mdb.MdbCommands import *
from .Odb.Odb import Odb
from .Session.Session import Session
from .UtilityAndView import abaqusConstants
from .UtilityAndView.abaqusConstants import OFF, Boolean
from .UtilityAndView.BackwardCompatibility import BackwardCompatibility
from .UtilityAndView.SymbolicConstant import SymbolicConstant
from .UtilityAndView.User import *

session = Session()
mdb = Mdb()

backwardCompatibility = BackwardCompatibility()

YES = abaqusConstants.YES
NO = abaqusConstants.NO

run(cae=True)

__main__ = sys.modules["__main__"]
