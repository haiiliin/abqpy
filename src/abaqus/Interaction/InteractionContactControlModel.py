from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ExpContactControl import ExpContactControl
from .StdContactControl import StdContactControl
from ..Model.ModelBase import ModelBase
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class InteractionContactControlModel(ModelBase):
    @abaqus_method_doc
    def ExpContactControl(
        self,
        name: str,
        globTrkChoice: SymbolicConstant = DEFAULT,
        globTrkInc: int = None,
        fastLocalTrk: Boolean = ON,
        scalePenalty: float = 1,
        warpCheckPeriod: int = 20,
        warpCutoff: float = 20,
    ) -> ExpContactControl:
        """This method creates an ExpContactControl object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ExpContactControl

        Parameters
        ----------
        name
            A String specifying the contact controls repository key.
        globTrkChoice
            A SymbolicConstant specifying whether or not the default value will be used for the
            maximum number of increments between global contact searches. Possible values are
            DEFAULT and SPECIFY. The default value is DEFAULT.
        globTrkInc
            An Int specifying the maximum number of increments between global contact searches. The
            **globTrkInc** argument applies only when **globTrkChoice** = SPECIFY. The default value is
            100 for surface-to-surface contact and 4 for self-contact.
        fastLocalTrk
            A Boolean specifying whether to use the more computationally efficient local tracking
            method. The default value is ON.
        scalePenalty
            A Float specifying the factor by which Abaqus/Explicit will scale the default penalty
            stiffness to obtain the stiffnesses used for the penalty contact pairs. The default
            value is 1.0.
        warpCheckPeriod
            An Int specifying the number of increments between checks for highly warped facets on
            main surfaces. The default value is 20.
        warpCutoff
            A Float specifying the out-of-plane warping angle (in degrees), at which a facet will be
            considered to be highly warped. The default value is 20.0.

        Returns
        -------
        ExpContactControl
            An :py:class:`~abaqus.Interaction.ExpContactControl.ExpContactControl` object.

        Raises
        ------
        RangeError
        """
        self.contactControls[name] = contactControl = ExpContactControl(
            name,
            globTrkChoice,
            globTrkInc,
            fastLocalTrk,
            scalePenalty,
            warpCheckPeriod,
            warpCutoff,
        )
        return contactControl

    @abaqus_method_doc
    def StdContactControl(
        self,
        name: str,
        stiffnessScaleFactor: float = 1,
        penetrationTolChoice: SymbolicConstant = RELATIVE,
        relativePenetrationTolerance: float = None,
        absolutePenetrationTolerance: float = None,
        frictionOnset: SymbolicConstant = None,
        automaticTolerances: Boolean = OFF,
        maxchp: int = 0,
        perrmx: float = 0,
        uerrmx: float = 0,
        stabilizeChoice: SymbolicConstant = NONE,
        dampFactor: float = 1,
        dampCoef: float = 0,
        tangFraction: float = 1,
        eosFraction: float = 0,
        zeroDampingChoice: SymbolicConstant = COMPUTE,
        zeroDamping: float = None,
        enforceWithLagrangeMultipliers: SymbolicConstant = DEFAULT,
    ) -> StdContactControl:
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
            by this argument. The default value is 10-3.The **relativePenetrationTolerance** argument
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
            A Float specifying the maximum overclosure distance allowed at a secondary node that is
            considered to be open. The default value is 0.0.The **uerrmx** argument must be specified
            in conjunction with the **maxchp** argument.

            .. versionchanged:: 2022
                Slave node was changed to secondary node.
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
            A :py:class:`~abaqus.Interaction.StdContactControl.StdContactControl` object.

        Raises
        ------
        RangeError
        """
        self.contactControls[name] = contactControl = StdContactControl(
            name,
            stiffnessScaleFactor,
            penetrationTolChoice,
            relativePenetrationTolerance,
            absolutePenetrationTolerance,
            frictionOnset,
            automaticTolerances,
            maxchp,
            perrmx,
            uerrmx,
            stabilizeChoice,
            dampFactor,
            dampCoef,
            tangFraction,
            eosFraction,
            zeroDampingChoice,
            zeroDamping,
            enforceWithLagrangeMultipliers,
        )
        return contactControl
