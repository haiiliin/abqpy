from typing import Optional

from abqpy.decorators import abaqus_class_doc

from .InteractionState import InteractionState
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class PressurePenetrationState(InteractionState):
    """The PressurePenetrationState object stores the propagating data of a PressurePenetration
    object in a step. One instance of this object is created internally by the
    PressurePenetration object for each step. The instance is also deleted internally by the
    PressurePenetration object.
    The PressurePenetrationState object has no constructor or methods.
    The PressurePenetrationState object is derived from the InteractionState object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].steps[name].interactionStates[name]

        The corresponding analysis keywords are:

        - PRESSURE PENETRATION
    """

    #: A Float specifying the fraction of the current step time over which the fluid pressure
    #: on newly penetrated contact surface segments is ramped up to the current magnitude. The
    #: default value is 10-3.
    penetrationTime: Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the **penetrationTime** member.
    #: Possible values are UNSET, SET, UNCHANGED, and FREED.
    penetrationTimeState: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    amplitudeState: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the **criticalPressure** member.
    #: Possible values are UNSET, SET, UNCHANGED, and FREED.
    criticalPressureState: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the **penetrationPressure** member.
    #: Possible values are UNSET, SET, UNCHANGED, and FREED.
    penetrationPressureState: Optional[SymbolicConstant] = None

    #: A tuple of Floats specifying the fluid pressure magnitude. For steady state dynamic
    #: analyses, a tuple of Complexes specifying the fluid pressure magnitude.
    penetrationPressure: Optional[float] = None

    #: A String specifying the name of the amplitude reference. The String is empty if the load
    #: has no amplitude reference.
    amplitude: str = ""

    #: A tuple of Floats specifying the critical contact pressure below which fluid penetration
    #: starts to occur.
    criticalPressure: Optional[float] = None

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
