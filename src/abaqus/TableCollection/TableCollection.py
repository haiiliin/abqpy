from ..TableCollection.DataTable import DataTable
from ..TableCollection.ParameterTable import ParameterTable
from ..TableCollection.PropertyTable import PropertyTable


class TableCollection:
    """A TableCollection is an object used to define the containers that encapsulate the
    ParameterTable and PropertyTable objects.

    Attributes
    ----------
    propertyTables: dict[str, PropertyTable]
        A repository of the :py:class:`~abaqus.TableCollection.PropertyTable.PropertyTable` object.
    parameterTables: dict[str, ParameterTable]
        A repository of the :py:class:`~abaqus.TableCollection.ParameterTable.ParameterTable` object
    dataTables: list[DataTable]
        sequence of the :py:class:`~abaqus.Field.DataTable.DataTable` object

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        mdb.models[name].tableCollections[name]

    The corresponding analysis keywords are:

    - *TABLE COLLECTION
    """

    # A repository of the PropertyTable object.
    propertyTables: dict[str, PropertyTable] = dict[str, PropertyTable]()

    # A repository of the ParameterTable object
    parameterTables: dict[str, ParameterTable] = dict[str, ParameterTable]()

    # sequence of the DataTable object
    dataTables: list[DataTable] = []

    def __init__(self, name: str):
        """This method creates a TableCollection object and places it in the tableCollections
        repository.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].TableCollection

        Parameters
        ----------
        name
            A String specifying the repository key.

        Returns
        -------
            A TableCollection object.
        """
        pass

    def DataTable(self, label: str) -> DataTable:
        """This method creates a DataTable object and places it in the dataTables array.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].TableCollection

        Parameters
        ----------
        label
            A String specifying a unique label name for the current ParameterTable object.

        Returns
        -------
            A DataTable object.

        Raises
        ------
            AbaqusException.
        """
        dataTable = DataTable(label)
        self.dataTables.append(dataTable)
        return dataTable

    def ParameterTable(self, name: str) -> ParameterTable:
        """This method creates a ParameterTable object and places it in the parameterTables
        repository.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].TableCollection

        Parameters
        ----------
        name
            A String specifying the repository key.

        Returns
        -------
            A ParameterTable object.
        """
        self.parameterTables[name] = parameterTable = ParameterTable(name)
        return parameterTable

    def PropertyTable(
        self, name: str, properties: str, variables: str = ""
    ) -> PropertyTable:
        """This method creates a PropertyTable object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].TableCollection

        Parameters
        ----------
        name
            A String specifying the repository key.
        properties
            A string array specifying the multiple properties to build the parameter table type.
        variables
            A String array specifying multiple independent variables. The default value is an empty
            array.

        Returns
        -------
            A PropertyTable object.

        Raises
        ------
            RangeError.
        """
        self.propertyTables[name] = propertyTable = PropertyTable(
            name, properties, variables
        )
        return propertyTable
