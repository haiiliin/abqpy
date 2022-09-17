from typing import Optional, Any


def execfile(
    filename: str,
    globals: Optional[dict[str, Any]] = None,
    locals: Optional[dict[str, Any]] = None,
) -> None:
    """Read and execute a Python script from a file.
    The globals and locals are dictionaries, defaulting to the current
    globals and locals.  If only globals is given, locals defaults to it.
    
    Parameters
    ----------
    filename : os.PathLike
    globals : Optional[dict], optional, by default None
    locals : Optional[dict], optional, by default None
    """
    ...


def execPyFile(
    filePath: str,
    globs: Optional[dict[str, Any]] = None,
    locs: Optional[dict[str, Any]] = None,
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
    globs : Optional[dict], optional, by default None
    locs : Optional[dict], optional, by default None
    atxPort : int, optional, by default -1
    """
    ...
