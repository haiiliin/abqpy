from math import *  # noqa # pylint: disable=unused-import

import abqpy.abaqus

abqpy.abaqus.run(cae=False)

from abaqus.Odb.OdbCommands import *  # noqa # pylint: disable=unused-import
from abaqus.UtilityAndView.BackwardCompatibility import BackwardCompatibility

backwardCompatibility = BackwardCompatibility()
