from typing import Optional

from abqpy.decorators import abaqus_class_doc
from .LoadState import LoadState
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class ConnectorMomentState(LoadState):
    """The ConnectorMomentState object stores the propagating data for a connector moment in a
    step. One instance of this object is created internally by the ConnectorMoment object
    for each step. The instance is also deleted internally by the ConnectorMoment object.
    The ConnectorMomentState object has no constructor or methods.
    The ConnectorMomentState object is derived from the LoadState object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].loadStates[name]

        The corresponding analysis keywords are:

        - CONNECTOR LOAD
    """

    #: A Float or a Complex specifying the connector moment component in the connector's local
    #: 4-direction. Although **m1**, **m2**, and **m3** are optional arguments, at least one of them
    #: must be nonzero.
    m1: Optional[float] = None

    #: A Float or a Complex specifying the connector moment component in the connector's local
    #: 5direction.
    m2: Optional[float] = None

    #: A Float or a Complex specifying the connector moment component in the connector's local
    #: 6-direction.
    m3: Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the load component in the
    #: connector's local 4-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.
    m1State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the load component in the
    #: connector's local 5-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.
    m2State: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the load component in the
    #: connector's local 6-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.
    m3State: Optional[SymbolicConstant] = None

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
