from typing import Optional

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class InteractionState:
    """The InteractionState object is the abstract base type for other InteractionState objects. The
    InteractionState object has no explicit constructor. The members of the InteractionState object are common
    to all objects derived from InteractionState.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].steps[name].interactionStates[name]
    """

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
