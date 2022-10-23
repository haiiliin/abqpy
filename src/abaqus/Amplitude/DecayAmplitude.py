from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Amplitude import Amplitude
from ..UtilityAndView.abaqusConstants import STEP, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class DecayAmplitude(Amplitude):
    """The DecayAmplitude object defines an amplitude curve using an exponential decay.
    The DecayAmplitude object is derived from the Amplitude object.

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

    #: A Float specifying the constant A0A0.
    initial: float

    #: A Float specifying the coefficient AA.
    maximum: float

    #: A Float specifying the starting time t0t0. Possible values are non-negative numbers.
    start: float

    #: A Float specifying the decay time tdtd. Possible values are non-negative numbers.
    decayTime: float

    #: A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
    #: and TOTAL. The default value is STEP.
    timeSpan: SymbolicConstant = STEP

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        initial: float,
        maximum: float,
        start: float,
        decayTime: float,
        timeSpan: Literal[C.STEP, C.TOTAL] = STEP,
    ):
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
        super().__init__()

    @abaqus_method_doc
    def setValues(self, timeSpan: Literal[C.STEP, C.TOTAL] = STEP):
        """This method modifies the DecayAmplitude object.

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
