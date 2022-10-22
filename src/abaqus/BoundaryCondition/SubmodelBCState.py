from typing import Optional

from abqpy.decorators import abaqus_class_doc

from .BoundaryConditionState import BoundaryConditionState
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class SubmodelBCState(BoundaryConditionState):
    """The SubmodelBCState object stores the propagating data for a Submodel boundary condition
    in a step. One instance of this object is created internally by the SubmodelBC object
    for each step. The instance is also deleted internally by the SubmodelBC object.
    The SubmodelBCState object has no constructor or methods.
    The SubmodelBCState object is derived from the BoundaryConditionState object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].boundaryConditionStates[name]

        The corresponding analysis keywords are:

        - SUBMODEL
        - BOUNDARY
    """

    #: A SymbolicConstant specifying the propagation state of the **dof** member. Possible values
    #: are SET and UNCHANGED.
    dofState: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the **globalStep** member. Possible
    #: values are SET and UNCHANGED.
    globalStepState: Optional[SymbolicConstant] = None

    #: An Int specifying the increment number in the global model step at which the solution
    #: will be used to specify the values of the driven variables. This argument is applicable
    #: only for linear perturbation steps.
    globalIncrement: Optional[int] = None

    #: A SymbolicConstant specifying the propagation state of the **globalIncrement** member.
    #: Possible values are SET and UNCHANGED.
    globalIncrementState: Optional[SymbolicConstant] = None

    #: None or a Float specifying the thickness of the center zone size around the shell
    #: midsurface. The default value is None.
    centerZoneSize: Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the **centerZoneSize** member.
    #: Possible values are SET and UNCHANGED.
    centerZoneSizefState: Optional[SymbolicConstant] = None

    #: None or a Float specifying a scaling value applied to the applied displacements at the
    #: interface. The default value is 1.0.
    scale: float = 1

    #: A SymbolicConstant specifying the propagation state of the **scale** member. Possible
    #: values are SET and UNCHANGED.
    scaleState: Optional[SymbolicConstant] = None

    #: A String specifying the step in the global model from which Abaqus reads the values of
    #: the variables that will drive the submodel analysis. The String indicates the position
    #: of the step in the sequence of analysis steps. For example, **globalStep** = '1' indicates
    #: the first step.
    globalStep: str = ""

    #: A tuple of Ints specifying the degrees of freedom to which the boundary condition is
    #: applied.
    dof: Optional[int] = None

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
