from __future__ import annotations

import ast
import os
from typing import Optional

from pydantic import BaseModel


class AbaqusCAEConfig(BaseModel):
    database: Optional[str] = None
    replay: Optional[str] = None
    recover: Optional[str] = None
    gui: bool = False
    envstartup: bool = True
    savedOptions: bool = True
    savedGuiPrefs: bool = True
    startupDialog: bool = True
    custom: Optional[str] = None
    guiTester: Optional[str] = None
    guiRecord: Optional[bool] = None


class AbaqusPythonConfig(BaseModel):
    sim: Optional[str] = None
    log: Optional[str] = None


class AbaqusConfig(BaseModel):
    cae: AbaqusCAEConfig
    python: AbaqusPythonConfig


class AbaqusCommandOptions(AbaqusCAEConfig, AbaqusPythonConfig):
    ...


defaults = ast.literal_eval(os.environ.get("ABAQUS_COMMAND_OPTIONS", str({})))
defaults.update(gui=defaults.get("gui", not defaults.pop("noGUI", True)))
options = AbaqusCommandOptions(**defaults)


trues = ["true", "1", "on", "yes"]
config = AbaqusConfig(
    cae=AbaqusCAEConfig(
        database=os.environ["ABAQUS_CAE_DATABASE"] if "ABAQUS_CAE_DATABASE" in os.environ else options.database,
        replay=os.environ["ABAQUS_CAE_REPLAY"] if "ABAQUS_CAE_REPLAY" in os.environ else options.replay,
        recover=os.environ["ABAQUS_CAE_RECOVER"] if "ABAQUS_CAE_RECOVER" in os.environ else options.recover,
        gui=os.environ["ABAQUS_CAE_GUI"].lower() in trues if "ABAQUS_CAE_GUI" in os.environ else options.gui,
        envstartup=(
            os.environ["ABAQUS_CAE_ENVSTARTUP"].lower() in trues
            if "ABAQUS_CAE_ENVSTARTUP" in os.environ
            else options.envstartup
        ),
        savedOptions=(
            os.environ["ABAQUS_CAE_SAVEDOPTIONS"].lower() in trues
            if "ABAQUS_CAE_SAVEDOPTIONS" in os.environ
            else options.savedOptions
        ),
        savedGuiPrefs=(
            os.environ["ABAQUS_CAE_SAVEDGUIPREFS"].lower() in trues
            if "ABAQUS_CAE_SAVEDGUIPREFS" in os.environ
            else options.savedGuiPrefs
        ),
        startupDialog=(
            os.environ["ABAQUS_CAE_STARTUPDIALOG"].lower() in trues
            if "ABAQUS_CAE_STARTUPDIALOG" in os.environ
            else options.startupDialog
        ),
        custom=os.environ["ABAQUS_CAE_CUSTOM"] if "ABAQUS_CAE_CUSTOM" in os.environ else options.custom,
        guiTester=os.environ["ABAQUS_CAE_GUITESTER"] if "ABAQUS_CAE_GUITESTER" in os.environ else options.guiTester,
        guiRecord=(
            os.environ["ABAQUS_CAE_GUIRECORD"].lower() in trues
            if "ABAQUS_CAE_GUIRECORD" in os.environ
            else options.guiRecord
        ),
    ),
    python=AbaqusPythonConfig(
        sim=os.environ["ABAQUS_PYTHON_SIM"] if "ABAQUS_PYTHON_SIM" in os.environ else options.sim,
        log=os.environ["ABAQUS_PYTHON_LOG"] if "ABAQUS_PYTHON_LOG" in os.environ else options.log,
    ),
)
