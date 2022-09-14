from abqpy.decorators import abaqus_class_doc
from .BoundaryConditionState import BoundaryConditionState
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class VelocityBCState(BoundaryConditionState):
    """The VelocityBCState object stores the propagating data for a velocity boundary condition
    in a step. One instance of this object is created internally by the VelocityBC object
    for each step. The instance is also deleted internally by the VelocityBC object.
    The VelocityBCState object has no constructor or methods.
    The VelocityBCState object is derived from the BoundaryConditionState object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].boundaryConditionStates[name]

        The corresponding analysis keywords are:

        - BOUNDARY
    """

    #: A Float specifying the velocity component in the 1-direction.
    v1: float = None

    #: A Float specifying the velocity component in the 2-direction.
    v2: float = None

    #: A Float specifying the velocity component in the 3-direction.
    v3: float = None

    #: A Float specifying the rotational velocity component about the 1-direction.
    vr1: float = None

    #: A Float specifying the rotational velocity component about the 2-direction.
    vr2: float = None

    #: A Float specifying the rotational velocity component about the 3-direction.
    vr3: float = None

    #: A SymbolicConstant specifying the propagation state of the velocity component in the
    #: 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    v1State: SymbolicConstant = None

    #: A SymbolicConstant specifying the propagation state of the velocity component in the
    #: 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    v2State: SymbolicConstant = None

    #: A SymbolicConstant specifying the propagation state of the velocity component in the
    #: 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    v3State: SymbolicConstant = None

    #: A SymbolicConstant specifying the propagation state of the rotational velocity component
    #: about the 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    vr1State: SymbolicConstant = None

    #: A SymbolicConstant specifying the propagation state of the rotational velocity component
    #: about the 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    vr2State: SymbolicConstant = None

    #: A SymbolicConstant specifying the propagation state of the rotational velocity component
    #: about the 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    vr3State: SymbolicConstant = None

    #: A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
    #: values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    amplitudeState: SymbolicConstant = None

    #: A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:
    #: 
    #: - NOT_YET_ACTIVE
    #: - CREATED
    #: - PROPAGATED
    #: - MODIFIED
    #: - DEACTIVATED
    #: - NO_LONGER_ACTIVE
    #: - TYPE_NOT_APPLICABLE
    #: - INSTANCE_NOT_APPLICABLE
    #: - PROPAGATED_FROM_BASE_STATE
    #: - MODIFIED_FROM_BASE_STATE
    #: - DEACTIVATED_FROM_BASE_STATE
    #: - BUILT_INTO_MODES
    status: SymbolicConstant = None

    #: A String specifying the name of the amplitude reference. The String is empty if the
    #: boundary condition has no amplitude reference.
    amplitude: str = ""
