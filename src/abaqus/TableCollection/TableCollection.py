from typing import Dict, List

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..TableCollection.DataTable import DataTable
from ..TableCollection.ParameterTable import ParameterTable
from ..TableCollection.PropertyTable import PropertyTable


@abaqus_class_doc
class TableCollection:
    """A TableCollection is an object used to define the containers that encapsulate the
    ParameterTable and PropertyTable objects.

    .. note:: 
        This object can be accessed by::

            mdb.models[name].tableCollections[name]

        The corresponding analysis keywords are:

        - TABLE COLLECTION

    .. versionadded:: 2020
        The `TableCollection` class was added.
    """

    #: A repository of the PropertyTable object.
    propertyTables: Dict[str, PropertyTable] = {}

    #: A repository of the ParameterTable object
    parameterTables: Dict[str, ParameterTable] = {}

    #: sequence of the DataTable object
    dataTables: List[DataTable] = []

    @abaqus_method_doc
    def __init__(self, name: str):
        """This method creates a TableCollection object and places it in the tableCollections
        repository.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].TableCollection

        Parameters
        ----------
        name
            A String specifying the repository key.

        Returns
        -------
        TableCollection
            A :py:class:`~abaqus.TableCollection.TableCollection.TableCollection` object.
        """
        ...

    @abaqus_method_doc
    def DataTable(self, label: str) -> DataTable:
        """This method creates a DataTable object and places it in the dataTables array.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].TableCollection

        Parameters
        ----------
        label
            A String specifying a unique label name for the current ParameterTable object.

        Returns
        -------
        DataTable
            A :py:class:`~abaqus.Field.DataTable.DataTable` object.

        Raises
        ------
        AbaqusException
        """
        dataTable = DataTable(label)
        self.dataTables.append(dataTable)
        return dataTable

    @abaqus_method_doc
    def ParameterTable(self, name: str) -> ParameterTable:
        """This method creates a ParameterTable object and places it in the parameterTables
        repository.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].TableCollection

        Parameters
        ----------
        name
            A String specifying the repository key.

        Returns
        -------
        ParameterTable
            A :py:class:`~abaqus.TableCollection.ParameterTable.ParameterTable` object.
        """
        self.parameterTables[name] = parameterTable = ParameterTable(name)
        return parameterTable

    @abaqus_method_doc
    def PropertyTable(
        self, name: str, properties: str, variables: str = ""
    ) -> PropertyTable:
        """This method creates a PropertyTable object.

        .. note:: 
            This function can be accessed by::

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
        PropertyTable
            A :py:class:`~abaqus.TableCollection.PropertyTable.PropertyTable` object.

        Raises
        ------
        RangeError
        """
        self.propertyTables[name] = propertyTable = PropertyTable(
            name, properties, variables
        )
        return propertyTable
