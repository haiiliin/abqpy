import typing
from abqpy.decorators import abaqus_class_doc
from .LoadState import LoadState
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class ConcentratedForceState(LoadState):
    """The ConcentratedForceState object stores the propagating data for a concentrated force
    in a step. One instance of this object is created internally by the ConcentratedForce
    object for each step. The instance is also deleted internally by the ConcentratedForce
    object.
    The ConcentratedForceState object has no constructor or methods.
    The ConcentratedForceState object is derived from the LoadState object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].loadStates[name]

        The corresponding analysis keywords are:

        - CLOAD
    """

    #: A Float or a Complex specifying the concentrated force component in the 1-direction.
    #: Although **cf1**, **cf2**, and **cf3** are optional arguments, at least one of them must be
    #: nonzero.
    cf1: typing.Optional[float] = None

    #: A Float or a Complex specifying the concentrated force component in the 2-direction.
    cf2: typing.Optional[float] = None

    #: A Float or a Complex specifying the concentrated force component in the 3-direction.
    cf3: typing.Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the concentrated force component
    #: in the 1-direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.
    cf1State: typing.Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the concentrated force component
    #: in the 2-direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.
    cf2State: typing.Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the concentrated force component
    #: in the 3-direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.
    cf3State: typing.Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    amplitudeState: typing.Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the LoadState object. Possible
    #: values are:
    status: typing.Optional[SymbolicConstant] = None

    #: A String specifying the name of the amplitude reference. The String is empty if the load
    #: has no amplitude reference.
    #: - NOT_YET_ACTIVE
    #: - CREATED
    #: - PROPAGATED
    #: - MODIFIED
    #: - DEACTIVATED
    #: - NO_LONGER_ACTIVE
    #: - TYPE_NOT_APPLICABLE
    #: - INSTANCE_NOT_APPLICABLE
    #: - BUILT_INTO_BASE_STATE
    amplitude: str = ""
