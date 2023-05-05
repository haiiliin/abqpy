from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class TimePoint:
    """The TimePoint object defines time points at which data are written to the output database or restart
    files.

    .. note::
        This object can be accessed by::

            import step
            mdb.models[name].timePoints[name]

        The corresponding analysis keywords are:

        - TIME POINTS
    """

    #: A String specifying the repository key.
    name: str

    #: A sequence of sequences of Floats specifying time points at which data are written to
    #: the output database or restart files.
    points: tuple

    @abaqus_method_doc
    def __init__(self, name: str, points: tuple):
        """This method creates a TimePoint object.

        .. note::
            This function can be accessed by::

                mdb.models[name].TimePoint

        Parameters
        ----------
        name
            A String specifying the repository key.
        points
            A sequence of sequences of Floats specifying time points at which data are written to
            the output database or restart files.

        Returns
        -------
        TimePoint
            A TimePoint object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the TimePoint object.

        Raises
        ------
        RangeError
        """
        ...
