import typing
from abqpy.decorators import abaqus_class_doc
from .LoadState import LoadState
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class PipePressureState(LoadState):
    """The PipePressureState object stores the propagating data for a pipe pressure in a step.
    One instance of this object is created internally by the PipePressure object for each
    step. The instance is also deleted internally by the PipePressure object.
    The PipePressureState object has no constructor or methods.
    The PipePressureState object is derived from the LoadState object.

    .. note:: 
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].loadStates[name]

        The corresponding analysis keywords are:

        - DSLOAD
        - DLOAD
    """

    #: A Float or a Complex specifying the load magnitude.
    magnitude: typing.Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the load magnitude. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    magnitudeState: typing.Optional[SymbolicConstant] = None

    #: A Float specifying the height of the zero pressure level when the pipe pressure
    #: **distributionType** = HYDROSTATIC.
    hZero: typing.Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of **hZero**. Possible values are
    #: UNSET, SET, UNCHANGED, and FREED.
    hZeroState: typing.Optional[SymbolicConstant] = None

    #: A Float specifying the height of the reference pressure level when the pipe pressure
    #: **distributionType** = HYDROSTATIC.
    hReference: typing.Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of **hReference**. Possible values are
    #: UNSET, SET, UNCHANGED, and FREED.
    hReferenceState: typing.Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    amplitudeState: typing.Optional[SymbolicConstant] = None

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
    status: typing.Optional[SymbolicConstant] = None

    #: A String specifying the name of the amplitude reference. The String is empty if the load
    #: has no amplitude reference.
    amplitude: str = ""
