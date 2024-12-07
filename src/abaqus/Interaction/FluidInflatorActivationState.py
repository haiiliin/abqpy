from __future__ import annotations

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .InteractionState import InteractionState


@abaqus_class_doc
class FluidInflatorActivationState(InteractionState):
    """The FluidInflatorActivationState object stores the propagating data for a FluidInflatorActivation object. One
    instance of this object is created internally by the FluidInflatorActivation object for each step. The instance
    is also deleted internally by the FluidInflatorActivation object.

    The FluidInflatorActivationState object has no constructor or methods.

    The FluidInflatorActivationState object is derived from the InteractionState object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].steps[name].interactionStates[name]

    .. versionadded:: 2025
        The ``FluidInflatorActivationState`` class was added.
    """

    #: A SymbolicConstant specifying the propagation state of the inflators member. Possible values are UNSET, SET,
    #: UNCHANGED, and FREED.
    inflatorsState: Literal[C.UNSET, C.SET, C.UNCHANGED, C.FREED]

    #: A String specifying the name of the FluidInflator object associated with this interaction.
    inflators: str

    #: A SymbolicConstant specifying the propagation state of the inflationTimeAmplitude member. Possible values are
    #: UNSET, SET, UNCHANGED, and FREED.
    inflationTimeAmplitudeState: Literal[C.UNSET, C.SET, C.UNCHANGED, C.FREED]

    #: A String specifying the name of the Amplitude object associated with this interaction.
    inflationTimeAmplitude: str

    #: A SymbolicConstant specifying the propagation state of the massFlowAmplitude member. Possible values are UNSET,
    #: SET, UNCHANGED, and FREED.
    massFlowAmplitudeState: Literal[C.UNSET, C.SET, C.UNCHANGED, C.FREED]

    #: A SymbolicConstant specifying the propagation state of the InteractionState object. Possible values are:
    #:
    #: - NOT_YET_ACTIVE
    #: - CREATED
    #: - PROPAGATED
    #: - MODIFIED
    #: - DEACTIVATED
    #: - NO_LONGER_ACTIVE
    #: - TYPE_NOT_APPLICABLE
    #: - INSTANCE_NOT_APPLICABLE
    #: - BUILT_INTO_BASE_STATE
    status: Literal[
        C.NOT_YET_ACTIVE,
        C.CREATED,
        C.PROPAGATED,
        C.MODIFIED,
        C.DEACTIVATED,
        C.NO_LONGER_ACTIVE,
        C.TYPE_NOT_APPLICABLE,
        C.INSTANCE_NOT_APPLICABLE,
        C.BUILT_INTO_BASE_STATE,
    ]
