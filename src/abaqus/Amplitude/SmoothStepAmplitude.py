from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Amplitude import Amplitude
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class SmoothStepAmplitude(Amplitude):
    """The SmoothStepAmplitude object defines an amplitude that ramps up or down smoothly from
    one data point to another.
    The SmoothStepAmplitude object is derived from the Amplitude object.

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

    #: A sequence of pairs of Floats specifying time/frequency and amplitude pairs. Possible
    #: values for time/frequency are positive numbers.
    data: tuple

    #: A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
    #: and TOTAL. The default value is STEP.
    timeSpan: SymbolicConstant = STEP

    @abaqus_method_doc
    def __init__(self, name: str, data: tuple, timeSpan: SymbolicConstant = STEP):
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
        super().__init__()

    @abaqus_method_doc
    def setValues(self, timeSpan: SymbolicConstant = STEP):
        """This method modifies the SmoothStepAmplitude object.

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
