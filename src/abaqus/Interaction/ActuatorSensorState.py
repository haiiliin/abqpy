from typing import Optional

from abqpy.decorators import abaqus_class_doc
from .InteractionState import InteractionState
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class ActuatorSensorState(InteractionState):
    """The ActuatorSensorState object stores the propagating data of an actuator sensor in a
    step. One instance of this object is created internally by the ActuatorSensor object for
    each step. The instance is also deleted internally by the ActuatorSensor object.
    The ActuatorSensorState object has no constructor, methods, or members.
    The ActuatorSensorState object is derived from the InteractionState object.

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
