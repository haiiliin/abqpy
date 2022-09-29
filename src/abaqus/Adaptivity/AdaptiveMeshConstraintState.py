from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class AdaptiveMeshConstraintState:
    """The AdaptiveMeshConstraintState object is the abstract base type for other Arbitrary
    Lagrangian Eularian (ALE) style AdaptiveMeshConstraintState objects. The
    AdaptiveMeshConstraintState object has no explicit constructor or methods. The members
    of the AdaptiveMeshConstraintState object are common to all objects derived from the
    AdaptiveMeshConstraintState object.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].adaptiveMeshConstraintStates[name]
    """

    #: A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
    #: values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    amplitudeState: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the AdaptiveMeshConstraintState
    #: object. Possible values are:
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
    #: adaptive mesh constraint has no amplitude reference.
    amplitude: str = ""

    @abaqus_method_doc
    def __init__(
        self,
        amplitudeState: Optional[SymbolicConstant] = None,
        status: Optional[SymbolicConstant] = None,
        amplitude: str = "",
    ):
        """The AdaptiveMeshConstraintState object is the abstract base type for other Arbitrary
        Lagrangian Eularian (ALE) style AdaptiveMeshConstraintState objects. The
        AdaptiveMeshConstraintState object has no explicit constructor or methods. The members
        of the AdaptiveMeshConstraintState object are common to all objects derived from the
        AdaptiveMeshConstraintState object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].steps[name].AdaptiveMeshConstraintState

        Parameters
        ----------
        amplitudeState
            A SymbolicConstant specifying the propagation state of the amplitude reference. Possible  values are
            UNSET, SET, UNCHANGED, FREED, and MODIFIED.
        status
            A SymbolicConstant specifying the propagation state of the AdaptiveMeshConstraintState  object. Possible
            values are:
             
            - NOT_YET_ACTIVE
            - CREATED
            - PROPAGATED
            - MODIFIED
            - DEACTIVATED
            - NO_LONGER_ACTIVE
            - TYPE_NOT_APPLICABLE
            - INSTANCE_NOT_APPLICABLE
            - PROPAGATED_FROM_BASE_STATE
            - MODIFIED_FROM_BASE_STATE
            - DEACTIVATED_FROM_BASE_STATE
            - BUILT_INTO_MODES
            
        amplitude
            A String specifying the name of the amplitude reference. The String is empty if the  adaptive mesh
            constraint has no amplitude reference.
        """
        ...
