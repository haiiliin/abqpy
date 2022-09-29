from typing import Optional

from abqpy.decorators import abaqus_class_doc
from .InteractionState import InteractionState
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class SurfaceToSurfaceExpState(InteractionState):
    """The SurfaceToSurfaceExpState object stores the propagating data for a
    SurfaceToSurfaceContactExp object. One instance of this object is created internally by
    the SurfaceToSurfaceContactExp object for each step. The instance is also deleted
    internally by the SurfaceToSurfaceContactExp object.
    The SurfaceToSurfaceExpState object has no constructor or methods.
    The SurfaceToSurfaceExpState object is derived from the InteractionState object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].steps[name].interactionStates[name]

        The corresponding analysis keywords are:

        - CONTACT CONTROLS
        - CONTACT PAIR
    """

    #: A SymbolicConstant specifying the propagation state of the **interactionProperty** member.
    #: Possible values are UNSET, SET, UNCHANGED, and FREED.
    interactionPropertyState: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the **contactControls** member.
    #: Possible values are UNSET, SET, UNCHANGED, and FREED.
    contactControlsState: Optional[SymbolicConstant] = None

    #: A String specifying the name of the ContactProperty object associated with this
    #: interaction.
    interactionProperty: str = ""

    #: A String specifying the name of the ContactControl object associated with this
    #: interaction.
    contactControls: str = ""

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
    status: Optional[SymbolicConstant] = None
