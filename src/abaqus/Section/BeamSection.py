from typing import Optional, Tuple

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Section import Section
from .TransverseShearBeam import TransverseShearBeam
from ..UtilityAndView.SymbolicConstant import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import ANALYSIS_DEFAULT, Boolean, CONSTANT, FULLY, LINEAR, OFF


@abaqus_class_doc
class BeamSection(Section):
    """The BeamSection object defines the properties of a beam section.
    The BeamSection object is derived from the Section object.

    .. note::
        This object can be accessed by::

            import section
            mdb.models[name].sections[name]
            import odbSection
            session.odbs[name].sections[name]

        The table data for this object are:

        - E, the Young's modulus of the section.
        - G, the torsional shear modulus of the section.
        - Thermal expansion coefficient, if using thermal expansion.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

        The corresponding analysis keywords are:

        - BEAM GENERAL SECTION
        - BEAM SECTION
        - BEAM FLUID INERTIA
        - CENTROID
        - DAMPING
        - SHEAR CENTER
        - SECTION POINTS
    """

    #: A :py:class:`~abaqus.Section.TransverseShearBeam.TransverseShearBeam` object specifying the transverse shear stiffness properties.
    beamTransverseShear: TransverseShearBeam = TransverseShearBeam(ANALYSIS_DEFAULT)

    #: A String specifying the repository key.
    name: str

    #: A SymbolicConstant specifying the integration method for the section. Possible values
    #: are BEFORE_ANALYSIS and DURING_ANALYSIS.
    integration: Literal[C.BEFORE_ANALYSIS, C.DURING_ANALYSIS]

    #: A String specifying the name of the profile. This argument represents the start profile
    #: in case of **beamShape** = TAPERED.
    profile: str

    #: A Float specifying the Poisson's ratio of the section. The default value is 0.0.
    poissonRatio: float = 0

    #: A Boolean specifying whether to use thermal expansion data. The default value is OFF.
    thermalExpansion: Boolean = OFF

    #: A Boolean specifying whether the data depend on temperature. The default value is OFF.
    temperatureDependency: Boolean = OFF

    #: An Int specifying the number of field variable dependencies. The default value is 0.
    dependencies: int = 0

    #: None or a Float specifying the density of the section. The default value is None.
    density: Optional[float] = None

    #: None or a Float specifying the reference temperature of the section. The default value
    #: is None.
    referenceTemperature: Optional[float] = None

    #: A SymbolicConstant specifying the temperature variation for the section. Possible values
    #: are LINEAR and INTERPOLATED. The default value is LINEAR.
    temperatureVar: Literal[C.LINEAR, C.INTERPOLATED] = LINEAR

    #: A Float specifying the αRαR factor to create mass proportional damping in
    #: direct-integration dynamics. The default value is 0.0.
    alphaDamping: float = 0

    #: A Float specifying the βRβR factor to create stiffness proportional damping in
    #: direct-integration dynamics. The default value is 0.0.
    betaDamping: float = 0

    #: A Float specifying the fraction of critical damping to be used in calculating composite
    #: damping factors for the modes (for use in modal dynamics). The default value is 0.0.
    compositeDamping: float = 0

    #: A Boolean specifying whether added mass effects will be simulated. The default value is
    #: OFF.
    useFluidInertia: Boolean = OFF

    #: A SymbolicConstant specifying whether the section is either full submerged or half
    #: submerged. This argument applies only when **useFluidInertia** = True. Possible values are
    #: FULLY and HALF. The default value is FULLY.
    submerged: Literal[C.FULLY, C.HALF] = FULLY

    #: None or a Float specifying the mass density of the fluid. This argument applies only
    #: when **useFluidInertia** = True and must be specified in that case. The default value is
    #: None.
    fluidMassDensity: Optional[float] = None

    #: None or a Float specifying the radius of the cylindrical cross-section. This argument
    #: applies only when **useFluidInertia** = True and must be specified in that case. The
    #: default value is None.
    crossSectionRadius: Optional[float] = None

    #: A Float specifying the added mass coefficient, CACA, for lateral motions of the beam.
    #: This argument applies only when*useFluidInertia* = True. The default value is 1.0.
    lateralMassCoef: float = 1

    #: A Float specifying the added mass coefficient, C(A−E)C(A-E), for motions along the axis
    #: of the beam. This argument affects only the term added to the free end(s) of the beam,
    #: and applies only when **useFluidInertia** = True. The default value is 0.0.
    axialMassCoef: float = 0

    #: A Float specifying the local 1-coordinate of the center of the cylindrical cross-section
    #: with respect to the beam cross-section. This argument applies only when
    #: **useFluidInertia** = True. The default value is 0.0.
    massOffsetX: float = 0

    #: A Float specifying the local 2-coordinate of the center of the cylindrical cross-section
    #: with respect to the beam cross-section. This argument applies only when
    #: **useFluidInertia** = True. The default value is 0.0.
    massOffsetY: float = 0

    #: A SymbolicConstant specifying the change in cross-section of the beam along length.
    #: Possible values are CONSTANT and TAPERED. The default value is CONSTANT. This parameter
    #: is available for manipulating the model database but not for the ODB API.
    beamShape: Literal[C.CONSTANT, C.TAPERED] = CONSTANT

    #: A String specifying the name of the material. The default value is an empty string. The
    #: material is required when **integration** is "DURING_ANALYSIS".
    material: str = ""

    #: A sequence of sequences of Floats specifying the items described below. The default
    #: value is an empty sequence.
    table: tuple = ()

    #: A sequence of pairs of Floats specifying the positions at which output is requested. The
    #: default value is an empty sequence.
    outputPts: tuple = ()

    #: A pair of Floats specifying the **X - Y** coordinates of the centroid. The default value is
    #: (0.0, 0.0).
    centroid: Tuple[float, float] = (0.0, 0.0)

    #: A pair of Floats specifying the **X - Y** coordinates of the shear center. The default value
    #: is (0.0, 0.0).
    shearCenter: Tuple[float, float] = (0.0, 0.0)

    #: A String specifying the name of the end profile. The type of the end profile must be
    #: same as that of the start profile. This argument is valid only when **beamShape** = TAPERED.
    #: The default value is an empty string. This parameter is available for manipulating the
    #: model database but not for the ODB API.
    profileEnd: str = ""

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        integration: Literal[C.BEFORE_ANALYSIS, C.DURING_ANALYSIS],
        profile: str,
        poissonRatio: float = 0,
        thermalExpansion: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        density: Optional[float] = None,
        referenceTemperature: Optional[float] = None,
        temperatureVar: Literal[C.LINEAR, C.INTERPOLATED] = LINEAR,
        alphaDamping: float = 0,
        betaDamping: float = 0,
        compositeDamping: float = 0,
        useFluidInertia: Boolean = OFF,
        submerged: Literal[C.FULLY, C.HALF] = FULLY,
        fluidMassDensity: Optional[float] = None,
        crossSectionRadius: Optional[float] = None,
        lateralMassCoef: float = 1,
        axialMassCoef: float = 0,
        massOffsetX: float = 0,
        massOffsetY: float = 0,
        beamShape: Literal[C.CONSTANT, C.TAPERED] = CONSTANT,
        material: str = "",
        table: tuple = (),
        outputPts: tuple = (),
        centroid: Tuple[float, float] = (0.0, 0.0),
        shearCenter: Tuple[float, float] = (0.0, 0.0),
        profileEnd: str = "",
    ) -> None:
        """This method creates a BeamSection object.

        .. note::
            This function can be accessed by::

                mdb.models[name].BeamSection
                session.odbs[name].BeamSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        integration
            A SymbolicConstant specifying the integration method for the section. Possible values
            are BEFORE_ANALYSIS and DURING_ANALYSIS.
        profile
            A String specifying the name of the profile. This argument represents the start profile
            in case of **beamShape** = TAPERED.
        poissonRatio
            A Float specifying the Poisson's ratio of the section. The default value is 0.0.
        thermalExpansion
            A Boolean specifying whether to use thermal expansion data. The default value is OFF.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        density
            None or a Float specifying the density of the section. The default value is None.
        referenceTemperature
            None or a Float specifying the reference temperature of the section. The default value
            is None.
        temperatureVar
            A SymbolicConstant specifying the temperature variation for the section. Possible values
            are LINEAR and INTERPOLATED. The default value is LINEAR.
        alphaDamping
            A Float specifying the αRαR factor to create mass proportional damping in
            direct-integration dynamics. The default value is 0.0.
        betaDamping
            A Float specifying the βRβR factor to create stiffness proportional damping in
            direct-integration dynamics. The default value is 0.0.
        compositeDamping
            A Float specifying the fraction of critical damping to be used in calculating composite
            damping factors for the modes (for use in modal dynamics). The default value is 0.0.
        useFluidInertia
            A Boolean specifying whether added mass effects will be simulated. The default value is
            OFF.
        submerged
            A SymbolicConstant specifying whether the section is either full submerged or half
            submerged. This argument applies only when **useFluidInertia** = True. Possible values are
            FULLY and HALF. The default value is FULLY.
        fluidMassDensity
            None or a Float specifying the mass density of the fluid. This argument applies only
            when **useFluidInertia** = True and must be specified in that case. The default value is
            None.
        crossSectionRadius
            None or a Float specifying the radius of the cylindrical cross-section. This argument
            applies only when **useFluidInertia** = True and must be specified in that case. The
            default value is None.
        lateralMassCoef
            A Float specifying the added mass coefficient, CACA, for lateral motions of the beam.
            This argument applies only when*useFluidInertia* = True. The default value is 1.0.
        axialMassCoef
            A Float specifying the added mass coefficient, C(A−E)C(A-E), for motions along the axis
            of the beam. This argument affects only the term added to the free end(s) of the beam,
            and applies only when **useFluidInertia** = True. The default value is 0.0.
        massOffsetX
            A Float specifying the local 1-coordinate of the center of the cylindrical cross-section
            with respect to the beam cross-section. This argument applies only when
            **useFluidInertia** = True. The default value is 0.0.
        massOffsetY
            A Float specifying the local 2-coordinate of the center of the cylindrical cross-section
            with respect to the beam cross-section. This argument applies only when
            **useFluidInertia** = True. The default value is 0.0.
        beamShape
            A SymbolicConstant specifying the change in cross-section of the beam along length.
            Possible values are CONSTANT and TAPERED. The default value is CONSTANT. This parameter
            is available for manipulating the model database but not for the ODB API.
        material
            A String specifying the name of the material. The default value is an empty string. The
            material is required when **integration** is "DURING_ANALYSIS".
        table
            A sequence of sequences of Floats specifying the items described below. The default
            value is an empty sequence.
        outputPts
            A sequence of pairs of Floats specifying the positions at which output is requested. The
            default value is an empty sequence.
        centroid
            A pair of Floats specifying the **X - Y** coordinates of the centroid. The default value is
            (0.0, 0.0).
        shearCenter
            A pair of Floats specifying the **X - Y** coordinates of the shear center. The default value
            is (0.0, 0.0).
        profileEnd
            A String specifying the name of the end profile. The type of the end profile must be
            same as that of the start profile. This argument is valid only when **beamShape** = TAPERED.
            The default value is an empty string. This parameter is available for manipulating the
            model database but not for the ODB API.

        Returns
        -------
        BeamSection
            A :py:class:`~abaqus.Section.BeamSection.BeamSection` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        poissonRatio: float = 0,
        thermalExpansion: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        density: Optional[float] = None,
        referenceTemperature: Optional[float] = None,
        temperatureVar: Literal[C.LINEAR, C.INTERPOLATED] = LINEAR,
        alphaDamping: float = 0,
        betaDamping: float = 0,
        compositeDamping: float = 0,
        useFluidInertia: Boolean = OFF,
        submerged: Literal[C.FULLY, C.HALF] = FULLY,
        fluidMassDensity: Optional[float] = None,
        crossSectionRadius: Optional[float] = None,
        lateralMassCoef: float = 1,
        axialMassCoef: float = 0,
        massOffsetX: float = 0,
        massOffsetY: float = 0,
        beamShape: Literal[C.CONSTANT, C.TAPERED] = CONSTANT,
        material: str = "",
        table: tuple = (),
        outputPts: tuple = (),
        centroid: Tuple[float, float] = (0.0, 0.0),
        shearCenter: Tuple[float, float] = (0.0, 0.0),
        profileEnd: str = "",
    ) -> None:
        """This method modifies the BeamSection object.

        Parameters
        ----------
        poissonRatio
            A Float specifying the Poisson's ratio of the section. The default value is 0.0.
        thermalExpansion
            A Boolean specifying whether to use thermal expansion data. The default value is OFF.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        density
            None or a Float specifying the density of the section. The default value is None.
        referenceTemperature
            None or a Float specifying the reference temperature of the section. The default value
            is None.
        temperatureVar
            A SymbolicConstant specifying the temperature variation for the section. Possible values
            are LINEAR and INTERPOLATED. The default value is LINEAR.
        alphaDamping
            A Float specifying the αRαR factor to create mass proportional damping in
            direct-integration dynamics. The default value is 0.0.
        betaDamping
            A Float specifying the βRβR factor to create stiffness proportional damping in
            direct-integration dynamics. The default value is 0.0.
        compositeDamping
            A Float specifying the fraction of critical damping to be used in calculating composite
            damping factors for the modes (for use in modal dynamics). The default value is 0.0.
        useFluidInertia
            A Boolean specifying whether added mass effects will be simulated. The default value is
            OFF.
        submerged
            A SymbolicConstant specifying whether the section is either full submerged or half
            submerged. This argument applies only when **useFluidInertia** = True. Possible values are
            FULLY and HALF. The default value is FULLY.
        fluidMassDensity
            None or a Float specifying the mass density of the fluid. This argument applies only
            when **useFluidInertia** = True and must be specified in that case. The default value is
            None.
        crossSectionRadius
            None or a Float specifying the radius of the cylindrical cross-section. This argument
            applies only when **useFluidInertia** = True and must be specified in that case. The
            default value is None.
        lateralMassCoef
            A Float specifying the added mass coefficient, CACA, for lateral motions of the beam.
            This argument applies only when*useFluidInertia* = True. The default value is 1.0.
        axialMassCoef
            A Float specifying the added mass coefficient, C(A−E)C(A-E), for motions along the axis
            of the beam. This argument affects only the term added to the free end(s) of the beam,
            and applies only when **useFluidInertia** = True. The default value is 0.0.
        massOffsetX
            A Float specifying the local 1-coordinate of the center of the cylindrical cross-section
            with respect to the beam cross-section. This argument applies only when
            **useFluidInertia** = True. The default value is 0.0.
        massOffsetY
            A Float specifying the local 2-coordinate of the center of the cylindrical cross-section
            with respect to the beam cross-section. This argument applies only when
            **useFluidInertia** = True. The default value is 0.0.
        beamShape
            A SymbolicConstant specifying the change in cross-section of the beam along length.
            Possible values are CONSTANT and TAPERED. The default value is CONSTANT. This parameter
            is available for manipulating the model database but not for the ODB API.
        material
            A String specifying the name of the material. The default value is an empty string. The
            material is required when **integration** is "DURING_ANALYSIS".
        table
            A sequence of sequences of Floats specifying the items described below. The default
            value is an empty sequence.
        outputPts
            A sequence of pairs of Floats specifying the positions at which output is requested. The
            default value is an empty sequence.
        centroid
            A pair of Floats specifying the **X - Y** coordinates of the centroid. The default value is
            (0.0, 0.0).
        shearCenter
            A pair of Floats specifying the **X - Y** coordinates of the shear center. The default value
            is (0.0, 0.0).
        profileEnd
            A String specifying the name of the end profile. The type of the end profile must be
            same as that of the start profile. This argument is valid only when **beamShape** = TAPERED.
            The default value is an empty string. This parameter is available for manipulating the
            model database but not for the ODB API.
        """
        ...
