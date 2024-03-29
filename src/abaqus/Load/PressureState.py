from __future__ import annotations

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant
from .LoadState import LoadState


@abaqus_class_doc
class PressureState(LoadState):
    """The PressureState object stores the propagating data for a pressure in a step. One instance of this
    object is created internally by the Pressure object for each step. The instance is also deleted internally
    by the Pressure object. The PressureState object has no constructor or methods. The PressureState object is
    derived from the LoadState object.

    .. note::
        This object can be accessed by::

            import load
            mdb.models[name].steps[name].loadStates[name]

        The corresponding analysis keywords are:

        - DSLOAD
        - DLOAD
    """

    #: A Float or a Complex specifying the pressure magnitude.
    magnitude: float | None = None

    #: A SymbolicConstant specifying the propagation state of the pressure magnitude. Possible
    #: values are UNSET, SET, UNCHANGED, and MODIFIED.
    magnitudeState: SymbolicConstant

    #: A Float specifying the height of the zero pressure level when the pressure
    #: **distributionType** = HYDROSTATIC.
    hZero: float | None = None

    #: A SymbolicConstant specifying the propagation state of **hZero**. Possible values are
    #: UNSET, SET, UNCHANGED, and FREED.
    hZeroState: SymbolicConstant

    #: A Float specifying the height of the reference pressure level when the pressure
    #: **distributionType** = HYDROSTATIC.
    hReference: float | None = None

    #: A SymbolicConstant specifying the propagation state of **hReference**. Possible values are
    #: UNSET, SET, UNCHANGED, and FREED.
    hReferenceState: SymbolicConstant

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
