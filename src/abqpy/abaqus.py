import ast
import os
import sys
from typing import Dict, Union

ABAQUS_COMMAND_OPTIONS = {"noGUI": True}


def run(cae: bool = True) -> None:
    """Runs Abaqus command in system's CLI

    This function uses the top level script file to run the Abaqus
    command, and the arguments passed to it

    Parameters
    ----------
    cae : bool, optional
        Whether to use `abaqus cae` command, True for `abaqus cae`, False for `abaqus python`, by default True
    """
    abaqus = os.environ.get("ABAQUS_BAT_PATH", "abaqus")
    main = sys.modules["__main__"]
    if not hasattr(main, "__file__") or main.__file__ is None:
        return

    filePath = os.path.abspath(main.__file__)
    args = " ".join(sys.argv[1:])

    try:  # If it is a jupyter notebook
        import ipynbname

        filePath = ipynbname.path()
        os.system(f"jupyter nbconvert --to python {filePath}")
        filePath = str(filePath).replace(".ipynb", ".py")
    except (FileNotFoundError, ImportError, Exception):
        pass

    # check if in debug mode and run
    debug = os.environ.get("ABQPY_DEBUG", "false").lower() == "true"
    gettrace = getattr(sys, "gettrace", None)
    debug = debug or (gettrace is not None and gettrace())

    # Check if it is imported by sphinx to generate docs
    make_docs = os.environ.get("ABQPY_MAKE_DOCS", "false").lower() == "true"

    # Alternative to use abaqus command line options at run time
    abq_cmd_opt: Dict[str, Union[str, bool]] = ast.literal_eval(
        os.environ.get("ABAQUS_COMMAND_OPTIONS", str(ABAQUS_COMMAND_OPTIONS))
    )

    if cae:
        proc = "cae"
        mode = f'noGUI="{filePath}"' if abq_cmd_opt.pop("noGUI", True) else f'script="{filePath}"'
        sep = "--" if args else ""
    else:
        proc = "python"
        mode = f'"{filePath}"'
        sep = ""

    options = [
        f"{key}={value}" if isinstance(value, str) else f"{key}" if value else "" for key, value in abq_cmd_opt.items()
    ]

    # If in debug mode do not run the abaqus command at all
    if not debug and not make_docs:
        cmd = f"{abaqus} {proc} {mode} {' '.join(options)} {sep} {' '.join(args)}".strip()
        message = f"Running the following abaqus command: {cmd}"
        print("", "-" * len(message), message, "-" * len(message), sep="\n")
        os.system(cmd)
        sys.exit(0)
