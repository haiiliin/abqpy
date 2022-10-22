from typing_extensions import Literal
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Constraint import Constraint
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import Boolean, COMPUTED, DEFAULT, OFF, SymbolicConstant


@abaqus_class_doc
class ShellSolidCoupling(Constraint):
    """The ShellSolidCoupling object defines two surfaces to be tied together for the duration
    of a simulation.
    The ShellSolidCoupling object is derived from the ConstrainedSketchConstraint object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].constraints[name]

        The corresponding analysis keywords are:

        - SHELL TO SOLID COUPLING
    """

    #: A Boolean specifying whether the constraint is suppressed or not. The default value is
    #: OFF.
    suppressed: Boolean = OFF

    #: A String specifying the constraint repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the name of the shell edge surface.
    shellEdge: Region

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the name of the solid surface.
    solidFace: Region

    #: A SymbolicConstant specifying the method used to determine the position tolerance.
    #: Possible values are COMPUTED and SPECIFIED. The default value is COMPUTED.
    positionToleranceMethod: SymbolicConstant = COMPUTED

    #: A Float specifying the position tolerance. The default value is 0.0.The
    #: **positionTolerance** argument applies only when
    #: **positionToleranceMethod** = SPECIFIED.Note:Abaqus will not constrain nodes on the solid
    #: face region outside the position tolerance.
    positionTolerance: float = 0

    #: A SymbolicConstant specifying the method used to determine the influence distance.
    #: Possible values are DEFAULT and SPECIFIED. The default value is DEFAULT.
    influenceDistanceMethod: SymbolicConstant = DEFAULT

    #: A Float specifying the influence distance. The **influenceDistance** argument applies only
    #: when **influenceDistanceMethod** = SPECIFIED. The default value is 0.0.
    influenceDistance: float = 0

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        shellEdge: Region,
        solidFace: Region,
        positionToleranceMethod: Literal[C.COMPUTED, C.SPECIFIED] = COMPUTED,
        positionTolerance: float = 0,
        influenceDistanceMethod: Literal[C.DEFAULT, C.SPECIFIED] = DEFAULT,
        influenceDistance: float = 0,
    ):
        """This method creates a ShellSolidCoupling object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].ShellSolidCoupling

        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        shellEdge
            A :py:class:`~abaqus.Region.Region.Region` object specifying the name of the shell edge surface.
        solidFace
            A :py:class:`~abaqus.Region.Region.Region` object specifying the name of the solid surface.
        positionToleranceMethod
            A SymbolicConstant specifying the method used to determine the position tolerance.
            Possible values are COMPUTED and SPECIFIED. The default value is COMPUTED.
        positionTolerance
            A Float specifying the position tolerance. The default value is 0.0.The
            **positionTolerance** argument applies only when
            **positionToleranceMethod** = SPECIFIED.Note:Abaqus will not constrain nodes on the solid
            face region outside the position tolerance.
        influenceDistanceMethod
            A SymbolicConstant specifying the method used to determine the influence distance.
            Possible values are DEFAULT and SPECIFIED. The default value is DEFAULT.
        influenceDistance
            A Float specifying the influence distance. The **influenceDistance** argument applies only
            when **influenceDistanceMethod** = SPECIFIED. The default value is 0.0.

        Returns
        -------
        ShellSolidCoupling
            A :py:class:`~abaqus.Constraint.ShellSolidCoupling.ShellSolidCoupling` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        positionToleranceMethod: Literal[C.COMPUTED, C.SPECIFIED] = COMPUTED,
        positionTolerance: float = 0,
        influenceDistanceMethod: Literal[C.DEFAULT, C.SPECIFIED] = DEFAULT,
        influenceDistance: float = 0,
    ):
        """This method modifies the ShellSolidCoupling object.

        Parameters
        ----------
        positionToleranceMethod
            A SymbolicConstant specifying the method used to determine the position tolerance.
            Possible values are COMPUTED and SPECIFIED. The default value is COMPUTED.
        positionTolerance
            A Float specifying the position tolerance. The default value is 0.0.The
            **positionTolerance** argument applies only when
            **positionToleranceMethod** = SPECIFIED.Note:Abaqus will not constrain nodes on the solid
            face region outside the position tolerance.
        influenceDistanceMethod
            A SymbolicConstant specifying the method used to determine the influence distance.
            Possible values are DEFAULT and SPECIFIED. The default value is DEFAULT.
        influenceDistance
            A Float specifying the influence distance. The **influenceDistance** argument applies only
            when **influenceDistanceMethod** = SPECIFIED. The default value is 0.0.
        """
        ...
