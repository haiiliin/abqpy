import ast
import os

from pydantic import BaseModel

defaults = ast.literal_eval(os.environ.get("ABAQUS_COMMAND_OPTIONS", str({})))
defaults.update(gui=defaults.get("gui", not defaults.pop("noGUI", True)))


class AbaqusCommandOptions(BaseModel):
    database: str | None = None
    replay: str | None = None
    recover: str | None = None
    gui: bool = False
    envstartup: bool = True
    savedOptions: bool = True
    savedGuiPrefs: bool = True
    startupDialog: bool = True
    custom: str | None = None
    guiTester: str | None = None
    guiRecord: bool | None = None
    sim: str | None = None
    log: str | None = None


options = AbaqusCommandOptions(**defaults)


class AbaqusCAEConfig(BaseModel):
    database: str | None = None
    replay: str | None = None
    recover: str | None = None
    gui: bool = False
    envstartup: bool = True
    savedOptions: bool = True
    savedGuiPrefs: bool = True
    startupDialog: bool = True
    custom: str | None = None
    guiTester: str | None = None
    guiRecord: bool | None = None


class AbaqusPythonConfig(BaseModel):
    sim: str | None = None
    log: str | None = None


class AbaqusConfig(BaseModel):
    cae: AbaqusCAEConfig
    python: AbaqusPythonConfig


trues = ["true", "1", "on", "yes"]
config = AbaqusConfig(
    cae=AbaqusCAEConfig(
        database=os.environ.get("ABAQUS_CAE_DATABASE", None) or options.database,
        replay=os.environ.get("ABAQUS_CAE_REPLAY", None) or options.replay,
        recover=os.environ.get("ABAQUS_CAE_RECOVER", None) or options.recover,
        gui=os.environ.get("ABAQUS_CAE_GUI", "").lower() in trues or options.gui,
        envstartup=os.environ.get("ABAQUS_CAE_ENVSTARTUP", "").lower() in trues or options.envstartup,
        savedOptions=os.environ.get("ABAQUS_CAE_SAVEDOPTIONS", "").lower() in trues or options.savedOptions,
        savedGuiPrefs=os.environ.get("ABAQUS_CAE_SAVEDGUIPREFS", "").lower() in trues or options.savedGuiPrefs,
        startupDialog=os.environ.get("ABAQUS_CAE_STARTUPDIALOG", "").lower() in trues or options.startupDialog,
        custom=os.environ.get("ABAQUS_CAE_CUSTOM", "") or options.custom,
        guiTester=os.environ.get("ABAQUS_CAE_GUITESTER", None) or options.guiTester,
        guiRecord=os.environ.get("ABAQUS_CAE_GUIRECORD", "").lower() in trues or options.guiRecord,
    ),
    python=AbaqusPythonConfig(
        sim=os.environ.get("ABAQUS_PYTHON_SIM", None) or options.sim,
        log=os.environ.get("ABAQUS_PYTHON_LOG", None) or options.log,
    ),
)
