from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class ContactTangentialBehavior:
    """The ContactTangentialBehavior object specifies tangential behavior for a contact
    interaction property.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactionProperties[name].tangentialBehavior

        The table data for this object are:

        - If **formulation** = PENALTY or LAGRANGE, the table data specify the following:
        
            - Friction coefficient in the first slip direction, μ1μ1.
            - Friction coefficient in the second slip direction, μ2μ2 (if **directionality** = ANISOTROPIC).
            - Slip rate, if the data depend on slip rate.
            - Contact pressure, if the data depend on contact pressure.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If **formulation** = EXPONENTIAL_DECAY and **exponentialDecayDefinition** = COEFFICIENTS, the table data specify the following:
        
            - Static friction coefficient.
            - Kinetic friction coefficient.
            - Decay coefficient.
        - If **formulation** = EXPONENTIAL_DECAY and **exponentialDecayDefinition** = TEST_DATA, the table data specify the following:
        
            - Friction coefficient.
            - Slip rate.
        - If **formulation** = USER_DEFINED, the table data specify the following:
        
            - Friction property.

        The corresponding analysis keywords are:

        - FRICTION
        - CHANGE FRICTION
    """

    #: A SymbolicConstant specifying the friction formulation. Possible values are
    #: FRICTIONLESS, PENALTY, EXPONENTIAL_DECAY, ROUGH, LAGRANGE, and USER_DEFINED. The default
    #: value is FRICTIONLESS.
    formulation: SymbolicConstant = FRICTIONLESS

    #: A SymbolicConstant specifying the directionality of the friction. Possible values are
    #: ISOTROPIC and ANISOTROPIC. The default value is ISOTROPIC.
    directionality: SymbolicConstant = ISOTROPIC

    #: A Boolean specifying whether the data depend on slip rate. The default value is OFF.
    slipRateDependency: Boolean = OFF

    #: A Boolean specifying whether the data depend on contact pressure. The default value is
    #: OFF.
    pressureDependency: Boolean = OFF

    #: A Boolean specifying whether the data depend on temperature. The default value is OFF.
    temperatureDependency: Boolean = OFF

    #: An Int specifying the number of field variables. The default value is 0.
    dependencies: int = 0

    #: A SymbolicConstant specifying the exponential decay definition. Possible values are
    #: COEFFICIENTS and TEST_DATA. The default value is COEFFICIENTS.
    exponentialDecayDefinition: SymbolicConstant = COEFFICIENTS

    #: None or a Float specifying the shear stress limit. If **shearStressLimit** = None, there is
    #: no upper limit. The default value is None.
    shearStressLimit: float = None

    #: A SymbolicConstant specifying what the maximum elastic slip will be. Possible values are
    #: FRACTION and ABSOLUTE_DISTANCE. The default value is FRACTION.
    maximumElasticSlip: SymbolicConstant = FRACTION

    #: A Float specifying the fraction of a characteristic surface dimension. The default value
    #: is 0.0.
    fraction: float = 0

    #: A Float specifying the absolute distance. The default value is 0.0.
    absoluteDistance: float = 0

    #: None or a Float specifying the elastic slip stiffness. If **elasticSlipStiffness** = None,
    #: there is no upper limit. The default value is None.
    elasticSlipStiffness: float = None

    #: An Int specifying the number of state-dependent variables. The default value is 0.
    nStateDependentVars: int = 0

    #: A Boolean specifying whether property values will be used. The default value is OFF.
    useProperties: Boolean = OFF

    #: A tuple of tuples of Floats specifying tangential behavior. The items in the table data
    #: are described below.
    table: float = None

    @abaqus_method_doc
    def __init__(
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

                mdb.models[name].interactionProperties[name].TangentialBehavior

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
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the ContactTangentialBehavior object."""
        ...
