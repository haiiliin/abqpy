from math import *  # noqa # pylint: disable=unused-import

from abqpy import run

run(cae=False)

from abaqus.Odb.OdbCommands import *  # noqa # pylint: disable=unused-import
from abaqus.UtilityAndView.BackwardCompatibility import BackwardCompatibility
from abaqusConstants import *  # noqa # pylint: disable=unused-import

backwardCompatibility = BackwardCompatibility()
