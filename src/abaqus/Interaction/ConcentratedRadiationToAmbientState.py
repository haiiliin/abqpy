from typing import Optional

from abqpy.decorators import abaqus_class_doc

from .InteractionState import InteractionState
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class ConcentratedRadiationToAmbientState(InteractionState):
    """The ConcentratedRadiationToAmbientState object stores the propagating data for a
    ConcentratedRadiationToAmbient object. One instance of this object is created internally
    by the ConcentratedRadiationToAmbient object for each step. The instance is also deleted
    internally by the ConcentratedRadiationToAmbient object.
    The ConcentratedRadiationToAmbientState object has no constructor or methods.
    The ConcentratedRadiationToAmbientState object is derived from the InteractionState
    object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].steps[name].interactionStates[name]

        The corresponding analysis keywords are:

        - CRADIATE
    """

    #: A Float specifying the ambient temperature.
    ambientTemperature: Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the **ambientTemperature** member.
    #: Possible values are UNSET, SET, UNCHANGED, and FREED.
    ambientTemperatureState: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the **ambientTemperatureAmp**
    #: member. Possible values are UNSET, SET, UNCHANGED, and FREED.
    ambientTemperatureAmpState: Optional[SymbolicConstant] = None

    #: A Float specifying the emissivity.
    emissivity: Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the **emissivity** member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    emissivityState: Optional[SymbolicConstant] = None

    #: A Float specifying the area associated with the node where the concentrated radiation is
    #: applied.
    nodalArea: Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the **nodalArea** member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    nodalAreaState: Optional[SymbolicConstant] = None

    #: A String specifying the name of the Amplitude object that gives the variation of the
    #: ambient temperature with time.
    ambientTemperatureAmp: str = ""

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
