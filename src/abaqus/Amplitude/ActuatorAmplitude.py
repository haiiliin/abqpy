from abaqusConstants import *
from .Amplitude import Amplitude


class ActuatorAmplitude(Amplitude):
    """The ActuatorAmplitude object defines an actuator amplitude curve.
    The ActuatorAmplitude object is derived from the Amplitude object.

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

    def __init__(self, name: str, timeSpan: SymbolicConstant = STEP):
        """This method creates a ActuatorAmplitude object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

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
            An ActuatorAmplitude object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        super().__init__()
        pass

    def setValues(self, timeSpan: SymbolicConstant = STEP):
        """This method modifies the ActuatorAmplitude object.

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
