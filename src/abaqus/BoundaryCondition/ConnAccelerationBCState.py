from typing import Optional

from abqpy.decorators import abaqus_class_doc
from .BoundaryConditionState import BoundaryConditionState
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class ConnAccelerationBCState(BoundaryConditionState):
    """The ConnAccelerationBCState object stores the propagating data of a connector
    acceleration boundary condition in a step. One instance of this object is created
    internally by the ConnAccelerationBC object for each step. The instance is also deleted
    internally by the ConnAccelerationBC object.
    The ConnAccelerationBCState object has no constructor or methods.
    The ConnAccelerationBCState object is derived from the BoundaryConditionState object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].boundaryConditionStates[name]

        The corresponding analysis keywords are:

        - CONNECTOR MOTION
    """

    #: A Float specifying the connector acceleration component in the connector's local
    #: 1-direction.
    a1: Optional[float] = None

    #: A Float specifying the connector acceleration component in the connector's local
    #: 2-direction.
    a2: Optional[float] = None

    #: A Float specifying the connector acceleration component in the connector's local
    #: 3-direction.
    a3: Optional[float] = None

    #: A Float specifying the connector acceleration component in the connector's local
    #: 4-direction.
    ar1: Optional[float] = None

    #: A Float specifying the connector acceleration component in the connector's local
    #: 5-direction.
    ar2: Optional[float] = None

    #: A Float specifying the connector acceleration component in the connector's local
    #: 6-direction.
    ar3: Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the connector acceleration
    #: component in the connector's local 1-direction. Possible values are UNSET, SET,
    #: UNCHANGED, FREED, and MODIFIED.
    a1State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the connector acceleration
    #: component in the connector's local 2-direction. Possible values are UNSET, SET,
    #: UNCHANGED, FREED, and MODIFIED.
    a2State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the connector acceleration
    #: component in the connector's local 3-direction. Possible values are UNSET, SET,
    #: UNCHANGED, FREED, and MODIFIED.
    a3State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the connector acceleration
    #: component in the connector's local 4-direction. Possible values are UNSET, SET,
    #: UNCHANGED, FREED, and MODIFIED.
    ar1State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the connector acceleration
    #: component in the connector's local 5-direction. Possible values are UNSET, SET,
    #: UNCHANGED, FREED, and MODIFIED.
    ar2State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the connector acceleration
    #: component in the connector's local 6-direction. Possible values are UNSET, SET,
    #: UNCHANGED, FREED, and MODIFIED.
    ar3State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
    #: values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    amplitudeState: Optional[SymbolicConstant] = None

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
    status: Optional[SymbolicConstant] = None

    #: A String specifying the name of the amplitude reference. The String is empty if the
    #: boundary condition has no amplitude reference.
    amplitude: str = ""
