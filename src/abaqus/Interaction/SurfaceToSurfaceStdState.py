from __future__ import annotations

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant
from .InteractionState import InteractionState


@abaqus_class_doc
class SurfaceToSurfaceStdState(InteractionState):
    """The SurfaceToSurfaceStdState object stores the propagating data for a SurfaceToSurfaceContactStd object.
    One instance of this object is created internally by the SurfaceToSurfaceContactStd object for each step.
    The instance is also deleted internally by the SurfaceToSurfaceContactStd object. The
    SurfaceToSurfaceStdState object has no constructor or methods. The SurfaceToSurfaceStdState object is
    derived from the InteractionState object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].steps[name].interactionStates[name]

        The corresponding analysis keywords are:

        - CONTACT CONTROLS
        - CONTACT PAIR
        - CONTACT INTERFERENCE
    """

    #: A SymbolicConstant specifying the propagation state of the **interactionProperty** member.
    #: Possible values are UNSET, SET, UNCHANGED, and FREED.
    interactionPropertyState: SymbolicConstant

    #: A SymbolicConstant specifying the interference type. Possible values are NONE,
    #: SHRINK_FIT, and UNIFORM.
    interferenceType: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the **interferenceType** member.
    #: Possible values are UNSET, SET, UNCHANGED, and FREED.
    interferenceTypeState: SymbolicConstant

    #: A Float specifying the allowable overclosure.
    overclosure: float | None = None

    #: A SymbolicConstant specifying the propagation state of the **overclosure** member.
    #: Possible values are COMPUTED and DIRECTION_COSINE.
    overclosureState: SymbolicConstant

    #: A SymbolicConstant specifying the interference direction type. Possible values are
    #: COMPUTED and DIRECTION_COSINE.
    interferenceDirectionType: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the **interferenceDirectionType**
    #: member. Possible values are UNSET, SET, UNCHANGED, and FREED.
    interferenceDirectionTypeState: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the **direction** member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    directionState: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    amplitudeState: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the **contactControls** member.
    #: Possible values are UNSET, SET, UNCHANGED, and FREED.
    contactControlsState: SymbolicConstant

    #: A String specifying the name of the ContactProperty object associated with this
    #: interaction.
    interactionProperty: str = ""

    #: A String specifying the name of the Amplitude object that defines the magnitude of the
    #: prescribed interference during the step.
    amplitude: str = ""

    #: A String specifying the name of the ContactControl object associated with this
    #: interaction.
    contactControls: str = ""

    #: A tuple of three Floats specifying the following:
    #: - X-direction cosine of the interference direction vector.
    #: - Y-direction cosine of the interference direction vector.
    #: - Z-direction cosine of the interference direction vector.
    direction: float | None = None

    #: A SymbolicConstant specifying the propagation state of the InteractionState object.
    #: Possible values are:
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
    status: SymbolicConstant
