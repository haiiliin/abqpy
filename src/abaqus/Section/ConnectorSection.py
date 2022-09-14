from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Section import Section
from ..Connector.ConnectorBehaviorOptionArray import ConnectorBehaviorOptionArray
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class ConnectorSection(Section):
    """A :py:class:`~abaqus.Connector.ConnectorSection.ConnectorSection` object describes the connection type and the behavior of a connector.
    The ConnectorSection object is derived from the Section object.

    .. note:: 
        This object can be accessed by::

            import section
            mdb.models[name].sections[name]
            import odbSection
            session.odbs[name].sections[name]

        The corresponding analysis keywords are:

        - CONNECTOR SECTION
        - CONNECTOR BEHAVIOR
        - CONNECTOR CONSTITUTIVE REFERENCE
    """

    #: A String specifying the repository key.
    name: str

    #: A SymbolicConstant specifying the assembled connection type. Possible values
    #: are:NONEBEAMBUSHINGCVJOINTCYLINDRICALHINGEPLANARRETRACTORSLIPRINGTRANSLATORUJOINTWELDThe
    #: default value is NONE.You cannot include the **assembledType** argument if
    #: **translationalType** or **rotationalType** are given a value other than NONE. At least one
    #: of the arguments **assembledType**, **translationalType**, or **rotationalType** must be given
    #: a value other than NONE.
    assembledType: SymbolicConstant = NONE

    #: A SymbolicConstant specifying the basic rotational connection type. Possible values
    #: are:NONEALIGNCARDANCONSTANT_VELOCITYEULERFLEXION_TORSIONFLOW_CONVERTERPROJECTION_FLEXION_TORSIONREVOLUTEROTATIONROTATION_ACCELEROMETERUNIVERSALThe
    #: default value is NONE.You cannot include the **rotationalType** argument if
    #: **assembledType** is given a value other than NONE. At least one of the arguments
    #: **assembledType**, **translationalType**, or **rotationalType** must be given an value other
    #: than NONE.
    rotationalType: SymbolicConstant = NONE

    #: A SymbolicConstant specifying the basic translational connection type. Possible values
    #: are:NONEACCELEROMETERAXIALCARTESIANJOINLINKPROJECTION_CARTESIANRADIAL_THRUSTSLIDE_PLANESLOTThe
    #: default value is NONE.You cannot include the **translationalType** argument if
    #: **assembledType** is given a value other than NONE. At least one of the arguments
    #: **assembledType**, **translationalType**, or **rotationalType** must be given an value other
    #: than NONE.
    translationalType: SymbolicConstant = NONE

    #: A SymbolicConstant specifying the time integration scheme to use for analysis. This
    #: argument is applicable only to an Abaqus/Explicit analysis. Possible values are
    #: UNSPECIFIED, IMPLICIT, and EXPLICIT. The default value is UNSPECIFIED.
    integration: SymbolicConstant = UNSPECIFIED

    #: None or a Float specifying the reference length associated with constitutive response
    #: for the first component of relative motion. The default value is None.
    u1ReferenceLength: float = None

    #: None or a Float specifying the reference length associated with constitutive response
    #: for the second component of relative motion. The default value is None.
    u2ReferenceLength: float = None

    #: None or a Float specifying the reference length associated with constitutive response
    #: for the third component of relative motion. The default value is None.
    u3ReferenceLength: float = None

    #: None or a Float specifying the reference angle in degrees associated with constitutive
    #: response for the fourth component of relative motion. The default value is None.
    ur1ReferenceAngle: float = None

    #: None or a Float specifying the reference angle in degrees associated with constitutive
    #: response for the fifth component of relative motion. The default value is None.
    ur2ReferenceAngle: float = None

    #: None or a Float specifying the reference angle in degrees associated with constitutive
    #: response for the sixth component of relative motion. The default value is None.
    ur3ReferenceAngle: float = None

    #: None or a Float specifying the mass per unit reference length of belt material. This
    #: argument is applicable only when **assembledType** = SLIPRING, and must be specified in that
    #: case. The default value is None.
    massPerLength: float = None

    #: None or a Float specifying the contact angle made by the belt wrapping around node b.
    #: This argument is applicable only to an Abaqus/Explicit analysis, and only when
    #: **assembledType** = SLIPRING. The default value is None.
    contactAngle: float = None

    #: A Float specifying the scaling factor for material flow at node b. This argument is
    #: applicable only when **assembledType** = RETRACTOR or **rotationalType** = FLOW_CONVERTER. The
    #: default value is 1.0.
    materialFlowFactor: float = 1

    #: A Boolean specifying whether or not all tabular data associated with the
    #: **behaviorOptions** will be regularized. This argument is applicable only for an
    #: Abaqus/Explicit analysis. The default value is ON.
    regularize: Boolean = ON

    #: A Boolean specifying whether or not the default regularization tolerance will be used
    #: for all tabular data associated with the **behaviorOptions**. This argument is applicable
    #: only for an Abaqus/Explicit analysis and only if **regularize** = ON. The default value is
    #: ON.
    defaultTolerance: Boolean = ON

    #: A Float specifying the regularization increment to be used for all tabular data
    #: associated with the **behaviorOptions**. This argument is applicable only for an
    #: Abaqus/Explicit analysis and only if **regularize** = ON and **defaultTolerance** = OFF. The
    #: default value is 0.03.
    regularization: float = 0

    #: A SymbolicConstant specifying the extrapolation technique to be used for all tabular
    #: data associated with the **behaviorOptions**. Possible values are CONSTANT and LINEAR. The
    #: default value is CONSTANT.
    extrapolation: SymbolicConstant = CONSTANT

    #: A :py:class:`~abaqus.Connector.ConnectorBehaviorOptionArray.ConnectorBehaviorOptionArray` object.
    behaviorOptions: ConnectorBehaviorOptionArray = None

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        assembledType: SymbolicConstant = NONE,
        rotationalType: SymbolicConstant = NONE,
        translationalType: SymbolicConstant = NONE,
        integration: SymbolicConstant = UNSPECIFIED,
        u1ReferenceLength: float = None,
        u2ReferenceLength: float = None,
        u3ReferenceLength: float = None,
        ur1ReferenceAngle: float = None,
        ur2ReferenceAngle: float = None,
        ur3ReferenceAngle: float = None,
        massPerLength: float = None,
        contactAngle: float = None,
        materialFlowFactor: float = 1,
        regularize: Boolean = ON,
        defaultTolerance: Boolean = ON,
        regularization: float = 0,
        extrapolation: SymbolicConstant = CONSTANT,
        behaviorOptions: ConnectorBehaviorOptionArray = None,
    ):
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
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        assembledType: SymbolicConstant = NONE,
        rotationalType: SymbolicConstant = NONE,
        translationalType: SymbolicConstant = NONE,
        integration: SymbolicConstant = UNSPECIFIED,
        u1ReferenceLength: float = None,
        u2ReferenceLength: float = None,
        u3ReferenceLength: float = None,
        ur1ReferenceAngle: float = None,
        ur2ReferenceAngle: float = None,
        ur3ReferenceAngle: float = None,
        massPerLength: float = None,
        contactAngle: float = None,
        materialFlowFactor: float = 1,
        regularize: Boolean = ON,
        defaultTolerance: Boolean = ON,
        regularization: float = 0,
        extrapolation: SymbolicConstant = CONSTANT,
        behaviorOptions: ConnectorBehaviorOptionArray = None,
    ):
        """This method modifies the ConnectorSection object.

        Parameters
        ----------
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

        Raises
        ------
        RangeError
        """
        ...
