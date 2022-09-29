from typing import Optional

from abqpy.decorators import abaqus_class_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class LoadState:
    """The LoadState object is the abstract base type for other LoadState objects. The
    LoadState object has no explicit constructor or methods. The members of the LoadState
    object are common to all objects derived from LoadState.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].loadStates[name]
    """

    #: A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    amplitudeState: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the LoadState object. Possible
    #: values are:
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

    #: A String specifying the name of the amplitude reference. The String is empty if the load
    #: has no amplitude reference.
    amplitude: str = ""
