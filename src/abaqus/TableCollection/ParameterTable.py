from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..TableCollection.ParameterColumn import ParameterColumn
from ..TableCollection.ParameterColumnArray import ParameterColumnArray
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class ParameterTable:
    """A ParameterTable is an object that is used to define the containers that encapsulate ParameterColumn and
    DataTable objects. The data of DataTable is dependent on the contents of ParameterColumn. After DataTable is
    instantiated, making changes to ParameterColumn may lead to data corruption.

    .. note::
        This object can be accessed by::

            mdb.models[name].tableCollections[name].parameterTables[name]

        The corresponding analysis keywords are:

        - PARAMETER TABLE TYPE
        - PARAMETER TABLE

    .. versionadded:: 2020
        The ``ParameterTable`` class was added.
    """

    #: A ParameterColumnArray specifying all the columns in the ParameterTable.
    columns: ParameterColumnArray = []

    #: A DataTableArray specifying all the dataTables in the ParameterTable.
    dataTables: str = ""

    @abaqus_method_doc
    def __init__(self, name: str):
        """This method creates a ParameterTable object and places it in the parameterTables repository.

        .. note::
            This function can be accessed by::

                mdb.models[name].tableCollections[name].ParameterTable

        Parameters
        ----------
        name
            A String specifying the repository key.

        Returns
        -------
        ParameterTable
            A ParameterTable object.
        """
        ...

    @abaqus_method_doc
    def Column(
        self,
        type: Literal[C.INTEGER, C.FLOAT, C.STRING],
        unit: str = "",
        description: str = "",
        default: str = "",
        allowedValues: str = "",
    ) -> ParameterColumn:
        """ParameterColumn is a constructor method that creates a ParameterColumn object and stores it in the
        array data structure. It is accessible from the ParameterTable object using a column member.

        .. note::
            This function can be accessed by::

                mdb.models[name].tableCollections[name].ParameterTable

        Parameters
        ----------
        type
            A SymbolicConstant specifying the data type of the parameter. Possible values are
            STRING, INTEGER, and FLOAT.
        unit
            A String specifying the unit of the parameter.
        description
            A String specifying the description of the parameter.
        default
            The default value of the first parameter. The data type of the value depends on the
            value of **type** argument.
        allowedValues
            A Set of allowed values for the parameter.

        Returns
        -------
        ParameterTable
            A ParameterTable object.

        Raises
        ------
        Incompatible data are given
        """
        parameterColumn = ParameterColumn(type, unit, description, default, allowedValues)
        self.columns.append(parameterColumn)
        return parameterColumn
