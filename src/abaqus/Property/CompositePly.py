from typing_extensions import Literal
from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import AXIS_1, ROTATION_NONE, SymbolicConstant


@abaqus_class_doc
class CompositePly:
    """The CompositePly object defines the material layers in a composite layup.

    .. note:: 
        This object can be accessed by::

            import section
            mdb.models[name].parts[name].compositeLayups[i].plies[i]
    """

    #: A Float specifying the thickness of the section layer.
    thickness: float

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the composite ply applies.
    region: Region

    #: A String specifying the name of the material for the ply.
    material: str

    #: A String specifying the ply identifier for this section layer. The default value is an
    #: empty string.
    plyName: str

    #: A SymbolicConstant specifying the method used to define the relative orientation. If
    #: **orientationType** = SPECIFY_ORIENT the **orientationValue** argument is required. If
    #: **orientationType** = CSYS the **orientation** argument is required. Possible values are CSYS,
    #: SPECIFY_ORIENT, ANGLE_0, ANGLE_45, ANGLE_90, and ANGLE_NEG45. The default value is
    #: ANGLE_0.
    orientationType: SymbolicConstant

    #: A SymbolicConstant specifying the method used to define the thickness. If
    #: thicknessType=SPECIFY_THICKNESS, the thickness argument is required.
    #: Possible values are SPECIFY_THICKNESS and FIELD_THICKNESS. The default
    #: value is SPECIFY_THICKNESS.
    #:
    #: ..versionchanged:: 2021
    #:     Add possible value ANALYTICAL_FIELD_THICKNESS.
    thicknessType: SymbolicConstant

    #: A Float specifying the relative orientation of the section layer. The default value is
    #: 0.0.
    orientationValue: float = 0

    #: A String specifying the name of the AnalyticalField or DiscreteField object used to
    #: define the thickness of the shell elements. The thicknessField argument applies only
    #: when thicknessType=ANALYTICAL_FIELD or thicknessType=DISCRETE_FIELD. The default
    #: value is an empty string.
    #:
    #: ..versionchanged:: 2021
    #:     Update docs for ANALYTICAL_FIELD_THICKNESS
    thicknessField: str = ""

    #: An Int specifying the number of integration points to be used through the section layer.
    #: This argument is valid only if **preIntegrate** = OFF. The default value is 3.
    numIntPts: int = 3

    #: A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
    #: system about which an additional rotation is applied. For shells this axis is also the
    #: shell normal. The **axis** argument applies only if a valid reference is provided for the
    #: **orientation**. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is
    #: AXIS_1.
    axis: SymbolicConstant = AXIS_1

    #: A Float specifying the angle of the additional rotation. The **angle** argument applies
    #: only if a valid reference is provided for the **orientation**. The default value is 0.0.
    angle: float = 0

    #: A SymbolicConstant specifying the method used to describe the additional rotation when a
    #: valid orientation is specified. Use **orientationType** = ANGLE_0 and
    #: **additionalRotationType** = ROTATION_FIELD to specify a discrete field of rotations for
    #: this CompositePly. Possible values are ROTATION_NONE, ROTATION_ANGLE, and
    #: ROTATION_FIELD. The default value is ROTATION_NONE.
    additionalRotationType: SymbolicConstant = ROTATION_NONE

    #: The SymbolicConstant None or a DatumCsys object specifying a coordinate system reference
    #: for the relative orientation of this layer. The default value is None.
    orientation: Optional[SymbolicConstant] = None

    #: A String specifying the name of the field specifying the additional rotation. The
    #: default value is an empty string.
    additionalRotationField: str = ""

    @abaqus_method_doc
    def __init__(
        self,
        thickness: float,
        region: Region,
        material: str,
        plyName: str,
        orientationType: Literal[C.ANGLE_45, C.ANGLE_0, C.CSYS, C.ANGLE_NEG45, C.SPECIFY_ORIENT, C.ANGLE_90],
        thicknessType: Literal[C.FIELD_THICKNESS, C.ANALYTICAL_FIELD_THICKNESS, C.SPECIFY_THICKNESS],
        orientationValue: float = 0,
        thicknessField: str = "",
        numIntPts: int = 3,
        axis: Literal[C.AXIS_1, C.AXIS_3, C.AXIS_2] = AXIS_1,
        angle: float = 0,
        additionalRotationType: Literal[C.ROTATION_NONE, C.ANGLE_0, C.ROTATION_FIELD, C.ROTATION_ANGLE] = ROTATION_NONE,
        orientation: Optional[SymbolicConstant] = None,
        additionalRotationField: str = "",
    ):
        """This method creates a CompositePly object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].compositeLayups[name].CompositePly

        Parameters
        ----------
        thickness
            A Float specifying the thickness of the section layer.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the composite ply applies.
        material
            A String specifying the name of the material for the ply.
        plyName
            A String specifying the ply identifier for this section layer. The default value is an
            empty string.
        orientationType
            A SymbolicConstant specifying the method used to define the relative orientation. If
            **orientationType** = SPECIFY_ORIENT the **orientationValue** argument is required. If
            **orientationType** = CSYS the **orientation** argument is required. Possible values are CSYS,
            SPECIFY_ORIENT, ANGLE_0, ANGLE_45, ANGLE_90, and ANGLE_NEG45. The default value is
            ANGLE_0.
        thicknessType
            A SymbolicConstant specifying the method used to define the thickness. If
            **thicknessType** = SPECIFY_THICKNESS, the **thickness** argument is required. Possible values
            are SPECIFY_THICKNESS, FIELD_THICKNESS, and ANALYTICAL_FIELD_THICKNESS. The default
            value is SPECIFY_THICKNESS.

            .. versionchanged:: 2021
                Add possible value ANALYTICAL_FIELD_THICKNESS.
        orientationValue
            A Float specifying the relative orientation of the section layer. The default value is
            0.0.
        thicknessField
            A String specifying the name of the AnalyticalField or DiscreteField object used to
            define the thickness of the shell elements and composite ply. The **thicknessField**
            argument applies when **thicknessType** = ANALYTICAL_FIELD or **thicknessType** = DISCRETE_FIELD
            for shell elements and **thicknessType** = FIELD_THICKNESS or
            **thicknessType** = ANALYTICAL_FIELD_THICKNESS for composite ply. The default value is an
            empty string.

            .. versionchanged:: 2021
                Update docs for ANALYTICAL_FIELD_THICKNESS
        numIntPts
            An Int specifying the number of integration points to be used through the section layer.
            This argument is valid only if **preIntegrate** = OFF. The default value is 3.
        axis
            A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
            system about which an additional rotation is applied. For shells this axis is also the
            shell normal. The **axis** argument applies only if a valid reference is provided for the
            **orientation**. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value is
            AXIS_1.
        angle
            A Float specifying the angle of the additional rotation. The **angle** argument applies
            only if a valid reference is provided for the **orientation**. The default value is 0.0.
        additionalRotationType
            A SymbolicConstant specifying the method used to describe the additional rotation when a
            valid orientation is specified. Use **orientationType** = ANGLE_0 and
            **additionalRotationType** = ROTATION_FIELD to specify a discrete field of rotations for
            this CompositePly. Possible values are ROTATION_NONE, ROTATION_ANGLE, and
            ROTATION_FIELD. The default value is ROTATION_NONE.
        orientation
            The SymbolicConstant None or a DatumCsys object specifying a coordinate system reference
            for the relative orientation of this layer. The default value is None.
        additionalRotationField
            A String specifying the name of the field specifying the additional rotation. The
            default value is an empty string.

        Returns
        -------
        CompositePly
            A :py:class:`~abaqus.Property.CompositePly.CompositePly` object.

        Raises
        ------
        AbaqusException
        """
        ...
