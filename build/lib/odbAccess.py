import abqpy.abaqus

abqpy.abaqus.run(cae=False)

from abaqus.Odb.OdbCommands import *
from abaqus.UtilityAndView.BackwardCompatibility import BackwardCompatibility

backwardCompatibility = BackwardCompatibility()
