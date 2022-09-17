import sys
from abaqus.Odb.OdbCommands import *
from abaqus.UtilityAndView.BackwardCompatibility import BackwardCompatibility

backwardCompatibility = BackwardCompatibility()

# check if in debug mode and run
gettrace = getattr(sys, 'gettrace', None)
exit_after = False
if gettrace is None or not gettrace():
    exit_after = True

abqpy.abaqus.run(cae=True, exit_after=exit_after)
