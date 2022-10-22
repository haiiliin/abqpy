from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .AdaptiveMeshConstraintState import AdaptiveMeshConstraintState
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class VelocityAdaptiveMeshConstraintState(AdaptiveMeshConstraintState):
    """The VelocityAdaptiveMeshConstraintState object stores the propagating data for an
    Arbitrary Lagrangian Eularian (ALE) style velocity adaptive mesh constraint in a step.
    One instance of this object is created internally by the VelocityAdaptiveMeshConstraint
    object for each step. The instance is also deleted internally by the
    VelocityAdaptiveMeshConstraint object.
    The VelocityAdaptiveMeshConstraintState object has no constructor or methods.
    The VelocityAdaptiveMeshConstraintState object is derived from the
    AdaptiveMeshConstraintState object.

    .. note:: 
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].adaptiveMeshConstraintStates[name]

        The corresponding analysis keywords are:

        - ADAPTIVE MESH CONSTRAINT
    """

    #: A Float specifying the velocity component in the 1-direction.
    v1: Optional[float] = None

    #: A Float specifying the velocity component in the 2-direction.
    v2: Optional[float] = None

    #: A Float specifying the velocity component in the 3-direction.
    v3: Optional[float] = None

    #: A Float specifying the rotational velocity component about the 1-direction.
    vr1: Optional[float] = None

    #: A Float specifying the rotational velocity component about the 2-direction.
    vr2: Optional[float] = None

    #: A Float specifying the rotational velocity component about the 3-direction.
    vr3: Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the velocity component in the
    #: 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    v1State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the velocity component in the
    #: 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    v2State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the velocity component in the
    #: 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    v3State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the rotational velocity component
    #: about the 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    vr1State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the rotational velocity component
    #: about the 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    vr2State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the rotational velocity component
    #: about the 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    vr3State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
    #: values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    amplitudeState: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the AdaptiveMeshConstraintState
    #: object. Possible values
    #: are: NOT_YET_ACTIVE, CREATED, PROPAGATED, MODIFIED, DEACTIVATED, NO_LONGER_ACTIVE, TYPE_NOT_APPLICABLE
    #: INSTANCE_NOT_APPLICABLE, PROPAGATED_FROM_BASE_STATE, MODIFIED_FROM_BASE_STATE, DEACTIVATED_FROM_BASE_STATE,
    #: BUILT_INTO_MODES
    status: Optional[SymbolicConstant] = None

    #: A String specifying the name of the amplitude reference. The String is empty if the
    #: adaptive mesh constraint has no amplitude reference.
    amplitude: str = ""

    @abaqus_method_doc
    def __init__(
        self,
        v1: Optional[float] = None,
        v2: Optional[float] = None,
        v3: Optional[float] = None,
        vr1: Optional[float] = None,
        vr2: Optional[float] = None,
        vr3: Optional[float] = None,
        v1State: Optional[SymbolicConstant] = None,
        v2State: Optional[SymbolicConstant] = None,
        v3State: Optional[SymbolicConstant] = None,
        vr1State: Optional[SymbolicConstant] = None,
        vr2State: Optional[SymbolicConstant] = None,
        vr3State: Optional[SymbolicConstant] = None,
        amplitudeState: Optional[SymbolicConstant] = None,
        status: Optional[SymbolicConstant] = None,
        amplitude: str = "",
    ):
        """The VelocityAdaptiveMeshConstraintState object stores the propagating data for an
        Arbitrary Lagrangian Eularian (ALE) style velocity adaptive mesh constraint in a step.
        One instance of this object is created internally by the VelocityAdaptiveMeshConstraint
        object for each step. The instance is also deleted internally by the
        VelocityAdaptiveMeshConstraint object.
        The VelocityAdaptiveMeshConstraintState object has no constructor or methods.
        The VelocityAdaptiveMeshConstraintState object is derived from the
        AdaptiveMeshConstraintState object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].steps[name].VelocityAdaptiveMeshConstraintState

        Parameters
        ----------
        v1
            A Float specifying the velocity component in the 1-direction.
        v2
            A Float specifying the velocity component in the 2-direction.
        v3
            A Float specifying the velocity component in the 3-direction.
        vr1
            A Float specifying the rotational velocity component about the 1-direction.
        vr2
            A Float specifying the rotational velocity component about the 2-direction.
        vr3
            A Float specifying the rotational velocity component about the 3-direction.
        v1State
            A SymbolicConstant specifying the propagation state of the velocity component in the  1-direction.
            Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
        v2State
            A SymbolicConstant specifying the propagation state of the velocity component in the  2-direction.
            Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
        v3State
            A SymbolicConstant specifying the propagation state of the velocity component in the  3-direction.
            Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
        vr1State
            A SymbolicConstant specifying the propagation state of the rotational velocity component  about the
            1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
        vr2State
            A SymbolicConstant specifying the propagation state of the rotational velocity component  about the
            2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
        vr3State
            A SymbolicConstant specifying the propagation state of the rotational velocity component  about the
            3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
        amplitudeState
            A SymbolicConstant specifying the propagation state of the amplitude reference. Possible  values are UNSET,
            SET, UNCHANGED, FREED, and MODIFIED.
        status
            A SymbolicConstant specifying the propagation state of the AdaptiveMeshConstraintState  object. Possible
            values  are:
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
        super().__init__(amplitudeState, status, amplitude)
