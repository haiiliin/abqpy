from typing import Optional

from abqpy.decorators import abaqus_class_doc
from .InteractionState import InteractionState
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class StdXplCosimulationState(InteractionState):
    """The StdXplCosimulationState object stores the propagating data for a StdXplCosimulation
    object. One instance of this object is created internally by the StdXplCosimulation
    object for each step. The instance is also deleted internally by the StdXplCosimulation
    object.
    The StdXplCosimulationState object has no constructor or methods.
    The StdXplCosimulationState object is derived from the InteractionState object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].steps[name].interactionStates[name]

        The corresponding analysis keywords are:

        - CO-SIMULATION
                - CO-SIMULATION REGION
                - CO-SIMULATION CONTROLS
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
