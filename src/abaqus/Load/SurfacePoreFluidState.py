from abqpy.decorators import abaqus_class_doc
from .LoadState import LoadState
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class SurfacePoreFluidState(LoadState):
    """The SurfacePoreFluidState object stores the propagating data for a SurfacePoreFluid
    object in a step. One instance of this object is created internally by the
    SurfacePoreFluid object for each step. The instance is also deleted internally by the
    SurfacePoreFluid object.
    The SurfacePoreFluidState object has no constructor or methods.
    The SurfacePoreFluidState object is derived from the LoadState object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].loadStates[name]

        The corresponding analysis keywords are:

        - DSFLOW
    """

    #: A Float specifying the surface pore fluid flow magnitude.
    magnitude: float = None

    #: A SymbolicConstant specifying the propagation state of the surface pore fluid flow
    #: magnitude. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.
    magnitudeState: SymbolicConstant = None

    #: A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    amplitudeState: SymbolicConstant = None

    #: A SymbolicConstant specifying the propagation state of the LoadState object. Possible
    #: values are:
    #: 
    #: - NOT_YET_ACTIVE
    #: - CREATED
    #: - PROPAGATED
    #: - MODIFIED
    #: - DEACTIVATED
    #: - NO_LONGER_ACTIVE
    #: - TYPE_NOT_APPLICABLE
    #: - INSTANCE_NOT_APPLICABLE
    #: - BUILT_INTO_BASE_STATE
    status: SymbolicConstant = None

    #: A String specifying the name of the amplitude reference. The String is empty if the load
    #: has no amplitude reference.
    amplitude: str = ""
