from typing import Optional

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Region.Region import Region
from ..Step.StepBase import StepBase
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .AdaptiveMeshConstraintState import AdaptiveMeshConstraintState
from .AdaptiveMeshDomain import AdaptiveMeshDomain
from .DisplacementAdaptiveMeshConstraintState import (
    DisplacementAdaptiveMeshConstraintState,
)
from .VelocityAdaptiveMeshConstraintState import VelocityAdaptiveMeshConstraintState


@abaqus_class_doc
class AdaptivityStep(StepBase):
    """The Step object stores the parameters that determine the context of the step. The Step object is the
    abstract base type for other Step objects. The Step object has no explicit constructor. The methods and
    members of the Step object are common to all objects derived from the Step.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].steps[name]
    """

    @abaqus_method_doc
    def AdaptiveMeshConstraintState(
        self,
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
    ) -> AdaptiveMeshConstraintState:
        """The AdaptiveMeshConstraintState object is the abstract base type for other Arbitrary Lagrangian
        Eularian (ALE) style AdaptiveMeshConstraintState objects. The AdaptiveMeshConstraintState object has no
        explicit constructor or methods. The members of the AdaptiveMeshConstraintState object are common to all
        objects derived from the AdaptiveMeshConstraintState object.

        .. note::
            This function can be accessed by::

                mdb.models[name].steps[name].AdaptiveMeshConstraintState

        Parameters
        ----------
        amplitudeState
            A SymbolicConstant specifying the propagation state of the amplitude reference. Possible values are

            - UNSET
            - SET
            - UNCHANGED
            - FREED
            - MODIFIED
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
        self.adaptiveMeshConstraintStates[amplitude] = adaptiveMeshConstraintState = AdaptiveMeshConstraintState(
            amplitudeState, status, amplitude
        )
        return adaptiveMeshConstraintState

    @abaqus_method_doc
    def DisplacementAdaptiveMeshConstraintState(
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
    ) -> DisplacementAdaptiveMeshConstraintState:
        """The DisplacementAdaptiveMeshConstraintState object stores the propagating data for an Arbitrary
        Lagrangian Eularian (ALE) style displacement/rotation adaptive mesh constraint in a step. One instance
        of this object is created internally by the DisplacementAdaptiveMeshConstraint object for each step. The
        instance is also deleted internally by the DisplacementAdaptiveMeshConstraint object. The
        DisplacementAdaptiveMeshConstraintState object has no constructor or methods. The
        DisplacementAdaptiveMeshConstraintState object is derived from the AdaptiveMeshConstraintState object.

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
        self.adaptiveMeshConstraintStates[
            amplitude
        ] = adaptiveMeshConstraintState = DisplacementAdaptiveMeshConstraintState(
            u1,
            u2,
            u3,
            ur1,
            ur2,
            ur3,
            u1State,
            u2State,
            u3State,
            ur1State,
            ur2State,
            ur3State,
            amplitudeState,
            status,
            amplitude,
        )
        return adaptiveMeshConstraintState

    @abaqus_method_doc
    def VelocityAdaptiveMeshConstraintState(
        self,
        v1: Optional[float] = None,
        v2: Optional[float] = None,
        v3: Optional[float] = None,
        vr1: Optional[float] = None,
        vr2: Optional[float] = None,
        vr3: Optional[float] = None,
        v1State: Optional[Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED]] = None,
        v2State: Optional[Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED]] = None,
        v3State: Optional[Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED]] = None,
        vr1State: Optional[Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED]] = None,
        vr2State: Optional[Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED]] = None,
        vr3State: Optional[Literal[C.UNSET, C.SET, C.FREED, C.UNCHANGED, C.MODIFIED]] = None,
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
    ) -> VelocityAdaptiveMeshConstraintState:
        """The VelocityAdaptiveMeshConstraintState object stores the propagating data for an Arbitrary
        Lagrangian Eularian (ALE) style velocity adaptive mesh constraint in a step. One instance of this object
        is created internally by the VelocityAdaptiveMeshConstraint object for each step. The instance is also
        deleted internally by the VelocityAdaptiveMeshConstraint object. The VelocityAdaptiveMeshConstraintState
        object has no constructor or methods. The VelocityAdaptiveMeshConstraintState object is derived from the
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
        self.adaptiveMeshConstraintStates[
            amplitude
        ] = adaptiveMeshConstraintState = VelocityAdaptiveMeshConstraintState(
            v1,
            v2,
            v3,
            vr1,
            vr2,
            vr3,
            v1State,
            v2State,
            v3State,
            vr1State,
            vr2State,
            vr3State,
            amplitudeState,
            status,
            amplitude,
        )
        return adaptiveMeshConstraintState

    @abaqus_method_doc
    def AdaptiveMeshDomain(
        self,
        region: Region,
        controls: str = "",
        frequency: int = 10,
        initialMeshSweeps: int = 5,
        meshSweeps: int = 1,
    ) -> AdaptiveMeshDomain:
        """The AdaptiveMeshDomain object defines the region and controls that govern an Arbitrary Lagrangian
        Eularian (ALE) style adaptive smoothing mesh domain.

        This method creates an AdaptiveMeshDomain object.

        .. note::
            This function can be accessed by::

                mdb.models[name].steps[name].AdaptiveMeshDomain

        Parameters
        ----------
        region
            A Region object specifying the region to which the adaptive mesh domain is applied.
        controls
            A String specifying the name of an AdaptiveMeshControl object.
        frequency
            An Int specifying the frequency in increments at which adaptive meshing will be
            performed. The default value is 10.
        initialMeshSweeps
            An Int specifying the number of mesh sweeps to be performed at the beginning of the
            first step in which this adaptive mesh definition is active. The default value is 5.
        meshSweeps
            An Int specifying the number of mesh sweeps to be performed in each adaptive mesh
            increment. The default value is 1.

        Returns
        -------
        AdaptiveMeshDomain
            An AdaptiveMeshDomain object
        """
        self.adaptiveMeshDomains[controls] = adaptiveMeshDomain = AdaptiveMeshDomain(
            region, controls, frequency, initialMeshSweeps, meshSweeps
        )
        return adaptiveMeshDomain
