import os
import sys
from abaqus.Odb.OdbCommands import *
from abaqus.UtilityAndView.BackwardCompatibility import BackwardCompatibility
from abaqus.Odb.OdbSequenceAnalyticSurfaceSegment import OdbSequenceAnalyticSurfaceSegment

def openOdb(name: str, *args, **kwargs) -> Odb:
    abaqus = 'abaqus'
    if 'ABAQUS_BAT_PATH' in os.environ.keys():
        abaqus = os.environ['ABAQUS_BAT_PATH']

    filePath = os.path.abspath(sys.argv[0])

    try:  # If it is a jupyter notebook
        import ipynbname

        filePath = ipynbname.path()
        os.system(f"jupyter nbconvert --to python {filePath}")
        filePath = filePath.replace(".ipynb", ".py")
    except:
        pass
    os.system(f'{abaqus} python {filePath}')
    sys.exit()
    return Odb(name)

def AnalyticSurfaceProfile() -> OdbSequenceAnalyticSurfaceSegment:
    """This method creates a OdbSequenceAnalyticSurfaceSegment object.
    
    Returns
    -------
    OdbSequenceAnalyticSurfaceSegment
        An :py:class:`~abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment` object.
    """
    return OdbSequenceAnalyticSurfaceSegment()

backwardCompatibility = BackwardCompatibility()
