import sys
import abqpy.abaqus
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

YES = SymbolicConstant('YES')
NO = SymbolicConstant('NO')

# check if in debug mode and run
gettrace = getattr(sys, 'gettrace', None)
exit_after = False
if gettrace is None or not gettrace():
    exit_after = True

abqpy.abaqus.run(cae=True, exit_after=exit_after)