import typing
from abqpy.decorators import abaqus_class_doc
from .InteractionState import InteractionState
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class SurfaceToSurfaceStdState(InteractionState):
    """The SurfaceToSurfaceStdState object stores the propagating data for a
    SurfaceToSurfaceContactStd object. One instance of this object is created internally by
    the SurfaceToSurfaceContactStd object for each step. The instance is also deleted
    internally by the SurfaceToSurfaceContactStd object.
    The SurfaceToSurfaceStdState object has no constructor or methods.
    The SurfaceToSurfaceStdState object is derived from the InteractionState object.

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
    interactionPropertyState: typing.Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the interference type. Possible values are NONE,
    #: SHRINK_FIT, and UNIFORM.
    interferenceType: typing.Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the **interferenceType** member.
    #: Possible values are UNSET, SET, UNCHANGED, and FREED.
    interferenceTypeState: typing.Optional[SymbolicConstant] = None

    #: A Float specifying the allowable overclosure.
    overclosure: typing.Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the **overclosure** member.
    #: Possible values are COMPUTED and DIRECTION_COSINE.
    overclosureState: typing.Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the interference direction type. Possible values are
    #: COMPUTED and DIRECTION_COSINE.
    interferenceDirectionType: typing.Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the **interferenceDirectionType**
    #: member. Possible values are UNSET, SET, UNCHANGED, and FREED.
    interferenceDirectionTypeState: typing.Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the **direction** member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    directionState: typing.Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    amplitudeState: typing.Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the **contactControls** member.
    #: Possible values are UNSET, SET, UNCHANGED, and FREED.
    contactControlsState: typing.Optional[SymbolicConstant] = None

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
    direction: typing.Optional[float] = None

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
    status: typing.Optional[SymbolicConstant] = None
