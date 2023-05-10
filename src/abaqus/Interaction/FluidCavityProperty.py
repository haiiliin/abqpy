from typing import Optional

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import (
    HYDRAULIC,
    OFF,
    POLYNOMIAL,
    Boolean,
    SymbolicConstant,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .ContactProperty import ContactProperty


@abaqus_class_doc
class FluidCavityProperty(ContactProperty):
    """The FluidCavityProperty object is an interaction property that defines the fluid behavior for a surface-
    based fluid cavity. The FluidCavityProperty object is derived from the InteractionProperty object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].interactionProperties[name]

        The corresponding analysis keywords are:

        - FLUID BEHAVIOR
        - CAPACITY
        - FLUID BULK MODULUS
        - FLUID DENSITY
        - FLUID EXPANSION
        - MOLECULAR WEIGHT
    """

    #: A String specifying the interaction property repository key.
    name: str

    #: A SymbolicConstant specifying the type of fluid cavity property to be defined. Possible
    #: values are HYDRAULIC and PNEUMATIC. The default value is HYDRAULIC.
    definition: SymbolicConstant = HYDRAULIC

    #: None or a Float specifying the reference fluid density. This argument is applicable only
    #: when **definition** = HYDRAULIC, and is required in that case. The default value is None.
    fluidDensity: Optional[float] = None

    #: None or a Float specifying the molecular weight of the ideal gas species. This argument
    #: is applicable only when **definition** = PNEUMATIC, and is required in that case. The
    #: default value is None.
    molecularWeight: Optional[float] = None

    #: A Boolean specifying whether thermal expansion coefficients will be defined. This
    #: argument is applicable only when **definition** = HYDRAULIC. The default value is OFF.
    useExpansion: Boolean = OFF

    #: A Boolean specifying whether the thermal fluid expansion data will have temperature
    #: dependency. This argument is applicable only when **definition** = HYDRAULIC and when
    #: **useExpansion** = True. The default value is OFF.
    expansionTempDep: Boolean = OFF

    #: An Int specifying the number of field variable dependencies in the thermal fluid
    #: expansion data. This argument is applicable only when **definition** = HYDRAULIC and when
    #: **useExpansion** = True. The default value is 0.
    expansionDependencies: int = 0

    #: A Float specifying the reference temperature for the coefficient of thermal expansion.
    #: This argument is applicable only when **definition** = HYDRAULIC, when **useExpansion** = True,
    #: and when either **expansionTempDep** = True or when **expansionDependencies** is greater than
    #: 0. The default value is 0.0.
    referenceTemperature: float = 0

    #: A sequence of sequences of Floats specifying the thermal expansion coefficients. This
    #: argument is applicable only when **definition** = HYDRAULIC and when **useExpansion** = True.
    #: Each sequence contains the following data:
    #:
    #: - The mean coefficient of thermal expansion.
    #: - Temperature, if the data depend on temperature.
    #: - Value of the first field variable, if the data depend on field variables.
    #: - Value of the second field variable.
    #: - Etc.
    expansionTable: tuple = ()

    #: A Boolean specifying whether fluid bulk modulus values will be defined. This argument is
    #: applicable only when **definition** = HYDRAULIC. The default value is OFF.
    useBulkModulus: Boolean = OFF

    #: A Boolean specifying whether the fluid bulk modulus data will have temperature
    #: dependency. This argument is applicable only when **definition** = HYDRAULIC and when
    #: **useBulkModulus** = True. The default value is OFF.
    bulkModulusTempDep: Boolean = OFF

    #: An Int specifying the number of field variable dependencies in the fluid bulk modulus
    #: data. This argument is applicable only when **definition** = HYDRAULIC and when
    #: **useBulkModulus** = True. The default value is 0.
    bulkModulusDependencies: int = 0

    #: A sequence of sequences of Floats specifying the fluid bulk modulus values. This
    #: argument is applicable only when **definition** = HYDRAULIC and when **useBulkModulus** = True.
    #: Each sequence contains the following data:
    #:
    #: - The fluid bulk modulus.
    #: - Temperature, if the data depend on temperature.
    #: - Value of the first field variable, if the data depend on field variables.
    #: - Value of the second field variable.
    #: - Etc.
    bulkModulusTable: tuple = ()

    #: A Boolean specifying whether molar heat capacity values will be defined. This argument
    #: is applicable only when **definition** = PNEUMATIC. The default value is OFF.
    useCapacity: Boolean = OFF

    #: A SymbolicConstant specifying the method to define the molar heat capacity. Possible
    #: values are POLYNOMIAL and TABULAR. The default value is POLYNOMIAL.
    capacityType: SymbolicConstant = POLYNOMIAL

    #: A Boolean specifying whether the molar heat capacity data will have temperature
    #: dependency. This argument is applicable only when **definition** = PNEUMATIC, when
    #: **useCapacity** = True, and when **capacityType** = TABULAR. The default value is OFF.
    capacityTempDep: Boolean = OFF

    #: An Int specifying the number of field variable dependencies in the molar heat capacity
    #: data. This argument is applicable only when **definition** = PNEUMATIC, when
    #: **useCapacity** = True, and when **capacityType** = TABULAR. The default value is 0.
    capacityDependencies: int = 0

    #: A sequence of sequences of Floats specifying the molar heat capacity values in the form
    #: of a polynomial expression. This argument is applicable only when
    #: **definition** = PNEUMATIC, when **useCapacity** = True, and when **capacityType** = POLYNOMIAL. In
    #: this form, only one sequence is specified and that sequence contains the following data:
    #:
    #: - The first molar heat capacity coefficient.
    #: - The second molar heat capacity coefficient.
    #: - The third molar heat capacity coefficient.
    #: - The fourth molar heat capacity coefficient.
    #: - The fifth molar heat capacity coefficient.
    #:
    #: Alternatively, the sequence data may specify the molar heat capacity values at constant
    #: pressure for an ideal gas species. This argument is applicable only when
    #: **definition** = PNEUMATIC, when **useCapacity** = True, and when **capacityType** = TABULAR. Each
    #: sequence contains the following data:
    #:
    #: - The molar heat capacity at constant pressure.
    #: - Temperature, if the data depend on temperature.
    #: - Value of the first field variable, if the data depend on field variables.
    #: - Value of the second field variable.
    #: - Etc.
    capacityTable: tuple = ()

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        definition: Literal[C.PNEUMATIC, C.HYDRAULIC] = HYDRAULIC,
        fluidDensity: Optional[float] = None,
        molecularWeight: Optional[float] = None,
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
        capacityType: Literal[C.POLYNOMIAL, C.TABULAR] = POLYNOMIAL,
        capacityTempDep: Boolean = OFF,
        capacityDependencies: int = 0,
        capacityTable: tuple = (),
    ):
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
            A FluidCavityProperty object.
        """
        super().__init__(name)

    @abaqus_method_doc
    def setValues(
        self,
        definition: Literal[C.PNEUMATIC, C.HYDRAULIC] = HYDRAULIC,
        fluidDensity: Optional[float] = None,
        molecularWeight: Optional[float] = None,
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
        capacityType: Literal[C.POLYNOMIAL, C.TABULAR] = POLYNOMIAL,
        capacityTempDep: Boolean = OFF,
        capacityDependencies: int = 0,
        capacityTable: tuple = (),
    ):
        """This method modifies the FluidCavityProperty object.

        Parameters
        ----------
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
        """
        ...
