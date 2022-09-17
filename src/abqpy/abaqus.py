import os
import sys


def run(cae: bool = True) -> None:
    """Runs Abaqus command in system's CLI
    
    This function uses the top level script file to run the Abaqus
    command, and the arguments passed to it
    
    Parameters
    ----------
    cae : bool, optional
        Wether or not to use `abaqus cae` command or
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
    gettrace = getattr(sys, 'gettrace', None)
    exit_after = False
    if gettrace is None or not gettrace():
        exit_after = True

    if exit_after and "pytest" not in sys.modules: # Reference: https://stackoverflow.com/a/44595269/9761768
        sys.exit(0)
