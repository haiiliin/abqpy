from typing import Optional

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant
from .LoadState import LoadState


@abaqus_class_doc
class BodyHeatFluxState(LoadState):
    """The BodyHeatFluxState object stores the propagating data for a Body BodyHeatFlux object in a step. One
    instance of this object is created internally by the BodyHeatFlux object for each step. The instance is also
    deleted internally by the BodyHeatFlux object. The BodyHeatFluxState object has no constructor or methods.
    The BodyHeatFluxState object is derived from the LoadState object.

    .. note::
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].loadStates[name]

        The corresponding analysis keywords are:

        - DFLUX
    """

    #: A Float specifying the Body heat flux magnitude.
    magnitude: Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the Body heat flux magnitude.
    #: Possible values are UNSET, SET, UNCHANGED, and MODIFIED.
    magnitudeState: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    amplitudeState: Optional[SymbolicConstant] = None

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
    status: Optional[SymbolicConstant] = None

    #: A String specifying the name of the amplitude reference. The String is empty if the load
    #: has no amplitude reference.
    amplitude: str = ""
