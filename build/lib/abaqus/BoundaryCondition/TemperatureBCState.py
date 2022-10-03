from typing import Optional

from abqpy.decorators import abaqus_class_doc
from .BoundaryConditionState import BoundaryConditionState
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class TemperatureBCState(BoundaryConditionState):
    """The TemperatureBCState object stores the propagating data for a temperature boundary
    condition in a step. One instance of this object is created internally by the
    TemperatureBC object for each step. The instance is also deleted internally by the
    TemperatureBC object.
    The TemperatureBCState object has no constructor or methods.
    The TemperatureBCState object is derived from the BoundaryConditionState object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].boundaryConditionStates[name]

        The corresponding analysis keywords are:

        - BOUNDARY
    """

    #: A Float specifying the temperature magnitude.
    magnitude: Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the temperature magnitude.
    #: Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    magnitudeState: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the **dof** member. Possible values
    #: are SET and UNCHANGED.
    dofState: Optional[SymbolicConstant] = None

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
