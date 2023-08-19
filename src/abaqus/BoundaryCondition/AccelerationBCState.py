from __future__ import annotations

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant
from .BoundaryConditionState import BoundaryConditionState


@abaqus_class_doc
class AccelerationBCState(BoundaryConditionState):
    """The AccelerationBCState object stores the propagating data of an acceleration boundary condition in a
    step. One instance of this object is created internally by the AccelerationBC object for each step. The
    instance is also deleted internally by the AccelerationBC object. The AccelerationBCState object has no
    constructor or methods. The AccelerationBCState object is derived from the BoundaryConditionState object.

    .. note::
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].boundaryConditionStates[name]

        The corresponding analysis keywords are:

        - BOUNDARY
    """

    #: A Float specifying the acceleration component in the 1-direction.
    a1: float | None = None

    #: A Float specifying the acceleration component in the 2-direction.
    a2: float | None = None

    #: A Float specifying the acceleration component in the 3-direction.
    a3: float | None = None

    #: A Float specifying the rotational acceleration component about the 1-direction.
    ar1: float | None = None

    #: A Float specifying the rotational acceleration component about the 2-direction.
    ar2: float | None = None

    #: A Float specifying the rotational acceleration component about the 3-direction.
    ar3: float | None = None

    #: A SymbolicConstant specifying the propagation state of the acceleration component in the
    #: 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    a1State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the acceleration component in the
    #: 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    a2State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the acceleration component in the
    #: 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    a3State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the rotational acceleration
    #: component about the 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
    #: MODIFIED.
    ar1State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the rotational acceleration
    #: component about the 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
    #: MODIFIED.
    ar2State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the rotational acceleration
    #: component about the 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
    #: MODIFIED.
    ar3State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
    #: values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    amplitudeState: SymbolicConstant

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
    status: SymbolicConstant

    #: A String specifying the name of the amplitude reference. The String is empty if the
    #: boundary condition has no amplitude reference.
    amplitude: str = ""
