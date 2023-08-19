from __future__ import annotations

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant
from .LoadState import LoadState


@abaqus_class_doc
class ConnectorForceState(LoadState):
    """The ConnectorForceState object stores the propagating data for a connector force in a step. One instance
    of this object is created internally by the ConnectorForce object for each step. The instance is also
    deleted internally by the ConnectorForce object. The ConnectorForceState object has no constructor or
    methods. The ConnectorForceState object is derived from the LoadState object.

    .. note::
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].loadStates[name]

        The corresponding analysis keywords are:

        - CONNECTOR LOAD
    """

    #: A Float or a Complex specifying the connector force component in the connector's local
    #: 1-direction.
    f1: float | None = None

    #: A Float or a Complex specifying the connector force component in the connector's local
    #: 2-direction.
    f2: float | None = None

    #: A Float or a Complex specifying the connector force component in the connector's local
    #: 3-direction.
    f3: float | None = None

    #: A SymbolicConstant specifying the propagation state of the connector force component in
    #: the connector's local 1-direction. Possible values are UNSET, SET, UNCHANGED, and
    #: MODIFIED.
    f1State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the connector force component in
    #: the connector's local 2-direction. Possible values are UNSET, SET, UNCHANGED, and
    #: MODIFIED.
    f2State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the connector force component in
    #: the connector's local 3-direction. Possible values are UNSET, SET, UNCHANGED, and
    #: MODIFIED.
    f3State: SymbolicConstant

    #: A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    amplitudeState: SymbolicConstant

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
    status: SymbolicConstant

    #: A String specifying the name of the amplitude reference. The String is empty if the load
    #: has no amplitude reference.
    amplitude: str = ""
