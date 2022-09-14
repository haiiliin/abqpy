from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .AcousticImpedanceProp import AcousticImpedanceProp
from .ActuatorSensorProp import ActuatorSensorProp
from .CavityRadiationProp import CavityRadiationProp
from .ContactProperty import ContactProperty
from .FilmConditionProp import FilmConditionProp
from .FluidCavityProperty import FluidCavityProperty
from .FluidExchangeProperty import FluidExchangeProperty
from .IncidentWaveProperty import IncidentWaveProperty
from ..Model.ModelBase import ModelBase
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class InteractionPropertyModel(ModelBase):
    @abaqus_method_doc
    def AcousticImpedanceProp(
        self,
        name: str,
        tableType: SymbolicConstant,
        table: tuple,
        frequencyDependency: Boolean = OFF,
    ) -> AcousticImpedanceProp:
        """This method creates an AcousticImpedanceProp object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].AcousticImpedanceProp

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        tableType
            A SymbolicConstant specifying the type of tabular data to be defined. Possible values
            are IMPEDANCE and ADMITTANCE.
        table
            A sequence of sequences of Floats specifying acoustic impedance properties.If
            **tableType** = IMPEDANCE, each sequence of the table data specifies:The real part of the
            complex impedance.The imaginary part of the complex impedance.Frequency, if the data
            depend on frequency.If **tableType** = ADMITTANCE, each sequence of the table data
            specifies:The real part of the complex admittance.The imaginary part of the complex
            admittance.Frequency, if the data depend on frequency.
        frequencyDependency
            A Boolean specifying whether the **table** data depend on frequency. The default value is
            OFF.

        Returns
        -------
        AcousticImpedanceProp
            An :py:class:`~abaqus.Interaction.AcousticImpedanceProp.AcousticImpedanceProp` object.
        """
        self.interactionProperties[name] = interactionProperty = AcousticImpedanceProp(
            name, tableType, table, frequencyDependency
        )
        return interactionProperty

    @abaqus_method_doc
    def ActuatorSensorProp(
        self, name: str, realProperties: tuple = (), integerProperties: tuple = ()
    ) -> ActuatorSensorProp:
        """This method creates an ActuatorSensorProp object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ActuatorSensorProp

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        realProperties
            A sequence of Floats specifying the PROPS array used by user subroutine UEL. The default
            value is an empty sequence.
        integerProperties
            A sequence of Ints specifying the JPROPS array used by user subroutine UEL. The default
            value is an empty sequence.

        Returns
        -------
        ActuatorSensorProp
            An :py:class:`~abaqus.Interaction.ActuatorSensorProp.ActuatorSensorProp` object.
        """
        self.interactionProperties[name] = interactionProperty = ActuatorSensorProp(
            name, realProperties, integerProperties
        )
        return interactionProperty

    @abaqus_method_doc
    def CavityRadiationProp(
        self,
        name: str,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        property: tuple = (),
    ) -> CavityRadiationProp:
        """This method creates a CavityRadiationProp object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].CavityRadiationProp

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        property
            A sequence of sequences of Floats specifying the following:The emissivity,
            ϵϵ.Temperature, if the data depend on temperature.Value of the first field variable, if
            the data depend on field variables.Value of the second field variable.Etc.

        Returns
        -------
        CavityRadiationProp
            A :py:class:`~abaqus.Interaction.CavityRadiationProp.CavityRadiationProp` object.
        """
        self.interactionProperties[name] = interactionProperty = CavityRadiationProp(
            name, temperatureDependency, dependencies, property
        )
        return interactionProperty

    @abaqus_method_doc
    def ContactProperty(self, name: str) -> ContactProperty:
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
        self.interactionProperties[name] = interactionProperty = ContactProperty(name)
        return interactionProperty

    @abaqus_method_doc
    def FilmConditionProp(
        self,
        name: str,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        property: tuple = (),
    ) -> FilmConditionProp:
        """This method creates a FilmConditionProp object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].FilmConditionProp

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        property
            A sequence of sequences of Floats specifying the following:
            
            - The film coefficient, hh.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        Returns
        -------
        FilmConditionProp
            A :py:class:`~abaqus.Interaction.FilmConditionProp.FilmConditionProp` object.
        """
        self.interactionProperties[name] = interactionProperty = FilmConditionProp(
            name, temperatureDependency, dependencies, property
        )
        return interactionProperty

    @abaqus_method_doc
    def FluidCavityProperty(
        self,
        name: str,
        definition: SymbolicConstant = HYDRAULIC,
        fluidDensity: float = None,
        molecularWeight: float = None,
        useExpansion: Boolean = OFF,
        expansionTempDep: Boolean = OFF,
        expansionDependencies: int = 0,
        referenceTemperature: float = 0,
        expansionTable: tuple = (),
        useBulkModulus: Boolean = OFF,
        bulkModulusTempDep: Boolean = OFF,
        bulkModulusDependencies: int = 0,
        bulkModulusTable: tuple = (),
        useCapacity: Boolean = OFF,
        capacityType: SymbolicConstant = POLYNOMIAL,
        capacityTempDep: Boolean = OFF,
        capacityDependencies: int = 0,
        capacityTable: tuple = (),
    ) -> FluidCavityProperty:
        """This method creates a FluidCavityProperty object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].FluidCavityProperty

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        definition
            A SymbolicConstant specifying the type of fluid cavity property to be defined. Possible
            values are HYDRAULIC and PNEUMATIC. The default value is HYDRAULIC.
        fluidDensity
            None or a Float specifying the reference fluid density. This argument is applicable only
            when **definition** = HYDRAULIC, and is required in that case. The default value is None.
        molecularWeight
            None or a Float specifying the molecular weight of the ideal gas species. This argument
            is applicable only when **definition** = PNEUMATIC, and is required in that case. The
            default value is None.
        useExpansion
            A Boolean specifying whether thermal expansion coefficients will be defined. This
            argument is applicable only when **definition** = HYDRAULIC. The default value is OFF.
        expansionTempDep
            A Boolean specifying whether the thermal fluid expansion data will have temperature
            dependency. This argument is applicable only when **definition** = HYDRAULIC and when
            **useExpansion** = True. The default value is OFF.
        expansionDependencies
            An Int specifying the number of field variable dependencies in the thermal fluid
            expansion data. This argument is applicable only when **definition** = HYDRAULIC and when
            **useExpansion** = True. The default value is 0.
        referenceTemperature
            A Float specifying the reference temperature for the coefficient of thermal expansion.
            This argument is applicable only when **definition** = HYDRAULIC, when **useExpansion** = True,
            and when either **expansionTempDep** = True or when **expansionDependencies** is greater than
            0. The default value is 0.0.
        expansionTable
            A sequence of sequences of Floats specifying the thermal expansion coefficients. This
            argument is applicable only when **definition** = HYDRAULIC and when **useExpansion** = True.
            Each sequence contains the following data:
            
            - The mean coefficient of thermal expansion.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        useBulkModulus
            A Boolean specifying whether fluid bulk modulus values will be defined. This argument is
            applicable only when **definition** = HYDRAULIC. The default value is OFF.
        bulkModulusTempDep
            A Boolean specifying whether the fluid bulk modulus data will have temperature
            dependency. This argument is applicable only when **definition** = HYDRAULIC and when
            **useBulkModulus** = True. The default value is OFF.
        bulkModulusDependencies
            An Int specifying the number of field variable dependencies in the fluid bulk modulus
            data. This argument is applicable only when **definition** = HYDRAULIC and when
            **useBulkModulus** = True. The default value is 0.
        bulkModulusTable
            A sequence of sequences of Floats specifying the fluid bulk modulus values. This
            argument is applicable only when **definition** = HYDRAULIC and when **useBulkModulus** = True.
            Each sequence contains the following data:
            
            - The fluid bulk modulus.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        useCapacity
            A Boolean specifying whether molar heat capacity values will be defined. This argument
            is applicable only when **definition** = PNEUMATIC. The default value is OFF.
        capacityType
            A SymbolicConstant specifying the method to define the molar heat capacity. Possible
            values are POLYNOMIAL and TABULAR. The default value is POLYNOMIAL.
        capacityTempDep
            A Boolean specifying whether the molar heat capacity data will have temperature
            dependency. This argument is applicable only when **definition** = PNEUMATIC, when
            **useCapacity** = True, and when **capacityType** = TABULAR. The default value is OFF.
        capacityDependencies
            An Int specifying the number of field variable dependencies in the molar heat capacity
            data. This argument is applicable only when **definition** = PNEUMATIC, when
            **useCapacity** = True, and when **capacityType** = TABULAR. The default value is 0.
        capacityTable
            A sequence of sequences of Floats specifying the molar heat capacity values in the form
            of a polynomial expression. This argument is applicable only when
            **definition** = PNEUMATIC, when **useCapacity** = True, and when **capacityType** = POLYNOMIAL. In
            this form, only one sequence is specified and that sequence contains the following data:
            
            - The first molar heat capacity coefficient.
            - The second molar heat capacity coefficient.
            - The third molar heat capacity coefficient.
            - The fourth molar heat capacity coefficient.
            - The fifth molar heat capacity coefficient.
            
            Alternatively, the sequence data may specify the molar heat capacity values at constant
            pressure for an ideal gas species. This argument is applicable only when
            **definition** = PNEUMATIC, when **useCapacity** = True, and when **capacityType** = TABULAR. Each
            sequence contains the following data:
            
            - The molar heat capacity at constant pressure.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        Returns
        -------
        FluidCavityProperty
            A :py:class:`~abaqus.Interaction.FluidCavityProperty.FluidCavityProperty` object.
        """
        self.interactionProperties[name] = interactionProperty = FluidCavityProperty(
            name,
            definition,
            fluidDensity,
            molecularWeight,
            useExpansion,
            expansionTempDep,
            expansionDependencies,
            referenceTemperature,
            expansionTable,
            useBulkModulus,
            bulkModulusTempDep,
            bulkModulusDependencies,
            bulkModulusTable,
            useCapacity,
            capacityType,
            capacityTempDep,
            capacityDependencies,
            capacityTable,
        )
        return interactionProperty

    @abaqus_method_doc
    def FluidExchangeProperty(
        self,
        name: str,
        dataTable: tuple,
        definition: SymbolicConstant = BULK_VISCOSITY,
        pressureDependency: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        fieldDependencies: int = 0,
    ) -> FluidExchangeProperty:
        """This method creates a FluidExchangeProperty object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].FluidExchangeProperty

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        dataTable
            A sequence of sequences of Floats specifying the viscous and hydrodynamic resistance
            coefficients when **definition** = BULK_VISCOSITY. Each sequence contains the following
            data:
            
            - The viscous resistance coefficient.
            - The hydrodynamic resistance coefficient.
            - The average absolute pressure, if the data depend on pressure.
            - The average temperature, if the data depend on temperature.
            - The value of the first field variable, if the data depend on field variables.
            - The value of the second field variable.
            - Etc.
            
            Alternatively, the sequence data may specify the mass flow rate. This is applicable only
            when **definition** = MASS_FLUX. In this form, only one sequence is specified and that
            sequence contains the following data:
            
            - The mass flow rate per unit area.
            
            Alternatively, the sequence data may specify the mass rate leakage. This is applicable
            only when **definition** = MASS_RATE_LEAK. Each sequence contains the following data:
              
            - The absolute value of the mass flow rate per unit area. (The first tabular value
              entered must always be zero.)
            - The absolute value of the pressure difference. (The first tabular value entered must
              always be zero.)
            - The average absolute pressure, if the data depend on pressure.
            - The average temperature, if the data depend on temperature.
            - The value of the first field variable, if the data depend on field variables.
            - The value of the second field variable.
            - Etc.
            
            Alternatively, the sequence data may specify the volume flow rate. This is applicable
            only when **definition** = VOL_FLUX. In this form, only one sequence is specified and that
            sequence contains the following data:
            
            - The volumetric flow rate per unit area.
              
            Alternatively, the sequence data may specify the volume rate leakage. This is applicable
            only when **definition** = VOL_RATE_LEAK. Each sequence contains the following data:
            
            - The absolute value of the volumetric flow rate per unit area. (The first tabular value
              entered must always be zero.)
            - The absolute value of the pressure difference. (The first tabular value entered must
              always be zero.)
            - The average absolute pressure, if the data depend on pressure.
            - The average temperature, if the data depend on temperature.
            - The value of the first field variable, if the data depend on field variables.
            - The value of the second field variable.
            - Etc.
            
        definition
            A SymbolicConstant specifying the type of fluid exchange property to be defined.
            Possible values are BULK_VISCOSITY, MASS_FLUX, MASS_RATE_LEAK, VOL_FLUX, and
            VOL_RATE_LEAK. The default value is BULK_VISCOSITY.
        pressureDependency
            A Boolean specifying whether the data will have pressure dependency. This argument is
            applicable only when **definition** = BULK_VISCOSITY, or when **definition** = MASS_RATE_LEAK,
            or when **definition** = VOL_RATE_LEAK. The default value is OFF.
        temperatureDependency
            A Boolean specifying whether the data will have temperature dependency. This argument is
            applicable only when **definition** = BULK_VISCOSITY, or when **definition** = MASS_RATE_LEAK,
            or when **definition** = VOL_RATE_LEAK. The default value is OFF.
        fieldDependencies
            An Int specifying the number of field variable dependencies in the data. This argument
            is applicable only when **definition** = BULK_VISCOSITY, or when
            **definition** = MASS_RATE_LEAK, or when **definition** = VOL_RATE_LEAK. The default value is 0.

        Returns
        -------
        FluidExchangeProperty
            A :py:class:`~abaqus.Interaction.FluidExchangeProperty.FluidExchangeProperty` object.
        """
        self.interactionProperties[name] = interactionProperty = FluidExchangeProperty(
            name,
            dataTable,
            definition,
            pressureDependency,
            temperatureDependency,
            fieldDependencies,
        )
        return interactionProperty

    @abaqus_method_doc
    def IncidentWaveProperty(
        self,
        name: str,
        definition: SymbolicConstant = PLANAR,
        propagationModel: SymbolicConstant = ACOUSTIC,
        soundSpeed: float = None,
        fluidDensity: float = None,
        specificHeatRatio: float = None,
        gravity: float = None,
        atmosphericPressure: float = None,
        dragCoefficient: float = None,
        dragExponent: float = 2,
        waveEffects: Boolean = ON,
        chargeDensity: float = None,
        chargeMass: float = None,
        constantK1: float = None,
        constantK2: float = None,
        constantA: float = None,
        constantB: float = None,
        constantKc: float = None,
        duration: float = None,
        maximumSteps: int = 1500,
        relativeStepControl: float = None,
        absoluteStepControl: float = None,
        stepControlExponent: float = 0,
        genDecayA: float = 0,
        genDecayB: float = 0,
        genDecayC: float = 0,
        seedNumber: int = None,
        massTNT: float = None,
        massFactor: float = 1,
        lengthFactor: float = 1,
        timeFactor: float = 1,
        pressureFactor: float = 1,
    ) -> IncidentWaveProperty:
        """This method creates an IncidentWaveProperty object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].IncidentWaveProperty

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        definition
            A SymbolicConstant specifying the type of wave to be defined. Possible values are
            PLANAR, SPHERICAL, DIFFUSE, AIR_BLAST, and SURFACE_BLAST. The default value is PLANAR.
        propagationModel
            A SymbolicConstant specifying the spherical propagation model. Possible values are
            ACOUSTIC, UNDEX_CHARGE, and GENERALIZED_DECAY. The default value is ACOUSTIC.This
            argument is valid only when **definition** = SPHERICAL.
        soundSpeed
            A Float specifying the speed of sound in the fluid.This argument is not valid when
            **definition** = AIR_BLAST or when **definition** = SURFACE_BLAST.
        fluidDensity
            A Float specifying the fluid mass density.This argument is not valid when
            **definition** = AIR_BLAST or when **definition** = SURFACE_BLAST.
        specificHeatRatio
            None or a Float specifying the ratio of specific heats for gas. The default value is
            None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        gravity
            None or a Float specifying the acceleration due to gravity. The default value is
            None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        atmosphericPressure
            None or a Float specifying the atmospheric pressure. The default value is None.This
            argument is valid only when **definition** = SPHERICAL and **propagationModel** = UNDEX_CHARGE.
        dragCoefficient
            None or a Float specifying the fluid drag coefficient. The default value is None.This
            argument is valid only when **definition** = SPHERICAL and **propagationModel** = UNDEX_CHARGE.
        dragExponent
            A Float specifying the fluid drag exponent. The default value is 2.0.This argument is
            valid only when **definition** = SPHERICAL and **propagationModel** = UNDEX_CHARGE.
        waveEffects
            A Boolean specifying whether or not to include wave effects in the fluid and gas. The
            default value is ON.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        chargeDensity
            None or a Float specifying the density of the charge material. The default value is
            None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        chargeMass
            None or a Float specifying the mass of the charge material. The default value is
            None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        constantK1
            None or a Float specifying the charge material constant K. The default value is
            None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        constantK2
            None or a Float specifying the charge material constant k. The default value is
            None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        constantA
            None or a Float specifying the charge material constant A. The default value is
            None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        constantB
            None or a Float specifying the charge material constant B. The default value is
            None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        constantKc
            None or a Float specifying the charge material constant Kc. The default value is
            None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        duration
            None or a Float specifying the time duration for the bubble simulation. The default
            value is None.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        maximumSteps
            An Int specifying the maximum number of time steps for the bubble simulation. The
            default value is 1500.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        relativeStepControl
            A Float specifying the relative step size control parameter. The default value is
            1x10-11.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        absoluteStepControl
            A Float specifying the absolute step size control parameter. The default value is
            1x10-11.This argument is valid only when **definition** = SPHERICAL and
            **propagationModel** = UNDEX_CHARGE.
        stepControlExponent
            A Float specifying the step size control exponent. The default value is 0.2.This
            argument is valid only when **definition** = SPHERICAL and **propagationModel** = UNDEX_CHARGE.
        genDecayA
            A Float specifying the constant A associated with the generalized decay propagation
            model. The default value is 0.0.This argument is valid only when **definition** = SPHERICAL
            and **propagationModel** = GENERALIZED_DECAY.
        genDecayB
            A Float specifying the constant B associated with the generalized decay propagation
            model. The default value is 0.0.This argument is valid only when **definition** = SPHERICAL
            and **propagationModel** = GENERALIZED_DECAY.
        genDecayC
            A Float specifying the constant C associated with the generalized decay propagation
            model. The default value is 0.0.This argument is valid only when **definition** = SPHERICAL
            and **propagationModel** = GENERALIZED_DECAY.
        seedNumber
            An Int specifying the seed number (N) for the diffuse source calculation. N2 sources
            will be used in the simulation.This argument is valid only when **definition** = DIFFUSE.
        massTNT
            A Float specifying the equivalent mass of TNT, in any preferred mass unit.This argument
            is valid only when **definition** = AIR_BLAST or **definition** = SURFACE_BLAST.
        massFactor
            A Float specifying the multiplication factor to convert from the preferred mass unit to
            kilograms. The default value is 1.0.This argument is valid only when
            **definition** = AIR_BLAST or **definition** = SURFACE_BLAST.
        lengthFactor
            A Float specifying the multiplication factor to convert from the analysis length unit to
            meters. The default value is 1.0.This argument is valid only when **definition** = AIR_BLAST
            or **definition** = SURFACE_BLAST.
        timeFactor
            A Float specifying the multiplication factor to convert from the analysis time unit to
            seconds. The default value is 1.0.This argument is valid only when
            **definition** = AIR_BLAST or **definition** = SURFACE_BLAST.
        pressureFactor
            A Float specifying the multiplication factor to convert from the analysis pressure unit
            to pascals. The default value is 1.0.This argument is valid only when
            **definition** = AIR_BLAST or **definition** = SURFACE_BLAST.

        Returns
        -------
        IncidentWaveProperty
            An :py:class:`~abaqus.Interaction.IncidentWaveProperty.IncidentWaveProperty` object.
        """
        self.interactionProperties[name] = interactionProperty = IncidentWaveProperty(
            name,
            definition,
            propagationModel,
            soundSpeed,
            fluidDensity,
            specificHeatRatio,
            gravity,
            atmosphericPressure,
            dragCoefficient,
            dragExponent,
            waveEffects,
            chargeDensity,
            chargeMass,
            constantK1,
            constantK2,
            constantA,
            constantB,
            constantKc,
            duration,
            maximumSteps,
            relativeStepControl,
            absoluteStepControl,
            stepControlExponent,
            genDecayA,
            genDecayB,
            genDecayC,
            seedNumber,
            massTNT,
            massFactor,
            lengthFactor,
            timeFactor,
            pressureFactor,
        )
        return interactionProperty
