from pathlib import Path

from setuptools import setup

setup(py_modules=[p.stem for p in Path("src").glob("*.py")])
