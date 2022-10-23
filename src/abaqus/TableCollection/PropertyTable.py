from typing import Dict, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .PropertyTableData import PropertyTableData
from ..UtilityAndView.abaqusConstants import Boolean, OFF, SymbolicConstant


@abaqus_class_doc
class PropertyTable:
    """A PropertyTable is an object that is used to define the container that encapsulates the
    PropertyTableData object.
    The data of the PropertyTableData object is dependent on the contents of the
    PropertyTable object.
    After PropertyTableDatais instantiated, making changes to PropertyTable may lead to data
    corruption.

    .. note:: 
        This object can be accessed by::

            mdb.models[name].tableCollections[name].propertyTables[name]

        The corresponding analysis keywords are:

        - PROPERTY TABLE TYPE
        - PROPERTY TABLE

    .. versionadded:: 2020
        The `PropertyTable` class was added.
    """

    #: A repository of PropertyTableData. Specifies all the propertyTableData in PropertyTable
    propertyTableDatas: Dict[str, PropertyTableData] = {}

    #: A String specifying the repository key.
    name: str

    #: A string array specifying the multiple properties to build the parameter table type.
    properties: str

    #: A String array specifying multiple independent variables. The default value is an empty
    #: array.
    variables: str = ""

    @abaqus_method_doc
    def __init__(self, name: str, properties: str, variables: str = ""):
        """This method creates a PropertyTable object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].tableCollections[name].PropertyTable

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
        ...

    @abaqus_method_doc
    def setValues(self, variables: str = ""):
        """This method modifies the PropertyTable object.

        Parameters
        ----------
        variables
            A String array specifying multiple independent variables. The default value is an empty
            array.

        Returns
        -------

        Raises
        ------
        RangeError
        """
        ...

    @abaqus_method_doc
    def PropertyTableData(
        self,
        label: str = "",
        regularize: Optional[SymbolicConstant] = None,
        extrapolate: Optional[SymbolicConstant] = None,
        isTemp: Boolean = OFF,
        fieldNums: Optional[int] = None,
        regularizeTolerance: str = "",
        data: str = "",
    ) -> PropertyTableData:
        """This method creates a PropertyTableData object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].tableCollections[name].PropertyTable

        Parameters
        ----------
        label
            A String specifying a unique label name for the current PropertyTable object.
        regularize
            A SymbolicConstant specifying the type of regularize to the user-defined property data.
        extrapolate
            A SymbolicConstant specifying the type of extrapolation of dependent variables outside
            the specified range of the independent variables.
        isTemp
            A Boolean specifying the dependency of properties on temperature.
        fieldNums
            An Int specifying the field variables on which properties are dependent.
        regularizeTolerance
            A Double specifying the tolerance to be used to regularize the property table data.
        data
            An Array of doubles specifying the values of the properties, the variables mentioned in
            PropertyTable, and the field variables mentioned in PropertyTableData.

        Returns
        -------
        PropertyTableData
            A :py:class:`~abaqus.TableCollection.PropertyTableData.PropertyTableData` object.

        Raises
        ------
        RangeError
        """
        self.propertyTableDatas[label] = propertyTableData = PropertyTableData(
            label, regularize, extrapolate, isTemp, fieldNums, regularizeTolerance, data
        )
        return propertyTableData
