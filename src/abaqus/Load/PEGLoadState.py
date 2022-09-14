from abqpy.decorators import abaqus_class_doc
from .LoadState import LoadState
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class PEGLoadState(LoadState):
    """The PEGLoadState object stores the propagating data for a concentrated force in a step.
    One instance of this object is created internally by the PEGLoad object for each step.
    The instance is also deleted internally by the PEGLoad object.
    The PEGLoadState object has no constructor or methods.
    The PEGLoadState object is derived from the LoadState object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].loadStates[name]

        The corresponding analysis keywords are:

        - CLOAD
    """

    #: A Float or a Complex specifying the load component at dof 1 of reference node 1.
    comp1: float = None

    #: A Float or a Complex specifying the load component at dof 1 of reference node 2.
    comp2: float = None

    #: A Float or a Complex specifying the load component at dof 2 of reference node 2.
    comp3: float = None

    #: A SymbolicConstant specifying the propagation state of the load component at dof 1 of
    #: reference node 1. Possible values are UNSET, SET, UNCHANGED, and FREED.
    comp1State: SymbolicConstant = None

    #: A SymbolicConstant specifying the propagation state of the load component at dof 1 of
    #: reference node 2. Possible values are UNSET, SET, UNCHANGED, and FREED.
    comp2State: SymbolicConstant = None

    #: A SymbolicConstant specifying the propagation state of the load component at dof 2 of
    #: reference node 2. Possible values are UNSET, SET, UNCHANGED, and FREED.
    comp3State: SymbolicConstant = None

    #: A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    amplitudeState: SymbolicConstant = None

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
    status: SymbolicConstant = None

    #: A String specifying the name of the amplitude reference. The String is empty if the load
    #: has no amplitude reference.
    amplitude: str = ""
