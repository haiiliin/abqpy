from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class DataTable:
    """The DataTable object is used to specify the parameter table of the respective parameter table type. The
    data type of the values in each column in the DataTable object corresponds to the data type mentioned for
    the respective ParameterColumn object. The DataTable object should be created when all the required
    ParameterColumn objects are created for the current ParameterTable.

    .. note::
        This object can be accessed by::

            mdb.models[name].tableCollections[name].parameterTables[name].dataTables[i]

        The corresponding analysis keywords are:

        - PARAMETER TABLE

    .. versionadded:: 2020
        The ``DataTable`` class was added.
    """

    #: A String specifying the label of the data table.
    label: str = ""

    #: A DataColumnArray specifying all the dataColumns in the DataTable object.
    columns: str = ""

    @abaqus_method_doc
    def __init__(self, label: str):
        """This method creates a DataTable object and places it in the dataTables array.

        .. note::
            This function can be accessed by::

                mdb.models[name].tableCollections[name].parameterTables[name].DataTable

        Parameters
        ----------
        label
            A String specifying a unique label name for the current ParameterTable object.

        Returns
        -------
        DataTable
            A DataTable object.

        Raises
        ------
        AbaqusException
        """
        ...
