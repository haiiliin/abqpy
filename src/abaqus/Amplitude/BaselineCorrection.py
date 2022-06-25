class BaselineCorrection:
    """The BaselineCorrection object modifies an acceleration history to minimize the overall
    drift of the displacement obtained from the time integration of the given acceleration.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import amplitude
            mdb.models[name].amplitudes[name].baselineCorrection
            import odbAmplitude
            session.odbs[name].amplitudes[name].baselineCorrection

        The corresponding analysis keywords are:

        - BASELINE CORRECTION
    """

    #: A sequence of Floats specifying the correction time interval end points. Possible values
    #: are positive and monotonically increasing Floats. The default value is an empty
    #: sequence.
    intervals: tuple = ()

    def __init__(self, intervals: tuple = ()):
        """This method creates a BaselineCorrection object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].amplitudes[name].BaselineCorrection
                session.odbs[name].amplitudes[name].BaselineCorrection

        Parameters
        ----------
        intervals
            A sequence of Floats specifying the correction time interval end points. Possible values
            are positive and monotonically increasing Floats. The default value is an empty
            sequence.

        Returns
        -------
        BaselineCorrection
            A :py:class:`~abaqus.Amplitude.BaselineCorrection.BaselineCorrection` object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the BaselineCorrection object.

        Raises
        ------
        RangeError
        """
        pass
