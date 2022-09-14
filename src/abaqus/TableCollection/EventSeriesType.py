from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

@abaqus_class_doc
class EventSeriesType:
    """The EventSeriesType object is used to define a type of event in a process.

    .. note:: 
        This object can be accessed by::

            mdb.models[name].eventSeriesTypes[name]

        The corresponding analysis keywords are:

        - EVENT SERIES TYPE
        - EVENT SERIES

    .. versionadded:: 2020
        The `EventSeriesType` class was added.
    """

    #: A String specifying the repository key.
    name: str

    #: A string specifying the step name.
    createStepName: str

    #: A String array specifying fields. The default value is an empty array.
    fields: str = ""

    @abaqus_method_doc
    def __init__(self, name: str, createStepName: str, fields: str = ""):
        """This method creates an EventSeriesType object.

        .. note:: 
            This function can be accessed by::

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
        EventSeriesType
            A :py:class:`~abaqus.TableCollection.EventSeriesType.EventSeriesType` object.

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
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
        ...
