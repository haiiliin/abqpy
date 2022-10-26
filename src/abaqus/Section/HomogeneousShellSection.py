from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .GeometryShellSection import GeometryShellSection
from .RebarLayers import RebarLayers
from .TransverseShearShell import TransverseShearShell
from ..UtilityAndView.SymbolicConstant import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import BENDING, Boolean, DEFAULT, GRADIENT, NO_IDEALIZATION, OFF, SIMPSON, UNIFORM


@abaqus_class_doc
class HomogeneousShellSection(GeometryShellSection):
    """The HomogeneousShellSection object defines the properties of a shell section.
    The HomogeneousShellSection object is derived from the GeometryShellSection object.

    .. note::
        This object can be accessed by::

            import section
            mdb.models[name].parts[name].compositeLayups[i].section
            mdb.models[name].sections[name]
            import odbSection
            session.odbs[name].sections[name]

        The corresponding analysis keywords are:

        - SHELL SECTION
        - SHELL GENERAL SECTION
    """

    #: A :py:class:`~abaqus.Section.RebarLayers.RebarLayers` object specifying reinforcement properties.
    rebarLayers: Optional[RebarLayers] = None

    #: A :py:class:`~abaqus.Section.TransverseShearShell.TransverseShearShell` object specifying the transverse shear stiffness properties.
    transverseShear: Optional[TransverseShearShell] = None

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of the section material.
    material: str

    #: A Float specifying the thickness of the section. The **thickness** argument applies only
    #: when **thicknessType** = UNIFORM. The default value is 0.0.
    thickness: float = 0

    #: An Int specifying the number of integration points to be used through the section.
    #: Possible values are **numIntPts** > 0. The default value is 5.To use the default settings
    #: of the analysis products, set **numIntPts** to 5 if **integrationRule** = SIMPSON or set
    #: **numIntPts** to 7 if **integrationRule** = GAUSS.
    numIntPts: int = 5

    #: A SymbolicConstant specifying the distribution used for defining the thickness of the
    #: elements. Possible values are UNIFORM, ANALYTICAL_FIELD, DISCRETE_FIELD,
    #: NODAL_ANALYTICAL_FIELD, and NODAL_DISCRETE_FIELD. The default value is UNIFORM.
    thicknessType: Literal[
        C.UNIFORM,
        C.ANALYTICAL_FIELD,
        C.DISCRETE_FIELD,
        C.NODAL_ANALYTICAL_FIELD,
        C.NODAL_DISCRETE_FIELD,
    ] = UNIFORM

    #: A Boolean specifying whether the shell section properties are specified by the user
    #: prior to the analysis (ON) or integrated during the analysis (OFF). The default value is
    #: OFF.
    preIntegrate: Boolean = OFF

    #: A SymbolicConstant specifying whether to use the default value for the Poisson's ratio.
    #: Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio
    #: is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an
    #: Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis
    #: is the value provided in **poisson**.The default value is DEFAULT.
    poissonDefinition: Literal[C.VALUE, C.DEFAULT] = DEFAULT

    #: A Float specifying the Poisson's ratio. Possible values are −1.0 ≤ **poisson** ≤ 0.5.
    #: This argument is valid only when **poissonDefinition** = VALUE. The default value is 0.5.
    poisson: float = 0

    #: A SymbolicConstant specifying the shell section integration rule. Possible values are
    #: SIMPSON and GAUSS. The default value is SIMPSON.
    integrationRule: Literal[C.SIMPSON, C.GAUSS] = SIMPSON

    #: A SymbolicConstant specifying the mode used for temperature and field variable input
    #: across the section thickness. Possible values are GRADIENT and POINTWISE. The default
    #: value is GRADIENT.
    temperature: Literal[C.GRADIENT, C.POINTWISE] = GRADIENT

    #: A SymbolicConstant specifying the mechanical idealization used for the section
    #: calculations. This member is only applicable when **preIntegrate** is set to ON. Possible
    #: values are NO_IDEALIZATION, SMEAR_ALL_LAYERS, MEMBRANE, and BENDING. The default value
    #: is NO_IDEALIZATION.
    idealization: Literal[C.NO_IDEALIZATION, C.SMEAR_ALL_LAYERS, C.MEMBRANE, C.BENDING] = NO_IDEALIZATION

    #: None or an Int specifying the number of temperature points to be input. This argument is
    #: valid only when **temperature** = POINTWISE. The default value is None.
    nTemp: Optional[int] = None

    #: None or a Float specifying the effective thickness modulus. This argument is relevant
    #: only for continuum shells and must be used in conjunction with the argument **poisson**.
    #: The default value is None.
    thicknessModulus: Optional[float] = None

    #: A Boolean specifying whether or not to use the value of **density**. The default value is
    #: OFF.
    useDensity: Boolean = OFF

    #: A Float specifying the value of density to apply to this section. The default value is
    #: 0.0.
    density: float = 0

    #: A String specifying the name of the AnalyticalField or DiscreteField object used to
    #: define the thickness of the shell elements. The **thicknessField** argument applies only
    #: when **thicknessType** = ANALYTICAL_FIELD or **thicknessType** = DISCRETE_FIELD. The default
    #: value is an empty string.
    thicknessField: str = ""

    #: A String specifying the name of the AnalyticalField or DiscreteField object used to
    #: define the thickness of the shell elements at each node. The **nodalThicknessField**
    #: argument applies only when **thicknessType** = NODAL_ANALYTICAL_FIELD or
    #: **thicknessType** = NODAL_DISCRETE_FIELD. The default value is an empty string.
    nodalThicknessField: str = ""

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        material: str,
        thickness: float = 0,
        numIntPts: int = 5,
        thicknessType: Literal[
            C.UNIFORM,
            C.ANALYTICAL_FIELD,
            C.DISCRETE_FIELD,
            C.NODAL_ANALYTICAL_FIELD,
            C.NODAL_DISCRETE_FIELD,
        ] = UNIFORM,
        preIntegrate: Boolean = OFF,
        poissonDefinition: Literal[C.VALUE, C.DEFAULT] = DEFAULT,
        poisson: float = 0,
        integrationRule: Literal[C.SIMPSON, C.GAUSS] = SIMPSON,
        temperature: Literal[C.GRADIENT, C.POINTWISE] = GRADIENT,
        idealization: Literal[C.NO_IDEALIZATION, C.SMEAR_ALL_LAYERS, C.MEMBRANE, BENDING] = NO_IDEALIZATION,
        nTemp: Optional[int] = None,
        thicknessModulus: Optional[float] = None,
        useDensity: Boolean = OFF,
        density: float = 0,
        thicknessField: str = "",
        nodalThicknessField: str = "",
    ) -> None:
        """This method creates a HomogeneousShellSection object.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].compositeLayups[i].HomogeneousShellSection
                mdb.models[name].HomogeneousShellSection
                session.odbs[name].HomogeneousShellSection

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
            A :py:class:`~abaqus.Section.HomogeneousShellSection.HomogeneousShellSection` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        thickness: float = 0,
        numIntPts: int = 5,
        thicknessType: Literal[
            C.UNIFORM,
            C.ANALYTICAL_FIELD,
            C.DISCRETE_FIELD,
            C.NODAL_ANALYTICAL_FIELD,
            C.NODAL_DISCRETE_FIELD,
        ] = UNIFORM,
        preIntegrate: Boolean = OFF,
        poissonDefinition: Literal[C.VALUE, C.DEFAULT] = DEFAULT,
        poisson: float = 0,
        integrationRule: Literal[C.SIMPSON, C.GAUSS] = SIMPSON,
        temperature: Literal[C.GRADIENT, C.POINTWISE] = GRADIENT,
        idealization: Literal[C.NO_IDEALIZATION, C.SMEAR_ALL_LAYERS, C.MEMBRANE, BENDING] = NO_IDEALIZATION,
        nTemp: Optional[int] = None,
        thicknessModulus: Optional[float] = None,
        useDensity: Boolean = OFF,
        density: float = 0,
        thicknessField: str = "",
        nodalThicknessField: str = "",
    ) -> None:
        """This method modifies the HomogeneousShellSection object.

        Parameters
        ----------
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
        """
        ...
