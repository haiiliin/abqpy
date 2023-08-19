from __future__ import annotations

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant
from .BoundaryConditionState import BoundaryConditionState


@abaqus_class_doc
class ConnDisplacementBCState(BoundaryConditionState):
    """The ConnDisplacementBCState object stores the propagating data for a connector displacement/rotation
    boundary condition in a step. One instance of this object is created internally by the ConnDisplacementBC
    object for each step. The instance is also deleted internally by the ConnDisplacementBC object. The
    ConnDisplacementBCState object has no constructor or methods. The ConnDisplacementBCState object is derived
    from the BoundaryConditionState object.

    .. note::
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].boundaryConditionStates[name]

        The corresponding analysis keywords are:

        - CONNECTOR MOTION
    """

    #: A Float or a Complex specifying the displacement component in the connector's local
    #: 1-direction.
    u1: float | None = None

    #: A Float or a Complex specifying the displacement component in the connector's local
    #: 2-direction.
    u2: float | None = None

    #: A Float or a Complex specifying the displacement component in the connector's local
    #: 3-direction.
    u3: float | None = None

    #: A Float or a Complex specifying the rotational component in the connector's local
    #: 4-direction.
    ur1: float | None = None

    #: A Float or a Complex specifying the rotational component in the connector's local
    #: 5-direction.
    ur2: float | None = None

    #: A Float or a Complex specifying the rotational component in the connector's local
    #: 6-direction.
    ur3: float | None = None

    #: A SymbolicConstant specifying the propagation state of the displacement component in the
    #: connector's local 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
    #: MODIFIED.
    u1State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the displacement component in the
    #: connector's local 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
    #: MODIFIED.
    u2State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the displacement component in the
    #: connector's local 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
    #: MODIFIED.
    u3State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the rotational component in the
    #: connector's local 4-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
    #: MODIFIED.
    ur1State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the rotational component in the
    #: connector's local 5-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
    #: MODIFIED.
    ur2State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the rotational component in the
    #: connector's local 6-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
    #: MODIFIED.
    ur3State: SymbolicConstant

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
