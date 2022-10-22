from typing import Optional

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class BoundaryConditionState:
    """The BoundaryConditionState object is the abstract base type for other
    BoundaryConditionState objects. The BoundaryConditionState object has no explicit
    constructor or methods. The members of the BoundaryConditionState object are common to
    all objects derived from the BoundaryConditionState object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].boundaryConditionStates[name]
    """

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
