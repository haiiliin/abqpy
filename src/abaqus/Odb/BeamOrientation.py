import typing
from abqpy.decorators import abaqus_class_doc
from .OdbSet import OdbSet
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class BeamOrientation:
    """The BeamOrientation object represents the direction of the first beam section axis n1n1.
    Specifying the beam orientation using an additional node in the element connectivity
    list is not supported.

    .. note:: 
        This object can be accessed by::

            import odbAccess
            session.odbs[name].parts[name].beamOrientations[i]
            session.odbs[name].rootAssembly.instances[name].beamOrientations[i]
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.beamOrientations[i]
    """

    #: A SymbolicConstant specifying the orientation assignment method. Possible values are
    #: N1_COSINES, CSYS, and VECT.
    method: typing.Optional[SymbolicConstant] = None

    #: An :py:class:`~abaqus.Odb.OdbSet.OdbSet` object specifying a region for which the beam orientation is defined.
    region: OdbSet = OdbSet("set", ())

    #: A tuple of Floats specifying direction cosines of the n1-direction of the beam
    #: cross-section.
    vector: typing.Optional[float] = None
