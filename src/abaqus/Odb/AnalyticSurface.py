from typing import Optional

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant
from .OdbSequenceAnalyticSurfaceSegment import OdbSequenceAnalyticSurfaceSegment


@abaqus_class_doc
class AnalyticSurface:
    """The AnalyticSurface object is a geometric surface that can be described with straight and/or curved line
    segments.

    .. note::
        This object can be accessed by::

            import odbAccess
            session.odbs[name].parts[name].analyticSurface
            session.odbs[name].rootAssembly.instances[name].analyticSurface
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.analyticSurface
    """

    #: A String specifying the name of the analytic surface.
    name: str = ""

    #: A SymbolicConstant specifying the type of AnalyticSurface object. Possible values are
    #: SEGMENTS, CYLINDER, and REVOLUTION.
    type: Optional[SymbolicConstant] = None

    #: A Float specifying radius of curvature to smooth discontinuities between adjoining
    #: segments. The default value is 0.0.
    filletRadius: float = 0

    #: An OdbSequenceAnalyticSurfaceSegment object specifying the profile associated with the
    #: surface.
    segments: OdbSequenceAnalyticSurfaceSegment = OdbSequenceAnalyticSurfaceSegment()

    #: A tuple of tuples of Floats specifying the global coordinates of points representing the
    #: local coordinate system, if used.
    localCoordData: Optional[float] = None
