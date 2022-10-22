from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Amplitude import Amplitude
from ..UtilityAndView.abaqusConstants import STEP, SymbolicConstant


@abaqus_class_doc
class PeriodicAmplitude(Amplitude):
    """The PeriodicAmplitude object defines an amplitude curve using a Fourier series.
    The PeriodicAmplitude object is derived from the Amplitude object.

    .. note:: 
        This object can be accessed by::

            import amplitude
            mdb.models[name].amplitudes[name]
            import odbAmplitude
            session.odbs[name].amplitudes[name]

        The corresponding analysis keywords are:

        - AMPLITUDE
    """

    #: A String specifying the repository key.
    name: str

    #: A Float specifying the circular frequency ωω. Possible values are positive numbers.
    frequency: float

    #: A Float specifying the starting time t0t0. Possible values are positive numbers.
    start: float

    #: A Float specifying the constant A0A0.
    a_0: float

    #: A sequence of pairs of Floats specifying AiAi and BiBi pairs.
    data: tuple

    #: A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
    #: and TOTAL. The default value is STEP.
    timeSpan: SymbolicConstant = STEP

    @abaqus_method_doc
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
        super().__init__()

    @abaqus_method_doc
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
        ...
