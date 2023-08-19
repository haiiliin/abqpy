from __future__ import annotations

from typing import Any


def execfile(
    filename: str,
    globals: dict[str, Any] | None = None,
    locals: dict[str, Any] | None = None,
) -> None:
    """Read and execute a Python script from a file. The globals and locals are dictionaries, defaulting to the
    current globals and locals.  If only globals is given, locals defaults to it.

    Parameters
    ----------
    filename : os.PathLike
    globals : dict | None, optional, by default None
    locals : dict | None, optional, by default None
    """
    ...


def execPyFile(
    filePath: str,
    globs: dict[str, Any] | None = None,
    locs: dict[str, Any] | None = None,
    atxPort: int = -1,
) -> None:
    """Similar to execfile, but will run a compiled .pyc file
    The default globals and locals must be those of the caller
    Reference:
    http://www.python.org/search/hypermail/python-recent/0186.html
    If atxPort != -1, being used to run Kernel from external tester

    Parameters
    ----------
    filePath : os.PathLike
    globs : dict | None, optional, by default None
    locs : dict | None, optional, by default None
    atxPort : int, optional, by default -1
    """
    ...


def raw_input(prompt: str = "") -> str:
    """Read a string from standard input.  The trailing newline is stripped. If the user hits EOF (Unix: Ctl-D,
    Windows: Ctl-Z+Return), raise EOFError. On Unix, GNU readline is used if enabled.  The prompt string, if
    given, is printed without a trailing newline before reading.

    Parameters
    ----------
    prompt : str, optional
        The prompt written to standard output, by default ''

    Returns
    -------
    str
        The input value converted to a string
    """
    return input(prompt)


def cliCommand(text: str) -> None:
    """Excutes Abaqus/CAE CLI command.

    called from cmdK_CommandDeliveryRole::sendCliCommand

    Parameters
    ----------
    text : str
        Command
    """
    ...
