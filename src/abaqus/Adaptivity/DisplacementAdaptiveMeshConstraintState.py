from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .AdaptiveMeshConstraintState import AdaptiveMeshConstraintState
from ..UtilityAndView.abaqusConstants import SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class DisplacementAdaptiveMeshConstraintState(AdaptiveMeshConstraintState):
    """The DisplacementAdaptiveMeshConstraintState object stores the propagating data for an
    Arbitrary Lagrangian Eularian (ALE) style displacement/rotation adaptive mesh constraint
    in a step. One instance of this object is created internally by the
    DisplacementAdaptiveMeshConstraint object for each step. The instance is also deleted
    internally by the DisplacementAdaptiveMeshConstraint object.
    The DisplacementAdaptiveMeshConstraintState object has no constructor or methods.
    The DisplacementAdaptiveMeshConstraintState object is derived from the
    AdaptiveMeshConstraintState object.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name].adaptiveMeshConstraintStates[name]

        The corresponding analysis keywords are:

        - ADAPTIVE MESH CONSTRAINT
    """

    #: A Float or a Complex specifying the displacement component in the 1-direction.
    u1: Optional[float] = None

    #: A Float or a Complex specifying the displacement component in the 2-direction.
    u2: Optional[float] = None

    #: A Float or a Complex specifying the displacement component in the 3-direction.
    u3: Optional[float] = None

    #: A Float or a Complex specifying the rotational displacement component about the
    #: 1-direction.
    ur1: Optional[float] = None

    #: A Float or a Complex specifying the rotational displacement component about the
    #: 2-direction.
    ur2: Optional[float] = None

    #: A Float or a Complex specifying the rotational displacement component about the
    #: 3-direction.
    ur3: Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the displacement component in the
    #: 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    u1State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the displacement component in the
    #: 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    u2State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the displacement component in the
    #: 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
    u3State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the rotational displacement
    #: component about the 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
    #: MODIFIED.
    ur1State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the rotational displacement
    #: component about the 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
    #: MODIFIED.
    ur2State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the rotational displacement
    #: component about the 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
    #: MODIFIED.
    ur3State: Optional[SymbolicConstant] = None

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
        u1: Optional[float] = None,
        u2: Optional[float] = None,
        u3: Optional[float] = None,
        ur1: Optional[float] = None,
        ur2: Optional[float] = None,
        ur3: Optional[float] = None,
        u1State: Optional[Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED]] = None,
        u2State: Optional[Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED]] = None,
        u3State: Optional[Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED]] = None,
        ur1State: Optional[Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED]] = None,
        ur2State: Optional[Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED]] = None,
        ur3State: Optional[Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED]] = None,
        amplitudeState: Optional[Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED]] = None,
        status: Optional[
            Literal[
                C.NOT_YET_ACTIVE,
                C.PROPAGATED_FROM_BASE_STATE,
                C.DEACTIVATED_FROM_BASE_STATE,
                C.DEACTIVATED,
                C.MODIFIED_FROM_BASE_STATE,
                C.PROPAGATED,
                C.NO_LONGER_ACTIVE,
                C.CREATED,
                C.INSTANCE_NOT_APPLICABLE,
                C.BUILT_INTO_MODES,
                C.TYPE_NOT_APPLICABLE,
                C.MODIFIED,
            ]
        ] = None,
        amplitude: str = "",
    ):
        """

        .. note::
            This function can be accessed by::

                mdb.models[name].steps[name].DisplacementAdaptiveMeshConstraintState

        Parameters
        ----------
        u1
            A Float or a Complex specifying the displacement component in the 1-direction.
        u2
            A Float or a Complex specifying the displacement component in the 2-direction.
        u3
            A Float or a Complex specifying the displacement component in the 3-direction.
        ur1
            A Float or a Complex specifying the rotational displacement component about the  1-direction.
        ur2
            A Float or a Complex specifying the rotational displacement component about the  2-direction.
        ur3
            A Float or a Complex specifying the rotational displacement component about the  3-direction.
        u1State
            A SymbolicConstant specifying the propagation state of the displacement component in the  1-direction.
            Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
        u2State
            A SymbolicConstant specifying the propagation state of the displacement component in the  2-direction.
            Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
        u3State
            A SymbolicConstant specifying the propagation state of the displacement component in the  3-direction.
            Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.
        ur1State
            A SymbolicConstant specifying the propagation state of the rotational displacement  component about the
            1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and  MODIFIED.
        ur2State
            A SymbolicConstant specifying the propagation state of the rotational displacement  component about the
            2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and  MODIFIED.
        ur3State
            A SymbolicConstant specifying the propagation state of the rotational displacement  component about the
            3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and  MODIFIED.
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
