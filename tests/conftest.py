"""
conftest.py: sharing fixtures across multiple files. https://docs.pytest.org/en/7.1.x/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files.
"""
import os
import sys
import pytest


def pytest_configure(config: pytest.Config) -> None:
    """Allow plugins and conftest files to perform initial configuration.

    This hook is called for every plugin and initial conftest file after command line options have been parsed.

    After that, the hook is called for other conftest files as they are imported.

    Args:
        config (pytest.Config): The pytest config object.
    """
    os.environ['ABQPY_DEBUG'] = 'true'
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, os.path.abspath('../src'))
