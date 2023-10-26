from __future__ import annotations

import os

from importlib import reload, import_module

import pytest
from typing_extensions import Literal


config_module = import_module("abqpy.config")


def verify_config(type: Literal["cae", "python"], envs: dict[str, str], expects: dict[str, str | bool]):
    for key, env in envs.items():
        os.environ[key] = env

    config = reload(config_module)
    for key, expect in expects.items():
        actual = getattr(config.config.cae if type == "cae" else config.config.python, key)
        assert actual == expect, f"Expected {key} to be {expect}, got {actual}"

    for key, env in envs.items():
        del os.environ[key]


@pytest.mark.parametrize(
    argnames="envs, expects",
    argvalues=[
        (dict(ABAQUS_COMMAND_OPTIONS="{'gui': True}"), dict(gui=True)),
        (dict(ABAQUS_COMMAND_OPTIONS="{'gui': True}", ABAQUS_CAE_GUI="on"), dict(gui=True)),
        (dict(ABAQUS_CAE_GUI="no"), dict(gui=False)),
        (dict(ABAQUS_CAE_DATABASE="test.odb"), dict(database="test.odb")),
        (dict(ABAQUS_CAE_REPLAY="test.rpy"), dict(replay="test.rpy")),
        (dict(ABAQUS_CAE_RECOVER="test.rpy"), dict(recover="test.rpy")),
        (dict(ABAQUS_CAE_ENVSTARTUP="off"), dict(envstartup=False)),
        (dict(ABAQUS_CAE_SAVEDOPTIONS="off"), dict(savedOptions=False)),
        (dict(ABAQUS_CAE_SAVEDGUIPREFS="off"), dict(savedGuiPrefs=False)),
        (dict(ABAQUS_CAE_STARTUPDIALOG="off"), dict(startupDialog=False)),
        (dict(ABAQUS_CAE_CUSTOM="test.py"), dict(custom="test.py")),
        (dict(ABAQUS_CAE_GUITESTER="test.py"), dict(guiTester="test.py")),
    ],
    ids=["GUI", "GUI override", "GUI off", "database", "replay", "recover", "envstartup", "savedOptions",
         "savedGuiPrefs", "startupDialog", "custom", "guiTester"],  # fmt: skip
)
def test_cae_config(envs: dict[str, str], expects: dict[str, str | bool]):
    verify_config("cae", envs, expects)


@pytest.mark.parametrize(
    argnames="envs, expects",
    argvalues=[
        (dict(ABAQUS_PYTHON_SIM="test.py"), dict(sim="test.py")),
        (dict(ABAQUS_PYTHON_LOG="test.log"), dict(log="test.log")),
    ],
    ids=["sim", "log"],  # fmt: skip
)
def test_python_config(envs: dict[str, str], expects: dict[str, str | bool]):
    verify_config("python", envs, expects)
