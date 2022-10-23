from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ..UtilityAndView.abaqusConstants import SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class AnalyticSurfaceSegment:
    """An individual segment of the analytic surface.

    .. note::
        This object can be accessed by::

            import odbAccess
            session.odbs[name].parts[name].analyticSurface.segments[i]
            session.odbs[name].rootAssembly.instances[name].analyticSurface.segments[i]
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.analyticSurface.segments[i]
    """

    #: A SymbolicConstant specifying the type of AnalyticSurfaceSegment. Possible values are
    #: START, LINE, CIRCLE, and PARABOLA.
    type: SymbolicConstant

    #: A sequence of sequences of Floats specifying the coordinates of point/s representing the
    #: segment of the AnalyticSurface object. If **type** = CIRCLE, the first row contains
    #: coordinates of the end point and the second row contains coordinates of the center
    #: point. If **type** = PARABOLA, the first row contains coordinates of the middle point and
    #: the second row contains coordinates of the end point. If **type** = START or **type** = LINE, a
    #: single row contains coordinates of the start/end point.
    data: tuple

    @abaqus_method_doc
    def __init__(self, type: Literal[C.CIRCLE, C.START, C.LINE, C.PARABOLA], data: tuple):
        """This method creates an AnalyticSurfaceSegment object.

        .. note::
            This function can be accessed by::

                odbAccess.AnalyticSurfaceSegment

        Parameters
        ----------
        type
            A SymbolicConstant specifying the type of AnalyticSurfaceSegment. Possible values are
            START, LINE, CIRCLE, and PARABOLA.
        data
            A sequence of sequences of Floats specifying the coordinates of point/s representing the
            segment of the AnalyticSurface object. If **type** = CIRCLE, the first row contains
            coordinates of the end point and the second row contains coordinates of the center
            point. If **type** = PARABOLA, the first row contains coordinates of the middle point and
            the second row contains coordinates of the end point. If **type** = START or **type** = LINE, a
            single row contains coordinates of the start/end point.

        Returns
        -------
        AnalyticSurfaceSegment
            An :py:class:`~abaqus.Odb.AnalyticSurfaceSegment.AnalyticSurfaceSegment` object.
        """
        ...
