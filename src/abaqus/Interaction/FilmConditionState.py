from typing import Optional

from abqpy.decorators import abaqus_class_doc

from .InteractionState import InteractionState
from ..UtilityAndView.abaqusConstants import SymbolicConstant


@abaqus_class_doc
class FilmConditionState(InteractionState):
    """The FilmConditionState object stores the propagating data for a FilmCondition object.
    One instance of this object is created internally by the FilmCondition object for each
    step. The instance is also deleted internally by the FilmCondition object.
    The FilmConditionState object has no constructor or methods.
    The FilmConditionState object is derived from the InteractionState object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].steps[name].interactionStates[name]

        The corresponding analysis keywords are:

        - SFILM
        - FILM
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
