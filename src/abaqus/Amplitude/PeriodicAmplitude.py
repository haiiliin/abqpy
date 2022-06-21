from abaqusConstants import *
from .Amplitude import Amplitude


class PeriodicAmplitude(Amplitude):
    """The PeriodicAmplitude object defines an amplitude curve using a Fourier series.
    The PeriodicAmplitude object is derived from the Amplitude object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import amplitude
        mdb.models[name].amplitudes[name]
        import odbAmplitude
        session.odbs[name].amplitudes[name]

    The corresponding analysis keywords are:

    - AMPLITUDE
    """

    def __init__(
        self,
        name: str,
        frequency: float,
        start: float,
        a_0: float,
        data: tuple,
        timeSpan: SymbolicConstant = STEP,
    ):
        """This method creates a PeriodicAmplitude object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

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
        A :py:class:`~abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        super().__init__()
        pass

    def setValues(self, timeSpan: SymbolicConstant = STEP):
        """This method modifies the PeriodicAmplitude object.

        Parameters
        ----------
        timeSpan
            A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
            and TOTAL. The default value is STEP.

        Raises
        ------
        RangeError
        """
        pass
