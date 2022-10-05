import sys

import abqpy.abaqus
from .Canvas.Highlight import *
from .Mdb.Mdb import Mdb
from .Odb.Odb import Odb
from .Session.Session import Session
from .UtilityAndView import abaqusConstants
from .UtilityAndView.BackwardCompatibility import BackwardCompatibility
from .UtilityAndView.SymbolicConstant import SymbolicConstant
from .UtilityAndView.User import *
from .UtilityAndView.abaqusConstants import Boolean, OFF
from .__builtin__ import execfile, execPyFile, raw_input, cliCommand, upgradeMdb

session = Session()
mdb = Mdb()

backwardCompatibility = BackwardCompatibility()

YES = abaqusConstants.YES
NO = abaqusConstants.NO

abqpy.abaqus.run(cae=True)

__main__ = sys.modules['__main__']
