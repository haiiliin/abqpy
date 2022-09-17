import sys
from abaqus.Odb.OdbCommands import *
from abaqus.UtilityAndView.BackwardCompatibility import BackwardCompatibility

backwardCompatibility = BackwardCompatibility()

abqpy.abaqus.run(cae=False)
