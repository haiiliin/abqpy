from typing_extensions import Literal
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Amplitude import Amplitude
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import (ABSOLUTE_VALUE, ACCELERATION, Boolean,
                                              EVENT_ACCELERATION, OFF, STEP, SymbolicConstant)


@abaqus_class_doc
class SpectrumAmplitude(Amplitude):
    """The SpectrumAmplitude object defines the spectrum of responses for displacement,
    velocity, or acceleration to be used in a response spectrum analysis.
    The SpectrumAmplitude object is derived from the Amplitude object.

    .. note:: 
        This object can be accessed by::

            import amplitude
            mdb.models[name].amplitudes[name]
            import odbAmplitude
            session.odbs[name].amplitudes[name]

        The corresponding analysis keywords are:

        - SPECTRUM
    """

    #: A String specifying the repository key.
    name: str

    #: A SymbolicConstant specifying the method for specifying the spectrum. Possible values
    #: are DEFINE and CALCULATE.
    method: SymbolicConstant

    #: A sequence of sequences of Floats specifying the magnitude, frequency, and damping
    #: values.
    data: tuple

    #: A SymbolicConstant specifying the units used for specifying the spectrum. Possible
    #: values are DISPLACEMENT, VELOCITY, ACCELERATION, and GRAVITY. The default value is
    #: ACCELERATION.
    specificationUnits: SymbolicConstant = ACCELERATION

    #: A SymbolicConstant specifying the units used to describe the dynamic event in the
    #: amplitude used for the calculation. Possible values are EVENT_DISPLACEMENT,
    #: EVENT_VELOCITY, EVENT_ACCELERATION, and EVENT_GRAVITY. The default value is
    #: EVENT_ACCELERATION.
    eventUnits: SymbolicConstant = EVENT_ACCELERATION

    #: A SymbolicConstant specifying the solution method for the dynamic equations. Possible
    #: values are ABSOLUTE_VALUE and RELATIVE_VALUE. The default value is ABSOLUTE_VALUE.
    solution: SymbolicConstant = ABSOLUTE_VALUE

    #: A Float specifying the implicit time increment used to calculate the spectrum. This
    #: argument is required when the **method** = CALCULATE. The default value is 0.0.
    timeIncrement: float = 0

    #: A Float specifying the acceleration due to gravity. This argument applies only when
    #: **specificationUnits** = GRAVITY or*eventUnits* = GRAVITY. The default value is 1.0.
    gravity: float = 1

    #: A Boolean specifying whether to calculate the spectrum for only the specified range of
    #: critical damping values or a list of values. If **criticalDamping** = ON, the spectrum is
    #: calculated only for the specified range of critical damping values. If **criticalDamping**
    #: = OFF, the spectrum is calculated for a list of damping values. The default value is
    #: OFF.
    criticalDamping: Boolean = OFF

    #: A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
    #: and TOTAL. The default value is STEP.
    timeSpan: SymbolicConstant = STEP

    #: A String specifying the name of the amplitude that describes the dynamic event used to
    #: calculate the spectrum. The default value is an empty string.
    amplitude: str = ""

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        method: Literal[C.DEFINE, C.CALCULATE],
        data: tuple,
        specificationUnits: Literal[C.ACCELERATION, C.VELOCITY, C.GRAVITY, C.DISPLACEMENT] = ACCELERATION,
        eventUnits: Literal[C.EVENT_DISPLACEMENT, C.EVENT_ACCELERATION, C.EVENT_GRAVITY, C.EVENT_VELOCITY] = EVENT_ACCELERATION,
        solution: Literal[C.ABSOLUTE_VALUE, C.RELATIVE_VALUE] = ABSOLUTE_VALUE,
        timeIncrement: float = 0,
        gravity: float = 1,
        criticalDamping: Boolean = OFF,
        timeSpan: Literal[C.STEP, C.TOTAL] = STEP,
        amplitude: str = "",
    ):
        """This method creates a SpectrumAmplitude object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].SpectrumAmplitude
                session.odbs[name].SpectrumAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key.
        method
            A SymbolicConstant specifying the method for specifying the spectrum. Possible values
            are DEFINE and CALCULATE.
        data
            A sequence of sequences of Floats specifying the magnitude, frequency, and damping
            values.
        specificationUnits
            A SymbolicConstant specifying the units used for specifying the spectrum. Possible
            values are DISPLACEMENT, VELOCITY, ACCELERATION, and GRAVITY. The default value is
            ACCELERATION.
        eventUnits
            A SymbolicConstant specifying the units used to describe the dynamic event in the
            amplitude used for the calculation. Possible values are EVENT_DISPLACEMENT,
            EVENT_VELOCITY, EVENT_ACCELERATION, and EVENT_GRAVITY. The default value is
            EVENT_ACCELERATION.
        solution
            A SymbolicConstant specifying the solution method for the dynamic equations. Possible
            values are ABSOLUTE_VALUE and RELATIVE_VALUE. The default value is ABSOLUTE_VALUE.
        timeIncrement
            A Float specifying the implicit time increment used to calculate the spectrum. This
            argument is required when the **method** = CALCULATE. The default value is 0.0.
        gravity
            A Float specifying the acceleration due to gravity. This argument applies only when
            **specificationUnits** = GRAVITY or*eventUnits* = GRAVITY. The default value is 1.0.
        criticalDamping
            A Boolean specifying whether to calculate the spectrum for only the specified range of
            critical damping values or a list of values. If **criticalDamping** = ON, the spectrum is
            calculated only for the specified range of critical damping values. If **criticalDamping**
            = OFF, the spectrum is calculated for a list of damping values. The default value is
            OFF.
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
            and TOTAL. The default value is STEP.
        amplitude
            A String specifying the name of the amplitude that describes the dynamic event used to
            calculate the spectrum. The default value is an empty string.

        Returns
        -------
        SpectrumAmplitude
            A :py:class:`~abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        specificationUnits: Literal[C.ACCELERATION, C.VELOCITY, C.GRAVITY, C.DISPLACEMENT] = ACCELERATION,
        eventUnits: Literal[C.EVENT_DISPLACEMENT, C.EVENT_ACCELERATION, C.EVENT_GRAVITY, C.EVENT_VELOCITY] = EVENT_ACCELERATION,
        solution: Literal[C.ABSOLUTE_VALUE, C.RELATIVE_VALUE] = ABSOLUTE_VALUE,
        timeIncrement: float = 0,
        gravity: float = 1,
        criticalDamping: Boolean = OFF,
        timeSpan: Literal[C.STEP, C.TOTAL] = STEP,
        amplitude: str = "",
    ):
        """This method modifies the SpectrumAmplitude object.

        Parameters
        ----------
        specificationUnits
            A SymbolicConstant specifying the units used for specifying the spectrum. Possible
            values are DISPLACEMENT, VELOCITY, ACCELERATION, and GRAVITY. The default value is
            ACCELERATION.
        eventUnits
            A SymbolicConstant specifying the units used to describe the dynamic event in the
            amplitude used for the calculation. Possible values are EVENT_DISPLACEMENT,
            EVENT_VELOCITY, EVENT_ACCELERATION, and EVENT_GRAVITY. The default value is
            EVENT_ACCELERATION.
        solution
            A SymbolicConstant specifying the solution method for the dynamic equations. Possible
            values are ABSOLUTE_VALUE and RELATIVE_VALUE. The default value is ABSOLUTE_VALUE.
        timeIncrement
            A Float specifying the implicit time increment used to calculate the spectrum. This
            argument is required when the **method** = CALCULATE. The default value is 0.0.
        gravity
            A Float specifying the acceleration due to gravity. This argument applies only when
            **specificationUnits** = GRAVITY or*eventUnits* = GRAVITY. The default value is 1.0.
        criticalDamping
            A Boolean specifying whether to calculate the spectrum for only the specified range of
            critical damping values or a list of values. If **criticalDamping** = ON, the spectrum is
            calculated only for the specified range of critical damping values. If **criticalDamping**
            = OFF, the spectrum is calculated for a list of damping values. The default value is
            OFF.
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
            and TOTAL. The default value is STEP.
        amplitude
            A String specifying the name of the amplitude that describes the dynamic event used to
            calculate the spectrum. The default value is an empty string.

        Raises
        ------
        RangeError
        """
        ...
