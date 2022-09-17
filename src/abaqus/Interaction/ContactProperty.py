import typing

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .CohesiveBehavior import CohesiveBehavior
from .ContactDamage import ContactDamage
from .ContactDamping import ContactDamping
from .ContactTangentialBehavior import ContactTangentialBehavior
from .FractureCriterion import FractureCriterion
from .GapElectricalConductance import GapElectricalConductance
from .GapHeatGeneration import GapHeatGeneration
from .GeometricProperties import GeometricProperties
from .InteractionProperty import InteractionProperty
from .NormalBehavior import NormalBehavior
from .Radiation import Radiation
from .ThermalConductance import ThermalConductance
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class ContactProperty(InteractionProperty):
    """The ContactProperty object defines a contact interaction property.
    The ContactProperty object is derived from the InteractionProperty object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactionProperties[name]

        The corresponding analysis keywords are:

        - SURFACE INTERACTION
    """

    #: A :py:class:`~abaqus.Interaction.ContactTangentialBehavior.ContactTangentialBehavior` object.
    tangentialBehavior: ContactTangentialBehavior = ContactTangentialBehavior()

    #: A :py:class:`~abaqus.Interaction.NormalBehavior.NormalBehavior` object.
    normalBehavior: NormalBehavior = NormalBehavior()

    #: A :py:class:`~abaqus.Interaction.ContactDamping.ContactDamping` object.
    damping: ContactDamping = ContactDamping()

    #: A :py:class:`~abaqus.Interaction.ContactDamage.ContactDamage` object.
    damage: ContactDamage = ContactDamage(((),))

    #: A :py:class:`~abaqus.Interaction.FractureCriterion.FractureCriterion` object.
    fractureCriterion: FractureCriterion = FractureCriterion(((),))

    #: A :py:class:`~abaqus.Interaction.CohesiveBehavior.CohesiveBehavior` object.
    cohesiveBehavior: CohesiveBehavior = CohesiveBehavior()

    #: A :py:class:`~abaqus.Interaction.ThermalConductance.ThermalConductance` object.
    thermalConductance: ThermalConductance = ThermalConductance()

    #: A :py:class:`~abaqus.Interaction.GapHeatGeneration.GapHeatGeneration` object.
    heatGeneration: GapHeatGeneration = GapHeatGeneration()

    #: A :py:class:`~abaqus.Interaction.Radiation.Radiation` object.
    radiation: Radiation = None

    #: A :py:class:`~abaqus.Interaction.GeometricProperties.GeometricProperties` object.
    geometricProperties: GeometricProperties = GeometricProperties()

    #: A :py:class:`~abaqus.Interaction.GapElectricalConductance.GapElectricalConductance` object.
    electricalConductance: GapElectricalConductance = GapElectricalConductance()

    @abaqus_method_doc
    def __init__(self, name: str):
        """This method creates a ContactProperty object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ContactProperty

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.

        Returns
        -------
        ContactProperty
            A :py:class:`~abaqus.Interaction.ContactProperty.ContactProperty` object.
        """
        super().__init__()

    @abaqus_method_doc
    def TangentialBehavior(
        self,
        formulation: SymbolicConstant = FRICTIONLESS,
        directionality: SymbolicConstant = ISOTROPIC,
        slipRateDependency: Boolean = OFF,
        pressureDependency: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        exponentialDecayDefinition: SymbolicConstant = COEFFICIENTS,
        table: tuple = (),
        shearStressLimit: float = None,
        maximumElasticSlip: SymbolicConstant = FRACTION,
        fraction: float = 0,
        absoluteDistance: float = 0,
        elasticSlipStiffness: float = None,
        nStateDependentVars: int = 0,
        useProperties: Boolean = OFF,
    ):
        """This method creates a ContactTangentialBehavior object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ContactProperty

        Parameters
        ----------
        formulation
            A SymbolicConstant specifying the friction formulation. Possible values are
            FRICTIONLESS, PENALTY, EXPONENTIAL_DECAY, ROUGH, LAGRANGE, and USER_DEFINED. The default
            value is FRICTIONLESS.
        directionality
            A SymbolicConstant specifying the directionality of the friction. Possible values are
            ISOTROPIC and ANISOTROPIC. The default value is ISOTROPIC.
        slipRateDependency
            A Boolean specifying whether the data depend on slip rate. The default value is OFF.
        pressureDependency
            A Boolean specifying whether the data depend on contact pressure. The default value is
            OFF.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variables. The default value is 0.
        exponentialDecayDefinition
            A SymbolicConstant specifying the exponential decay definition. Possible values are
            COEFFICIENTS and TEST_DATA. The default value is COEFFICIENTS.
        table
            A sequence of sequences of Floats specifying tangential behavior. The items in the table
            data are described below.
        shearStressLimit
            None or a Float specifying the shear stress limit. If **shearStressLimit** = None, there is
            no upper limit. The default value is None.
        maximumElasticSlip
            A SymbolicConstant specifying what the maximum elastic slip will be. Possible values are
            FRACTION and ABSOLUTE_DISTANCE. The default value is FRACTION.
        fraction
            A Float specifying the fraction of a characteristic surface dimension. The default value
            is 0.0.
        absoluteDistance
            A Float specifying the absolute distance. The default value is 0.0.
        elasticSlipStiffness
            None or a Float specifying the elastic slip stiffness. If **elasticSlipStiffness** = None,
            there is no upper limit. The default value is None.
        nStateDependentVars
            An Int specifying the number of state-dependent variables. The default value is 0.
        useProperties
            A Boolean specifying whether property values will be used. The default value is OFF.

        Returns
        -------
        ContactTangentialBehavior
            A :py:class:`~abaqus.Interaction.ContactTangentialBehavior.ContactTangentialBehavior` object.
        """
        self.tangentialBehavior = ContactTangentialBehavior(
            formulation,
            directionality,
            slipRateDependency,
            pressureDependency,
            temperatureDependency,
            dependencies,
            exponentialDecayDefinition,
            table,
            shearStressLimit,
            maximumElasticSlip,
            fraction,
            absoluteDistance,
            elasticSlipStiffness,
            nStateDependentVars,
            useProperties,
        )
        return self.tangentialBehavior

    @abaqus_method_doc
    def NormalBehavior(
        self,
        contactStiffness: typing.Union[SymbolicConstant, float] = DEFAULT,
        pressureOverclosure: SymbolicConstant = HARD,
        allowSeparation: Boolean = ON,
        maxStiffness: float = None,
        table: tuple = (),
        constraintEnforcementMethod: SymbolicConstant = DEFAULT,
        overclosureFactor: float = 0,
        overclosureMeasure: float = 0,
        contactStiffnessScaleFactor: float = 1,
        initialStiffnessScaleFactor: float = 1,
        clearanceAtZeroContactPressure: float = 0,
        stiffnessBehavior: SymbolicConstant = LINEAR,
        stiffnessRatio: float = 0,
        upperQuadraticFactor: float = 0,
        lowerQuadraticRatio: float = 0,
    ):
        """This method creates a NormalBehavior object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ContactProperty

        Parameters
        ----------
        contactStiffness
            The SymbolicConstant DEFAULT or a Float specifying the contact stiffness. This argument
            is valid for **pressureOverclosure** = LINEAR. This argument is also valid for
            **pressureOverclosure** = HARD when **constraintEnforcementMethod** = AUGMENTED_LAGRANGE or
            PENALTY. A value of DEFAULT is valid only when the later conditions are met. A value of
            zero is equivalent to specifying DEFAULT. The default value is DEFAULT.
        pressureOverclosure
            A SymbolicConstant specifying the pressure-overclosure relationship to be used. Possible
            values are HARD, EXPONENTIAL, LINEAR, TABULAR, and SCALE_FACTOR. The default value is
            HARD.
        allowSeparation
            A Boolean specifying whether to allow separation after contact. The default value is ON.
        maxStiffness
            None or a Float specifying the maximum stiffness. If **maxStiffness** = None, there is no
            upper limit. The default value is None.
        table
            A sequence of sequences of Floats specifying the normal behavior properties. This
            argument is valid only for **pressureOverclosure** = EXPONENTIAL or TABULAR. The items in
            the table data are described below.
        constraintEnforcementMethod
            A SymbolicConstant specifying the method for enforcement of the contact constraint.
            Possible values are DEFAULT, AUGMENTED_LAGRANGE, PENALTY, and DIRECT. The default value
            is DEFAULT.
        overclosureFactor
            A Float specifying the overclosure measure (used to delineate the segments of the
            pressure-overclosure curve) as a percentage of the minimum element size in the contact
            region. The default value is 0.0.
        overclosureMeasure
            A Float specifying the overclosure measure (used to delineate the segments of the
            pressure-overclosure curve) directly. The default value is 0.0.
        contactStiffnessScaleFactor
            A Float specifying scale factor for the penalty stiffness or the geometric scaling of
            the "base" stiffness. The default value is 1.0.
        initialStiffnessScaleFactor
            A Float specifying an additional scale factor for the "base" default contact stiffness.
            The default value is 1.0.
        clearanceAtZeroContactPressure
            A Float specifying the clearance at which the contact pressure is zero. The default
            value is 0.0.
        stiffnessBehavior
            A SymbolicConstant specifying the type of penalty stiffness to be defined. This argument
            is valid only when **constraintEnforcementMethod** = PENALTY. Possible values are LINEAR and
            NONLINEAR. The default value is LINEAR.
        stiffnessRatio
            A Float specifying the ratio of the initial stiffness divided by the final stiffness.
            This argument is valid only when **stiffnessBehavior** = NONLINEAR. Possible values are 0 ≤
            **stiffnessRatio** << 1. The default value is 0.01.
        upperQuadraticFactor
            A Float specifying the ratio of the overclosure at the maximum stiffness divided by the
            characteristic facet length. This argument is valid only when
            **stiffnessBehavior** = NONLINEAR. The default value is 0.03.
        lowerQuadraticRatio
            A Float specifying the ratio of the overclosure at the initial stiffness divided by the
            overclosure at the maximum stiffness, both relative to the clearance at which the
            contact pressure is zero. This argument is valid only when
            **stiffnessBehavior** = NONLINEAR. Possible values are 0 ≤ **stiffnessRatio** << 1. The
            default value is 0.33333.

        Returns
        -------
        NormalBehavior
            A :py:class:`~abaqus.Interaction.NormalBehavior.NormalBehavior` object.
        """
        self.normalBehavior = NormalBehavior(
            contactStiffness,
            pressureOverclosure,
            allowSeparation,
            maxStiffness,
            table,
            constraintEnforcementMethod,
            overclosureFactor,
            overclosureMeasure,
            contactStiffnessScaleFactor,
            initialStiffnessScaleFactor,
            clearanceAtZeroContactPressure,
            stiffnessBehavior,
            stiffnessRatio,
            upperQuadraticFactor,
            lowerQuadraticRatio,
        )
        return self.normalBehavior

    @abaqus_method_doc
    def Damping(
        self,
        definition: SymbolicConstant = DAMPING_COEFFICIENT,
        tangentFraction: typing.Union[SymbolicConstant, float] = DEFAULT,
        clearanceDependence: SymbolicConstant = STEP,
        table: tuple = (),
    ):
        """This method creates a ContactDamping object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ContactProperty

        Parameters
        ----------
        definition
            A SymbolicConstant specifying the method used to define the damping. Possible values are
            DAMPING_COEFFICIENT and CRITICAL_DAMPING_FRACTION. The default value is
            DAMPING_COEFFICIENT.
        tangentFraction
            The SymbolicConstant DEFAULT or a Float specifying the tangential damping coefficient
            divided by the normal damping coefficient. The default value is DEFAULT.
        clearanceDependence
            A SymbolicConstant specifying the variation of the damping coefficient or fraction with
            respect to clearance. Possible values are STEP, LINEAR, and BILINEAR. The default value
            is STEP.If **definition** = CRITICAL_DAMPING_FRACTION, the only possible value is STEP.
        table
            A sequence of pairs of Floats specifying the damping properties. The items in the table
            data are described below.

        Returns
        -------
        ContactDamping
            A :py:class:`~abaqus.Interaction.ContactDamping.ContactDamping` object.
        """
        self.damping = ContactDamping(
            definition, tangentFraction, clearanceDependence, table
        )
        return self.damping

    @abaqus_method_doc
    def Damage(
        self,
        initTable: tuple,
        criterion: SymbolicConstant = MAX_STRESS,
        initTempDep: Boolean = OFF,
        initDependencies: int = 0,
        useEvolution: Boolean = OFF,
        evolutionType: SymbolicConstant = DISPLACEMENT,
        softening: SymbolicConstant = LINEAR,
        useMixedMode: Boolean = OFF,
        mixedModeType: SymbolicConstant = TABULAR,
        modeMixRatio: SymbolicConstant = ENERGY,
        exponent: float = None,
        evolTempDep: Boolean = OFF,
        evolDependencies: int = 0,
        evolTable: tuple = (),
        useStabilization: Boolean = OFF,
        viscosityCoef: float = None,
    ):
        """This method creates a ContactDamage object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ContactProperty

        Parameters
        ----------
        initTable
            A sequence of sequences of Floats specifying the values defining the damage initiation.
            The items in the table data are described below.
        criterion
            A SymbolicConstant specifying the type of data used to define the initiation of damage.
            Possible values are MAX_STRESS, MAX_SEPARATION, QUAD_TRACTION, and QUAD_SEPARATION. The
            default value is MAX_STRESS.
        initTempDep
            A Boolean specifying whether the initiation data depend on temperature. The default
            value is OFF.
        initDependencies
            An Int specifying the number of initiation data field variables. The default value is 0.
        useEvolution
            A Boolean specifying whether evolution data will be defined. The default value is OFF.
        evolutionType
            A SymbolicConstant specifying the type of data used to define the evolution of damage.
            This argument is valid only when **useEvolution** = ON. Possible values are DISPLACEMENT and
            ENERGY. The default value is DISPLACEMENT.
        softening
            A SymbolicConstant specifying the type of data used to define the evolution softening
            response. This argument is valid only when **useEvolution** = ON. The TABULAR value can be
            used only when **evolutionType** = DISPLACEMENT. Possible values are LINEAR, EXPONENTIAL,
            and TABULAR. The default value is LINEAR.
        useMixedMode
            A Boolean specifying whether evolution data be defined using dependent behavior modes.
            This argument is valid only when **useEvolution** = ON. The default value is OFF.
        mixedModeType
            A SymbolicConstant specifying the mode mix fracture criterion. This argument is valid
            only when **useEvolution** = ON and when **useMixedMode** = ON. The POWER_LAW and BK values can
            be used only when **evolutionType** = ENERGY. Possible values are TABULAR, POWER_LAW, and
            BK. The default value is TABULAR.
        modeMixRatio
            A SymbolicConstant specifying the mode mix ratio type. This argument is valid only when
            **useEvolution** = ON and when **useMixedMode** = ON. The TRACTION value can be used only when
            **mixedModeType** = TABULAR. Possible values are ENERGY and TRACTION. The default value is
            ENERGY.
        exponent
            None or a Float specifying the exponent in the power-law or BK criterion that defines
            the variation of fracture energy with mode mix. This argument is valid only when
            **useEvolution** = ON and when **mixedModeType** = POWER_LAW or BK. The default value is None.
        evolTempDep
            A Boolean specifying whether the evolution data depend on temperature. This argument is
            valid only when **useEvolution** = ON. The default value is OFF.
        evolDependencies
            An Int specifying the number of evolution data field variables. This argument is valid
            only when **useEvolution** = ON. The default value is 0.
        evolTable
            A sequence of sequences of Floats specifying the values defining the damage evolution.
            The items in the table data are described below. This argument is valid only when
            **useEvolution** = ON.
        useStabilization
            A Boolean specifying whether stabilization data will be defined. This argument is valid
            only when **useEvolution** = ON. The default value is OFF.
        viscosityCoef
            None or a Float specifying the viscosity coefficient. This argument is valid only when
            **useStabilization** = ON. The default value is None.

        Returns
        -------
        ContactDamage
            A :py:class:`~abaqus.Interaction.ContactDamage.ContactDamage` object.
        """
        self.damage = ContactDamage(
            initTable,
            criterion,
            initTempDep,
            initDependencies,
            useEvolution,
            evolutionType,
            softening,
            useMixedMode,
            mixedModeType,
            modeMixRatio,
            exponent,
            evolTempDep,
            evolDependencies,
            evolTable,
            useStabilization,
            viscosityCoef,
        )
        return self.damage

    @abaqus_method_doc
    def FractureCriterion(
        self,
        initTable: tuple,
        type: SymbolicConstant = VCCT,
        mixedModeBehavior: SymbolicConstant = BK,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        tolerance: float = 0,
        specifyUnstableCrackProp: SymbolicConstant = OFF,
        unstableTolerance: typing.Union[SymbolicConstant, float] = DEFAULT,
    ):
        """This method creates a FractureCriterion object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ContactProperty

        Parameters
        ----------
        initTable
            A sequence of sequences of Floats specifying the value defining the fracture criterion.
            The items in the table data are described below.
        type
            A SymbolicConstant specifying the type of data used to define the fracture criterion.
            Possible values are VCCT and ENHANCED VCCT. The default value is VCCT.
        mixedModeBehavior
            A SymbolicConstant specifying the mixed mode behavior type used to define fracture
            criterion. Possible values are BK, POWER, and REEDER. The default value is BK.
        temperatureDependency
            A Boolean specifying whether the fracture criterion data depend on temperature. The
            default value is OFF.
        dependencies
            An Int specifying the number of fracture criterion data field variables. The default
            value is 0.
        tolerance
            A Float specifying the tolerance for VCCT Enhanced VCCT type. The default value is 0.2.
        specifyUnstableCrackProp
            A SymbolicConstant specifying whether to include unstable crack growth tolerance in
            fracture criterion. Possible values are ON and OFF. The default value is OFF.
        unstableTolerance
            The SymbolicConstant DEFAULT or a Float specifying the tolerance for unstable crack
            propagation. This parameter specified only if **specifyUnstableCrackProp** = ON. The default
            value is DEFAULT.

        Returns
        -------
        FractureCriterion
            A :py:class:`~abaqus.Interaction.FractureCriterion.FractureCriterion` object.
        """
        self.fractureCriterion = FractureCriterion(
            initTable,
            type,
            mixedModeBehavior,
            temperatureDependency,
            dependencies,
            tolerance,
            specifyUnstableCrackProp,
            unstableTolerance,
        )
        return self.fractureCriterion

    @abaqus_method_doc
    def CohesiveBehavior(
        self,
        repeatedContacts: Boolean = OFF,
        eligibility: SymbolicConstant = ALL_NODES,
        defaultPenalties: Boolean = ON,
        coupling: SymbolicConstant = UNCOUPLED,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        table: tuple = (),
    ):
        """This method creates a CohesiveBehavior object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ContactProperty

        Parameters
        ----------
        repeatedContacts
            A Boolean specifying whether to enforce cohesive behavior for recurrent contacts at
            nodes on the slave surface subsequent to ultimate failure. The default value is OFF.
        eligibility
            A SymbolicConstant specifying the eligible slave nodes. Possible values are
            ALL_NODES, INITIAL_NODES, and SPECIFIED. The default value is ALL_NODES.
        defaultPenalties
            A Boolean specifying whether to use the default contact penalties. The default value is
            ON.
        coupling
            A SymbolicConstant specifying whether the traction-separation coefficients are coupled
            or uncoupled. This argument is valid only for **defaultPenalties** = OFF. Possible values
            are UNCOUPLED and COUPLED. The default value is UNCOUPLED.
        temperatureDependency
            A Boolean specifying whether the coefficient data depend on temperature. This argument
            is valid only for **defaultPenalties** = OFF. The default value is OFF.
        dependencies
            An Int specifying the number of field variables. This argument is valid only for
            **defaultPenalties** = OFF. The default value is 0.
        table
            A sequence of sequences of Floats specifying the traction-separation coefficients. The
            items in the table data are described below. This argument is valid only for
            **defaultPenalties** = OFF.

        Returns
        -------
        CohesiveBehavior
            A :py:class:`~abaqus.Interaction.CohesiveBehavior.CohesiveBehavior` object.
        """
        self.cohesiveBehavior = CohesiveBehavior(
            repeatedContacts,
            eligibility,
            defaultPenalties,
            coupling,
            temperatureDependency,
            dependencies,
            table,
        )
        return self.cohesiveBehavior

    @abaqus_method_doc
    def ThermalConductance(
        self,
        definition: SymbolicConstant = TABULAR,
        clearanceDependency: Boolean = ON,
        pressureDependency: Boolean = OFF,
        temperatureDependencyC: Boolean = OFF,
        massFlowRateDependencyC: Boolean = OFF,
        dependenciesC: int = 0,
        clearanceDepTable: tuple = (),
        temperatureDependencyP: Boolean = OFF,
        massFlowRateDependencyP: Boolean = OFF,
        dependenciesP: int = 0,
        pressureDepTable: tuple = (),
    ):
        """This method creates a ThermalConductance object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ContactProperty

        Parameters
        ----------
        definition
            A SymbolicConstant specifying how the thermal conductance is defined. Possible values
            are TABULAR and USER_DEFINED. The default value is TABULAR.
        clearanceDependency
            A Boolean specifying whether to use clearance-dependent data. The default value is ON.
        pressureDependency
            A Boolean specifying whether to use pressure-dependent data. The default value is OFF.
        temperatureDependencyC
            A Boolean specifying whether to use temperature-dependent data with clearance
            dependency. The default value is OFF.
        massFlowRateDependencyC
            A Boolean specifying whether to use mass-flow-rate-dependent data with clearance
            dependency. The default value is OFF.
        dependenciesC
            An Int specifying the number of field variables to use with clearance dependency. The
            default value is 0.
        clearanceDepTable
            A sequence of sequences of Floats specifying clearance dependency data. The items in the
            table data are described below.
        temperatureDependencyP
            A Boolean specifying whether to use temperature-dependent data with pressure dependency.
            The default value is OFF.
        massFlowRateDependencyP
            A Boolean specifying whether to use mass-flow-rate-dependent data with pressure
            dependency. The default value is OFF.
        dependenciesP
            An Int specifying the number of field variables to use with pressure dependency. The
            default value is 0.
        pressureDepTable
            A sequence of sequences of Floats specifying pressure dependency data. The items in the
            table data are described below.

        Returns
        -------
        ThermalConductance
            A :py:class:`~abaqus.Interaction.ThermalConductance.ThermalConductance` object.
        """
        self.thermalConductance = ThermalConductance(
            definition,
            clearanceDependency,
            pressureDependency,
            temperatureDependencyC,
            massFlowRateDependencyC,
            dependenciesC,
            clearanceDepTable,
            temperatureDependencyP,
            massFlowRateDependencyP,
            dependenciesP,
            pressureDepTable,
        )
        return self.thermalConductance

    @abaqus_method_doc
    def HeatGeneration(
        self, conversionFraction: float = 1, slaveFraction: float = 0
    ):
        """This method creates a GapHeatGeneration object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ContactProperty

        Parameters
        ----------
        conversionFraction
            A Float specifying the fraction of dissipated energy caused by friction or electric
            currents that is converted to heat. The default value is 1.0.
        slaveFraction
            A Float specifying the fraction of converted heat distributed to the slave surface.
            The default value is 0.5.

        Returns
        -------
        GapHeatGeneration
            A :py:class:`~abaqus.Interaction.GapHeatGeneration.GapHeatGeneration` object.
        """
        self.heatGeneration = GapHeatGeneration(conversionFraction, slaveFraction)
        return self.heatGeneration

    @abaqus_method_doc
    def Radiation(
        self, masterEmissivity: float, slaveEmissivity: float, table: tuple
    ):
        """This method creates a Radiation object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ContactProperty

        Parameters
        ----------
        masterEmissivity
            A Float specifying the emissivity of the master surface.
        slaveEmissivity
            A Float specifying the emissivity of the slave surface.
        table
            A sequence of sequences of Floats specifying the following:Effective viewfactor, FF.Gap
            clearance, dd.

        Returns
        -------
        Radiation
            A :py:class:`~abaqus.Interaction.Radiation.Radiation` object.
        """
        self.radiation = Radiation(masterEmissivity, slaveEmissivity, table)
        return self.radiation

    @abaqus_method_doc
    def GeometricProperties(
        self,
        contactArea: float = 1,
        padThickness: float = None,
        trackingThickness: float = None,
        dependentVariables: int = 0,
        numProperties: int = 0,
        useUnsymmetricEqunProcedure: Boolean = OFF,
        modelType: SymbolicConstant = None,
    ):
        """This method creates a GeometricProperties object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ContactProperty

        Parameters
        ----------
        contactArea
            A Float specifying the out-of-plane thickness of the surface for a two-dimensional model
            or cross-sectional area for every node in the node-based surface. The default value is
            1.0.
        padThickness
            None or a Float specifying the thickness of an interfacial layer between the contacting
            surfaces. If **padThickness** = None, there is no interfacial layer. The default value is
            None.
        trackingThickness
            None or a Float specifying the thickness that determines the contacting surfaces to be
            tracked. The input value for this parameter cannot be negative. An internal default
            value is used if a zero value is input or if the parameter is omitted.
        dependentVariables
            An Int specifying the number of state-dependent variables. The default value is 0. This
            argument is applicable only if **modelType** = MODELTYPE_USER or
            **modelType** = MODELTYPE_USER_INTERACTION.
        numProperties
            An Int specifying the number of property values required. The default value is 0. This
            argument is applicable only if **modelType** = MODELTYPE_USER or
            **modelType** = MODELTYPE_USER_INTERACTION.
        useUnsymmetricEqunProcedure
            A Boolean specifying whether to use unsymmetric equation solution procedures. This
            argument is applicable only if **modelType** = MODELTYPE_USER or
            **modelType** = MODELTYPE_USER_INTERACTION.
        modelType
            A SymbolicConstant specifying the surface interaction model type.

        Returns
        -------
        GeometricProperties
            A :py:class:`~abaqus.Interaction.GeometricProperties.GeometricProperties` object.
        """
        self.geometricProperties = GeometricProperties(
            contactArea,
            padThickness,
            trackingThickness,
            dependentVariables,
            numProperties,
            useUnsymmetricEqunProcedure,
            modelType,
        )
        return self.geometricProperties

    @abaqus_method_doc
    def ElectricalConductance(
        self,
        definition: SymbolicConstant = TABULAR,
        clearanceDependency: Boolean = ON,
        pressureDependency: Boolean = OFF,
        temperatureDependencyC: Boolean = OFF,
        dependenciesC: int = 0,
        clearanceDepTable: tuple = (),
        temperatureDependencyP: Boolean = OFF,
        dependenciesP: int = 0,
        pressureDepTable: tuple = (),
    ):
        """This method creates a GapElectricalConductance object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ContactProperty

        Parameters
        ----------
        definition
            A SymbolicConstant specifying how the electrical conductance is defined. Possible values
            are TABULAR and USER_DEFINED. The default value is TABULAR.
        clearanceDependency
            A Boolean specifying whether to use clearance-dependent data. The default value is ON.
        pressureDependency
            A Boolean specifying whether to use pressure-dependent data. The default value is OFF.
        temperatureDependencyC
            A Boolean specifying whether to use temperature-dependent data with clearance
            dependency. The default value is OFF.
        dependenciesC
            An Int specifying the number of field variables to use with clearance dependency. The
            default value is 0.
        clearanceDepTable
            A sequence of sequences of Floats specifying clearance dependency data. The items in the
            table data are described below.
        temperatureDependencyP
            A Boolean specifying whether to use temperature-dependent data with pressure dependency.
            The default value is OFF.
        dependenciesP
            An Int specifying the number of field variables to use with pressure dependency. The
            default value is 0.
        pressureDepTable
            A sequence of sequences of Floats specifying pressure dependency data. The items in the
            table data are described below.

        Returns
        -------
        GapElectricalConductance
            A :py:class:`~abaqus.Interaction.GapElectricalConductance.GapElectricalConductance` object.
        """
        self.electricalConductance = GapElectricalConductance(
            definition,
            clearanceDependency,
            pressureDependency,
            temperatureDependencyC,
            dependenciesC,
            clearanceDepTable,
            temperatureDependencyP,
            dependenciesP,
            pressureDepTable,
        )
        return self.electricalConductance
