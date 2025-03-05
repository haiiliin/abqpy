import os
import sys
import warnings

from .cli import abaqus
from .config import config


class AbaqusError(Exception):
    pass


def run(cae: bool = True) -> None:
    """Runs Abaqus command in system's CLI.

    This function uses the top level script file to run the Abaqus
    command, and the arguments passed to it

    Parameters
    ----------
    cae : bool, optional
        Whether to use `abaqus cae` command, True for `abaqus cae`, False for `abaqus python`, by default True
    """
    # If making docs or skipping abaqus, do nothing
    if config.make_docs or config.skip_abaqus:
        return

    # If it is a jupyter notebook, convert it to python script
    try:  # If it is a jupyter notebook
        import ipynbname

        filePath = ipynbname.path()
        print("You are running a jupyter notebook, it will be converted to a pure python script.")
        os.system(f"jupyter nbconvert --to python {filePath}")
        filePath = os.path.relpath(filePath.with_suffix(".py"))
    except (FileNotFoundError, ImportError, Exception):
        # Get the main script file
        main = sys.modules["__main__"]
        if not hasattr(main, "__file__") or main.__file__ is None:
            raise RuntimeError("Cannot find the main script file, please run the script in a file.")

        try:
            filePath = os.path.relpath(main.__file__)
        except ValueError:
            filePath = main.__file__

    # Alternative to use abaqus command line options at run time
    print("The script will be submitted to Abaqus next and the current Python session will be closed.")
    gettrace = getattr(sys, "gettrace", None)
    if config.debug or (gettrace is not None and gettrace()):
        warnings.warn(
            "You are running the script in debug mode, the script will be opened in Abaqus PDE where you can debug it."
        )
        ret = abaqus.pde(script=filePath)
    elif cae:
        ret = abaqus.cae(filePath, *sys.argv[1:], **config.cae.model_dump())
    else:
        ret = abaqus.python(filePath, *sys.argv[1:], **config.python.model_dump())
    if config.execution_method == "subprocess":
        if ret.returncode != 0 or "Abaqus Error:" in ret.stdout:
            raise AbaqusError(f"The abaqus command exited with an error: {ret.stdout}, {ret.stderr}")
    sys.exit(0)
