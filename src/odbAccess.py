from __future__ import annotations

import auto_all

from abqpy import run

run(cae=False)
auto_all.start_all()

from math import *  # noqa

from abaqus.Odb.Odb import Odb  # noqa
from abaqus.Odb.OdbCommands import (  # noqa
    AnalyticSurfaceProfile,
    isUpgradeRequiredForOdb,
    maxEnvelope,
    minEnvelope,
    openOdb,
    upgradeOdb,
)
from abaqus.UtilityAndView.BackwardCompatibility import BackwardCompatibility  # noqa
from abaqusConstants import *  # noqa

backwardCompatibility = BackwardCompatibility()

auto_all.end_all()
