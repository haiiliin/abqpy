from abqpy.decorators import abaqus_class_doc
from .BoundaryConditionState import BoundaryConditionState
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class EulerianBCState(BoundaryConditionState):
    """The EulerianBCState object stores the propagating data for an Eulerian boundary
    condition in a step. One instance of this object is created internally by the EulerianBC
    object for each step. The instance is also deleted internally by the EulerianBC object.
    The EulerianBCState object has no constructor or methods.
    The EulerianBCState object is derived from the BoundaryConditionState object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].boundaryConditionStates[name]

        The corresponding analysis keywords are:

        - EULERIAN BOUNDARY
    """

    #: A SymbolicConstant specifying the material flow conditions to be defined. Possible
    #: values are INFLOW, OUTFLOW, and BOTH. The default value is INFLOW.
    definition: SymbolicConstant = INFLOW

    #: A SymbolicConstant specifying the propagation state of the definition member. Possible
    #: values are UNSET, SET, and UNCHANGED.
    definitionState: SymbolicConstant = None

    #: A SymbolicConstant specifying the material flow conditions to be defined. Possible
    #: values are FREE, NONE, and VOID. The default value is FREE.
    inflowType: SymbolicConstant = FREE

    #: A SymbolicConstant specifying the propagation state of the definition member. Possible
    #: values are UNSET, SET, and UNCHANGED.
    inflowTypeState: SymbolicConstant = None

    #: A SymbolicConstant specifying the material flow conditions to be defined. Possible
    #: values are ZERO_PRESSURE, FREE, NON_REFLECTING, and EQUILIBRIUM. The default value is
    #: ZERO_PRESSURE.
    outflowType: SymbolicConstant = ZERO_PRESSURE

    #: A SymbolicConstant specifying the propagation state of the definition member. Possible
    #: values are UNSET, SET, and UNCHANGED.
    outflowTypeState: SymbolicConstant = None

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
