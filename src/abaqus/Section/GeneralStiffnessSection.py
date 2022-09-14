from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .RebarLayers import RebarLayers
from .ShellSection import ShellSection
from .TransverseShearShell import TransverseShearShell
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class GeneralStiffnessSection(ShellSection):
    """The GeneralStiffnessSection object defines the properties of a shell section via the
    stiffness matrix.
    The GeneralStiffnessSection object is derived from the ShellSection object.

    .. note:: 
        This object can be accessed by::

            import section
            mdb.models[name].sections[name]
            import odbSection
            session.odbs[name].sections[name]

        The corresponding analysis keywords are:

        - SHELL GENERAL SECTION
    """

    #: A :py:class:`~abaqus.Section.RebarLayers.RebarLayers` object specifying reinforcement properties.
    rebarLayers: RebarLayers = None

    #: A :py:class:`~abaqus.Section.TransverseShearShell.TransverseShearShell` object specifying the transverse shear stiffness properties.
    transverseShear: TransverseShearShell = None

    #: A String specifying the repository key.
    name: str

    #: A sequence of Floats specifying the stiffness matrix for the section in the order D11,
    #: D12, D22, D13, D23, D33, ...., D66. Twenty-one entries must be given.
    stiffnessMatrix: tuple

    #: None or a Float specifying the reference temperature for thermal expansion. The default
    #: value is None.
    referenceTemperature: float = None

    #: A Boolean specifying whether or not the section stiffness varies with thermal stresses.
    #: The default value is OFF.
    applyThermalStress: Boolean = OFF

    #: A Boolean specifying whether the data depend on temperature. The default value is OFF.
    temperatureDependency: Boolean = OFF

    #: An Int specifying the number of field variable dependencies. The default value is 0.
    dependencies: int = 0

    #: A SymbolicConstant specifying whether to use the default value for the Poisson's ratio.
    #: Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio
    #: is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an
    #: Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis
    #: is the value provided in **poisson**.The default value is DEFAULT.
    poissonDefinition: SymbolicConstant = DEFAULT

    #: A Float specifying the Poisson's ratio. Possible values are −1.0 ≤ **poisson** ≤ 0.5.
    #: This argument is valid only when **poissonDefinition** = VALUE. The default value is 0.5.
    poisson: float = 0

    #: A Boolean specifying whether or not to use the value of **density**. The default value is
    #: OFF.
    useDensity: Boolean = OFF

    #: A Float specifying the value of density to apply to this section. The default value is
    #: 0.0.
    density: float = 0

    #: A sequence of Floats specifying the generalized stress values caused by a unit
    #: temperature rise. Six entries must be given if the value of **applyThermalStress** is set
    #: to True. The default value is ("").
    thermalStresses: tuple = ()

    #: A sequence of sequences of Floats specifying the scaling factors for given temperatures
    #: and/or field data. Each row should contain (Y, alpha, T, F1,...,Fn). The default value
    #: is an empty sequence.
    scalingData: tuple = ()

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        stiffnessMatrix: tuple,
        referenceTemperature: float = None,
        applyThermalStress: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        poissonDefinition: SymbolicConstant = DEFAULT,
        poisson: float = 0,
        useDensity: Boolean = OFF,
        density: float = 0,
        thermalStresses: tuple = (),
        scalingData: tuple = (),
    ):
        """This method creates a GeneralStiffnessSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].GeneralStiffnessSection
                session.odbs[name].GeneralStiffnessSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        stiffnessMatrix
            A sequence of Floats specifying the stiffness matrix for the section in the order D11,
            D12, D22, D13, D23, D33, ...., D66. Twenty-one entries must be given.
        referenceTemperature
            None or a Float specifying the reference temperature for thermal expansion. The default
            value is None.
        applyThermalStress
            A Boolean specifying whether or not the section stiffness varies with thermal stresses.
            The default value is OFF.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        poissonDefinition
            A SymbolicConstant specifying whether to use the default value for the Poisson's ratio.
            Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio
            is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an
            Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis
            is the value provided in **poisson**.The default value is DEFAULT.
        poisson
            A Float specifying the Poisson's ratio. Possible values are −1.0 ≤ **poisson** ≤ 0.5.
            This argument is valid only when **poissonDefinition** = VALUE. The default value is 0.5.
        useDensity
            A Boolean specifying whether or not to use the value of **density**. The default value is
            OFF.
        density
            A Float specifying the value of density to apply to this section. The default value is
            0.0.
        thermalStresses
            A sequence of Floats specifying the generalized stress values caused by a unit
            temperature rise. Six entries must be given if the value of **applyThermalStress** is set
            to True. The default value is ("").
        scalingData
            A sequence of sequences of Floats specifying the scaling factors for given temperatures
            and/or field data. Each row should contain (Y, alpha, T, F1,...,Fn). The default value
            is an empty sequence.

        Returns
        -------
        GeneralStiffnessSection
            A :py:class:`~abaqus.Section.GeneralStiffnessSection.GeneralStiffnessSection` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        referenceTemperature: float = None,
        applyThermalStress: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        poissonDefinition: SymbolicConstant = DEFAULT,
        poisson: float = 0,
        useDensity: Boolean = OFF,
        density: float = 0,
        thermalStresses: tuple = (),
        scalingData: tuple = (),
    ):
        """This method modifies the GeneralStiffnessSection object.

        Parameters
        ----------
        referenceTemperature
            None or a Float specifying the reference temperature for thermal expansion. The default
            value is None.
        applyThermalStress
            A Boolean specifying whether or not the section stiffness varies with thermal stresses.
            The default value is OFF.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        poissonDefinition
            A SymbolicConstant specifying whether to use the default value for the Poisson's ratio.
            Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio
            is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an
            Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis
            is the value provided in **poisson**.The default value is DEFAULT.
        poisson
            A Float specifying the Poisson's ratio. Possible values are −1.0 ≤ **poisson** ≤ 0.5.
            This argument is valid only when **poissonDefinition** = VALUE. The default value is 0.5.
        useDensity
            A Boolean specifying whether or not to use the value of **density**. The default value is
            OFF.
        density
            A Float specifying the value of density to apply to this section. The default value is
            0.0.
        thermalStresses
            A sequence of Floats specifying the generalized stress values caused by a unit
            temperature rise. Six entries must be given if the value of **applyThermalStress** is set
            to True. The default value is ("").
        scalingData
            A sequence of sequences of Floats specifying the scaling factors for given temperatures
            and/or field data. Each row should contain (Y, alpha, T, F1,...,Fn). The default value
            is an empty sequence.
        """
        ...
