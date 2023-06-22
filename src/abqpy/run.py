import ast
import os
import sys

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
    if debug or make_docs:
        return

    # If it is a jupyter notebook, convert it to python script
    try:  # If it is a jupyter notebook
        import ipynbname

        filePath = ipynbname.path()
        os.system(f"jupyter nbconvert --to python {filePath}")
        filePath = os.path.relpath(filePath.with_suffix(".py"))
    except (FileNotFoundError, ImportError, Exception):
        # Get the main script file
        main = sys.modules["__main__"]
        if not hasattr(main, "__file__") or main.__file__ is None:
            return
        filePath = os.path.relpath(main.__file__)

    # Alternative to use abaqus command line options at run time
    options: dict = ast.literal_eval(os.environ.get("ABAQUS_COMMAND_OPTIONS", str(ABAQUS_COMMAND_OPTIONS)))
    noGUI = options.pop("noGUI", True)
    if cae:
        options["gui"] = not noGUI
        abaqus.cae(filePath, *sys.argv[1:], **options)
    else:
        abaqus.python(filePath, *sys.argv[1:], **options)
    sys.exit(0)
