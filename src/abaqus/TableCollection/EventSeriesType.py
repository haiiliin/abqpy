class EventSeriesType:
    """The EventSeriesType object is used to define a type of event in a process.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        mdb.models[name].eventSeriesTypes[name]

    The corresponding analysis keywords are:

    - EVENT SERIES TYPE
            - EVENT SERIES
    """

    def __init__(self, name: str, createStepName: str, fields: str = ""):
        """This method creates an EventSeriesType object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].EventSeriesType

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A string specifying the step name.
        fields
            A String array specifying fields. The default value is an empty array.

        Returns
        -------
        A EventSeriesType object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self, fields: str = ""):
        """This method modifies the EventSeriesType object.

        Parameters
        ----------
        fields
            A String array specifying fields. The default value is an empty array.

        Returns
        -------

        Raises
        ------
        RangeError
        """
        pass
