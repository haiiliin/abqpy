import os
import sys
from abaqus.Odb.OdbCommands import *
from abaqus.UtilityAndView.BackwardCompatibility import BackwardCompatibility


def openOdb(name: str, *args, **kwargs) -> Odb:
    abaqus = 'abaqus'
    if 'ABAQUS_BAT_PATH' in os.environ.keys():
        abaqus = os.environ['ABAQUS_BAT_PATH']

    filePath = os.path.abspath(sys.argv[0])
    fileDir = os.path.dirname(filePath)
    fileName = os.path.basename(filePath)
    odbName = os.path.basename(os.path.abspath(name))

    os.system(f'cd {fileDir}')
    try:  # If it is a jupyter notebook
        import ipynbname
        fileName = os.path.basename(ipynbname.path())
        os.system(f'jupyter nbconvert --to python {fileName}')
        fileName = fileName.replace('.ipynb', '.py')
    except:
        pass
    os.system(f'{abaqus} cae database={odbName} script={fileName}')
    sys.exit()
    return Odb(name)


backwardCompatibility = BackwardCompatibility()
