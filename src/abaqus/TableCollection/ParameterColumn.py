from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class ParameterColumn:
    """The ParameterColumn object is used to define the type of parameters that will collectively build the type
    of parameter table. Once the object is created, it is noneditable.

    .. note::
        This object can be accessed by::

            mdb.models[name].tableCollections[name].parameterTables[name].columns[i]

        The corresponding analysis keywords are:

        - PARAMETER TABLE TYPE
        - PARAMETER TABLE

    .. versionadded:: 2020
        The ``ParameterColumn`` class was added.
    """

    #: A SymbolicConstant specifying the data type of the parameter. Possible values are
    #: STRING, INTEGER, and FLOAT.
    type: SymbolicConstant

    #: A String specifying the unit of the parameter.
    unit: str = ""

    #: A String specifying the description of the parameter.
    description: str = ""

    #: The default value of the first parameter. The data type of the value depends on the
    #: value of **type** argument.
    default: str = ""

    #: A Set of allowed values for the parameter.
    allowedValues: str = ""

    @abaqus_method_doc
    def __init__(
        self,
        type: Literal[C.INTEGER, C.FLOAT, C.STRING],
        unit: str = "",
        description: str = "",
        default: str = "",
        allowedValues: str = "",
    ):
        """ParameterColumn is a constructor method that creates a ParameterColumn object and stores it in the
        array data structure. It is accessible from the ParameterTable object using a column member.

        .. note::
            This function can be accessed by::

                mdb.models[name].tableCollections[name].parameterTables[name].Column

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
        ...
