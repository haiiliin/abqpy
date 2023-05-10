from typing import Optional

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant
from .InteractionState import InteractionState


@abaqus_class_doc
class ConcentratedFilmConditionState(InteractionState):
    """The ConcentratedFilmConditionState object stores the propagating data for a ConcentratedFilmCondition
    object. One instance of this object is created internally by the ConcentratedFilmCondition object for each
    step. The instance is also deleted internally by the ConcentratedFilmCondition object. The
    ConcentratedFilmConditionState object has no constructor or methods. The ConcentratedFilmConditionState
    object is derived from the InteractionState object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].steps[name].interactionStates[name]

        The corresponding analysis keywords are:

        - CFILM
    """

    #: A SymbolicConstant specifying the propagation state of the **interactionProperty** member.
    #: Possible values are UNSET, SET, UNCHANGED, and FREED.
    interactionPropertyState: Optional[SymbolicConstant] = None

    #: A Float specifying the sink temperature.
    sinkTemperature: Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the **sinkTemperature** member.
    #: Possible values are UNSET, SET, UNCHANGED, and FREED.
    sinkTemperatureState: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the **sinkAmplitude** member.
    #: Possible values are UNSET, SET, UNCHANGED, and FREED.
    sinkAmplitudeState: Optional[SymbolicConstant] = None

    #: A Float specifying the film coefficient.
    filmCoeff: Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the **filmCoeff** member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    filmCoeffState: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the propagation state of the **filmCoeffAmplitude** member.
    #: Possible values are UNSET, SET, UNCHANGED, and FREED.
    filmCoeffAmplitudeState: Optional[SymbolicConstant] = None

    #: A Float specifying the area associated with the node where the concentrated film
    #: condition is applied.
    nodalArea: Optional[float] = None

    #: A SymbolicConstant specifying the propagation state of the **nodalArea** member. Possible
    #: values are UNSET, SET, UNCHANGED, and FREED.
    nodalAreaState: Optional[SymbolicConstant] = None

    #: A String specifying the FilmConditionProp object associated with this interaction.
    interactionProperty: str = ""

    #: A String specifying the name of the Amplitude object that gives the variation of the
    #: sink temperature.
    sinkAmplitude: str = ""

    #: A String specifying the name of the Amplitude object that gives the variation of the
    #: film coefficient.
    filmCoeffAmplitude: str = ""

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
