from abaqusConstants import *


class EventSeries:
    """The EventSeries object is used to define an event based on an already defined
    EventSeriesType object.
    After EventSeries is instantiated, making changes to EventSeriesType may lead to data
    corruption.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        mdb.models[name].eventSeriesDatas[name]

    The corresponding analysis keywords are:

    - EVENT SERIES TYPE
            - EVENT SERIES
    """

    def __init__(
        self,
        name: str,
        createStepName: str,
        eventSeriesType: str,
        transformType: str = NONE,
        timeSpan: str = STEP_TIME,
        transformations: str = "",
        fileName: str = "",
        data: str = "",
    ):
        """This method creates an EventSeries object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].EventSeriesData

        Parameters
        ----------
        name
            A String specifying the repository key.
        createStepName
            A string specifying the step name.
        eventSeriesType
            A string specifying the type of event series.
        transformType
            A Symbolic constant specifying the type of transformation. Possible values are NONE,
            BOTH, TRANSLATE, and ROTATE. The default value is NONE.
        timeSpan
            A Symbolic constant specifying time. Possible values are TOTAL_TIME and STEP_TIME. The
            default value is STEP_TIME.
        transformations
            An Array specifying the required transformations over event series data.
        fileName
            A String specifying the filename.
        data
            An Array of double specifying the values of fields provided in EventSeriesType.

        Returns
        -------
        An EventSeries object.

        Raises
        ------
        RangeError
        """
        pass

    def setValues(
        self,
        transformType: str = NONE,
        timeSpan: str = STEP_TIME,
        transformations: str = "",
        fileName: str = "",
        data: str = "",
    ):
        """This method modifies the EventSeries object.

        Parameters
        ----------
        transformType
            A Symbolic constant specifying the type of transformation. Possible values are NONE,
            BOTH, TRANSLATE, and ROTATE. The default value is NONE.
        timeSpan
            A Symbolic constant specifying time. Possible values are TOTAL_TIME and STEP_TIME. The
            default value is STEP_TIME.
        transformations
            An Array specifying the required transformations over event series data.
        fileName
            A String specifying the filename.
        data
            An Array of double specifying the values of fields provided in EventSeriesType.

        Returns
        -------

        Raises
        ------
        RangeError
        """
        pass
