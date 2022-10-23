from typing import Optional

from abqpy.decorators import abaqus_class_doc

from .InteractionState import InteractionState
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class FluidExchangeState(InteractionState):
    """The FluidExchangeState object stores the propagating data for an FluidExchange object.
    One instance of this object is created internally by the FluidExchange object for each
    step. The instance is also deleted internally by the FluidExchange object.
    The FluidExchangeState object has no constructor or methods.
    The FluidExchangeState object is derived from the InteractionState object.

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
