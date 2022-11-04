from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .ContactControl import ContactControl
from ..UtilityAndView.abaqusConstants import Boolean, COMPUTE, DEFAULT, NONE, OFF, RELATIVE, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class StdContactControl(ContactControl):
    """The StdContactControl object is used in Abaqus/Standard analyses to specify optional
    solution controls for problems involving contact between bodies.
    The StdContactControl object is derived from the ContactControl object.

    .. note::
        This object can be accessed by::

            import interaction
            mdb.models[name].contactControls[name]

        The corresponding analysis keywords are:

        - CONTACT CONTROLS
    """

    #: A String specifying the contact controls repository key.
    name: str

    #: A Float specifying the factor by which Abaqus/Standard will scale the default penalty
    #: stiffness to obtain the stiffnesses used for the contact pairs. Only contact
    #: interactions defined with augmented Lagrangian surface behavior will be affected by this
    #: argument. The default value is 1.0.
    stiffnessScaleFactor: float = 1

    #: A SymbolicConstant specifying whether the allowable penetration is an absolute value or
    #: a value relative to the characteristic contact surface face dimension. Only contact
    #: interactions defined with augmented Lagrangian surface behavior will be affected by this
    #: argument. Possible values are RELATIVE and ABSOLUTE. The default value is RELATIVE.
    penetrationTolChoice: SymbolicConstant = RELATIVE

    #: A Float specifying the ratio of the allowable penetration to the characteristic contact
    #: surface face dimension. The float values represent percentages (e.g.: 0.001=0.1%). Only
    #: contact interactions defined with augmented Lagrangian surface behavior will be affected
    #: by this argument. The default value is 10⁻³.The **relativePenetrationTolerance** argument
    #: applies only when **penetrationTolChoice** = RELATIVE. The **relativePenetrationTolerance**
    #: and **absolutePenetrationTolerance** arguments are mutually exclusive.
    relativePenetrationTolerance: Optional[float] = None

    #: None or a Float specifying the allowable penetration. Only contact interactions defined
    #: with augmented Lagrangian surface behavior will be affected by this argument. The
    #: **absolutePenetrationTolerance** argument applies only when
    #: **penetrationTolChoice** = ABSOLUTE. The **relativePenetrationTolerance** and
    #: **absolutePenetrationTolerance** arguments are mutually exclusive. The default value is
    #: None.
    absolutePenetrationTolerance: Optional[float] = None

    #: A SymbolicConstant specifying when the application of friction occurs. Possible values
    #: are:
    #:
    #: - IMMEDIATE, specifying the friction is included in the increment when contact occurs.
    #: - DELAYED, specifying the application of friction is delayed until the increment after
    #:
    #: contact occurs.
    frictionOnset: Optional[SymbolicConstant] = None

    #: A Boolean specifying whether Abaqus/Standard should automatically compute an overclosure
    #: tolerance and a separation tolerance to prevent chattering in contact. The default value
    #: is OFF.The **automaticTolerances** argument cannot be used with the **maxchp**, **perrmx**,
    #: and **uerrmx** arguments.
    automaticTolerances: Boolean = OFF

    #: An Int specifying the maximum number of points that are permitted to violate contact
    #: conditions in any increment. The default value is 0.Either the **perrmx** or the **uerrmx**
    #: argument must be specified in conjunction with the **maxchp** argument.
    maxchp: int = 0

    #: A Float specifying the maximum value of tensile stress (tensile force in GAP- or
    #: ITT-type contact elements) allowed to be transmitted at a contact point. The default
    #: value is 0.0.The **perrmx** argument must be specified in conjunction with the **maxchp**
    #: argument.
    perrmx: float = 0

    #: A Float specifying the maximum overclosure distance allowed at a slave node that is
    #: considered to be open. The default value is 0.0.The **uerrmx** argument must be specified
    #: in conjunction with the **maxchp** argument.
    uerrmx: float = 0

    #: A SymbolicConstant specifying whether or not viscous damping will be specified, and if
    #: so, how it will be specified. Possible values are NONE, AUTOMATIC, and COEFFICIENT. The
    #: default value is NONE.
    stabilizeChoice: SymbolicConstant = NONE

    #: A Float specifying the value of the damping factor. This value is multiplied by the
    #: calculated damping coefficient. The default value is 1.0.This argument is only valid
    #: when **stabilizeChoice** = AUTOMATIC.
    dampFactor: float = 1

    #: A Float specifying the damping coefficient. The default value is 0.0.This argument is
    #: only valid when **stabilizeChoice** = COEFFICIENT.
    dampCoef: float = 0

    #: A Float specifying the tangential stabilization as a fraction of the normal
    #: stabilization (damping). The default value is 1.0.This argument is valid only if
    #: **stabilizeChoice** = AUTOMATIC or COEFFICIENT.
    tangFraction: float = 1

    #: A Float specifying the fraction of the damping that remains at the end of the step. The
    #: default value is 0.0.This argument is valid only if **stabilizeChoice** = AUTOMATIC or
    #: COEFFICIENT.
    eosFraction: float = 0

    #: A SymbolicConstant specifying how the zero-damping clearance will be specified. Possible
    #: values are COMPUTE and SPECIFY. The default value is COMPUTE.This argument is valid only
    #: if **stabilizeChoice** = AUTOMATIC or COEFFICIENT.
    zeroDampingChoice: SymbolicConstant = COMPUTE

    #: None or a Float specifying the clearance at which damping becomes zero. This argument is
    #: valid only when **zeroDampingChoice** = SPECIFY. This argument is valid only if
    #: **stabilizeChoice** = AUTOMATIC or COEFFICIENT. The default value is None.
    zeroDamping: Optional[float] = None

    #: A SymbolicConstant specifying whether to enforce the contact constraints with Lagrange
    #: multipliers. Possible values are DEFAULT, ENFORCEMENT_OFF, and ENFORCEMENT_ON. The
    #: default value is DEFAULT.
    enforceWithLagrangeMultipliers: SymbolicConstant = DEFAULT

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        stiffnessScaleFactor: float = 1,
        penetrationTolChoice: Literal[C.RELATIVE, C.ABSOLUTE] = RELATIVE,
        relativePenetrationTolerance: Optional[float] = None,
        absolutePenetrationTolerance: Optional[float] = None,
        frictionOnset: Optional[Literal[C.IMMEDIATE, C.DELAYED]] = None,
        automaticTolerances: Boolean = OFF,
        maxchp: int = 0,
        perrmx: float = 0,
        uerrmx: float = 0,
        stabilizeChoice: Literal[C.AUTOMATIC, C.NONE, C.COEFFICIENT] = NONE,
        dampFactor: float = 1,
        dampCoef: float = 0,
        tangFraction: float = 1,
        eosFraction: float = 0,
        zeroDampingChoice: Literal[C.COMPUTE, C.AUTOMATIC, C.SPECIFY, C.COEFFICIENT] = COMPUTE,
        zeroDamping: Optional[float] = None,
        enforceWithLagrangeMultipliers: Literal[C.ENFORCEMENT_OFF, C.DEFAULT, C.ENFORCEMENT_ON] = DEFAULT,
    ):
        """This method creates an StdContactControl object.

        .. note::
            This function can be accessed by::

                mdb.models[name].StdContactControl

        Parameters
        ----------
        name
            A String specifying the contact controls repository key.
        stiffnessScaleFactor
            A Float specifying the factor by which Abaqus/Standard will scale the default penalty
            stiffness to obtain the stiffnesses used for the contact pairs. Only contact
            interactions defined with augmented Lagrangian surface behavior will be affected by this
            argument. The default value is 1.0.
        penetrationTolChoice
            A SymbolicConstant specifying whether the allowable penetration is an absolute value or
            a value relative to the characteristic contact surface face dimension. Only contact
            interactions defined with augmented Lagrangian surface behavior will be affected by this
            argument. Possible values are RELATIVE and ABSOLUTE. The default value is RELATIVE.
        relativePenetrationTolerance
            A Float specifying the ratio of the allowable penetration to the characteristic contact
            surface face dimension. The float values represent percentages (e.g.: 0.001=0.1%). Only
            contact interactions defined with augmented Lagrangian surface behavior will be affected
            by this argument. The default value is 10⁻³.The **relativePenetrationTolerance** argument
            applies only when **penetrationTolChoice** = RELATIVE. The **relativePenetrationTolerance**
            and **absolutePenetrationTolerance** arguments are mutually exclusive.
        absolutePenetrationTolerance
            None or a Float specifying the allowable penetration. Only contact interactions defined
            with augmented Lagrangian surface behavior will be affected by this argument. The
            **absolutePenetrationTolerance** argument applies only when
            **penetrationTolChoice** = ABSOLUTE. The **relativePenetrationTolerance** and
            **absolutePenetrationTolerance** arguments are mutually exclusive. The default value is
            None.
        frictionOnset
            A SymbolicConstant specifying when the application of friction occurs. Possible values
            are:
            - IMMEDIATE, specifying the friction is included in the increment when contact occurs.
            - DELAYED, specifying the application of friction is delayed until the increment after
              contact occurs.
        automaticTolerances
            A Boolean specifying whether Abaqus/Standard should automatically compute an overclosure
            tolerance and a separation tolerance to prevent chattering in contact. The default value
            is OFF.The **automaticTolerances** argument cannot be used with the **maxchp**, **perrmx**,
            and **uerrmx** arguments.
        maxchp
            An Int specifying the maximum number of points that are permitted to violate contact
            conditions in any increment. The default value is 0.Either the **perrmx** or the **uerrmx**
            argument must be specified in conjunction with the **maxchp** argument.
        perrmx
            A Float specifying the maximum value of tensile stress (tensile force in GAP- or
            ITT-type contact elements) allowed to be transmitted at a contact point. The default
            value is 0.0.The **perrmx** argument must be specified in conjunction with the **maxchp**
            argument.
        uerrmx
            A Float specifying the maximum overclosure distance allowed at a slave node that is
            considered to be open. The default value is 0.0.The **uerrmx** argument must be specified
            in conjunction with the **maxchp** argument.
        stabilizeChoice
            A SymbolicConstant specifying whether or not viscous damping will be specified, and if
            so, how it will be specified. Possible values are NONE, AUTOMATIC, and COEFFICIENT. The
            default value is NONE.
        dampFactor
            A Float specifying the value of the damping factor. This value is multiplied by the
            calculated damping coefficient. The default value is 1.0.This argument is only valid
            when **stabilizeChoice** = AUTOMATIC.
        dampCoef
            A Float specifying the damping coefficient. The default value is 0.0.This argument is
            only valid when **stabilizeChoice** = COEFFICIENT.
        tangFraction
            A Float specifying the tangential stabilization as a fraction of the normal
            stabilization (damping). The default value is 1.0.This argument is valid only if
            **stabilizeChoice** = AUTOMATIC or COEFFICIENT.
        eosFraction
            A Float specifying the fraction of the damping that remains at the end of the step. The
            default value is 0.0.This argument is valid only if **stabilizeChoice** = AUTOMATIC or
            COEFFICIENT.
        zeroDampingChoice
            A SymbolicConstant specifying how the zero-damping clearance will be specified. Possible
            values are COMPUTE and SPECIFY. The default value is COMPUTE.This argument is valid only
            if **stabilizeChoice** = AUTOMATIC or COEFFICIENT.
        zeroDamping
            None or a Float specifying the clearance at which damping becomes zero. This argument is
            valid only when **zeroDampingChoice** = SPECIFY. This argument is valid only if
            **stabilizeChoice** = AUTOMATIC or COEFFICIENT. The default value is None.
        enforceWithLagrangeMultipliers
            A SymbolicConstant specifying whether to enforce the contact constraints with Lagrange
            multipliers. Possible values are DEFAULT, ENFORCEMENT_OFF, and ENFORCEMENT_ON. The
            default value is DEFAULT.

        Returns
        -------
        StdContactControl
            A StdContactControl object.

        Raises
        ------
        RangeError
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        stiffnessScaleFactor: float = 1,
        penetrationTolChoice: Literal[C.RELATIVE, C.ABSOLUTE] = RELATIVE,
        relativePenetrationTolerance: Optional[float] = None,
        absolutePenetrationTolerance: Optional[float] = None,
        frictionOnset: Optional[Literal[C.IMMEDIATE, C.DELAYED]] = None,
        automaticTolerances: Boolean = OFF,
        maxchp: int = 0,
        perrmx: float = 0,
        uerrmx: float = 0,
        stabilizeChoice: Literal[C.AUTOMATIC, C.NONE, C.COEFFICIENT] = NONE,
        dampFactor: float = 1,
        dampCoef: float = 0,
        tangFraction: float = 1,
        eosFraction: float = 0,
        zeroDampingChoice: Literal[C.COMPUTE, C.AUTOMATIC, C.SPECIFY, C.COEFFICIENT] = COMPUTE,
        zeroDamping: Optional[float] = None,
        enforceWithLagrangeMultipliers: Literal[C.ENFORCEMENT_OFF, C.DEFAULT, C.ENFORCEMENT_ON] = DEFAULT,
    ):
        """This method modifies the StdContactControl object.

        Parameters
        ----------
        stiffnessScaleFactor
            A Float specifying the factor by which Abaqus/Standard will scale the default penalty
            stiffness to obtain the stiffnesses used for the contact pairs. Only contact
            interactions defined with augmented Lagrangian surface behavior will be affected by this
            argument. The default value is 1.0.
        penetrationTolChoice
            A SymbolicConstant specifying whether the allowable penetration is an absolute value or
            a value relative to the characteristic contact surface face dimension. Only contact
            interactions defined with augmented Lagrangian surface behavior will be affected by this
            argument. Possible values are RELATIVE and ABSOLUTE. The default value is RELATIVE.
        relativePenetrationTolerance
            A Float specifying the ratio of the allowable penetration to the characteristic contact
            surface face dimension. The float values represent percentages (e.g.: 0.001=0.1%). Only
            contact interactions defined with augmented Lagrangian surface behavior will be affected
            by this argument. The default value is 10⁻³.The **relativePenetrationTolerance** argument
            applies only when **penetrationTolChoice** = RELATIVE. The **relativePenetrationTolerance**
            and **absolutePenetrationTolerance** arguments are mutually exclusive.
        absolutePenetrationTolerance
            None or a Float specifying the allowable penetration. Only contact interactions defined
            with augmented Lagrangian surface behavior will be affected by this argument. The
            **absolutePenetrationTolerance** argument applies only when
            **penetrationTolChoice** = ABSOLUTE. The **relativePenetrationTolerance** and
            **absolutePenetrationTolerance** arguments are mutually exclusive. The default value is
            None.
        frictionOnset
            A SymbolicConstant specifying when the application of friction occurs. Possible values
            are:

            - IMMEDIATE, specifying the friction is included in the increment when contact occurs.
            - DELAYED, specifying the application of friction is delayed until the increment after
              contact occurs.
        automaticTolerances
            A Boolean specifying whether Abaqus/Standard should automatically compute an overclosure
            tolerance and a separation tolerance to prevent chattering in contact. The default value
            is OFF.The **automaticTolerances** argument cannot be used with the **maxchp**, **perrmx**,
            and **uerrmx** arguments.
        maxchp
            An Int specifying the maximum number of points that are permitted to violate contact
            conditions in any increment. The default value is 0.Either the **perrmx** or the **uerrmx**
            argument must be specified in conjunction with the **maxchp** argument.
        perrmx
            A Float specifying the maximum value of tensile stress (tensile force in GAP- or
            ITT-type contact elements) allowed to be transmitted at a contact point. The default
            value is 0.0.The **perrmx** argument must be specified in conjunction with the **maxchp**
            argument.
        uerrmx
            A Float specifying the maximum overclosure distance allowed at a slave node that is
            considered to be open. The default value is 0.0.The **uerrmx** argument must be specified
            in conjunction with the **maxchp** argument.
        stabilizeChoice
            A SymbolicConstant specifying whether or not viscous damping will be specified, and if
            so, how it will be specified. Possible values are NONE, AUTOMATIC, and COEFFICIENT. The
            default value is NONE.
        dampFactor
            A Float specifying the value of the damping factor. This value is multiplied by the
            calculated damping coefficient. The default value is 1.0.This argument is only valid
            when **stabilizeChoice** = AUTOMATIC.
        dampCoef
            A Float specifying the damping coefficient. The default value is 0.0.This argument is
            only valid when **stabilizeChoice** = COEFFICIENT.
        tangFraction
            A Float specifying the tangential stabilization as a fraction of the normal
            stabilization (damping). The default value is 1.0.This argument is valid only if
            **stabilizeChoice** = AUTOMATIC or COEFFICIENT.
        eosFraction
            A Float specifying the fraction of the damping that remains at the end of the step. The
            default value is 0.0.This argument is valid only if **stabilizeChoice** = AUTOMATIC or
            COEFFICIENT.
        zeroDampingChoice
            A SymbolicConstant specifying how the zero-damping clearance will be specified. Possible
            values are COMPUTE and SPECIFY. The default value is COMPUTE.This argument is valid only
            if **stabilizeChoice** = AUTOMATIC or COEFFICIENT.
        zeroDamping
            None or a Float specifying the clearance at which damping becomes zero. This argument is
            valid only when **zeroDampingChoice** = SPECIFY. This argument is valid only if
            **stabilizeChoice** = AUTOMATIC or COEFFICIENT. The default value is None.
        enforceWithLagrangeMultipliers
            A SymbolicConstant specifying whether to enforce the contact constraints with Lagrange
            multipliers. Possible values are DEFAULT, ENFORCEMENT_OFF, and ENFORCEMENT_ON. The
            default value is DEFAULT.

        Raises
        ------
        RangeError
        """
        ...
