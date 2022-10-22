from typing_extensions import Literal
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Constraint import Constraint
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import (Boolean, COMPUTED, DEFAULT, OFF, ON, SOLVER_DEFAULT,
                                              SymbolicConstant)


@abaqus_class_doc
class Tie(Constraint):
    """The Tie object defines two surfaces to be tied together for the duration of a
    simulation.
    The Tie object is derived from the ConstrainedSketchConstraint object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].constraints[name]

        The corresponding analysis keywords are:

        - TIE
    """

    #: A Boolean specifying whether the constraint is suppressed or not. The default value is
    #: OFF.
    suppressed: Boolean = OFF

    #: A String specifying the constraint repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the name of the main surface.
    #:
    #: .. versionchanged:: 2022
    #:     The `master` attribute was renamed to `main`.
    main: Region

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the name of the secondary surface.
    #:
    #: .. versionchanged:: 2022
    #:     The `slave` attribute was renamed to `secondary`.
    secondary: Region

    #: A Boolean specifying whether initial positions of tied secondary nodes are adjusted to
    #: lie on the main surface. The default value is ON.
    adjust: Boolean = ON

    #: A SymbolicConstant specifying the method used to determine the position tolerance.
    #: Possible values are COMPUTED and SPECIFIED. The default value is COMPUTED.
    positionToleranceMethod: SymbolicConstant = COMPUTED

    #: A Float specifying the position tolerance. The **positionTolerance** argument applies only
    #: when **positionToleranceMethod** = SPECIFIED. The default value is 0.0.
    positionTolerance: float = 0

    #: A Boolean specifying whether rotation degrees of freedom should be tied. The default
    #: value is ON.
    tieRotations: Boolean = ON

    #: A SymbolicConstant specifying the method used to determine the constraint ratio.
    #: Possible values are DEFAULT and SPECIFIED. The default value is DEFAULT.
    constraintRatioMethod: SymbolicConstant = DEFAULT

    #: A Float specifying the fractional distance between the main reference surface and the
    #: secondary node at which the translational constraint should act. The **constraintRatio**
    #: argument applies only when **constraintRatioMethod** = SPECIFIED. The default value is 0.0.
    constraintRatio: float = 0

    #: A SymbolicConstant specifying the discretization method. Possible values are
    #: SOLVER_DEFAULT, NODE_TO_SURFACE, and SURFACE_TO_SURFACE. The default value is
    #: SOLVER_DEFAULT.
    constraintEnforcement: SymbolicConstant = SOLVER_DEFAULT

    #: A Boolean specifying whether shell element thickness is considered. The default value is
    #: ON.
    thickness: Boolean = ON

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        main: Region,
        secondary: Region,
        adjust: Boolean = ON,
        positionToleranceMethod: Literal[C.COMPUTED, C.SPECIFIED] = COMPUTED,
        positionTolerance: float = 0,
        tieRotations: Boolean = ON,
        constraintRatioMethod: Literal[C.DEFAULT, C.SPECIFIED] = DEFAULT,
        constraintRatio: float = 0,
        constraintEnforcement: Literal[C.NODE_TO_SURFACE, C.SOLVER_DEFAULT, C.SURFACE_TO_SURFACE] = SOLVER_DEFAULT,
        thickness: Boolean = ON,
    ):
        """This method creates a Tie object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].Tie

        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        main
            A :py:class:`~abaqus.Region.Region.Region` object specifying the name of the main surface.

            .. versionchanged:: 2022
                The `master` argument was renamed to `main`.
        secondary
            A :py:class:`~abaqus.Region.Region.Region` object specifying the name of the secondary surface.

            .. versionchanged:: 2022
                The `slave` argument was renamed to `secondary`.
        adjust
            A Boolean specifying whether initial positions of tied secondary nodes are adjusted to
            lie on the main surface. The default value is ON.
        positionToleranceMethod
            A SymbolicConstant specifying the method used to determine the position tolerance.
            Possible values are COMPUTED and SPECIFIED. The default value is COMPUTED.
        positionTolerance
            A Float specifying the position tolerance. The **positionTolerance** argument applies only
            when **positionToleranceMethod** = SPECIFIED. The default value is 0.0.
        tieRotations
            A Boolean specifying whether rotation degrees of freedom should be tied. The default
            value is ON.
        constraintRatioMethod
            A SymbolicConstant specifying the method used to determine the constraint ratio.
            Possible values are DEFAULT and SPECIFIED. The default value is DEFAULT.
        constraintRatio
            A Float specifying the fractional distance between the main reference surface and the
            secondary node at which the translational constraint should act. The **constraintRatio**
            argument applies only when **constraintRatioMethod** = SPECIFIED. The default value is 0.0.
        constraintEnforcement
            A SymbolicConstant specifying the discretization method. Possible values are
            SOLVER_DEFAULT, NODE_TO_SURFACE, and SURFACE_TO_SURFACE. The default value is
            SOLVER_DEFAULT.
        thickness
            A Boolean specifying whether shell element thickness is considered. The default value is
            ON.

        Returns
        -------
        Tie
            A :py:class:`~abaqus.Constraint.Tie.Tie` object.
        """
        super().__init__()

    @abaqus_method_doc
    def swapSurfaces(self):
        """This method switches the main and secondary surfaces of a tied constraint. This command
        is valid only during the step in which the interaction is created.
        """
        ...

    @abaqus_method_doc
    def setValues(
        self,
        adjust: Boolean = ON,
        positionToleranceMethod: Literal[C.COMPUTED, C.SPECIFIED] = COMPUTED,
        positionTolerance: float = 0,
        tieRotations: Boolean = ON,
        constraintRatioMethod: Literal[C.DEFAULT, C.SPECIFIED] = DEFAULT,
        constraintRatio: float = 0,
        constraintEnforcement: Literal[C.NODE_TO_SURFACE, C.SOLVER_DEFAULT, C.SURFACE_TO_SURFACE] = SOLVER_DEFAULT,
        thickness: Boolean = ON,
    ):
        """This method modifies the Tie object.

        Parameters
        ----------
        adjust
            A Boolean specifying whether initial positions of tied secondary nodes are adjusted to
            lie on the main surface. The default value is ON.
        positionToleranceMethod
            A SymbolicConstant specifying the method used to determine the position tolerance.
            Possible values are COMPUTED and SPECIFIED. The default value is COMPUTED.
        positionTolerance
            A Float specifying the position tolerance. The **positionTolerance** argument applies only
            when **positionToleranceMethod** = SPECIFIED. The default value is 0.0.
        tieRotations
            A Boolean specifying whether rotation degrees of freedom should be tied. The default
            value is ON.
        constraintRatioMethod
            A SymbolicConstant specifying the method used to determine the constraint ratio.
            Possible values are DEFAULT and SPECIFIED. The default value is DEFAULT.
        constraintRatio
            A Float specifying the fractional distance between the main reference surface and the
            secondary node at which the translational constraint should act. The **constraintRatio**
            argument applies only when **constraintRatioMethod** = SPECIFIED. The default value is 0.0.
        constraintEnforcement
            A SymbolicConstant specifying the discretization method. Possible values are
            SOLVER_DEFAULT, NODE_TO_SURFACE, and SURFACE_TO_SURFACE. The default value is
            SOLVER_DEFAULT.
        thickness
            A Boolean specifying whether shell element thickness is considered. The default value is
            ON.
        """
        ...
