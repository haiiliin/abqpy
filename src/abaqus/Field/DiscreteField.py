from typing_extensions import Literal
from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .DataTableArray import DataTableArray
from .Field import Field
from ..Assembly.PartInstance import PartInstance
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import (Boolean, CARTESIAN, INSIDE, MEDIUM, NODES, OFF,
                                              SymbolicConstant)


@abaqus_class_doc
class DiscreteField(Field):
    """The DiscreteField object defines a varying field whose values correspond to distinct
    points within a domain.
    The DiscreteField object is derived from the Field object.

    .. note:: 
        This object can be accessed by::

            import fields
            mdb.models[name].discreteFields[name]
    """

    #: A String specifying the repository key.
    name: str

    #: A sequence of Floats specifying a sequence of floats specifying the default values.
    defaultValues: tuple

    #: A SymbolicConstant or an Int specifying the type of data represented by this discrete
    #: field. Possible values are SCALAR, ORIENTATION, and PRESCRIBEDCONDITION_DOF.
    fieldType: SymbolicConstant

    #: A SymbolicConstant or an Int specifying the location of the domain data. Possible values
    #: are NODES and ELEMENTS. The default value is NODES.
    location: SymbolicConstant = NODES

    #: An Int specifying the width of the supplied data. The default value is 1.
    dataWidth: int = 1

    #: A :py:class:`~abaqus.Field.DataTableArray.DataTableArray` object.
    data: Optional[DataTableArray] = None

    #: A String specifying the description of the field. The default value is an empty string.
    description: str = ""

    #: A SymbolicConstant specifying the type of the system being described by a discrete field
    #: used for an orientation. Possible values are CARTESIAN, CYLINDRICAL, and SPHERICAL. The
    #: default value is CARTESIAN.
    orientationType: SymbolicConstant = CARTESIAN

    #: A Boolean specifying whether or not the orientations are described in terms of part
    #: level coordinates. The default value is OFF.
    partLevelOrientation: Boolean = OFF

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        defaultValues: tuple,
        fieldType: Literal[C.PRESCRIBEDCONDITION_DOF, C.SCALAR, C.ORIENTATION],
        location: Literal[C.NODES, C.ELEMENTS] = NODES,
        dataWidth: int = 1,
        data: Optional[DataTableArray] = None,
        description: str = "",
        orientationType: Literal[C.CYLINDRICAL, C.CARTESIAN, C.SPHERICAL] = CARTESIAN,
        partLevelOrientation: Boolean = OFF,
    ):
        """This method creates a DiscreteField object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].DiscreteField

        Parameters
        ----------
        name
            A String specifying the repository key.
        defaultValues
            A sequence of Floats specifying a sequence of floats specifying the default values.
        fieldType
            A SymbolicConstant or an Int specifying the type of data represented by this discrete
            field. Possible values are SCALAR, ORIENTATION, and PRESCRIBEDCONDITION_DOF.
        location
            A SymbolicConstant or an Int specifying the location of the domain data. Possible values
            are NODES and ELEMENTS. The default value is NODES.
        dataWidth
            An Int specifying the width of the supplied data. The default value is 1.
        data
            A :py:class:`~abaqus.Field.DataTableArray.DataTableArray` object.
        description
            A String specifying the description of the field. The default value is an empty string.
        orientationType
            A SymbolicConstant specifying the type of the system being described by a discrete field
            used for an orientation. Possible values are CARTESIAN, CYLINDRICAL, and SPHERICAL. The
            default value is CARTESIAN.
        partLevelOrientation
            A Boolean specifying whether or not the orientations are described in terms of part
            level coordinates. The default value is OFF.

        Returns
        -------
        DiscreteField
            A :py:class:`~abaqus.Field.DiscreteField.DiscreteField` object.

        Raises
        ------
        AbaqusException
        """
        super().__init__()

    @abaqus_method_doc
    def DiscreteFieldByVolumeFraction(
        self,
        name: str,
        eulerianInstance: PartInstance,
        referenceInstance: PartInstance,
        accuracy: str = MEDIUM,
        materialLocation: str = INSIDE,
        description: str = "",
        scaleFactor: str = "",
    ):
        """This method creates a DiscreteField object that represents the volume fraction of each
        element of an Eulerian Instance that is occupied by a reference instance.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].DiscreteField

        Parameters
        ----------
        name
            A String specifying the repository key.
        eulerianInstance
            A :py:class:`~abaqus.Assembly.PartInstance.PartInstance` object specifying the elements for which volume fraction values will be
            computed.
        referenceInstance
            A :py:class:`~abaqus.Assembly.PartInstance.PartInstance` object specifying the region that either contains material or is empty of
            material.
        accuracy
            A Symbolic Constant specifying the level of accuracy that will be used in computing
            volume fractions. Possible values are LOW, MEDIUM, or HIGH. The default value is MEDIUM.
        materialLocation
            A Symbolic Constant indicating whether the material is inside or outside the
            **referenceInstance**. Possible values are INSIDE or OUTSIDE. The default value is INSIDE.
        description
            A String specifying the description of the field. The default value is an empty string.
        scaleFactor
            A float specifying the fraction of the volume that is occupied by the
            *referenceInstance.* Valid values are between 0 and 1.

        Returns
        -------
        DiscreteField
            A :py:class:`~abaqus.Field.DiscreteField.DiscreteField` object.

        Raises
        ------
        AbaqusException
        """
        ...

    @abaqus_method_doc
    def DiscreteFieldFromAnalytic(
        self,
        name: str,
        location: Literal[C.NODES, C.ELEMENTS],
        analyticFieldName: str,
        region: Region,
    ):
        """This method creates a DiscreteField object from a AnalyticalField object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].DiscreteField

        Parameters
        ----------
        name
            A String specifying the repository key.
        location
            A SymbolicConstant or an Int specifying the location of the domain data. Possible values
            are NODES and ELEMENTS. The default value is NODES.
        analyticFieldName
            A String specifying the name of the AnalyticalField containing the source data.
        region
            A :py:class:`~abaqus.Region.Region.Region` object for the field.

        Returns
        -------
        DiscreteField
            A :py:class:`~abaqus.Field.DiscreteField.DiscreteField` object.

        Raises
        ------
        AbaqusException
        """
        ...

    @abaqus_method_doc
    def setValues(
        self,
        location: Literal[C.NODES, C.ELEMENTS] = NODES,
        dataWidth: int = 1,
        data: Optional[DataTableArray] = None,
        description: str = "",
        orientationType: Literal[C.CYLINDRICAL, C.CARTESIAN, C.SPHERICAL] = CARTESIAN,
        partLevelOrientation: Boolean = OFF,
    ):
        """This method modifies the DiscreteField object.

        Parameters
        ----------
        location
            A SymbolicConstant or an Int specifying the location of the domain data. Possible values
            are NODES and ELEMENTS. The default value is NODES.
        dataWidth
            An Int specifying the width of the supplied data. The default value is 1.
        data
            A :py:class:`~abaqus.Field.DataTableArray.DataTableArray` object.
        description
            A String specifying the description of the field. The default value is an empty string.
        orientationType
            A SymbolicConstant specifying the type of the system being described by a discrete field
            used for an orientation. Possible values are CARTESIAN, CYLINDRICAL, and SPHERICAL. The
            default value is CARTESIAN.
        partLevelOrientation
            A Boolean specifying whether or not the orientations are described in terms of part
            level coordinates. The default value is OFF.
        """
        ...
