from typing_extensions import Literal
from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import Boolean, OFF, SymbolicConstant


@abaqus_class_doc
class PropertyTableData:
    """A PropertyTableData is an object that is used to specify the property table of the
    respective property table type.
    The values in each column in the PropertyTableData object corresponds to the properties
    and variables mentioned in the PropertyTable object.

    .. note:: 
        This object can be accessed by::

            mdb.models[name].tableCollections[name].propertyTables[name].propertyTableDatas[name]

        The corresponding analysis keywords are:

        - PROPERTY TABLE TYPE
        - PROPERTY TABLE

    .. versionadded:: 2020
        The `PropertyTableData` class was added.
    """

    #: A String specifying a unique label name for the current PropertyTable object.
    label: str = ""

    #: A SymbolicConstant specifying the type of regularize to the user-defined property data.
    regularize: Optional[SymbolicConstant] = None

    #: A SymbolicConstant specifying the type of extrapolation of dependent variables outside
    #: the specified range of the independent variables.
    extrapolate: Optional[SymbolicConstant] = None

    #: A Boolean specifying the dependency of properties on temperature.
    isTemp: Boolean = OFF

    #: An Int specifying the field variables on which properties are dependent.
    fieldNums: Optional[int] = None

    #: A Double specifying the tolerance to be used to regularize the property table data.
    regularizeTolerance: str = ""

    #: An Array of doubles specifying the values of the properties, the variables mentioned in
    #: PropertyTable, and the field variables mentioned in PropertyTableData.
    data: str = ""

    @abaqus_method_doc
    def __init__(
        self,
        label: str = "",
        regularize: Optional[SymbolicConstant] = None,
        extrapolate: Optional[SymbolicConstant] = None,
        isTemp: Boolean = OFF,
        fieldNums: Optional[int] = None,
        regularizeTolerance: str = "",
        data: str = "",
    ):
        """This method creates a PropertyTableData object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].tableCollections[name].propertyTables[name].PropertTableData

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
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the PropertyTableData object.

        Returns
        -------

        Raises
        ------
        RangeError
        """
        ...
