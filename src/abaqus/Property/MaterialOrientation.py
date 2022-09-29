from typing import Optional
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..Datum.DatumAxis import DatumAxis
from ..Datum.DatumCsys import DatumCsys
from ..Region.Set import Set
from ..Region.Surface import Surface
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class MaterialOrientation:
    """The MaterialOrientation object represents the orientation of the material properties and
    composite layups.

    .. note:: 
        This object can be accessed by::

            import section
            mdb.models[name].parts[name].compositeLayups[i].orientation
            mdb.models[name].parts[name].materialOrientations[i]
            import odbAccess
            session.odbs[name].parts[name].materialOrientations[i]
            session.odbs[name].rootAssembly.instances[name].materialOrientations[i]
            session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.materialOrientations[i]
    """

    #: A SymbolicConstant specifying the method used to describe the additional rotation when a
    #: valid orientation is specified. Possible values are ROTATION_NONE, ROTATION_ANGLE, and
    #: ROTATION_FIELD. The default value is ROTATION_NONE.
    additionalRotationType: SymbolicConstant = ROTATION_NONE

    #: A String specifying the name of the DiscreteField object specifying the additional
    #: rotation. The default value is an empty string.
    additionalRotationField: str = ""

    #: A :py:class:`~abaqus.Region.Set.Set` object specifying a region for which the material orientation is defined.
    region: Set

    #: A :py:class:`~abaqus.Datum.DatumCsys.DatumCsys` object specifying the local coordinate system or None, describing the
    #: material orientation for the given region. In the ODB, this member was previously
    #: accessible using "csys," but support has now been added for localCsys and the csys
    #: member will be deprecated.
    localCsys: Optional[DatumCsys] = None

    #: A SymbolicConstant specifying the axis of a datum coordinate system about which an
    #: additional rotation is applied. For shells this axis is also the shell normal. Possible
    #: values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_1.
    axis: SymbolicConstant = AXIS_1

    #: A Float specifying the angle of the additional rotation (if accessed from the ODB
    #: instead of the MDB, it will be a string instead of a float). The default value is 0.0.
    angle: float = 0

    #: A SymbolicConstant specifying the stack or thickness direction. Possible values are
    #: STACK_1, STACK_2, STACK_3, and STACK_ORIENTATION. The default value is STACK_3.
    stackDirection: SymbolicConstant = STACK_3

    #: A String specifying the name of the DiscreteField object specifying the orientation. The
    #: default value is an empty string.
    fieldName: str = ""

    #: A SymbolicConstant specifying the method used to define the material orientation. If
    #: **orientationType** = SYSTEM, the **region** and **localCsys** arguments are required. If
    #: **orientationType** = FIELD, the **fieldName** argument is required. Possible values are
    #: GLOBAL, SYSTEM, FIELD, DISCRETE, and USER. The default value is GLOBAL.
    orientationType: SymbolicConstant = GLOBAL

    #: A SymbolicConstant specifying the axis that is defined by the normal axis direction for
    #: a discrete orientation. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default
    #: value is AXIS_3.
    normalAxisDirection: SymbolicConstant = AXIS_3

    #: A SymbolicConstant specifying the method used to define the normal axis direction for a
    #: discrete orientation. Possible values are SURFACE, NORMAL_DATUM, and NORMAL_VECTOR. The
    #: default value is NORMAL_VECTOR.
    normalAxisDefinition: SymbolicConstant = NORMAL_VECTOR

    #: A :py:class:`~abaqus.Region.Surface.Surface` object specifying a region whose geometric normals define the normal axis for
    #: the discrete orientation.
    normalAxisRegion: Optional[Surface] = None

    #: A :py:class:`~abaqus.Datum.DatumAxis.DatumAxis` object specifying the Datum Axis or None, describing the normal axis
    #: direction for the discrete orientation.
    normalAxisDatum: Optional[DatumAxis] = None

    #: A Boolean specifying the flag to reverse the direction of the defined normal axis
    #: direction. The default value is OFF.
    flipNormalDirection: Boolean = OFF

    #: A sequence of Floats specifying the vector that defines the direction of the normal axis
    #: of the discrete orientation.
    normalAxisVector: tuple = ()

    #: A SymbolicConstant specifying the axis that is defined by the primary axis direction for
    #: a discrete orientation. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default
    #: value is AXIS_1.
    primaryAxisDirection: SymbolicConstant = AXIS_1

    #: A SymbolicConstant specifying the method used to define the primary axis direction for a
    #: discrete orientation. Possible values are SURFACE, PRIMARY_DATUM, and PRIMARY_VECTOR.
    #: The default value is PRIMARY_VECTOR.
    primaryAxisDefinition: SymbolicConstant = PRIMARY_VECTOR

    #: A :py:class:`~abaqus.Region.Set.Set` object specifying a region whose geometric tangents define the primary axis for
    #: the discrete orientation.
    primaryAxisRegion: Optional[Set] = None

    #: A :py:class:`~abaqus.Datum.DatumAxis.DatumAxis` object specifying the Datum Axis or None, describing the primary axis
    #: direction for the discrete orientation.
    primaryAxisDatum: Optional[DatumAxis] = None

    #: A Boolean specifying the flag to reverse the direction of the defined primary axis
    #: direction. The default value is OFF.
    flipPrimaryDirection: Boolean = OFF

    #: A sequence of Floats specifying the vector that defines the direction of the primary
    #: axis of the discrete orientation.
    primaryAxisVector: tuple = ()

    @abaqus_method_doc
    def __init__(
        self,
        region: Set,
        localCsys: Optional[DatumCsys] = None, 
        axis: SymbolicConstant = AXIS_1,
        angle: float = 0,
        stackDirection: SymbolicConstant = STACK_3,
        fieldName: str = "",
        orientationType: SymbolicConstant = GLOBAL,
        normalAxisDirection: SymbolicConstant = AXIS_3,
        normalAxisDefinition: SymbolicConstant = NORMAL_VECTOR,
        normalAxisRegion: Optional[Surface] = None,
        normalAxisDatum: Optional[DatumAxis] = None, 
        flipNormalDirection: Boolean = OFF,
        normalAxisVector: tuple = (),
        primaryAxisDirection: SymbolicConstant = AXIS_1,
        primaryAxisDefinition: SymbolicConstant = PRIMARY_VECTOR,
        primaryAxisRegion: Optional[Set] = None,
        primaryAxisDatum: Optional[DatumAxis] = None, 
        flipPrimaryDirection: Boolean = OFF,
        primaryAxisVector: tuple = (),
    ):
        """This method creates a MaterialOrientation object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].MaterialOrientation

        Parameters
        ----------
        region
            A :py:class:`~abaqus.Region.Set.Set` object specifying a region for which the material orientation is defined.
        localCsys
            A :py:class:`~abaqus.Datum.DatumCsys.DatumCsys` object specifying the local coordinate system or None, describing the
            material orientation for the given region. In the ODB, this member was previously
            accessible using "csys," but support has now been added for localCsys and the csys
            member will be deprecated.
        axis
            A SymbolicConstant specifying the axis of a datum coordinate system about which an
            additional rotation is applied. For shells this axis is also the shell normal. Possible
            values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_1.
        angle
            A Float specifying the angle of the additional rotation (if accessed from the ODB
            instead of the MDB, it will be a string instead of a float). The default value is 0.0.
        stackDirection
            A SymbolicConstant specifying the stack or thickness direction. Possible values are
            STACK_1, STACK_2, STACK_3, and STACK_ORIENTATION. The default value is STACK_3.
        fieldName
            A String specifying the name of the DiscreteField object specifying the orientation. The
            default value is an empty string.
        orientationType
            A SymbolicConstant specifying the method used to define the material orientation. If
            **orientationType** = SYSTEM, the **region** and **localCsys** arguments are required. If
            **orientationType** = FIELD, the **fieldName** argument is required. Possible values are
            GLOBAL, SYSTEM, FIELD, DISCRETE, and USER. The default value is GLOBAL.
        normalAxisDirection
            A SymbolicConstant specifying the axis that is defined by the normal axis direction for
            a discrete orientation. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default
            value is AXIS_3.
        normalAxisDefinition
            A SymbolicConstant specifying the method used to define the normal axis direction for a
            discrete orientation. Possible values are SURFACE, NORMAL_DATUM, and NORMAL_VECTOR. The
            default value is NORMAL_VECTOR.
        normalAxisRegion
            A :py:class:`~abaqus.Region.Surface.Surface` object specifying a region whose geometric normals define the normal axis for
            the discrete orientation.
        normalAxisDatum
            A :py:class:`~abaqus.Datum.DatumAxis.DatumAxis` object specifying the Datum Axis or None, describing the normal axis
            direction for the discrete orientation.
        flipNormalDirection
            A Boolean specifying the flag to reverse the direction of the defined normal axis
            direction. The default value is OFF.
        normalAxisVector
            A sequence of Floats specifying the vector that defines the direction of the normal axis
            of the discrete orientation.
        primaryAxisDirection
            A SymbolicConstant specifying the axis that is defined by the primary axis direction for
            a discrete orientation. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default
            value is AXIS_1.
        primaryAxisDefinition
            A SymbolicConstant specifying the method used to define the primary axis direction for a
            discrete orientation. Possible values are SURFACE, PRIMARY_DATUM, and PRIMARY_VECTOR.
            The default value is PRIMARY_VECTOR.
        primaryAxisRegion
            A :py:class:`~abaqus.Region.Set.Set` object specifying a region whose geometric tangents define the primary axis for
            the discrete orientation.
        primaryAxisDatum
            A :py:class:`~abaqus.Datum.DatumAxis.DatumAxis` object specifying the Datum Axis or None, describing the primary axis
            direction for the discrete orientation.
        flipPrimaryDirection
            A Boolean specifying the flag to reverse the direction of the defined primary axis
            direction. The default value is OFF.
        primaryAxisVector
            A sequence of Floats specifying the vector that defines the direction of the primary
            axis of the discrete orientation.

        Returns
        -------
        MaterialOrientation
            A :py:class:`~abaqus.Property.MaterialOrientation.MaterialOrientation` object.
        """
        ...

    @abaqus_method_doc
    def ReferenceOrientation(
        self,
        localCsys: Optional[DatumCsys] = None, 
        axis: SymbolicConstant = AXIS_1,
        angle: float = 0,
        stackDirection: SymbolicConstant = STACK_3,
        fieldName: str = "",
        orientationType: SymbolicConstant = GLOBAL,
        additionalRotationField: str = "",
        additionalRotationType: SymbolicConstant = ROTATION_NONE,
        normalAxisDirection: SymbolicConstant = AXIS_3,
        normalAxisDefinition: SymbolicConstant = VECTOR,
        normalAxisRegion: Optional[Surface] = None,
        normalAxisDatum: Optional[DatumAxis] = None, 
        flipNormalDirection: Boolean = OFF,
        normalAxisVector: tuple = (),
        primaryAxisDirection: SymbolicConstant = AXIS_1,
        primaryAxisDefinition: SymbolicConstant = VECTOR,
        primaryAxisRegion: Optional[Set] = None,
        primaryAxisDatum: Optional[DatumAxis] = None, 
        flipPrimaryDirection: Boolean = OFF,
        primaryAxisVector: tuple = (),
    ):
        """This method creates a MaterialOrientation object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].MaterialOrientation

        Parameters
        ----------
        localCsys
            A :py:class:`~abaqus.Datum.DatumCsys.DatumCsys` object specifying the local coordinate system or None, describing the
            material orientation for the given region. In the ODB, this member was previously
            accessible using "csys," but support has now been added for localCsys and the csys
            member will be deprecated.
        axis
            A SymbolicConstant specifying the axis of a datum coordinate system about which an
            additional rotation is applied. For shells this axis is also the shell normal. Possible
            values are AXIS_1, AXIS_2, and AXIS_3. The default value is AXIS_1.
        angle
            A Float specifying the angle of the additional rotation (if accessed from the ODB
            instead of the MDB, it will be a string instead of a float). The default value is 0.0.
        stackDirection
            A SymbolicConstant specifying the stack or thickness direction. Possible values are
            STACK_1, STACK_2, STACK_3, and STACK_ORIENTATION. The default value is STACK_3.
        fieldName
            A String specifying the name of the DiscreteField object specifying the orientation. The
            default value is an empty string.
        orientationType
            A SymbolicConstant specifying the method used to define the material orientation. If
            **orientationType** = SYSTEM, the **region** and **localCsys** arguments are required. If
            **orientationType** = FIELD, the **fieldName** argument is required. Possible values are
            GLOBAL, SYSTEM, FIELD, DISCRETE, and USER. The default value is GLOBAL.
        additionalRotationField
            A String specifying the name of the DiscreteField object specifying the additional
            rotation. The default value is an empty string.
        additionalRotationType
            A SymbolicConstant specifying the method used to describe the additional rotation when a
            valid orientation is specified. Possible values are ROTATION_NONE, ROTATION_ANGLE, and
            ROTATION_FIELD. The default value is ROTATION_NONE.
        normalAxisDirection
            A SymbolicConstant specifying the axis that is defined by the normal axis direction for
            a discrete orientation. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default
            value is AXIS_3.
        normalAxisDefinition
            A SymbolicConstant specifying the method used to define the normal axis direction for a
            discrete orientation. Possible values are SURFACE, DATUM, and VECTOR. The default value
            is VECTOR.
        normalAxisRegion
            A :py:class:`~abaqus.Region.Surface.Surface` object specifying a region whose geometric normals define the normal axis for
            the discrete orientation.
        normalAxisDatum
            A :py:class:`~abaqus.Datum.DatumAxis.DatumAxis` object specifying the Datum Axis or None, describing the normal axis
            direction for the discrete orientation.
        flipNormalDirection
            A Boolean specifying the flag to reverse the direction of the defined normal axis
            direction. The default value is OFF.
        normalAxisVector
            A sequence of Floats specifying the vector that defines the direction of the normal axis
            of the discrete orientation.
        primaryAxisDirection
            A SymbolicConstant specifying the axis that is defined by the primary axis direction for
            a discrete orientation. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default
            value is AXIS_1.
        primaryAxisDefinition
            A SymbolicConstant specifying the method used to define the primary axis direction for a
            discrete orientation. Possible values are EDGE, DATUM, and VECTOR. The default value is
            VECTOR.
        primaryAxisRegion
            A :py:class:`~abaqus.Region.Set.Set` object specifying a region whose geometric tangents define the primary axis for
            the discrete orientation.
        primaryAxisDatum
            A :py:class:`~abaqus.Datum.DatumAxis.DatumAxis` object specifying the Datum Axis or None, describing the primary axis
            direction for the discrete orientation.
        flipPrimaryDirection
            A Boolean specifying the flag to reverse the direction of the defined primary axis
            direction. The default value is OFF.
        primaryAxisVector
            A sequence of Floats specifying the vector that defines the direction of the primary
            axis of the discrete orientation.

        Returns
        -------
        MaterialOrientation
            A :py:class:`~abaqus.Property.MaterialOrientation.MaterialOrientation` object.
        """
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the MaterialOrientation object."""
        ...
