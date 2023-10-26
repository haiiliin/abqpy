from __future__ import annotations

import os
from importlib import import_module, reload

import pytest
from typing_extensions import Literal

config_module = import_module("abqpy.config")


@pytest.mark.parametrize(
    argnames="type, envs, expects",
    argvalues=[
        ("cae", dict(ABAQUS_COMMAND_OPTIONS="{'noGUI': True}"), dict(gui=False)),
        ("cae", dict(ABAQUS_COMMAND_OPTIONS="{'noGUI': True}", ABAQUS_CAE_GUI="true"), dict(gui=True)),
        ("cae", dict(ABAQUS_CAE_GUI="no"), dict(gui=False)),
        ("cae", dict(ABAQUS_CAE_DATABASE="test.odb"), dict(database="test.odb")),
        ("cae", dict(ABAQUS_CAE_REPLAY="test.rpy"), dict(replay="test.rpy")),
        ("cae", dict(ABAQUS_CAE_RECOVER="test.rpy"), dict(recover="test.rpy")),
        ("cae", dict(ABAQUS_CAE_ENVSTARTUP="off"), dict(envstartup=False)),
        ("cae", dict(ABAQUS_CAE_SAVEDOPTIONS="off"), dict(savedOptions=False)),
        ("cae", dict(ABAQUS_CAE_SAVEDGUIPREFS="off"), dict(savedGuiPrefs=False)),
        ("cae", dict(ABAQUS_CAE_STARTUPDIALOG="off"), dict(startupDialog=False)),
        ("cae", dict(ABAQUS_CAE_CUSTOM="test.py"), dict(custom="test.py")),
        ("cae", dict(ABAQUS_CAE_GUITESTER="test.py"), dict(guiTester="test.py")),
        ("python", dict(ABAQUS_PYTHON_SIM="test.py"), dict(sim="test.py")),
        ("python", dict(ABAQUS_PYTHON_LOG="test.log"), dict(log="test.log")),
    ],
    ids=["GUI", "GUI override", "GUI off", "database", "replay", "recover", "envstartup", "savedOptions",
         "savedGuiPrefs", "startupDialog", "custom", "guiTester", "sim", "log"],  # fmt: skip
)
def test_config(type: Literal["cae", "python"], envs: dict[str, str], expects: dict[str, str | bool]):
    for key, env in envs.items():
        os.environ[key] = env

    config = reload(config_module)
    for key, expect in expects.items():
        actual = getattr(config.config.cae if type == "cae" else config.config.python, key)
        assert actual == expect, f"Expected {key} to be {expect}, got {actual}"

    for key, env in envs.items():
        del os.environ[key]
