from typing import Union, Optional, Tuple

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .AcousticInfiniteSection import AcousticInfiniteSection
from .AcousticInterfaceSection import AcousticInterfaceSection
from .BeamSection import BeamSection
from .CohesiveSection import CohesiveSection
from .CompositeShellSection import CompositeShellSection
from .CompositeSolidSection import CompositeSolidSection
from .ConnectorSection import ConnectorSection
from .EulerianSection import EulerianSection
from .GasketSection import GasketSection
from .GeneralStiffnessSection import GeneralStiffnessSection
from .HomogeneousShellSection import HomogeneousShellSection
from .HomogeneousSolidSection import HomogeneousSolidSection
from .MPCSection import MPCSection
from .MembraneSection import MembraneSection
from .PEGSection import PEGSection
from .SectionLayerArray import SectionLayerArray
from .SurfaceSection import SurfaceSection
from .TrussSection import TrussSection
from ..Connector.ConnectorBehaviorOptionArray import ConnectorBehaviorOptionArray
from ..Model.ModelBase import ModelBase
from ..UtilityAndView.SymbolicConstant import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import (BENDING, Boolean,
                                              CONSTANT, DEFAULT,
                                              DOF_MODE, FULLY, GRADIENT, LINEAR, NONE, NO_IDEALIZATION, OFF, ON,
                                              SIMPSON,
                                              SOLVER_DEFAULT, UNIFORM,
                                              UNSPECIFIED)


@abaqus_class_doc
class SectionModel(ModelBase):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    .. note:: 
        This object can be accessed by::

            mdb.models[name]
    """

    @abaqus_method_doc
    def AcousticInfiniteSection(
        self, name: str, material: str, thickness: float = 1, order: int = 10
    ) -> AcousticInfiniteSection:
        """This method creates an AcousticInfiniteSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].AcousticInfiniteSection
                session.odbs[name].AcousticInfiniteSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        material
            A String specifying the name of the material.
        thickness
            A Float specifying the thickness of the section. Possible values are **thickness** >> 0.0.
            The default value is 1.0.
        order
            An Int specifying the number of ninth-order polynomials that will be used to resolve the
            variation of the acoustic field in the infinite direction. Possible values are 0 <<
            **order** ≤ 10. The default value is 10.

        Returns
        -------
        AcousticInfiniteSection
            An :py:class:`~abaqus.Section.AcousticInfiniteSection.AcousticInfiniteSection` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.sections[name] = section = AcousticInfiniteSection(
            name, material, thickness, order
        )
        return section

    @abaqus_method_doc
    def AcousticInterfaceSection(
        self, name: str, thickness: float = 1
    ) -> AcousticInterfaceSection:
        """This method creates an AcousticInterfaceSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].AcousticInterfaceSection
                session.odbs[name].AcousticInterfaceSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        thickness
            A Float specifying the thickness of the section. Possible values are **thickness** >> 0.0.
            The default value is 1.0.

        Returns
        -------
        AcousticInterfaceSection
            An :py:class:`~abaqus.Section.AcousticInterfaceSection.AcousticInterfaceSection` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.sections[name] = section = AcousticInterfaceSection(name, thickness)
        return section

    @abaqus_method_doc
    def BeamSection(
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
    ) -> BeamSection:
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
        self.sections[name] = section = BeamSection(
            name,
            integration,
            profile,
            poissonRatio,
            thermalExpansion,
            temperatureDependency,
            dependencies,
            density,
            referenceTemperature,
            temperatureVar,
            alphaDamping,
            betaDamping,
            compositeDamping,
            useFluidInertia,
            submerged,
            fluidMassDensity,
            crossSectionRadius,
            lateralMassCoef,
            axialMassCoef,
            massOffsetX,
            massOffsetY,
            beamShape,
            material,
            table,
            outputPts,
            centroid,
            shearCenter,
            profileEnd,
        )
        return section

    @abaqus_method_doc
    def CohesiveSection(
        self,
        name: str,
        response: Literal[C.TRACTION_SEPARATION, C.CONTINUUM, C.GASKET],
        material: str,
        initialThicknessType: Literal[C.SOLVER_DEFAULT, C.SPECIFY] = SOLVER_DEFAULT,
        initialThickness: float = 1,
        outOfPlaneThickness: Optional[float] = None,
    ) -> CohesiveSection:
        """This method creates a CohesiveSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].CohesiveSection
                session.odbs[name].CohesiveSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        response
            A SymbolicConstant specifying the geometric assumption that defines the constitutive
            behavior of the cohesive elements. Possible values are TRACTION_SEPARATION, CONTINUUM,
            and GASKET.
        material
            A String specifying the name of the material.
        initialThicknessType
            A SymbolicConstant specifying the method used to compute the initial thickness. Possible
            values are:SOLVER_DEFAULT, specifying that Abaqus will use the analysis product
            defaultGEOMETRY, specifying that Abaqus will compute the thickness from the nodal
            coordinates of the elements.SPECIFY, specifying that Abaqus will use the value given for
            **initialThickness** The default value is SOLVER_DEFAULT.
        initialThickness
            A Float specifying the initial thickness for the section. The **initialThickness**
            argument applies only when **initialThicknessType** = SPECIFY. The default value is 1.0.
        outOfPlaneThickness
            None or a Float specifying the out-of-plane thickness for the section. The default value
            is None.

        Returns
        -------
        CohesiveSection
            A :py:class:`~abaqus.Section.CohesiveSection.CohesiveSection` object.

        Raises
        ------
        RangeError and InvalidNameError
        """
        self.sections[name] = section = CohesiveSection(
            name,
            response,
            material,
            initialThicknessType,
            initialThickness,
            outOfPlaneThickness,
        )
        return section

    @abaqus_method_doc
    def CompositeShellSection(
        self,
        name: str,
        layup: SectionLayerArray,
        symmetric: Boolean = OFF,
        thicknessType: Literal[
            C.UNIFORM,
            C.ANALYTICAL_FIELD,
            C.DISCRETE_FIELD,
            C.NODAL_ANALYTICAL_FIELD,
            C.NODAL_DISCRETE_FIELD,
        ] = UNIFORM,
        preIntegrate: Boolean = OFF,
        poissonDefinition: Literal[C.DEFAULT, C.VALUE] = DEFAULT,
        poisson: float = 0,
        integrationRule: Literal[C.SIMPSON, C.GAUSS] = SIMPSON,
        temperature: Literal[C.GRADIENT, C.POINTWISE] = GRADIENT,
        idealization: Literal[
            C.NO_IDEALIZATION, C.SMEAR_ALL_LAYERS, C.MEMBRANE, C.BENDING
        ] = NO_IDEALIZATION,
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

                mdb.models[name].parts[name].compositeLayups[i].CompositeShellSection
                mdb.models[name].CompositeShellSection
                session.odbs[name].CompositeShellSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        layup
            A :py:class:`~abaqus.Section.SectionLayerArray.SectionLayerArray` object specifying the shell cross-section.
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
            A :py:class:`~abaqus.Section.CompositeShellSection.CompositeShellSection` object.
        """
        self.sections[name] = section = CompositeShellSection(
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
        return section

    @abaqus_method_doc
    def CompositeSolidSection(
        self,
        name: str,
        layup: SectionLayerArray,
        symmetric: Boolean = OFF,
        layupName: str = "",
    ) -> CompositeSolidSection:
        """This method creates a CompositeSolidSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].CompositeSolidSection
                session.odbs[name].CompositeSolidSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        layup
            A :py:class:`~abaqus.Section.SectionLayerArray.SectionLayerArray` object specifying the solid cross-section.
        symmetric
            A Boolean specifying whether or not the layup should be made symmetric by the analysis.
            The default value is OFF.
        layupName
            A String specifying the layup name for this section. The default value is an empty
            string.

        Returns
        -------
        CompositeSolidSection
            A :py:class:`~abaqus.Section.CompositeSolidSection.CompositeSolidSection` object.
        """
        self.sections[name] = section = CompositeSolidSection(
            name, layup, symmetric, layupName
        )
        return section

    @abaqus_method_doc
    def ConnectorSection(
        self,
        name: str,
        assembledType: Literal[
            C.NONE,
            C.BEAM,
            C.BUSHING,
            C.CVJOINT,
            C.CYLINDRICAL,
            C.HINGE,
            C.PLANAR,
            C.RETRACTOR,
            C.SLIPRING,
            C.TRANSLATOR,
            C.UJOINT,
            C.WELD,
        ] = NONE,
        rotationalType: Literal[
            C.NONE,
            C.ALIGN,
            C.CARDAN,
            C.CONSTANT_VELOCITY,
            C.EULER,
            C.FLEXION_TORSION,
            C.FLOW_CONVERTER,
            C.PROJECTION_FLEXION_TORSION,
            C.REVOLUTE,
            C.ROTATION,
            C.ROTATION_ACCELEROMETER,
            C.UNIVERSAL,
        ] = NONE,
        translationalType: Literal[
            C.NONE,
            C.ACCELEROMETER,
            C.AXIAL,
            C.CARTESIAN,
            C.JOIN,
            C.LINK,
            C.PROJECTION_CARTESIAN,
            C.RADIAL_THRUST,
            C.SLIDE_PLANE,
            C.SLOT,
        ] = NONE,
        integration: Literal[C.UNSPECIFIED, C.IMPLICIT, C.EXPLICIT] = UNSPECIFIED,
        u1ReferenceLength: Optional[float] = None,
        u2ReferenceLength: Optional[float] = None,
        u3ReferenceLength: Optional[float] = None,
        ur1ReferenceAngle: Optional[float] = None,
        ur2ReferenceAngle: Optional[float] = None,
        ur3ReferenceAngle: Optional[float] = None,
        massPerLength: Optional[float] = None,
        contactAngle: Optional[float] = None,
        materialFlowFactor: float = 1.0,
        regularize: Boolean = ON,
        defaultTolerance: Boolean = ON,
        regularization: float = 0.03,
        extrapolation: Literal[C.CONSTANT, C.LINEAR] = CONSTANT,
        behaviorOptions: ConnectorBehaviorOptionArray = ...,
    ) -> ConnectorSection:
        """This method creates a ConnectorSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ConnectorSection
                session.odbs[name].ConnectorSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        assembledType
            A SymbolicConstant specifying the assembled connection type. Possible values
            are:NONEBEAMBUSHINGCVJOINTCYLINDRICALHINGEPLANARRETRACTORSLIPRINGTRANSLATORUJOINTWELDThe
            default value is NONE.You cannot include the **assembledType** argument if
            **translationalType** or **rotationalType** are given a value other than NONE. At least one
            of the arguments **assembledType**, **translationalType**, or **rotationalType** must be given
            a value other than NONE.
        rotationalType
            A SymbolicConstant specifying the basic rotational connection type. Possible values
            are:NONEALIGNCARDANCONSTANT_VELOCITYEULERFLEXION_TORSIONFLOW_CONVERTERPROJECTION_FLEXION_TORSIONREVOLUTEROTATIONROTATION_ACCELEROMETERUNIVERSALThe
            default value is NONE.You cannot include the **rotationalType** argument if
            **assembledType** is given a value other than NONE. At least one of the arguments
            **assembledType**, **translationalType**, or **rotationalType** must be given an value other
            than NONE.
        translationalType
            A SymbolicConstant specifying the basic translational connection type. Possible values
            are:NONEACCELEROMETERAXIALCARTESIANJOINLINKPROJECTION_CARTESIANRADIAL_THRUSTSLIDE_PLANESLOTThe
            default value is NONE.You cannot include the **translationalType** argument if
            **assembledType** is given a value other than NONE. At least one of the arguments
            **assembledType**, **translationalType**, or **rotationalType** must be given an value other
            than NONE.
        integration
            A SymbolicConstant specifying the time integration scheme to use for analysis. This
            argument is applicable only to an Abaqus/Explicit analysis. Possible values are
            UNSPECIFIED, IMPLICIT, and EXPLICIT. The default value is UNSPECIFIED.
        u1ReferenceLength
            None or a Float specifying the reference length associated with constitutive response
            for the first component of relative motion. The default value is None.
        u2ReferenceLength
            None or a Float specifying the reference length associated with constitutive response
            for the second component of relative motion. The default value is None.
        u3ReferenceLength
            None or a Float specifying the reference length associated with constitutive response
            for the third component of relative motion. The default value is None.
        ur1ReferenceAngle
            None or a Float specifying the reference angle in degrees associated with constitutive
            response for the fourth component of relative motion. The default value is None.
        ur2ReferenceAngle
            None or a Float specifying the reference angle in degrees associated with constitutive
            response for the fifth component of relative motion. The default value is None.
        ur3ReferenceAngle
            None or a Float specifying the reference angle in degrees associated with constitutive
            response for the sixth component of relative motion. The default value is None.
        massPerLength
            None or a Float specifying the mass per unit reference length of belt material. This
            argument is applicable only when **assembledType** = SLIPRING, and must be specified in that
            case. The default value is None.
        contactAngle
            None or a Float specifying the contact angle made by the belt wrapping around node b.
            This argument is applicable only to an Abaqus/Explicit analysis, and only when
            **assembledType** = SLIPRING. The default value is None.
        materialFlowFactor
            A Float specifying the scaling factor for material flow at node b. This argument is
            applicable only when **assembledType** = RETRACTOR or **rotationalType** = FLOW_CONVERTER. The
            default value is 1.0.
        regularize
            A Boolean specifying whether or not all tabular data associated with the
            **behaviorOptions** will be regularized. This argument is applicable only for an
            Abaqus/Explicit analysis. The default value is ON.
        defaultTolerance
            A Boolean specifying whether or not the default regularization tolerance will be used
            for all tabular data associated with the **behaviorOptions**. This argument is applicable
            only for an Abaqus/Explicit analysis and only if **regularize** = ON. The default value is
            ON.
        regularization
            A Float specifying the regularization increment to be used for all tabular data
            associated with the **behaviorOptions**. This argument is applicable only for an
            Abaqus/Explicit analysis and only if **regularize** = ON and **defaultTolerance** = OFF. The
            default value is 0.03.
        extrapolation
            A SymbolicConstant specifying the extrapolation technique to be used for all tabular
            data associated with the **behaviorOptions**. Possible values are CONSTANT and LINEAR. The
            default value is CONSTANT.
        behaviorOptions
            A :py:class:`~abaqus.Connector.ConnectorBehaviorOptionArray.ConnectorBehaviorOptionArray` object.

        Returns
        -------
        ConnectorSection
            A :py:class:`~abaqus.Connector.ConnectorSection.ConnectorSection` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.sections[name] = section = ConnectorSection(
            name,
            assembledType,
            rotationalType,
            translationalType,
            integration,
            u1ReferenceLength,
            u2ReferenceLength,
            u3ReferenceLength,
            ur1ReferenceAngle,
            ur2ReferenceAngle,
            ur3ReferenceAngle,
            massPerLength,
            contactAngle,
            materialFlowFactor,
            regularize,
            defaultTolerance,
            regularization,
            extrapolation,
            behaviorOptions,
        )
        return section

    @abaqus_method_doc
    def EulerianSection(self, name: str, data: str) -> EulerianSection:
        """This method creates a EulerianSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].EulerianSection
                session.odbs[name].EulerianSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        data
            A String-to-String Dictionary specifying a dictionary mapping Material instance names to
            Material names. Internally the specified mapping gets sorted on Material instance name.

        Returns
        -------
        EulerianSection
            An :py:class:`~abaqus.Section.EulerianSection.EulerianSection` object.
        """
        self.sections[name] = section = EulerianSection(name, data)
        return section

    @abaqus_method_doc
    def GasketSection(
        self,
        name: str,
        material: str,
        crossSection: float = 1,
        initialGap: float = 0,
        initialThickness: Union[Literal[C.DEFAULT], float] = DEFAULT,
        initialVoid: float = 0,
        stabilizationStiffness: Union[Literal[C.DEFAULT], float] = DEFAULT,
    ) -> GasketSection:
        """This method creates a GasketSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].GasketSection
                session.odbs[name].GasketSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        material
            A String specifying the name of the material of which the gasket is made or material
            that defines gasket behavior.
        crossSection
            A Float specifying the cross-sectional area, width, or out-of-plane thickness, if
            applicable, depending on the gasket element type. The default value is 1.0.
        initialGap
            A Float specifying the initial gap. The default value is 0.0.
        initialThickness
            The SymbolicConstant DEFAULT or a Float specifying the initial gasket thickness. If
            DEFAULT is specified, the initial thickness is determined using nodal coordinates. The
            default value is DEFAULT.
        initialVoid
            A Float specifying the initial void. The default value is 0.0.
        stabilizationStiffness
            The SymbolicConstant DEFAULT or a Float specifying the default stabilization stiffness
            used in all but link elements to stabilize gasket elements that are not supported at all
            nodes, such as those that extend outside neighboring components. If DEFAULT is
            specified, a value is used equal to 10-9 times the initial compressive stiffness in the
            thickness direction. The default value is DEFAULT.

        Returns
        -------
        GasketSection
            A :py:class:`~abaqus.Section.GasketSection.GasketSection` object. and ValueError.
        """
        self.sections[name] = section = GasketSection(
            name,
            material,
            crossSection,
            initialGap,
            initialThickness,
            initialVoid,
            stabilizationStiffness,
        )
        return section

    @abaqus_method_doc
    def GeneralStiffnessSection(
        self,
        name: str,
        stiffnessMatrix: tuple,
        referenceTemperature: Optional[float] = None,
        applyThermalStress: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        poissonDefinition: Literal[C.VALUE, C.DEFAULT] = DEFAULT,
        poisson: float = 0,
        useDensity: Boolean = OFF,
        density: float = 0,
        thermalStresses: tuple = (),
        scalingData: tuple = (),
    ) -> GeneralStiffnessSection:
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
        self.sections[name] = section = GeneralStiffnessSection(
            name,
            stiffnessMatrix,
            referenceTemperature,
            applyThermalStress,
            temperatureDependency,
            dependencies,
            poissonDefinition,
            poisson,
            useDensity,
            density,
            thermalStresses,
            scalingData,
        )
        return section

    @abaqus_method_doc
    def HomogeneousShellSection(
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
        poissonDefinition: Literal[C.DEFAULT, C.VALUE] = DEFAULT,
        poisson: float = 0,
        integrationRule: Literal[C.SIMPSON, C.GAUSS] = SIMPSON,
        temperature: Literal[C.GRADIENT, C.POINTWISE] = GRADIENT,
        idealization: Literal[
            C.NO_IDEALIZATION, C.SMEAR_ALL_LAYERS, C.MEMBRANE, BENDING
        ] = NO_IDEALIZATION,
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
            Possible values are **numIntPts** >> 0. The default value is 5.To use the default settings
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
        self.sections[name] = section = HomogeneousShellSection(
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
        return section

    @abaqus_method_doc
    def HomogeneousSolidSection(
        self, name: str, material: str, thickness: Optional[float] = None
    ) -> HomogeneousSolidSection:
        """This method creates a HomogeneousSolidSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].HomogeneousSolidSection
                session.odbs[name].HomogeneousSolidSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        material
            A String specifying the name of the material.
        thickness
            None or a Float specifying the thickness of the section. Possible values
            are None or a floating point value such that thickness >  0.0. The default value is None.

        Returns
        -------
        HomogeneousSolidSection
            A :py:class:`~abaqus.Section.HomogeneousSolidSection.HomogeneousSolidSection` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.sections[name] = section = HomogeneousSolidSection(
            name, material, thickness
        )
        return section

    @abaqus_method_doc
    def MembraneSection(
        self,
        name: str,
        material: str,
        thickness: float = 1,
        thicknessType: Literal[C.UNIFORM, C.ANALYTICAL_FIELD, C.DISCRETE_FIELD] = UNIFORM,
        poissonDefinition: Literal[C.DEFAULT, C.VALUE] = DEFAULT,
        poisson: float = 0,
        thicknessField: str = "",
    ) -> MembraneSection:
        """This method creates a MembraneSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].MembraneSection
                session.odbs[name].MembraneSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        material
            A String specifying the name of the material.
        thickness
            A Float specifying the thickness for the section. Possible values are **thickness** >>
            0.0. The default value is 1.0.
        thicknessType
            A SymbolicConstant specifying the distribution used for defining the thickness of the
            elements. Possible values are UNIFORM, ANALYTICAL_FIELD, and DISCRETE_FIELD. The default
            value is UNIFORM.
        poissonDefinition
            A SymbolicConstant specifying whether to use the default value for the Poisson's ratio.
            Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio
            is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an
            Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis
            is the value provided in **poisson**.The default value is DEFAULT.
        poisson
            A Float specifying the section Poisson's ratio. Possible values are −1.0 ≤ **poisson** ≤
            0.5. This argument is valid only when **poissonDefinition** = VALUE. The default value is
            0.5.
        thicknessField
            A String specifying the name of the AnalyticalField or DiscreteField object used to
            define the thickness of the shell elements. The **thicknessField** argument applies only
            when **thicknessType** = ANALYTICAL_FIELD or **thicknessType** = DISCRETE_FIELD. The default
            value is an empty string.

        Returns
        -------
        MembraneSection
            A :py:class:`~abaqus.Section.MembraneSection.MembraneSection` object.

        Raises
        ------
        RangeError and InvalidNameError
        """
        self.sections[name] = section = MembraneSection(
            name,
            material,
            thickness,
            thicknessType,
            poissonDefinition,
            poisson,
            thicknessField,
        )
        return section

    @abaqus_method_doc
    def MPCSection(
        self,
        name: str,
        mpcType: Literal[C.BEAM_MPC, C.ELBOW_MPC, C.PIN_MPC, C.LINK_MPC, C.TIE_MPC, C.USER_DEFINED],
        userMode: Literal[C.DOF_MODE, C.NODE_MODE] = DOF_MODE,
        userType: int = 0,
    ) -> MPCSection:
        """This method creates a MPCSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].MPCSection
                session.odbs[name].MPCSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        mpcType
            A SymbolicConstant specifying the MPC type of the section. Possible values are BEAM_MPC,
            ELBOW_MPC, PIN_MPC, LINK_MPC, TIE_MPC, and USER_DEFINED.
        userMode
            A SymbolicConstant specifying the mode of the MPC when it is user-defined. Possible
            values are DOF_MODE and NODE_MODE. The default value is DOF_MODE.The **userMode** argument
            applies only when **mpcType** = USER_DEFINED.
        userType
            An Int specifying to differentiate between different constraint types in a user-defined
            MPCSection. The default value is 0.The **userType** argument applies only when
            **mpcType** = USER_DEFINED.

        Returns
        -------
        MPCSection
            A :py:class:`~abaqus.Section.MPCSection.MPCSection` object.

        Raises
        ------
        RangeError and InvalidNameError
        """
        self.sections[name] = section = MPCSection(name, mpcType, userMode, userType)
        return section

    @abaqus_method_doc
    def PEGSection(
        self,
        name: str,
        material: str,
        thickness: float = 1,
        wedgeAngle1: float = 0,
        wedgeAngle2: float = 0,
    ) -> PEGSection:
        """This method creates a PEGSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].PEGSection
                session.odbs[name].PEGSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        material
            A String specifying the name of the material.
        thickness
            A Float specifying the thickness of the section. Possible values are **thickness** >> 0.0.
            The default value is 1.0.
        wedgeAngle1
            A Float specifying the value of the x component of the angle between the bounding
            planes, ΔϕxΔ⁢ϕx. The default value is 0.0.
        wedgeAngle2
            A Float specifying the value of the y component of the angle between the bounding
            planes, ΔϕyΔ⁢ϕy. The default value is 0.0.

        Returns
        -------
        PEGSection
            A :py:class:`~abaqus.Section.PEGSection.PEGSection` object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.sections[name] = section = PEGSection(
            name, material, thickness, wedgeAngle1, wedgeAngle2
        )
        return section

    @abaqus_method_doc
    def SurfaceSection(
        self, name: str, useDensity: Boolean = OFF, density: float = 0
    ) -> SurfaceSection:
        """This method creates a SurfaceSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].SurfaceSection
                session.odbs[name].SurfaceSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        useDensity
            A Boolean specifying whether or not to use the value of **density**. The default value is
            OFF.
        density
            A Float specifying the value of density to apply to this section. The default value is
            0.0.

        Returns
        -------
        SurfaceSection
            A :py:class:`~abaqus.Section.SurfaceSection.SurfaceSection` object.

        Raises
        ------
        RangeError and InvalidNameError
        """
        self.sections[name] = section = SurfaceSection(name, useDensity, density)
        return section

    @abaqus_method_doc
    def TrussSection(self, name: str, material: str, area: float = 1) -> TrussSection:
        """This method creates a TrussSection object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].TrussSection
                session.odbs[name].TrussSection

        Parameters
        ----------
        name
            A String specifying the repository key.
        material
            A String specifying the name of the material.
        area
            A Float specifying the cross-sectional area for the section. Possible values are **area**
            >> 0. The default value is 1.0.

        Returns
        -------
        TrussSection
            A :py:class:`~abaqus.Section.TrussSection.TrussSection` object.

        Raises
        ------
        RangeError and InvalidNameError
        """
        self.sections[name] = section = TrussSection(name, material, area)
        return section
