from typing import Optional

from abqpy.decorators import abaqus_class_doc

from .BoundaryConditionState import BoundaryConditionState
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class TypeBCState(BoundaryConditionState):
    """The TypeBCState object stores the propagating data for a predefined boundary condition
    in a step. One instance of this object is created internally by the TypeBC object for
    each step. The instance is also deleted internally by the TypeBC object.
    The TypeBCState object has no constructor or methods.
    The TypeBCState object is derived from the BoundaryConditionState object.

    .. note::
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].boundaryConditionStates[name]

        The corresponding analysis keywords are:

        - BOUNDARY
    """

    #: A SymbolicConstant specifying the predefined boundary condition type. Possible values
    #: are XSYMM, YSYMM, ZSYMM, XASYMM, YASYMM, ZASYMM, PINNED, and ENCASTRE.
    typeName: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the predefined boundary condition
    #: type. The only possible value is UNCHANGED.
    typeNameState: Optional[SymbolicConstant] = None

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
