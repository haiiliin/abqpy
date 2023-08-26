import ast
import os
import sys
import warnings

from .cli import abaqus

ABAQUS_COMMAND_OPTIONS = {"noGUI": True}


def run(cae: bool = True) -> None:
    """Runs Abaqus command in system's CLI.

    This function uses the top level script file to run the Abaqus
    command, and the arguments passed to it

    Parameters
    ----------
    cae : bool, optional
        Whether to use `abaqus cae` command, True for `abaqus cae`, False for `abaqus python`, by default True
    """
    # check if in debug mode and run
    debug = os.environ.get("ABQPY_DEBUG", "false").lower() == "true"
    gettrace = getattr(sys, "gettrace", None)
    debug = debug or (gettrace is not None and gettrace())

    # Check if it is imported by sphinx to generate docs
    make_docs = os.environ.get("ABQPY_MAKE_DOCS", "false").lower() == "true"

    # If in debug mode or making docs, return
    if debug:
        warnings.warn("You are running the script in debug mode, the script will run in the current Python session "
                      "and it will not be submitted to Abaqus.")  # fmt: skip
        return
    elif make_docs:
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
        filePath = os.path.relpath(main.__file__)

    # Alternative to use abaqus command line options at run time
    print("The script will be submitted to Abaqus next and the current Python session will be closed.")
    options: dict = ast.literal_eval(os.environ.get("ABAQUS_COMMAND_OPTIONS", str(ABAQUS_COMMAND_OPTIONS)))
    if cae:
        gui = options.pop("gui", None)
        noGUI = options.pop("noGUI", None)
        options["gui"] = gui if gui is not None else not noGUI if noGUI is not None else False
        abaqus.cae(filePath, *sys.argv[1:], **options)
    else:
        abaqus.python(filePath, *sys.argv[1:], **options)
    sys.exit(0)
