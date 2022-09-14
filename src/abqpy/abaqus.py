import os
import sys


def run(cae=True, exit_after=True):
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
    if exit_after:
        sys.exit(0)
