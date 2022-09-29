from typing import Union

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ActuatorAmplitude import ActuatorAmplitude
from .DecayAmplitude import DecayAmplitude
from .EquallySpacedAmplitude import EquallySpacedAmplitude
from .ModulatedAmplitude import ModulatedAmplitude
from .PeriodicAmplitude import PeriodicAmplitude
from .PsdDefinition import PsdDefinition
from .SmoothStepAmplitude import SmoothStepAmplitude
from .SolutionDependentAmplitude import SolutionDependentAmplitude
from .SpectrumAmplitude import SpectrumAmplitude
from .TabularAmplitude import TabularAmplitude
from ..Odb.OdbBase import OdbBase
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class AmplitudeOdb(OdbBase):
    """The Odb object is the in-memory representation of an output database (ODB) file.

    .. note:: 
        This object can be accessed by::

            import odbAccess
            session.odbs[name]
    """

    @abaqus_method_doc
    def ActuatorAmplitude(
        self, name: str, timeSpan: SymbolicConstant = STEP
    ) -> ActuatorAmplitude:
        """This method creates a ActuatorAmplitude object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ActuatorAmplitude
                session.odbs[name].ActuatorAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key.
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
            and TOTAL. The default value is STEP.

        Returns
        -------
        ActuatorAmplitude
            An :py:class:`~abaqus.Amplitude.ActuatorAmplitude.ActuatorAmplitude` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.amplitudes[name] = amplitude = ActuatorAmplitude(name, timeSpan)
        return amplitude

    @abaqus_method_doc
    def DecayAmplitude(
        self,
        name: str,
        initial: float,
        maximum: float,
        start: float,
        decayTime: float,
        timeSpan: SymbolicConstant = STEP,
    ) -> DecayAmplitude:
        """This method creates a DecayAmplitude object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].DecayAmplitude
                session.odbs[name].DecayAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key.
        initial
            A Float specifying the constant A0A0.
        maximum
            A Float specifying the coefficient AA.
        start
            A Float specifying the starting time t0t0. Possible values are non-negative numbers.
        decayTime
            A Float specifying the decay time tdtd. Possible values are non-negative numbers.
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
            and TOTAL. The default value is STEP.

        Returns
        -------
        DecayAmplitude
            A :py:class:`~abaqus.Amplitude.DecayAmplitude.DecayAmplitude` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.amplitudes[name] = amplitude = DecayAmplitude(
            name, initial, maximum, start, decayTime, timeSpan
        )
        return amplitude

    @abaqus_method_doc
    def EquallySpacedAmplitude(
        self,
        name: str,
        fixedInterval: float,
        data: tuple,
        begin: float = 0,
        smooth: Union[SymbolicConstant, float] = SOLVER_DEFAULT,
        timeSpan: SymbolicConstant = STEP,
    ) -> EquallySpacedAmplitude:
        """This method creates an EquallySpacedAmplitude object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].EquallySpacedAmplitude
                session.odbs[name].EquallySpacedAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key.
        fixedInterval
            A Float specifying the fixed time interval at which the amplitude data are given.
            Possible values are positive numbers.
        data
            A sequence of Floats specifying the amplitude values.
        begin
            A Float specifying the time at which the first amplitude data are given. Possible values
            are non-negative numbers. The default value is 0.0.
        smooth
            The SymbolicConstant SOLVER_DEFAULT or a Float specifying the degree of smoothing.
            Possible float values are 0 ≤ **smoothing** ≤ 0.5. If **smooth** = SOLVER_DEFAULT, the
            default degree of smoothing will be determined by the solver. The default value is
            SOLVER_DEFAULT.
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
            and TOTAL. The default value is STEP.

        Returns
        -------
        EquallySpacedAmplitude
            An :py:class:`~abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.amplitudes[name] = amplitude = EquallySpacedAmplitude(
            name, fixedInterval, data, begin, smooth, timeSpan
        )
        return amplitude

    @abaqus_method_doc
    def ModulatedAmplitude(
        self,
        name: str,
        initial: float,
        magnitude: float,
        start: float,
        frequency1: float,
        frequency2: float,
        timeSpan: SymbolicConstant = STEP,
    ) -> ModulatedAmplitude:
        """This method creates a ModulatedAmplitude object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ModulatedAmplitude
                session.odbs[name].ModulatedAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key.
        initial
            A Float specifying the constant A0A0.
        magnitude
            A Float specifying the coefficient AA.
        start
            A Float specifying the starting time t0t0. Possible values are non-negative numbers.
        frequency1
            A Float specifying the circular frequency 1 (ω1ω1). Possible values are positive
            numbers.
        frequency2
            A Float specifying the circular frequency 2 (ω2ω2). Possible values are positive
            numbers.
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
            and TOTAL. The default value is STEP.

        Returns
        -------
        ModulatedAmplitude
            A :py:class:`~abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.amplitudes[name] = amplitude = ModulatedAmplitude(
            name, initial, magnitude, start, frequency1, frequency2, timeSpan
        )
        return amplitude

    @abaqus_method_doc
    def PeriodicAmplitude(
        self,
        name: str,
        frequency: float,
        start: float,
        a_0: float,
        data: tuple,
        timeSpan: SymbolicConstant = STEP,
    ) -> PeriodicAmplitude:
        """This method creates a PeriodicAmplitude object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].PeriodicAmplitude
                session.odbs[name].PeriodicAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key.
        frequency
            A Float specifying the circular frequency ωω. Possible values are positive numbers.
        start
            A Float specifying the starting time t0t0. Possible values are positive numbers.
        a_0
            A Float specifying the constant A0A0.
        data
            A sequence of pairs of Floats specifying AiAi and BiBi pairs.
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
            and TOTAL. The default value is STEP.

        Returns
        -------
        PeriodicAmplitude
            A :py:class:`~abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.amplitudes[name] = amplitude = PeriodicAmplitude(
            name, frequency, start, a_0, data, timeSpan
        )
        return amplitude

    @abaqus_method_doc
    def PsdDefinition(
        self,
        name: str,
        data: tuple,
        unitType: SymbolicConstant = FORCE,
        referenceGravityAcceleration: float = 1,
        referenecePower: float = 0,
        user: Boolean = OFF,
        timeSpan: SymbolicConstant = STEP,
        amplitude: str = "",
    ) -> PsdDefinition:
        """This method creates a PsdDefinition object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].PsdDefinition
                session.odbs[name].PsdDefinition

        Parameters
        ----------
        name
            A String specifying the repository key.
        data
            A sequence of sequences of Floats specifying the real part of the frequency function,
            the imaginary part of the frequency function, and the frequency or frequency band number
            values, depending on the value of **unitType**.
        unitType
            A SymbolicConstant specifying the type of units for specifying the frequency function.
            FORCE implies power units. BASE implies gravity used to define base motion. DB implies
            decibel units. Possible values are FORCE, BASE, and DB. The default value is FORCE.
        referenceGravityAcceleration
            A Float specifying the reference gravity acceleration. This argument applies when
            **unitType** = BASE. The default value is 1.0.
        referenecePower
            A Float specifying the reference power value, in load units squared. This argument
            applies when **unitType** = DB. The default value is 0.0.
        user
            A Boolean specifying whether the frequency function is defined in user subroutine UPSD.
            If specified, then **data** is not applicable, and the **unitType** value must not be DB.
            The default value is OFF.
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
            and TOTAL. The default value is STEP.
        amplitude
            A String specifying the name of the amplitude that describes the dynamic event used to
            define the cross-spectral density frequency function. The default value is an empty
            string.

        Returns
        -------
        PsdDefinition
            A :py:class:`~abaqus.Amplitude.PsdDefinition.PsdDefinition` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.amplitudes[name] = amplitude = PsdDefinition(
            name,
            data,
            unitType,
            referenceGravityAcceleration,
            referenecePower,
            user,
            timeSpan,
            amplitude,
        )
        return amplitude

    @abaqus_method_doc
    def SmoothStepAmplitude(
        self, name: str, data: tuple, timeSpan: SymbolicConstant = STEP
    ) -> SmoothStepAmplitude:
        """This method creates a SmoothStepAmplitude object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].SmoothStepAmplitude
                session.odbs[name].SmoothStepAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key.
        data
            A sequence of pairs of Floats specifying time/frequency and amplitude pairs. Possible
            values for time/frequency are positive numbers.
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
            and TOTAL. The default value is STEP.

        Returns
        -------
        SmoothStepAmplitude
            A :py:class:`~abaqus.Amplitude.SmoothStepAmplitude.SmoothStepAmplitude` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.amplitudes[name] = amplitude = SmoothStepAmplitude(name, data, timeSpan)
        return amplitude

    @abaqus_method_doc
    def SolutionDependentAmplitude(
        self,
        name: str,
        initial: float = 1,
        minimum: float = 0,
        maximum: float = 1000,
        timeSpan: SymbolicConstant = STEP,
    ) -> SolutionDependentAmplitude:
        """This method creates a SolutionDependentAmplitude object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].SolutionDependentAmplitude
                session.odbs[name].SolutionDependentAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key.
        initial
            A Float specifying the initial amplitude value. Possible values are those between
            **minimum** and **maximum**. The default value is 1.0.
        minimum
            A Float specifying the minimum amplitude value. Possible values are those smaller than
            **maximum** and **initial**. The default value is 0.1.
        maximum
            A Float specifying the maximum amplitude value. Possible values are those larger than
            **minimum** and **initial**. The default value is 1000.0.
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
            and TOTAL. The default value is STEP.

        Returns
        -------
        SolutionDependentAmplitude
            A :py:class:`~abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.amplitudes[name] = amplitude = SolutionDependentAmplitude(
            name, initial, minimum, maximum, timeSpan
        )
        return amplitude

    @abaqus_method_doc
    def SpectrumAmplitude(
        self,
        name: str,
        method: SymbolicConstant,
        data: tuple,
        specificationUnits: SymbolicConstant = ACCELERATION,
        eventUnits: SymbolicConstant = EVENT_ACCELERATION,
        solution: SymbolicConstant = ABSOLUTE_VALUE,
        timeIncrement: float = 0,
        gravity: float = 1,
        criticalDamping: Boolean = OFF,
        timeSpan: SymbolicConstant = STEP,
        amplitude: str = "",
    ) -> SpectrumAmplitude:
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
        self.amplitudes[name] = amplitude = SpectrumAmplitude(
            name,
            method,
            data,
            specificationUnits,
            eventUnits,
            solution,
            timeIncrement,
            gravity,
            criticalDamping,
            timeSpan,
            amplitude,
        )
        return amplitude

    @abaqus_method_doc
    def TabularAmplitude(
        self,
        name: str,
        data: tuple,
        smooth: Union[SymbolicConstant, float] = SOLVER_DEFAULT,
        timeSpan: SymbolicConstant = STEP,
    ) -> TabularAmplitude:
        """This method creates a TabularAmplitude object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].TabularAmplitude
                session.odbs[name].TabularAmplitude

        Parameters
        ----------
        name
            A String specifying the repository key.
        data
            A sequence of pairs of Floats specifying time/frequency and amplitude pairs. Possible
            values for time/frequency are positive numbers.
        smooth
            The SymbolicConstant SOLVER_DEFAULT or a Float specifying the degree of smoothing.
            Possible float values are between 0 and 0.5. If **smooth** = SOLVER_DEFAULT, the default
            degree of smoothing will be determined by the solver. The default value is
            SOLVER_DEFAULT.
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
            and TOTAL. The default value is STEP.

        Returns
        -------
        TabularAmplitude
            A :py:class:`~abaqus.Amplitude.TabularAmplitude.TabularAmplitude` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.amplitudes[name] = amplitude = TabularAmplitude(
            name, data, smooth, timeSpan
        )
        return amplitude
