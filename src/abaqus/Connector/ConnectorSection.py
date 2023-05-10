from typing import Optional

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Section.SectionBase import SectionBase
from ..UtilityAndView.abaqusConstants import (
    ABS,
    ALL,
    COMPONENT_NUMBER,
    FORCE,
    HALF_CYCLE,
    LINEAR,
    MAXIMUM,
    MOTION_TYPE,
    NO_INDEPENDENT_COMPONENTS,
    OFF,
    ON,
    POSITIVE,
    PREDEFINED,
    SPECIFY,
    SUM,
    TABULAR,
    UNCOUPLED,
    Boolean,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .ConnectorDamage import ConnectorDamage
from .ConnectorDamping import ConnectorDamping
from .ConnectorElasticity import ConnectorElasticity
from .ConnectorFailure import ConnectorFailure
from .ConnectorFriction import ConnectorFriction
from .ConnectorLock import ConnectorLock
from .ConnectorPlasticity import ConnectorPlasticity
from .ConnectorPotential import ConnectorPotential
from .ConnectorPotentialArray import ConnectorPotentialArray
from .ConnectorStop import ConnectorStop


@abaqus_class_doc
class ConnectorSection(SectionBase):
    @abaqus_method_doc
    def ConnectorDamage(
        self,
        coupling: Literal[C.COUPLED, C.UNCOUPLED] = UNCOUPLED,
        criterion: Literal[C.PLASTIC_MOTION, C.FORCE, C.MOTION] = FORCE,
        initiationTemperature: Boolean = OFF,
        initiationPotentialOperator: Literal[C.SUM, C.MOTION, C.COUPLED, C.FORCE, C.MAXIMUM] = SUM,
        initiationPotentialExponent: float = 2,
        initiationDependencies: int = 0,
        evolution: Boolean = ON,
        evolutionType: Literal[C.ENERGY_TYPE, C.MOTION_TYPE] = MOTION_TYPE,
        softening: Literal[C.EXPONENTIAL, C.TABULAR, C.MOTION_TYPE, C.LINEAR] = LINEAR,
        useAffected: Boolean = OFF,
        degradation: Literal[C.MULTIPLICATIVE, C.MAXIMUM] = MAXIMUM,
        evolutionTemperature: Boolean = OFF,
        evolutionDependencies: int = 0,
        evolutionPotentialOperator: Literal[C.SUM, C.MOTION, C.MOTION_TYPE, C.COUPLED, C.FORCE, C.MAXIMUM] = SUM,
        evolutionPotentialExponent: float = 2,
        initiationPotentials: Optional[ConnectorPotentialArray] = None,
        evolutionPotentials: Optional[ConnectorPotentialArray] = None,
        initiationTable: tuple = (),
        evolutionTable: tuple = (),
        affectedComponents: tuple = (),
        components: tuple = (),
    ):
        """This method creates a connector damage behavior option for a ConnectorSection object.

        .. note::
            This function can be accessed by::

                import connectorBehavior
                connectorBehavior.ConnectorDamage
                import odbConnectorBehavior
                odbConnectorBehavior.ConnectorDamage

        Parameters
        ----------
        coupling
            A SymbolicConstant specifying whether or not the behavior is coupled. Possible values
            are UNCOUPLED and COUPLED. The default value is UNCOUPLED.
        criterion
            A SymbolicConstant specifying the damage initiation criterion to be used. Possible
            values are FORCE, MOTION, and PLASTIC_MOTION. The default value is FORCE.
        initiationTemperature
            A Boolean specifying whether the initiation data depend on temperature. The default
            value is OFF.
        initiationPotentialOperator
            A SymbolicConstant specifying the contribution operator for the initiation potential
            contributions. Possible values are SUM and MAXIMUM. The default value is SUM.This
            argument is only if **coupling** = COUPLED and if **criterion** = FORCE or MOTION.
        initiationPotentialExponent
            A Float specifying the number equal to the inverse of the overall exponent in the
            initiation potential definition. The default value is 2.0.This argument is applicable
            only if **coupling** = COUPLED, when **initiationPotentialOperator** = SUM, and when
            **criterion** = FORCE or MOTION.
        initiationDependencies
            An Int specifying the number of field variable dependencies for the initiation data. The
            default value is 0.
        evolution
            A Boolean specifying whether damage evolution data will be used. The default value is
            ON.
        evolutionType
            A SymbolicConstant specifying the type of damage evolution to be specified. Possible
            values are MOTION_TYPE and ENERGY_TYPE. The default value is MOTION_TYPE.This argument
            is applicable only if **evolution** = ON.
        softening
            A SymbolicConstant specifying the damage evolution law to be specified. Possible values
            are LINEAR, EXPONENTIAL, and TABULAR. The default value is LINEAR.This argument is
            applicable only if **evolution** = ON and when **evolutionType** = MOTION_TYPE.
        useAffected
            A Boolean specifying whether or not **affectedComponents** will be specified. If
            **useAffected** = OFF, then only the components of relative motion specified by **components**
            will undergo damage. The default value is OFF.This argument is applicable only if
            **evolution** = ON.
        degradation
            A SymbolicConstant specifying the contribution of each damage mechanism when more than
            one damage mechanism is defined. Possible values are MAXIMUM and MULTIPLICATIVE. The
            default value is MAXIMUM.This argument is applicable if **evolution** = ON.
        evolutionTemperature
            A Boolean specifying whether the evolution data depend on temperature. The default value
            is OFF.This argument is applicable only if **evolution** = ON.
        evolutionDependencies
            An Int specifying the number of field variable dependencies for the evolution data. The
            default value is 0.This argument is applicable only if **evolution** = ON.
        evolutionPotentialOperator
            A SymbolicConstant specifying the contribution operator for the evolution potential
            contributions. Possible values are SUM and MAXIMUM. The default value is SUM.This
            argument is applicable only if **coupling** = COUPLED, when **evolution** = ON, when
            **evolutionType** = MOTION_TYPE, and when **criterion** = FORCE or MOTION.
        evolutionPotentialExponent
            A Float specifying the number equal to the inverse of the overall exponent in the
            evolution potential definition. The default value is 2.0.This argument is applicable
            only if **coupling** = COUPLED, when **evolution** = ON, when **evolutionPotentialOperator** = SUM,
            when **evolutionType** = MOTION, and when **criterion** = FORCE or MOTION.
        initiationPotentials
            A ConnectorPotentialArray object specifying one ConnectorPotential object for each
            initiation potential contribution. This member can be specified only if
            **coupling** = COUPLED and if **criterion** = FORCE or MOTION.
        evolutionPotentials
            A ConnectorPotentialArray object specifying one ConnectorPotential object for each
            evolution potential contribution). This member can be specified only if
            **coupling** = COUPLED, if **evolution** = ON, if **evolutionType** = MOTION, and if
            **criterion** = FORCE or MOTION.
        initiationTable
            A sequence of sequences of Floats specifying the initiation properties. The default
            value is an empty sequence.Items in the **initiationTable** data are described below.
        evolutionTable
            A sequence of sequences of Floats specifying the evolution properties. The default value
            is an empty sequence.Items in the **evolutionTable** data are described below. This
            argument is only applicable if **evolution** = ON.
        affectedComponents
            A sequence of Ints specifying the components of relative motion that will be damaged.
            Possible values are 1 ≤ **components** ≤ 6. Only available components can be specified.
            This argument is applicable only if **evolution** = ON and **useAffected** = ON. The default
            value is an empty sequence.
        components
            A sequence of Ints specifying the components of relative motion for which the behavior
            is defined. Possible values are 1 ≤ **components** ≤ 6. Only available components can be
            specified. This argument can be specified only if **coupling** = UNCOUPLED. The default
            value is an empty sequence.

        Returns
        -------
        ConnectorDamage
            A ConnectorDamage object.

        Raises
        ------
        ValueError and TextError
        """
        option = ConnectorDamage()
        self.behaviorOptions.append(option)
        return option

    @abaqus_method_doc
    def ConnectorDamping(
        self,
        behavior: Literal[C.NONLINEAR, C.LINEAR] = LINEAR,
        coupling: Literal[
            C.UNCOUPLED, C.NONLINEAR, C.COUPLED_POSITION, C.COUPLED_MOTION, C.COUPLED, C.LINEAR
        ] = UNCOUPLED,
        dependencies: int = 0,
        temperatureDependency: Boolean = OFF,
        frequencyDependency: Boolean = OFF,
        table: tuple = (),
        independentComponents: tuple = (),
        components: tuple = (),
    ):
        """This method creates a connector damping behavior option for a ConnectorSection object.

        .. note::
            This function can be accessed by::

                import connectorBehavior
                connectorBehavior.ConnectorDamping
                import odbConnectorBehavior
                odbConnectorBehavior.ConnectorDamping

        Parameters
        ----------
        behavior
            A SymbolicConstant specifying if the damping behavior is linear or nonlinear. Possible
            values are LINEAR and NONLINEAR. The default value is LINEAR.
        coupling
            A SymbolicConstant specifying whether the damping behavior is coupled between the
            connector's components of relative motion. If **behavior** = LINEAR, then possible values
            are UNCOUPLED and COUPLED. If **behavior** = NONLINEAR, then possible values are UNCOUPLED,
            COUPLED_POSITION, and COUPLED_MOTION. Possible values are UNCOUPLED, COUPLED,
            COUPLED_POSITION, and COUPLED_MOTION. The default value is UNCOUPLED.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        temperatureDependency
            A Boolean specifying whether the behavior data depend on temperature. The default value
            is OFF.
        frequencyDependency
            A Boolean specifying whether the behavior data depend on frequency. This value is
            applicable only if **behavior** =  LINEAR and **coupling** = UNCOUPLED. The default value is
            OFF.
        table
            A sequence of sequences of Floats specifying damping properties. Items in the table data
            are described below. The default value is an empty sequence.
        independentComponents
            A sequence of Ints specifying the list of independent components that are included in
            the definition of the connector damping data. This argument is applicable only if
            **behavior** = NONLINEAR and **coupling** = COUPLED_POSITION or COUPLED_MOTION. When this
            argument is applicable, at least one value must be specified. Only available components
            can be specified. The default value is an empty sequence.
        components
            A sequence of Ints specifying the components of relative motion for which the behavior
            is defined. Possible values are 1 ≤ **components** ≤ 6. Only available components can be
            specified. The default value is an empty sequence.

        Returns
        -------
        ConnectorDamping
            A ConnectorDamping object.

        Raises
        ------
        ValueError and TextError
        """
        option = ConnectorDamping()
        self.behaviorOptions.append(option)
        return option

    @abaqus_method_doc
    def ConnectorElasticity(
        self,
        behavior: Literal[C.RIGID, C.NONLINEAR, C.LINEAR] = LINEAR,
        coupling: Literal[
            C.RIGID, C.UNCOUPLED, C.NONLINEAR, C.COUPLED_POSITION, C.COUPLED_MOTION, C.COUPLED, C.LINEAR
        ] = UNCOUPLED,
        dependencies: int = 0,
        temperatureDependency: Boolean = OFF,
        frequencyDependency: Boolean = OFF,
        table: tuple = (),
        independentComponents: tuple = (),
        components: tuple = (),
    ):
        """This method creates a connector elasticity behavior option for a ConnectorSection object.

        .. note::
            This function can be accessed by::

                import connectorBehavior
                connectorBehavior.ConnectorElasticity
                import odbConnectorBehavior
                odbConnectorBehavior.ConnectorElasticity

        Parameters
        ----------
        behavior
            A SymbolicConstant specifying whether the elastic behavior is linear, nonlinear, or
            rigid. Possible values are LINEAR, NONLINEAR, and RIGID. The default value is LINEAR.
        coupling
            A SymbolicConstant specifying whether the elastic behavior is coupled between the
            connector's components of relative motion. If **behavior** = LINEAR, then possible values
            are UNCOUPLED and COUPLED. If **behavior** = NONLINEAR, then possible values are UNCOUPLED,
            COUPLED_POSITION, and COUPLED_MOTION. Possible values are UNCOUPLED, COUPLED,
            COUPLED_POSITION, and COUPLED_MOTION. The default value is UNCOUPLED.This argument is
            not applicable if **behavior** = RIGID.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.This
            argument is not applicable if **behavior** = RIGID.
        temperatureDependency
            A Boolean specifying whether the behavior data depend on temperature. The default value
            is OFF.This argument is not applicable if **behavior** = RIGID.
        frequencyDependency
            A Boolean specifying whether the behavior data depend on frequency. This value is
            applicable only if **behavior** = LINEAR and **coupling** = UNCOUPLED. The default value is
            OFF.This argument is not applicable if **behavior** = RIGID.
        table
            A sequence of sequences of Floats specifying elasticity properties. Items in the table
            data are described below. This argument is not applicable if **behavior** = RIGID. The
            default value is an empty sequence.
        independentComponents
            A sequence of Ints specifying the list of independent components that are included in
            the definition of the connector elasticity data. This argument is applicable only if
            **behavior** = NONLINEAR and **coupling** = COUPLED_POSITION or COUPLED_MOTION. If this argument
            is applicable, at least one value must be specified. Only available components can be
            specified. The default value is an empty sequence.
        components
            A sequence of Ints specifying the components of relative motion for which the behavior
            is defined. Possible values are 1 ≤ **components** ≤ 6. Only available components can be
            specified. The default value is an empty sequence.

        Returns
        -------
        ConnectorElasticity
            A ConnectorElasticity object.

        Raises
        ------
        ValueError and TextError
        """
        option = ConnectorElasticity()
        self.behaviorOptions.append(option)
        return option

    @abaqus_method_doc
    def ConnectorFailure(
        self,
        releaseComponent: Literal[C.ALL] = ALL,
        minMotion: Optional[float] = None,
        maxMotion: Optional[float] = None,
        minForce: Optional[float] = None,
        maxForce: Optional[float] = None,
        components: tuple = (),
    ):
        """This method creates a connector failure behavior option for a ConnectorSection object.

        .. note::
            This function can be accessed by::

                import connectorBehavior
                connectorBehavior.ConnectorFailure
                import odbConnectorBehavior
                odbConnectorBehavior.ConnectorFailure

        Parameters
        ----------
        releaseComponent
            The SymbolicConstant ALL or an Int specifying the motion components that fail. If an Int
            is specified, only that motion component fails when the failure criteria are satisfied.
            If **releaseComponent** = ALL, all motion components fail. The default value is ALL.
        minMotion
            None or a Float specifying the lower bound for the connector's relative position for all
            specified components, or no lower bound. The default value is None.
        maxMotion
            None or a Float specifying the upper bound for the connector's relative position for all
            specified components, or no upper bound. The default value is None.
        minForce
            None or a Float specifying the lower bound of the force or moment in the directions of
            the specified components at which locking occurs, or no lower bound. The default value
            is None.
        maxForce
            None or a Float specifying the upper bound of the force or moment in the directions of
            the specified components at which locking occurs, or no upper bound. The default value
            is None.
        components
            A sequence of Ints specifying the components of relative motion for which the behavior
            is defined. Possible values are 1 ≤ **components** ≤ 6. Only available components can be
            specified. The default value is an empty sequence.

        Returns
        -------
        ConnectorFailure
            A ConnectorFailure object.

        Raises
        ------
        ValueError and TextError
        """
        option = ConnectorFailure()
        self.behaviorOptions.append(option)
        return option

    @abaqus_method_doc
    def ConnectorFriction(
        self,
        frictionModel: Literal[C.PREDEFINED, C.USER_CUSTOMIZED] = PREDEFINED,
        slipStyle: Literal[C.COMPUTE, C.SPECIFY, C.USER_CUSTOMIZED] = SPECIFY,
        tangentDirection: Optional[int] = None,
        stickStiffness: Optional[float] = None,
        componentType: Literal[C.POSITION, C.MOTION, C.NO_INDEPENDENT_COMPONENTS] = NO_INDEPENDENT_COMPONENTS,
        slipDependency: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        useContactForceComponent: Boolean = OFF,
        contactForceStyle: Literal[C.COMPONENT_NUMBER, C.USER_CUSTOMIZED, C.DERIVED_COMPONENT] = COMPONENT_NUMBER,
        contactForceComponent: int = 0,
        forcePotentialOperator: Literal[C.SUM, C.COMPUTE, C.USER_CUSTOMIZED, C.MAXIMUM] = SUM,
        forcePotentialExponent: float = 2,
        connectorPotentials: Optional[ConnectorPotentialArray] = None,
        table: tuple = (),
        independentComponents: tuple = (),
    ):
        """This method creates a connector friction behavior option for a ConnectorSection object. Depending
        upon the arguments provided, the friction behavior can be Coulomb-like or hysteretic in nature.

        .. note::
            This function can be accessed by::

                import connectorBehavior
                connectorBehavior.ConnectorFriction
                import odbConnectorBehavior
                odbConnectorBehavior.ConnectorFriction

        Parameters
        ----------
        frictionModel
            A SymbolicConstant specifying the desired frictional response model. Possible values are
            PREDEFINED and USER_CUSTOMIZED. The default value is PREDEFINED.
        slipStyle
            A SymbolicConstant specifying the method of indicating the slip direction: either
            specified or computed based upon the force potential data. Possible values are SPECIFY
            and COMPUTE. The default value is SPECIFY.This argument is applicable only if
            **frictionModel** = USER_CUSTOMIZED.
        tangentDirection
            None or an Int specifying the direction for which the frictional behavior is specified.
            Possible values are 1 ≤ **tangentDirection** ≤ 6, indicating an available component of
            relative motion. This argument applies only if **frictionModel** = USER_CUSTOMIZED and if
            **slipStyle** = SPECIFY. The default value is None.
        stickStiffness
            None or a Float specifying the stick stiffness associated with the frictional behavior
            in the direction specified by **tangentDirection**. If this argument is omitted, Abaqus
            computes an appropriate number for the stick stiffness. The default value is None.
        componentType
            A SymbolicConstant specifying the type of the **independentComponents**. Possible values
            are POSITION, MOTION, and NO_INDEPENDENT_COMPONENTS. The default value is
            NO_INDEPENDENT_COMPONENTS.
        slipDependency
            A Boolean specifying whether the table data depend on accumulated slip. The default
            value is OFF.This argument applies only if **frictionModel** = USER_CUSTOMIZED.
        temperatureDependency
            A Boolean specifying whether the table data depend on temperature. The default value is
            OFF.This argument applies only if **frictionModel** = USER_CUSTOMIZED.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.This
            argument applies only if **frictionModel** = USER_CUSTOMIZED.
        useContactForceComponent
            A Boolean specifying whether the contact force component will be defined. The default
            value is OFF.This argument applies only if **frictionModel** = USER_CUSTOMIZED.
        contactForceStyle
            A SymbolicConstant specifying the method of indicating the contact force component
            direction: either specified or computed based on upon a DerivedComponent. Possible
            values are COMPONENT_NUMBER and DERIVED_COMPONENT. The default value is
            COMPONENT_NUMBER.This argument is applicable only if **frictionModel** = USER_CUSTOMIZED and
            if **useContactForceComponent** = ON.
        contactForceComponent
            An Int specifying the contact force component direction. This argument applies only if
            **frictionModel** = USER_CUSTOMIZED, if **useContactForceComponent** = ON, and if
            **contactForceStyle** = COMPONENT_NUMBER. The default value is 0.
        forcePotentialOperator
            A SymbolicConstant specifying the contribution operator for the force potential
            contributions. Possible values are SUM and MAXIMUM. The default value is SUM.This
            argument is applicable only if **frictionModel** = USER_CUSTOMIZED and if
            **slipStyle** = COMPUTE.
        forcePotentialExponent
            A Float specifying the number equal to the inverse of the overall exponent in the force
            potential definition. The default value is 2.0.This argument is applicable only if
            **frictionModel** = USER_CUSTOMIZED, if **slipStyle** = COMPUTE, and if
            **forcePotentialOperator** = SUM.
        connectorPotentials
            A ConnectorPotentialArray object specifying one ConnectorPotential object for each force
            potential contribution. This member can be specified only if
            **frictionModel** = USER_CUSTOMIZED, and if **slipStyle** = COMPUTE.
        table
            A sequence of sequences of Floats specifying friction properties. The default value is
            an empty sequence.If **frictionModel** = PREDEFINED, each sequence of the table data
            specifies:If applicable, the first geometric scaling constant relevant to frictional
            interactions.Etc., up to as many geometric scaling constants as are associated with this
            connection type.Internal contact force/moment generating friction in the first
            predefined slip direction.If applicable, internal contact force/moment generating
            friction in the second predefined slip direction.Connector constitutive relative motion
            in the direction specified by **independentComponent**.Accumulated slip in the first
            predefined slip direction, if the data depend on accumulated slip.Temperature, if the
            data depend on temperature.Value of the first field variable, if the data depend on
            field variables.Value of the second field variable.Etc.If
            **frictionModel** = USER_CUSTOMIZED, each sequence of the table data specifies:Effective
            radius of the cylindrical or spherical surface over which frictional slip occurs in the
            connector associated with frictional effects in the direction specified by
            **tangentDirection**. This radius is relevant only if the connection type includes an
            available rotational component of relative motion and
            **tangentDirection** = SLIP_DIRECTION.Internal contact force/moment generating friction in
            the direction specified by **tangentDirection**.Connector constitutive relative motion in
            the direction specified by **independentComponent**.Accumulated slip in the direction
            specified by **tangentDirection**, if the data depend on accumulated slip.Temperature, if
            the data depend on temperature.Value of the first field variable, if the data depend on
            field variables.Value of the second field variable.Etc.
        independentComponents
            A sequence of Ints specifying the independent components. Possible values are 1 ≤
            **independentComponents** ≤ 6. In addition, each independent component value must be
            unique. The **independentComponents** argument applies only if
            **frictionModel** = USER_CUSTOMIZED. Only available components can be specified. The default
            value is an empty sequence.

        Returns
        -------
        ConnectorFriction
            A ConnectorFriction object.

        Raises
        ------
        ValueError and TextError
        """
        option = ConnectorFriction()
        self.behaviorOptions.append(option)
        return option

    @abaqus_method_doc
    def ConnectorLock(
        self,
        lockingComponent: Literal[C.ALL] = ALL,
        minMotion: Optional[float] = None,
        maxMotion: Optional[float] = None,
        minForce: Optional[float] = None,
        maxForce: Optional[float] = None,
        components: tuple = (),
    ):
        """This method creates a connector lock behavior option for a ConnectorSection.

        .. note::
            This function can be accessed by::

                import connectorBehavior
                connectorBehavior.ConnectorLock
                import odbConnectorBehavior
                odbConnectorBehavior.ConnectorLock

        Parameters
        ----------
        lockingComponent
            The SymbolicConstant ALL or an Int specifying the motion components that are locked. If
            an Int is specified, only that motion component is locked when the locking criteria are
            satisfied. If **lockingComponent** = ALL, all motion components are locked. The default
            value is ALL.
        minMotion
            None or a Float specifying the lower bound for the connector's relative position for all
            specified components, or no lower bound. The default value is None.
        maxMotion
            None or a Float specifying the upper bound for the connector's relative position for all
            specified components, or no upper bound. The default value is None.
        minForce
            None or a Float specifying the lower bound of the force or moment in the directions of
            the specified components at which locking occurs, or no lower bound. The default value
            is None.
        maxForce
            None or a Float specifying the upper bound of the force or moment in the directions of
            the specified components at which locking occurs, or no upper bound. The default value
            is None.
        components
            A sequence of Ints specifying the components of relative motion for which the behavior
            is defined. Possible values are 1 ≤ **components** ≤ 6. Only available components can be
            specified. The default value is an empty sequence.

        Returns
        -------
        ConnectorLock
            A ConnectorLock object.

        Raises
        ------
        ValueError and TextError
        """
        option = ConnectorLock()
        self.behaviorOptions.append(option)
        return option

    @abaqus_method_doc
    def ConnectorPlasticity(
        self,
        coupling: Literal[C.COUPLED, C.UNCOUPLED] = UNCOUPLED,
        isotropic: Boolean = ON,
        isotropicType: Literal[C.TABULAR, C.EXPONENTIAL_LAW] = TABULAR,
        isotropicTemperature: Boolean = OFF,
        isotropicDependencies: int = 0,
        kinematic: Boolean = OFF,
        kinematicType: Literal[C.PARAMETERS, C.HALF_CYCLE, C.STABILIZED] = HALF_CYCLE,
        kinematicTemperature: Boolean = OFF,
        kinematicDependencies: int = 0,
        forcePotentialOperator: Literal[C.SUM, C.COUPLED, C.MAXIMUM] = SUM,
        forcePotentialExponent: float = 2,
        connectorPotentials: Optional[ConnectorPotentialArray] = None,
        isotropicTable: tuple = (),
        kinematicTable: tuple = (),
        components: tuple = (),
    ):
        """This method creates a connector plasticity behavior option for a ConnectorSection object.

        .. note::
            This function can be accessed by::

                import connectorBehavior
                connectorBehavior.ConnectorPlasticity
                import odbConnectorBehavior
                odbConnectorBehavior.ConnectorPlasticity

        Parameters
        ----------
        coupling
            A SymbolicConstant specifying whether or not the behavior is coupled. Possible values
            are UNCOUPLED and COUPLED. The default value is UNCOUPLED.
        isotropic
            A Boolean specifying whether isotropic hardening data will be used. The default value is
            ON.If **isotropic** = OFF, then **kinematic** must be specified as ON.
        isotropicType
            A SymbolicConstant specifying the type of isotropic hardening to be specified. Possible
            values are TABULAR and EXPONENTIAL_LAW. The default value is TABULAR.This argument is
            applicable only if **isotropic** = ON.
        isotropicTemperature
            A Boolean specifying whether the isotropic data depend on temperature. The default value
            is OFF.This argument is applicable only if **isotropic** = ON.
        isotropicDependencies
            An Int specifying the number of field variable dependencies for the isotropic data. The
            default value is 0.This argument is applicable only if **isotropic** = ON.
        kinematic
            A Boolean specifying whether kinematic hardening data will be used. The default value is
            OFF.If **kinematic** = OFF, then **isotropic** must be specified as ON.
        kinematicType
            A SymbolicConstant specifying the type of kinematic hardening to be specified. Possible
            values are HALF_CYCLE, STABILIZED, and PARAMETERS. The default value is HALF_CYCLE.This
            argument is applicable only if **kinematic** = ON.
        kinematicTemperature
            A Boolean specifying whether the kinematic data depend on temperature. The default value
            is OFF.This argument is applicable only if **kinematic** = ON.
        kinematicDependencies
            An Int specifying the number of field variable dependencies for the kinematic data. The
            default value is 0.This argument is applicable only if **kinematic** = ON.
        forcePotentialOperator
            A SymbolicConstant specifying the contribution operator for the force potential
            contributions. Possible values are SUM and MAXIMUM. The default value is SUM.This
            argument is applicable only if **coupling** = COUPLED.
        forcePotentialExponent
            A Float specifying the number equal to the inverse of the overall exponent in the force
            potential definition. The default value is 2.0.This argument is applicable only if
            **coupling** = COUPLED and if **forcePotentialOperator** = SUM.
        connectorPotentials
            A ConnectorPotentialArray object specifying one ConnectorPotential object for each force
            potential contribution. This member can be specified only if **coupling** = COUPLED.
        isotropicTable
            A sequence of sequences of Floats specifying isotropic plasticity properties. Items in
            the **isotropicTable** data are described below. This argument is applicable only if
            **isotropic** = ON. The default value is an empty sequence.
        kinematicTable
            A sequence of sequences of Floats specifying kinematic plasticity properties. Items in
            the **kinematicTable** data are described below. This argument is applicable only if
            **kinematic** = ON. The default value is an empty sequence.
        components
            A sequence of Ints specifying the components of relative motion for which the behavior
            is defined. Possible values are 1 ≤ **components** ≤ 6. Only available components can be
            specified. This argument can be specified only if **coupling** = UNCOUPLED. The default
            value is an empty sequence.

        Returns
        -------
        ConnectorPlasticity
            A ConnectorPlasticity object.

        Raises
        ------
        ValueError and TextError
        """
        option = ConnectorPlasticity()
        self.behaviorOptions.append(option)
        return option

    @abaqus_method_doc
    def ConnectorPotential(
        self,
        componentStyle: Literal[C.COMPONENT_NUMBER, C.DERIVED_COMPONENT] = COMPONENT_NUMBER,
        componentNumber: int = 0,
        sign: Literal[C.POSITIVE, C.NEGATIVE] = POSITIVE,
        scaleFactor: float = 1,
        positiveExponent: float = 2,
        shiftFactor: float = 0,
        hFunction: Literal[C.MACAULEY, C.IDENTITY, C.ABS] = ABS,
    ):
        """This method creates a connector potential object to be used in conjunction with an allowable
        connector behavior option.

        .. note::
            This function can be accessed by::

                mdb.models[name].sections[name].behaviorOptions[i].ConnectorPotential
                session.odbs[name].sections[name].behaviorOptions[i].ConnectorPotential

        Parameters
        ----------
        componentStyle
            A SymbolicConstant specifying whether a component number or the name of the
            DerivedComponent object will be used in the contribution. Possible values are
            COMPONENT_NUMBER and DERIVED_COMPONENT. The default value is COMPONENT_NUMBER.
        componentNumber
            An Int specifying the component number used in the contribution. This argument is
            applicable only if **componentStyle** = COMPONENT_NUMBER. Possible values are 1 ≤
            **componentNumber** ≤ 6. Only available components can be specified. The default value is
            0.
        sign
            A SymbolicConstant specifying the sign of the contribution. Possible values are POSITIVE
            and NEGATIVE. The default value is POSITIVE.
        scaleFactor
            A Float specifying the scaling factor for the contribution. The default value is 1.0.
        positiveExponent
            A Float specifying the positive exponent for the contribution. The default value is
            2.0.This argument is ignored if the potential operator of the invoking behavior option
            is set to MAXIMUM.
        shiftFactor
            A Float specifying the shift factor for the contribution. The default value is 0.0.
        hFunction
            A SymbolicConstant specifying the H function of the contribution: either absolute value,
            Macauley bracket, or the identity function. Possible values are ABS, MACAULEY, and
            IDENTITY. The default value is ABS.The value of IDENTITY can be used only if
            **positiveExponent** = 1.0 and the potential exponent of the invoking behavior option is
            also 1.0 (i.e., the potential operator of the invoking behavior option must be SUM).

        Returns
        -------
        ConnectorPotential
            A ConnectorPotential object.

        Raises
        ------
        ValueError and TextError
        """
        self.behaviorOptions[componentNumber].connectorPotentials = option = ConnectorPotential()
        return option

    @abaqus_method_doc
    def ConnectorStop(
        self, minMotion: Optional[float] = None, maxMotion: Optional[float] = None, components: tuple = ()
    ):
        """This method creates a connector stop behavior option for a ConnectorSection object.

        .. note::
            This function can be accessed by::

                import connectorBehavior
                connectorBehavior.ConnectorStop
                import odbConnectorBehavior
                odbConnectorBehavior.ConnectorStop

        Parameters
        ----------
        minMotion
            None or a Float specifying the lower bound for the connector's relative position for all
            specified components, or no lower bound. The default value is None.
        maxMotion
            None or a Float specifying the upper bound for the connector's relative position for all
            specified components, or no upper bound. The default value is None.
        components
            A sequence of Ints specifying the components of relative motion for which the behavior
            is defined. Possible values are 1 ≤ **components** ≤ 6. Only available components can be
            specified. The default value is an empty sequence.

        Returns
        -------
        ConnectorStop
            A ConnectorStop object.

        Raises
        ------
        ValueError and TextError
        """
        option = ConnectorStop()
        self.behaviorOptions.append(option)
        return option
