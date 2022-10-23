from typing import Optional

from abqpy.decorators import abaqus_class_doc

from .LoadState import LoadState
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class LineLoadState(LoadState):
    """The LineLoadState object stores the propagating data of a line load in a step. One
    instance of this object is created internally by the LineLoad object for each step. The
    instance is also deleted internally by the LineLoad object.
    The LineLoadState object has no constructor or methods.
    The LineLoadState object is derived from the LoadState object.

    .. note::
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].loadStates[name]

        The corresponding analysis keywords are:

        - DLOAD
    """

    #: A Float or a Complex specifying the load component in the global or the beam local
    #: 1-direction.
    comp1: Optional[float] = None

    #: A Float or a Complex specifying the load component in the global or the beam local
    #: 2-direction.
    comp2: Optional[float] = None

    #: A Float or a Complex specifying the load component in the global 3-direction.
    comp3: Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the load component in the global
    #: or the beam local 1-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.
    comp1State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the load component in the global
    #: or the beam local 2-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.
    comp2State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the load component in the global
    #: 3-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.
    comp3State: Optional[SymbolicConstant] = None

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
