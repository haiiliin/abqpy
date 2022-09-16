from abaqus.Odb.OdbCommands import *
from abaqus.UtilityAndView.BackwardCompatibility import BackwardCompatibility
from abaqus.Odb.OdbSequenceAnalyticSurfaceSegment import OdbSequenceAnalyticSurfaceSegment


def AnalyticSurfaceProfile() -> OdbSequenceAnalyticSurfaceSegment:
    """This method creates a OdbSequenceAnalyticSurfaceSegment object.
    
    Returns
    -------
    OdbSequenceAnalyticSurfaceSegment
        An :py:class:`~abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment` object.
    """
    return OdbSequenceAnalyticSurfaceSegment()


backwardCompatibility = BackwardCompatibility()
