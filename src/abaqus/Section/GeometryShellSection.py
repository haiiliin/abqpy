import typing
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .LayerPropertiesArray import LayerPropertiesArray
from .RebarLayers import RebarLayers
from .ShellSection import ShellSection
from .TransverseShearShell import TransverseShearShell
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class GeometryShellSection(ShellSection):
    """The GeometryShellSection object defines the properties of a geometry shell section. The
    GeometryShellSection object has no explicit constructor and no methods. The
    GeometryShellSection object is an abstract base type.
    The GeometryShellSection object is derived from the ShellSection object.

    .. note:: 
        This object can be accessed by::

            import section
            mdb.models[name].parts[name].compositeLayups[i].section
            mdb.models[name].sections[name]
            import odbSection
            session.odbs[name].sections[name]
    """

    #: A String specifying the repository key.
    name: str = ""

    #: A SymbolicConstant specifying the distribution used for defining the thickness of the
    #: elements. Possible values are UNIFORM, ANALYTICAL_FIELD, DISCRETE_FIELD,
    #: NODAL_ANALYTICAL_FIELD, and NODAL_DISCRETE_FIELD. The default value is UNIFORM.
    thicknessType: SymbolicConstant = UNIFORM

    #: A Boolean specifying whether the shell section properties are specified by the user
    #: prior to the analysis (ON) or integrated during the analysis (OFF). The default value is
    #: OFF.
    preIntegrate: Boolean = OFF

    #: A SymbolicConstant specifying whether to use the default value for the Poisson's ratio.
    #: Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio
    #: is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an
    #: Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis
    #: is the value provided in **poisson**.The default value is DEFAULT.
    poissonDefinition: SymbolicConstant = DEFAULT

    #: A Float specifying the Poisson's ratio. Possible values are −1.0 ≤ **poisson** ≤ 0.5.
    #: This argument is valid only when **poissonDefinition** = VALUE. The default value is 0.5.
    poisson: float = 0

    #: A SymbolicConstant specifying the shell section integration rule. Possible values are
    #: SIMPSON and GAUSS. The default value is SIMPSON.
    integrationRule: SymbolicConstant = SIMPSON

    #: A SymbolicConstant specifying the mode used for temperature and field variable input
    #: across the section thickness. Possible values are GRADIENT and POINTWISE. The default
    #: value is GRADIENT.
    temperature: SymbolicConstant = GRADIENT

    #: A SymbolicConstant specifying the mechanical idealization used for the section
    #: calculations. This member is only applicable when **preIntegrate** is set to ON. Possible
    #: values are NO_IDEALIZATION, SMEAR_ALL_LAYERS, MEMBRANE, and BENDING. The default value
    #: is NO_IDEALIZATION.
    idealization: SymbolicConstant = NO_IDEALIZATION

    #: None or an Int specifying the number of temperature points to be input. This argument is
    #: valid only when **temperature** = POINTWISE. The default value is None.
    nTemp: typing.Optional[int] = None

    #: None or a Float specifying the effective thickness modulus. This argument is relevant
    #: only for continuum shells and must be used in conjunction with the argument **poisson**.
    #: The default value is None.
    thicknessModulus: typing.Optional[float] = None

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

    #: A :py:class:`~abaqus.Section.RebarLayers.RebarLayers` object specifying reinforcement properties.
    rebarLayers: RebarLayers = RebarLayers(CONSTANT, [])

    #: A String specifying the name of the AnalyticalField or DiscreteField object used to
    #: define the thickness of the shell elements at each node. The **nodalThicknessField**
    #: argument applies only when **thicknessType** = NODAL_ANALYTICAL_FIELD or
    #: **thicknessType** = NODAL_DISCRETE_FIELD. The default value is an empty string.
    nodalThicknessField: str = ""

    #: A :py:class:`~abaqus.Section.TransverseShearShell.TransverseShearShell` object specifying the transverse shear stiffness properties.
    transverseShear: typing.Optional[TransverseShearShell] = None

    @abaqus_method_doc
    def __init__(
        self,
        nodalThicknessField: str = "",
        thicknessField: str = "",
        thicknessType: SymbolicConstant = UNIFORM,
        preIntegrate: Boolean = OFF,
        poissonDefinition: SymbolicConstant = DEFAULT,
        poisson: float = 0,
        integrationRule: SymbolicConstant = SIMPSON,
        temperature: SymbolicConstant = GRADIENT,
        nTemp: typing.Optional[int] = None,
        thicknessModulus: typing.Optional[float] = None,
        useDensity: Boolean = OFF,
        density: float = 0,
    ):
        """This method creates a GeometryShellSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].compositeLayups[name].Section

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
            A :py:class:`~abaqus.Section.GeometryShellSection.GeometryShellSection` object.
        """
        ...

    @abaqus_method_doc
    def RebarLayers(
        self, rebarSpacing: SymbolicConstant, layerTable: LayerPropertiesArray
    ) -> RebarLayers:
        """This method creates a RebarLayers object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].compositeLayups[name].Section

        Parameters
        ----------
        rebarSpacing
            A SymbolicConstant specifying the type of rebar geometry. Possible values are CONSTANT,
            ANGULAR, and LIFT_EQUATION.
        layerTable
            A :py:class:`~abaqus.Section.LayerPropertiesArray.LayerPropertiesArray` object specifying the layers of reinforcement.

        Returns
        -------
        RebarLayers
            A :py:class:`~abaqus.Section.RebarLayers.RebarLayers` object.
        """
        self.rebarLayers = rebarLayers = RebarLayers(rebarSpacing, layerTable)
        return rebarLayers
