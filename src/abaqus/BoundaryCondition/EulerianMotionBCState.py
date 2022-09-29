import typing
from abqpy.decorators import abaqus_class_doc
from .BoundaryConditionState import BoundaryConditionState
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class EulerianMotionBCState(BoundaryConditionState):
    """The EulerianMotionBCState object stores the propagating data for an Eulerian mesh motion
    boundary condition in a step. One instance of this object is created internally by the
    EulerianMotionBC object for each step. The instance is also deleted internally by the
    EulerianMotionBC object.
    The EulerianMotionBCState object has no constructor or methods.
    The EulerianMotionBCState object is derived from the BoundaryConditionState object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].boundaryConditionStates[name]

        The corresponding analysis keywords are:

        - EULERIAN MESH MOTION
    """

    #: A SymbolicConstant specifying the 1-direction translational constraint on the center of
    #: the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.
    ctrPosition1: SymbolicConstant = FREE

    #: A SymbolicConstant specifying the 2-direction translational constraint on the center of
    #: the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.
    ctrPosition2: SymbolicConstant = FREE

    #: A SymbolicConstant specifying the 3-direction translational constraint on the center of
    #: the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.
    ctrPosition3: SymbolicConstant = FREE

    #: A SymbolicConstant specifying the translational constraint on the positive (maximum)
    #: bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
    #: value is FREE.
    posPosition1: SymbolicConstant = FREE

    #: A SymbolicConstant specifying the translational constraint on the positive (maximum)
    #: bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
    #: value is FREE.
    posPosition2: SymbolicConstant = FREE

    #: A SymbolicConstant specifying the translational constraint on the positive (maximum)
    #: bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
    #: value is FREE.
    posPosition3: SymbolicConstant = FREE

    #: A SymbolicConstant specifying the translational constraint on the negative (minimum)
    #: bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
    #: value is FREE.
    negPosition1: SymbolicConstant = FREE

    #: A SymbolicConstant specifying the translational constraint on the negative (minimum)
    #: bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
    #: value is FREE.
    negPosition2: SymbolicConstant = FREE

    #: A SymbolicConstant specifying the translational constraint on the negative (minimum)
    #: bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
    #: value is FREE.
    negPosition3: SymbolicConstant = FREE

    #: None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
    #: 1 direction. If **expansionRatio1** = None, then there is no upper limit. The default value
    #: is None.
    expansionRatio1: typing.Optional[float] = None

    #: None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
    #: 2 direction. If **expansionRatio2** = None, then there is no upper limit. The default value
    #: is None.
    expansionRatio2: typing.Optional[float] = None

    #: None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
    #: 3 direction. If **expansionRatio3** = None, then there is no upper limit. The default value
    #: is None.
    expansionRatio3: typing.Optional[float] = None

    #: A Float specifying the lower bounds on the allowable scaling of the mesh in the 1
    #: direction. The default value is 0.0.
    contractRatio1: float = 0

    #: A Float specifying the lower bounds on the allowable scaling of the mesh in the 2
    #: direction. The default value is 0.0.
    contractRatio2: float = 0

    #: A Float specifying the lower bounds on the allowable scaling of the mesh in the 3
    #: direction. The default value is 0.0.
    contractRatio3: float = 0

    #: A Boolean specifying whether the mesh is allowed to contract . The default value is ON.
    allowContraction: Boolean = ON

    #: A Float specifying the maximum change in allowed aspect ratio (for any of the three mesh
    #: aspects, 1-2, 2-3, 3-1). The default value is 10.0.
    aspectLimit: float = 10

    #: A Float specifying the multiplier for the mesh nodal velocity limit. The default value
    #: is 1.01.
    vmaxFactor: float = 1

    #: A Float specifying the lower bounds on the volume fraction when determining which nodes
    #: to include in the surface bounding box calculation for an Eulerian material surface.
    #: This argument applies only when **followRegion** = False. The default value is 0.5.
    volThreshold: float = 0

    #: None or a Float specifying the buffer between the surface box and the Eulerian section
    #: mesh bounding box. The default value is 2.0.
    bufferSize: float = 2

    #: A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
    #: values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    amplitudeState: typing.Optional[SymbolicConstant] = None

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
    status: typing.Optional[SymbolicConstant] = None

    #: A String specifying the name of the amplitude reference. The String is empty if the
    #: boundary condition has no amplitude reference.
    amplitude: str = ""
