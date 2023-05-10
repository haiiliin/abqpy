from typing import Optional

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant
from .InteractionState import InteractionState


@abaqus_class_doc
class FluidCavityState(InteractionState):
    """The FluidCavityState object stores the propagating data for an FluidCavity object. One instance of this
    object is created internally by the FluidCavity object for each step. The instance is also deleted
    internally by the FluidCavity object. The FluidCavityState object has no constructor or methods. The
    FluidCavityState object is derived from the InteractionState object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].steps[name].interactionStates[name]
    """

    #: A SymbolicConstant specifying the propagation state of the InteractionState object.
    #: Possible values are:
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
