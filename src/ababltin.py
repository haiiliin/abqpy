import os
import re
import sys

from abaqus import Mdb, backwardCompatibility, getInput, mdb
from abaqus.Mdb.MdbCommands import CombineOptResults, openMdb, upgradeMdb
from abaqus.Session.Session import Session
from abaqus.UtilityAndView import BackwardCompatibility, SymbolicConstant
from abaqus.UtilityAndView.AbaqusBoolean import AbaqusBoolean
from abaqus.UtilityAndView.abaqusConstants import (
    CFD,
    EMAG,
    FALSE,
    NOT_SET,
    OFF,
    ON,
    SCATTERED,
    STANDARD_EXPLICIT,
    STEP_END,
    TOTAL,
    TRUE,
    AbaqusBooleanType,
    Boolean,
    BooleanType,
    SymbolicConstantType,
)
from abaqus.UtilityAndView.Repository import Repository

NoneType = type(None)


MdbType = Mdb
BackwardCompatibilityType = BackwardCompatibility
SessionType = Session
RepositoryType = Repository


# Inspected from Abaqus/CAE 2021 Command Line Interface
__all__ = [
    "AbaqusBoolean",
    "AbaqusBooleanType",
    # 'AbaqusException',
    # 'AbaqusShutdown',
    "BackwardCompatibilityType",
    "Boolean",
    "BooleanType",
    "CFD",
    "EMAG",
    "FALSE",
    "Mdb",
    "MdbType",
    "NOT_SET",
    "NoneType",
    "OFF",
    "ON",
    "RepositoryType",
    "SCATTERED",
    "STANDARD_EXPLICIT",
    "STEP_END",
    "SessionType",
    "SymbolicConstant",
    "SymbolicConstantType",
    "TOTAL",
    "TRUE",
    # '__builtins__',
    # '__doc__',
    # '__name__',
    # '__package__',
    # '_fireQuery',
    # '_getCurrentExecFileCmd',
    # '_getDebug',
    # '_getMdbSchema',
    # '_getMdbUpToDateStatus',
    # '_getShowDisplaysState',
    # '_getShowLandmarksState',
    # '_getShowVerbosesState',
    # '_getShowWarningsState',
    # '_getWarningReply',
    # '_journalMethodCallInternal',
    # '_listDebug',
    # '_pprint',
    # '_printToCli',
    # '_replayCapture',
    # '_setCallVerifyMdb',
    # '_setDebug',
    # '_setImportModuleHook',
    # '_setMessagesState',
    # '_shutdowm',
    # '_upgradeTableMdb',
    # 'addCmdToCommandHistory',
    # 'applicationName',
    "backwardCompatibility",
    # 'compress',
    # 'copyrightYear',
    "getInput",
    # 'getInputs',
    # 'getMdbVersionNumbers',
    # 'getReplayFileName',
    # 'isMdbChanged',
    # 'isMdbStudentEdition',
    # 'isStudentEdition',
    # 'journalMethodDecrement',
    # 'journalMethodIncrement',
    # 'landmark',
    # 'majorVersion',
    "mdb",
    # 'mdbVersion',
    # 'milestone',
    # 'minorVersion',
    # 'odbVersion',
    # 'openMdb',
    "os",
    "re",
    # 'showStopButtonInGui',
    "sys",
    # 'uncompress',
    # 'updateVersion',
    # 'upgradeMdb',
    # 'version'
]
