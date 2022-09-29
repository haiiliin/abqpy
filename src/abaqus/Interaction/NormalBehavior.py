import typing

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class NormalBehavior:
    """The NormalBehavior object specifies normal behavior for a contact interaction property.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].interactionProperties[name].normalBehavior

        The table data for this object are:

        - If **pressureOverclosure** = EXPONENTIAL, the table data specify the following:
        
            - Pressure at zero clearance, p0p0.
            - Clearance at which the contact pressure is zero, c0c0.
        - If **pressureOverclosure** = TABULAR, the table data specify the following:
        
            - Pressure.
            - Overclosure.

        The corresponding analysis keywords are:

        - SURFACE BEHAVIOR
    """

    #: The SymbolicConstant DEFAULT or a Float specifying the contact stiffness. This argument
    #: is valid for **pressureOverclosure** = LINEAR. This argument is also valid for
    #: **pressureOverclosure** = HARD when **constraintEnforcementMethod** = AUGMENTED_LAGRANGE or
    #: PENALTY. A value of DEFAULT is valid only when the later conditions are met. A value of
    #: zero is equivalent to specifying DEFAULT. The default value is DEFAULT.
    contactStiffness: typing.Union[SymbolicConstant, float] = DEFAULT

    #: A SymbolicConstant specifying the pressure-overclosure relationship to be used. Possible
    #: values are HARD, EXPONENTIAL, LINEAR, TABULAR, and SCALE_FACTOR. The default value is
    #: HARD.
    pressureOverclosure: SymbolicConstant = HARD

    #: A Boolean specifying whether to allow separation after contact. The default value is ON.
    allowSeparation: Boolean = ON

    #: None or a Float specifying the maximum stiffness. If **maxStiffness** = None, there is no
    #: upper limit. The default value is None.
    maxStiffness: typing.Optional[float] = None

    #: A sequence of sequences of Floats specifying the normal behavior properties. This
    #: argument is valid only for **pressureOverclosure** = EXPONENTIAL or TABULAR. The items in
    #: the table data are described below.
    table: tuple = ()

    #: A SymbolicConstant specifying the method for enforcement of the contact constraint.
    #: Possible values are DEFAULT, AUGMENTED_LAGRANGE, PENALTY, and DIRECT. The default value
    #: is DEFAULT.
    constraintEnforcementMethod: SymbolicConstant = DEFAULT

    #: A Float specifying the overclosure measure (used to delineate the segments of the
    #: pressure-overclosure curve) as a percentage of the minimum element size in the contact
    #: region. The default value is 0.0.
    overclosureFactor: float = 0

    #: A Float specifying the overclosure measure (used to delineate the segments of the
    #: pressure-overclosure curve) directly. The default value is 0.0.
    overclosureMeasure: float = 0

    #: A Float specifying scale factor for the penalty stiffness or the geometric scaling of
    #: the "base" stiffness. The default value is 1.0.
    contactStiffnessScaleFactor: float = 1

    #: A Float specifying an additional scale factor for the "base" default contact stiffness.
    #: The default value is 1.0.
    initialStiffnessScaleFactor: float = 1

    #: A Float specifying the clearance at which the contact pressure is zero. The default
    #: value is 0.0.
    clearanceAtZeroContactPressure: float = 0

    #: A SymbolicConstant specifying the type of penalty stiffness to be defined. This argument
    #: is valid only when **constraintEnforcementMethod** = PENALTY. Possible values are LINEAR and
    #: NONLINEAR. The default value is LINEAR.
    stiffnessBehavior: SymbolicConstant = LINEAR

    #: A Float specifying the ratio of the initial stiffness divided by the final stiffness.
    #: This argument is valid only when **stiffnessBehavior** = NONLINEAR. Possible values are 0 ≤
    #: **stiffnessRatio** << 1. The default value is 0.01.
    stiffnessRatio: float = 0

    #: A Float specifying the ratio of the overclosure at the maximum stiffness divided by the
    #: characteristic facet length. This argument is valid only when
    #: **stiffnessBehavior** = NONLINEAR. The default value is 0.03.
    upperQuadraticFactor: float = 0

    #: A Float specifying the ratio of the overclosure at the initial stiffness divided by the
    #: overclosure at the maximum stiffness, both relative to the clearance at which the
    #: contact pressure is zero. This argument is valid only when
    #: **stiffnessBehavior** = NONLINEAR. Possible values are 0 ≤ **stiffnessRatio** << 1. The
    #: default value is 0.33333.
    lowerQuadraticRatio: float = 0

    @abaqus_method_doc
    def __init__(
        self,
        contactStiffness: typing.Union[SymbolicConstant, float] = DEFAULT,
        pressureOverclosure: SymbolicConstant = HARD,
        allowSeparation: Boolean = ON,
        maxStiffness: typing.Optional[float] = None,
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

                mdb.models[name].interactionProperties[name].NormalBehavior

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
        ...

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the NormalBehavior object."""
        ...
