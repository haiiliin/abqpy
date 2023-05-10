from typing import Optional

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant
from .LoadState import LoadState


@abaqus_class_doc
class MomentState(LoadState):
    """The MomentState object stores the propagating data for a moment in a step. One instance of this object is
    created internally by the Moment object for each step. The instance is also deleted internally by the Moment
    object. The MomentState object has no constructor or methods. The MomentState object is derived from the
    LoadState object.

    .. note::
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].loadStates[name]

        The corresponding analysis keywords are:

        - CLOAD
    """

    #: A Float or a Complex specifying the load component in the 4-direction.
    cm1: Optional[float] = None

    #: A Float or a Complex specifying the load component in the 5-direction.
    cm2: Optional[float] = None

    #: A Float or a Complex specifying the load component in the 6-direction.
    cm3: Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the load component in the
    #: 4-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.
    cm1State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the load component in the
    #: 5-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.
    cm2State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the load component in the
    #: 6-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.
    cm3State: Optional[SymbolicConstant] = None

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
