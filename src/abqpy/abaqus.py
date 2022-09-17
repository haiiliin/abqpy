import os
import sys


def run(cae: bool = True) -> None:
    """Runs Abaqus command in system's CLI
    
    This function uses the top level script file to run the Abaqus
    command, and the arguments passed to it
    
    Parameters
    ----------
    cae : bool, optional
        Whether to use `abaqus cae` command or
        `abaqus python`, by default True
    """
    abaqus = os.environ.get("ABAQUS_BAT_PATH", "abaqus")
    filePath = os.path.abspath(sys.modules['__main__'].__file__)
    args = " ".join(sys.argv[1:])

    try:  # If it is a jupyter notebook
        import ipynbname
        filePath = ipynbname.path()
        os.system(f"jupyter nbconvert --to python {filePath}")
        filePath = str(filePath).replace(".ipynb", ".py")
    except (FileNotFoundError, ImportError, Exception):
        pass
    if cae:
        os.system(f"{abaqus} cae noGUI={filePath} -- {args}")
    else:
        os.system(f"{abaqus} python {filePath} {args}")
    
    # check if in debug mode and run
    debug = os.environ.get("ABQPY_DEBUG", "False").lower() == "true"
    gettrace = getattr(sys, 'gettrace', None)
    if not debug and gettrace is not None and gettrace():
        debug = True
    
    # if not in debug mode, exit the program
    if not debug:
        sys.exit(0)
