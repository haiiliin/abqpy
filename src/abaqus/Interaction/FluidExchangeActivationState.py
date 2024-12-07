from __future__ import annotations

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import Boolean
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .InteractionState import InteractionState


@abaqus_class_doc
class FluidExchangeActivationState(InteractionState):
    """The FluidExchangeActivationState object stores the propagating data for a FluidExchangeActivation object. One
    instance of this object is created internally by the FluidExchangeActivation object for each step. The instance
    is also deleted internally by the FluidExchangeActivation object.

    The FluidExchangeActivationState object has no constructor or methods.

    The FluidExchangeActivationState object is derived from the InteractionState object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].steps[name].interactionStates[name]

    .. versionadded:: 2025
        The ``FluidExchangeActivationState`` class was added.
    """

    #: A SymbolicConstant specifying the propagation state of the exchanges member. Possible values are UNSET, SET, UNCHANGED, and FREED.
    exchangesState: Literal[C.UNSET, C.SET, C.UNCHANGED, C.FREED]

    #: A String specifying the name of the FluidExchange object associated with this interaction.
    exchanges: str

    #: A SymbolicConstant specifying the propagation state of the amplitude member. Possible values are UNSET, SET, UNCHANGED, and FREED.
    amplitudeState: Literal[C.UNSET, C.SET, C.UNCHANGED, C.FREED]

    #: A String specifying the name of the Amplitude object associated with this interaction.
    amplitude: str

    #: A SymbolicConstant specifying the propagation state of the isBlockage member. Possible values are UNSET, SET, UNCHANGED, and FREED.
    isBlockageState: Literal[C.UNSET, C.SET, C.UNCHANGED, C.FREED]

    #: A Boolean specifying whether to consider vent and leakage area obstruction by contacted surfaces.
    isBlockage: Boolean

    #: A SymbolicConstant specifying the propagation state of the isOnlyOutflow member. Possible values are UNSET, SET, UNCHANGED, and FREED.
    isOnlyOutflowState: Literal[C.UNSET, C.SET, C.UNCHANGED, C.FREED]

    #: A Boolean specifying whether the flow of fluid is allowed only from the first fluid cavity to the second fluid cavity defined in the FluidExchange object.
    isOnlyOutflow: Boolean

    #: A SymbolicConstant specifying the propagation state of the deltaLeakageArea member. Possible values are UNSET, SET, UNCHANGED, and FREED.
    deltaLeakageAreaState: Literal[C.UNSET, C.SET, C.UNCHANGED, C.FREED]

    #: A Float specifying the ratio of the actual surface area over the initial surface area at which you want the fluid to leak.
    deltaLeakageArea: float

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
