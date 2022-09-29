import typing
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ConnectorOptions import ConnectorOptions
from .ConnectorPotentialArray import ConnectorPotentialArray
from .TangentialBehavior import TangentialBehavior
from ..UtilityAndView.abaqusConstants import *


# Prevent circular import
class DerivedComponent:
    ...


@abaqus_class_doc
class ConnectorBehaviorOption:
    """The ConnectorBehaviorOption object is the abstract base type for other
    ConnectorBehaviorOption objects. The ConnectorBehaviorOption object has no explicit
    constructor. The members of the ConnectorBehaviorOption object are common to all objects
    derived from the ConnectorBehaviorOption.

    .. note:: 
        This object can be accessed by::

            import section
            mdb.models[name].sections[name].behaviorOptions[i]
            import odbSection
            session.odbs[name].sections[name].behaviorOptions[i]
    """

    #: A :py:class:`~abaqus.Connector.ConnectorPotentialArray.ConnectorPotentialArray` object.
    connectorPotentials: ConnectorPotentialArray = []

    #: A :py:class:`~abaqus.Connector.ConnectorBehaviorOption.DerivedComponent` object.
    derivedComponent: DerivedComponent = DerivedComponent()

    #: A :py:class:`~abaqus.Connector.ConnectorPotentialArray.ConnectorPotentialArray` object.
    evolutionPotentials: ConnectorPotentialArray = []

    #: A :py:class:`~abaqus.Connector.ConnectorPotentialArray.ConnectorPotentialArray` object.
    initiationPotentials: ConnectorPotentialArray = []

    #: A :py:class:`~abaqus.Connector.ConnectorOptions.ConnectorOptions` object.
    initiationOptions: ConnectorOptions = ConnectorOptions()

    #: A :py:class:`~abaqus.Connector.ConnectorOptions.ConnectorOptions` object.
    isotropicOptions: ConnectorOptions = ConnectorOptions()

    #: A :py:class:`~abaqus.Connector.ConnectorOptions.ConnectorOptions` object.
    kinematicOptions: ConnectorOptions = ConnectorOptions()

    #: A :py:class:`~abaqus.Connector.ConnectorOptions.ConnectorOptions` object specifying the ConnectorOptions used to define tabular options
    #: for this ConnectorBehaviorOption.
    options: ConnectorOptions = ConnectorOptions()

    #: A :py:class:`~abaqus.Connector.TangentialBehavior.TangentialBehavior` object
    tangentialBehavior: TangentialBehavior = TangentialBehavior()

    @abaqus_method_doc
    def TangentialBehavior(
        self,
        formulation: SymbolicConstant = PENALTY,
        slipRateDependency: Boolean = OFF,
        pressureDependency: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        exponentialDecayDefinition: SymbolicConstant = COEFFICIENTS,
        shearStressLimit: typing.Optional[float] = None,
        maximumElasticSlip: SymbolicConstant = FRACTION,
        fraction: typing.Optional[float] = None,
        absoluteDistance: typing.Optional[float] = None,
        table: tuple = (),
    ) -> TangentialBehavior:
        """This method creates a TangentialBehavior object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sections[name].behaviorOptions[i].TangentialBehavior
                session.odbs[name].sections[name].behaviorOptions[i].TangentialBehavior

        Parameters
        ----------
        formulation
            A SymbolicConstant specifying the friction coefficient formulation. Possible values are
            PENALTY and EXPONENTIAL_DECAY. The default value is PENALTY.
        slipRateDependency
            A Boolean specifying whether the data depend on slip rate. The default value is OFF.
        pressureDependency
            A Boolean specifying whether the data depend on contact pressure. The default value is
            OFF.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variables for the data. The default value is 0.
        exponentialDecayDefinition
            A SymbolicConstant specifying the exponential decay definition for the data. Possible
            values are COEFFICIENTS and TEST_DATA. The default value is COEFFICIENTS.
        shearStressLimit
            None or a Float specifying no upper limit or the friction coefficient shear stress
            limit. The default value is None.
        maximumElasticSlip
            A SymbolicConstant specifying the method for modifying the allowable elastic slip.
            Possible values are FRACTION and ABSOLUTE_DISTANCE. The default value is FRACTION.This
            argument applies only to Abaqus/Standard analyses.
        fraction
            A Float specifying the ratio of the allowable maximum elastic slip to a characteristic
            model dimension. The default value is 10-4.This argument applies only to Abaqus/Standard
            analyses.
        absoluteDistance
            None or a Float specifying the absolute magnitude of the allowable elastic slip. The
            default value is None.This argument applies only to Abaqus/Standard analyses.
        table
            A sequence of sequences of Floats specifying the tangential properties. Items in the
            table data are described below. The default value is an empty sequence.

        Returns
        -------
        TangentialBehavior
            A :py:class:`~abaqus.Connector.TangentialBehavior.TangentialBehavior` object.
        """
        self.tangentialBehavior = tangentialBehavior = TangentialBehavior(
            formulation,
            slipRateDependency,
            pressureDependency,
            temperatureDependency,
            dependencies,
            exponentialDecayDefinition,
            shearStressLimit,
            maximumElasticSlip,
            fraction,
            absoluteDistance,
            table,
        )
        return tangentialBehavior

    @abaqus_method_doc
    def DerivedComponent(self) -> DerivedComponent:
        """This method creates a DerivedComponent object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sections[name].behaviorOptions[i].TangentialBehavior
                session.odbs[name].sections[name].behaviorOptions[i].TangentialBehavior

        Returns
        -------
        DerivedComponent
            A :py:class:`~abaqus.Connector.ConnectorBehaviorOption.DerivedComponent` object.

        Raises
        ------
        ValueError and TextError
        """
        self.derivedComponent = derivedComponent = DerivedComponent()
        return derivedComponent

    @abaqus_method_doc
    def ConnectorOptions(
        self,
        useBehRegSettings: Boolean = ON,
        regularize: Boolean = ON,
        defaultTolerance: Boolean = ON,
        regularization: float = 0,
        defaultRateFactor: Boolean = ON,
        rateFactor: float = 0,
        interpolation: SymbolicConstant = LINEAR,
        useBehExtSettings: Boolean = ON,
        extrapolation: SymbolicConstant = CONSTANT,
    ) -> ConnectorOptions:
        """This method creates a connector options object to be used in conjunction with an
        allowable connector behavior option, derived component term, or connector section.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sections[name].behaviorOptions[i].TangentialBehavior
                session.odbs[name].sections[name].behaviorOptions[i].TangentialBehavior

        Parameters
        ----------
        useBehRegSettings
            A Boolean specifying whether or not to use the behavior-level settings for
            regularization options. This argument is applicable only for an Abaqus/Explicit
            analysis. The default value is ON.
        regularize
            A Boolean specifying whether or not the tabular data will be regularized. This argument
            is applicable only for an Abaqus/Explicit analysis and only if **useBehRegSettings** = OFF.
            The default value is ON.
        defaultTolerance
            A Boolean specifying whether or not the analysis default regularization tolerance will
            be used. This argument is applicable only for an Abaqus/Explicit analysis and only if
            **useBehRegSettings** = OFF and **regularize** = ON. The default value is ON.
        regularization
            A Float specifying the regularization increment to be used. This argument is applicable
            only for an Abaqus/Explicit analysis and only if **useBehRegSettings** = OFF,
            **regularize** = ON, and **defaultTolerance** = OFF. The default value is 0.03.
        defaultRateFactor
            A Boolean specifying whether or not the analysis default rate filter factor will be
            used. This argument is applicable only for an Abaqus/Explicit analysis that includes
            isotropic hardening with tabular definition or damage initiation with Plastic motion
            criteria. The default value is ON.
        rateFactor
            A Float specifying the rate filter factor to be used. This argument is applicable only
            for an Abaqus/Explicit analysis that includes isotropic hardening with tabular
            definition or damage initiation with Plastic motion criteria. This argument is also
            applicable only if **defaultRateFactor** = OFF. The default value is 0.9.
        interpolation
            A SymbolicConstant specifying the type of interpolation increment to be used on
            rate-dependent tabular data. This argument is applicable only for an Abaqus/Explicit
            analysis that includes isotropic hardening with tabular definition or damage initiation
            with Plastic motion criteria. Possible values are LINEAR and LOGARITHMIC. The default
            value is LINEAR.
        useBehExtSettings
            A Boolean specifying whether or not to use the behavior-level settings for extrapolation
            options. The default value is ON.
        extrapolation
            A SymbolicConstant specifying the extrapolation technique to be used. This argument is
            applicable only if **useBehExtSettings** = OFF. Possible values are CONSTANT and LINEAR. The
            default value is CONSTANT.

        Returns
        -------
        ConnectorOptions
            A :py:class:`~abaqus.Connector.ConnectorOptions.ConnectorOptions` object.

        Raises
        ------
        ValueError and TextError.
        """
        self.options = connectorOptions = ConnectorOptions(
            useBehRegSettings,
            regularize,
            defaultTolerance,
            regularization,
            defaultRateFactor,
            rateFactor,
            interpolation,
            useBehExtSettings,
            extrapolation,
        )
        return connectorOptions
