from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .CompositePly import CompositePly
from .CompositePlyArray import CompositePlyArray
from .MaterialOrientation import MaterialOrientation
from ..Region.Region import Region
from ..Region.Set import Set
from ..Section.CompositeShellSection import CompositeShellSection
from ..Section.GeometryShellSection import GeometryShellSection
from ..Section.HomogeneousShellSection import HomogeneousShellSection
from ..Section.SectionLayerArray import SectionLayerArray
from ..UtilityAndView.abaqusConstants import (
    AXIS_1,
    Boolean,
    DEFAULT,
    GLOBAL,
    GRADIENT,
    NO_IDEALIZATION,
    OFF,
    ROTATION_NONE,
    SHELL,
    SIMPSON,
    SymbolicConstant,
    UNIFORM,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class CompositeLayup:
    """The CompositeLayup object is used to specify a composite layup on a part.

    .. note::
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].compositeLayups[i]

        The corresponding analysis keywords are:

        - SHELL SECTION
        - SHELL GENERAL SECTION
        - SOLID SECTION
    """

    #: A GeometryShellSection object.
    section: GeometryShellSection = GeometryShellSection()

    #: A MaterialOrientation object.
    orientation: MaterialOrientation = MaterialOrientation(Set(""))

    #: A CompositePlyArray object specifying the plies that make up this composite layup.
    plies: CompositePlyArray = []

    #: A String specifying the repository key.
    name: str

    #: A String specifying a description of the composite layup.
    description: str = ""

    #: A SymbolicConstant specifying the method used to define the shell offset. If
    #: **offsetType** = OFFSET_FIELD the **offsetField** argument is required. This member is valid
    #: only if **elementType** = SHELL. Possible values are SINGLE_VALUE, MIDDLE_SURFACE,
    #: TOP_SURFACE, BOTTOM_SURFACE, OFFSET_FIELD, and GLOBAL. The default value is GLOBAL.
    offsetType: SymbolicConstant = GLOBAL

    #: A String specifying The name of the field specifying the offset. This member is valid
    #: only if **elementType** = SHELL. The default value is an empty string.
    offsetField: str = ""

    #: A Float specifying The offset of the shell section. This member is valid only if
    #: **elementType** = SHELL. The default value is 0.0.
    offsetValues: float = 0

    #: A SymbolicConstant specifying the type of element in the composite layup. Possible
    #: values are SHELL, CONTINUUM_SHELL, and SOLID. The default value is SHELL.
    elementType: SymbolicConstant = SHELL

    #: A Boolean specifying whether or not the layup should be made symmetric by the analysis.
    #: The default value is OFF.
    symmetric: Boolean = OFF

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        description: str = "",
        offsetType: Literal[
            C.TOP_SURFACE, C.MIDDLE_SURFACE, C.BOTTOM_SURFACE, C.GLOBAL, C.SINGLE_VALUE, C.OFFSET_FIELD, C.SHELL
        ] = GLOBAL,
        offsetField: str = "",
        offsetValues: float = 0,
        elementType: Literal[C.SOLID, C.SHELL, C.CONTINUUM_SHELL] = SHELL,
        symmetric: Boolean = OFF,
    ):
        """This method creates a CompositeLayup object.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].CompositeLayup

        Parameters
        ----------
        name
            A String specifying the repository key.
        description
            A String specifying a description of the composite layup.
        offsetType
            A SymbolicConstant specifying the method used to define the shell offset. If
            **offsetType** = OFFSET_FIELD the **offsetField** argument is required. This member is valid
            only if **elementType** = SHELL. Possible values are SINGLE_VALUE, MIDDLE_SURFACE,
            TOP_SURFACE, BOTTOM_SURFACE, OFFSET_FIELD, and GLOBAL. The default value is GLOBAL.
        offsetField
            A String specifying The name of the field specifying the offset. This member is valid
            only if **elementType** = SHELL. The default value is an empty string.
        offsetValues
            A Float specifying The offset of the shell section. This member is valid only if
            **elementType** = SHELL. The default value is 0.0.
        elementType
            A SymbolicConstant specifying the type of element in the composite layup. Possible
            values are SHELL, CONTINUUM_SHELL, and SOLID. The default value is SHELL.
        symmetric
            A Boolean specifying whether or not the layup should be made symmetric by the analysis.
            The default value is OFF.

        Returns
        -------
        CompositeLayup
            A CompositeLayup object.

        Raises
        ------
        AbaqusException
        """
        ...

    @abaqus_method_doc
    def suppress(self):
        """This method suppresses a composite layup."""
        ...

    @abaqus_method_doc
    def resume(self):
        """This method resumes a composite layup that was previously suppressed."""
        ...

    @abaqus_method_doc
    def deletePlies(self):
        """This method deletes all of the plies from a composite layup."""
        ...

    @abaqus_method_doc
    def setValues(
        self,
        description: str = "",
        offsetType: Literal[
            C.TOP_SURFACE, C.MIDDLE_SURFACE, C.BOTTOM_SURFACE, C.GLOBAL, C.SINGLE_VALUE, C.OFFSET_FIELD, C.SHELL
        ] = GLOBAL,
        offsetField: str = "",
        offsetValues: float = 0,
        elementType: Literal[C.SOLID, C.SHELL, C.CONTINUUM_SHELL] = SHELL,
        symmetric: Boolean = OFF,
    ):
        """This method modifies the CompositeLayup object.

        Parameters
        ----------
        description
            A String specifying a description of the composite layup.
        offsetType
            A SymbolicConstant specifying the method used to define the shell offset. If
            **offsetType** = OFFSET_FIELD the **offsetField** argument is required. This member is valid
            only if **elementType** = SHELL. Possible values are SINGLE_VALUE, MIDDLE_SURFACE,
            TOP_SURFACE, BOTTOM_SURFACE, OFFSET_FIELD, and GLOBAL. The default value is GLOBAL.
        offsetField
            A String specifying The name of the field specifying the offset. This member is valid
            only if **elementType** = SHELL. The default value is an empty string.
        offsetValues
            A Float specifying The offset of the shell section. This member is valid only if
            **elementType** = SHELL. The default value is 0.0.
        elementType
            A SymbolicConstant specifying the type of element in the composite layup. Possible
            values are SHELL, CONTINUUM_SHELL, and SOLID. The default value is SHELL.
        symmetric
            A Boolean specifying whether or not the layup should be made symmetric by the analysis.
            The default value is OFF.
        """
        ...

    @abaqus_method_doc
    def CompositePly(
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
    ) -> CompositePly:
        """This method creates a CompositePly object.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].CompositeLayup

        Parameters
        ----------
        thickness
            A Float specifying the thickness of the section layer.
        region
            A Region object specifying the region to which the composite ply applies.
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
            A CompositePly object.

        Raises
        ------
        AbaqusException
        """
        compositePly = CompositePly(
            thickness,
            region,
            material,
            plyName,
            orientationType,
            thicknessType,
            orientationValue,
            thicknessField,
            numIntPts,
            axis,
            angle,
            additionalRotationType,
            orientation,
            additionalRotationField,
        )
        self.plies.append(compositePly)
        return compositePly

    @abaqus_method_doc
    def CompositeShellSection(
        self,
        name: str,
        layup: SectionLayerArray,
        symmetric: Boolean = OFF,
        thicknessType: Literal[
            C.DISCRETE_FIELD, C.NODAL_ANALYTICAL_FIELD, C.ANALYTICAL_FIELD, C.UNIFORM, C.NODAL_DISCRETE_FIELD
        ] = UNIFORM,
        preIntegrate: Boolean = OFF,
        poissonDefinition: Literal[C.DEFAULT] = DEFAULT,
        poisson: float = 0,
        integrationRule: Literal[C.GAUSS, C.SIMPSON] = SIMPSON,
        temperature: Literal[C.GRADIENT, C.POINTWISE] = GRADIENT,
        idealization: Literal[C.SMEAR_ALL_LAYERS, C.BENDING, C.MEMBRANE, C.NO_IDEALIZATION] = NO_IDEALIZATION,
        nTemp: Optional[int] = None,
        thicknessModulus: Optional[float] = None,
        useDensity: Boolean = OFF,
        density: float = 0,
        layupName: str = "",
        thicknessField: str = "",
        nodalThicknessField: str = "",
    ) -> CompositeShellSection:
        """This method creates a CompositeShellSection object.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].CompositeLayup

        Parameters
        ----------
        name
            A String specifying the repository key.
        layup
            A SectionLayerArray object specifying the shell cross-section.
        symmetric
            A Boolean specifying whether or not the layup should be made symmetric by the analysis.
            The default value is OFF.
        thicknessType
            A SymbolicConstant specifying the distribution used for defining the thickness of the
            elements. Possible values are UNIFORM, ANALYTICAL_FIELD, DISCRETE_FIELD,
            NODAL_ANALYTICAL_FIELD, and NODAL_DISCRETE_FIELD. The default value is UNIFORM.
        preIntegrate
            A Boolean specifying whether the shell section properties are specified by the user
            prior to the analysis (ON) or integrated during the analysis (OFF). The default value is
            OFF.
        poissonDefinition
            A SymbolicConstant specifying whether to use the default value for the Poisson's ratio.
            Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio
            is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an
            Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis
            is the value provided in **poisson**.The default value is DEFAULT.
        poisson
            A Float specifying the Poisson's ratio. Possible values are −1.0 ≤ **poisson** ≤ 0.5.
            This argument is valid only when **poissonDefinition** = VALUE. The default value is 0.5.
        integrationRule
            A SymbolicConstant specifying the shell section integration rule. Possible values are
            SIMPSON and GAUSS. The default value is SIMPSON.
        temperature
            A SymbolicConstant specifying the mode used for temperature and field variable input
            across the section thickness. Possible values are GRADIENT and POINTWISE. The default
            value is GRADIENT.
        idealization
            A SymbolicConstant specifying the mechanical idealization used for the section
            calculations. This member is only applicable when **preIntegrate** is set to ON. Possible
            values are NO_IDEALIZATION, SMEAR_ALL_LAYERS, MEMBRANE, and BENDING. The default value
            is NO_IDEALIZATION.
        nTemp
            None or an Int specifying the number of temperature points to be input. This argument is
            valid only when **temperature** = POINTWISE. The default value is None.
        thicknessModulus
            None or a Float specifying the effective thickness modulus. This argument is relevant
            only for continuum shells and must be used in conjunction with the argument **poisson**.
            The default value is None.
        useDensity
            A Boolean specifying whether or not to use the value of **density**. The default value is
            OFF.
        density
            A Float specifying the value of density to apply to this section. The default value is
            0.0.
        layupName
            A String specifying the layup name for this section. The default value is an empty
            string.
        thicknessField
            A String specifying the name of the AnalyticalField or DiscreteField object used to
            define the thickness of the shell elements. The **thicknessField** argument applies only
            when **thicknessType** = ANALYTICAL_FIELD or **thicknessType** = DISCRETE_FIELD. The default
            value is an empty string.
        nodalThicknessField
            A String specifying the name of the AnalyticalField or DiscreteField object used to
            define the thickness of the shell elements at each node. The **nodalThicknessField**
            argument applies only when **thicknessType** = NODAL_ANALYTICAL_FIELD or
            **thicknessType** = NODAL_DISCRETE_FIELD. The default value is an empty string.

        Returns
        -------
        CompositeShellSection
            A CompositeShellSection object.
        """
        self.section = compositeShellSection = CompositeShellSection(
            name,
            layup,
            symmetric,
            thicknessType,
            preIntegrate,
            poissonDefinition,
            poisson,
            integrationRule,
            temperature,
            idealization,
            nTemp,
            thicknessModulus,
            useDensity,
            density,
            layupName,
            thicknessField,
            nodalThicknessField,
        )
        return compositeShellSection

    @abaqus_method_doc
    def GeometryShellSection(
        self,
        nodalThicknessField: str = "",
        thicknessField: str = "",
        thicknessType: Literal[
            C.DISCRETE_FIELD, C.NODAL_ANALYTICAL_FIELD, C.ANALYTICAL_FIELD, C.UNIFORM, C.NODAL_DISCRETE_FIELD
        ] = UNIFORM,
        preIntegrate: Boolean = OFF,
        poissonDefinition: Literal[C.DEFAULT] = DEFAULT,
        poisson: float = 0,
        integrationRule: Literal[C.GAUSS, C.SIMPSON] = SIMPSON,
        temperature: Literal[C.GRADIENT, C.POINTWISE] = GRADIENT,
        nTemp: Optional[int] = None,
        thicknessModulus: Optional[float] = None,
        useDensity: Boolean = OFF,
        density: float = 0,
    ) -> GeometryShellSection:
        """This method creates a GeometryShellSection object.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].CompositeLayup

        Parameters
        ----------
        nodalThicknessField
            A String specifying the name of the AnalyticalField or DiscreteField object used to
            define the thickness of the shell elements at each node. The **nodalThicknessField**
            argument applies only when **thicknessType** = NODAL_ANALYTICAL_FIELD or
            **thicknessType** = NODAL_DISCRETE_FIELD. The default value is an empty string.
        thicknessField
            A String specifying the name of the AnalyticalField or DiscreteField object used to
            define the thickness of the shell elements. The **thicknessField** argument applies only
            when **thicknessType** = ANALYTICAL_FIELD or **thicknessType** = DISCRETE_FIELD. The default
            value is an empty string.
        thicknessType
            A SymbolicConstant specifying the distribution used for defining the thickness of the
            elements. Possible values are UNIFORM, ANALYTICAL_FIELD, DISCRETE_FIELD,
            NODAL_ANALYTICAL_FIELD, and NODAL_DISCRETE_FIELD. The default value is UNIFORM.
        preIntegrate
            A Boolean specifying whether the shell section properties are specified by the user
            prior to the analysis (ON) or integrated during the analysis (OFF). The default value is
            OFF.
        poissonDefinition
            A SymbolicConstant specifying whether to use the default value for the Poisson's ratio.
            Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio
            is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an
            Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis
            is the value provided in **poisson**.The default value is DEFAULT.
        poisson
            A Float specifying the Poisson's ratio. Possible values are −1.0 ≤ **poisson** ≤ 0.5.
            This argument is valid only when **poissonDefinition** = VALUE. The default value is 0.5.
        integrationRule
            A SymbolicConstant specifying the shell section integration rule. Possible values are
            SIMPSON and GAUSS. The default value is SIMPSON.
        temperature
            A SymbolicConstant specifying the mode used for temperature and field variable input
            across the section thickness. Possible values are GRADIENT and POINTWISE. The default
            value is GRADIENT.
        nTemp
            None or an Int specifying the number of temperature points to be input. This argument is
            valid only when **temperature** = POINTWISE. The default value is None.
        thicknessModulus
            None or a Float specifying the effective thickness modulus. This argument is relevant
            only for continuum shells and must be used in conjunction with the argument **poisson**.
            The default value is None.
        useDensity
            A Boolean specifying whether or not to use the value of **density**. The default value is
            OFF.
        density
            A Float specifying the value of density to apply to this section. The default value is
            0.0.

        Returns
        -------
        GeometryShellSection
            A GeometryShellSection object.
        """
        self.section = geometryShellSection = GeometryShellSection(
            nodalThicknessField,
            thicknessField,
            thicknessType,
            preIntegrate,
            poissonDefinition,
            poisson,
            integrationRule,
            temperature,
            nTemp,
            thicknessModulus,
            useDensity,
            density,
        )
        return geometryShellSection

    @abaqus_method_doc
    def HomogeneousShellSection(
        self,
        name: str,
        material: str,
        thickness: float = 0,
        numIntPts: int = 5,
        thicknessType: Literal[
            C.DISCRETE_FIELD, C.NODAL_ANALYTICAL_FIELD, C.ANALYTICAL_FIELD, C.UNIFORM, C.NODAL_DISCRETE_FIELD
        ] = UNIFORM,
        preIntegrate: Boolean = OFF,
        poissonDefinition: Literal[C.DEFAULT] = DEFAULT,
        poisson: float = 0,
        integrationRule: Literal[C.GAUSS, C.SIMPSON] = SIMPSON,
        temperature: Literal[C.GRADIENT, C.POINTWISE] = GRADIENT,
        idealization: Literal[C.SMEAR_ALL_LAYERS, C.BENDING, C.MEMBRANE, C.NO_IDEALIZATION] = NO_IDEALIZATION,
        nTemp: Optional[int] = None,
        thicknessModulus: Optional[float] = None,
        useDensity: Boolean = OFF,
        density: float = 0,
        thicknessField: str = "",
        nodalThicknessField: str = "",
    ) -> HomogeneousShellSection:
        """This method creates a HomogeneousShellSection object.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].CompositeLayup

        Parameters
        ----------
        name
            A String specifying the repository key.
        material
            A String specifying the name of the section material.
        thickness
            A Float specifying the thickness of the section. The **thickness** argument applies only
            when **thicknessType** = UNIFORM. The default value is 0.0.
        numIntPts
            An Int specifying the number of integration points to be used through the section.
            Possible values are **numIntPts** > 0. The default value is 5.To use the default settings
            of the analysis products, set **numIntPts** to 5 if **integrationRule** = SIMPSON or set
            **numIntPts** to 7 if **integrationRule** = GAUSS.
        thicknessType
            A SymbolicConstant specifying the distribution used for defining the thickness of the
            elements. Possible values are UNIFORM, ANALYTICAL_FIELD, DISCRETE_FIELD,
            NODAL_ANALYTICAL_FIELD, and NODAL_DISCRETE_FIELD. The default value is UNIFORM.
        preIntegrate
            A Boolean specifying whether the shell section properties are specified by the user
            prior to the analysis (ON) or integrated during the analysis (OFF). The default value is
            OFF.
        poissonDefinition
            A SymbolicConstant specifying whether to use the default value for the Poisson's ratio.
            Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio
            is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an
            Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis
            is the value provided in **poisson**.The default value is DEFAULT.
        poisson
            A Float specifying the Poisson's ratio. Possible values are −1.0 ≤ **poisson** ≤ 0.5.
            This argument is valid only when **poissonDefinition** = VALUE. The default value is 0.5.
        integrationRule
            A SymbolicConstant specifying the shell section integration rule. Possible values are
            SIMPSON and GAUSS. The default value is SIMPSON.
        temperature
            A SymbolicConstant specifying the mode used for temperature and field variable input
            across the section thickness. Possible values are GRADIENT and POINTWISE. The default
            value is GRADIENT.
        idealization
            A SymbolicConstant specifying the mechanical idealization used for the section
            calculations. This member is only applicable when **preIntegrate** is set to ON. Possible
            values are NO_IDEALIZATION, SMEAR_ALL_LAYERS, MEMBRANE, and BENDING. The default value
            is NO_IDEALIZATION.
        nTemp
            None or an Int specifying the number of temperature points to be input. This argument is
            valid only when **temperature** = POINTWISE. The default value is None.
        thicknessModulus
            None or a Float specifying the effective thickness modulus. This argument is relevant
            only for continuum shells and must be used in conjunction with the argument **poisson**.
            The default value is None.
        useDensity
            A Boolean specifying whether or not to use the value of **density**. The default value is
            OFF.
        density
            A Float specifying the value of density to apply to this section. The default value is
            0.0.
        thicknessField
            A String specifying the name of the AnalyticalField or DiscreteField object used to
            define the thickness of the shell elements. The **thicknessField** argument applies only
            when **thicknessType** = ANALYTICAL_FIELD or **thicknessType** = DISCRETE_FIELD. The default
            value is an empty string.
        nodalThicknessField
            A String specifying the name of the AnalyticalField or DiscreteField object used to
            define the thickness of the shell elements at each node. The **nodalThicknessField**
            argument applies only when **thicknessType** = NODAL_ANALYTICAL_FIELD or
            **thicknessType** = NODAL_DISCRETE_FIELD. The default value is an empty string.

        Returns
        -------
        HomogeneousShellSection
            A HomogeneousShellSection object.
        """
        self.section[name] = homogeneousShellSection = HomogeneousShellSection(
            name,
            material,
            thickness,
            numIntPts,
            thicknessType,
            preIntegrate,
            poissonDefinition,
            poisson,
            integrationRule,
            temperature,
            idealization,
            nTemp,
            thicknessModulus,
            useDensity,
            density,
            thicknessField,
            nodalThicknessField,
        )
        return homogeneousShellSection
