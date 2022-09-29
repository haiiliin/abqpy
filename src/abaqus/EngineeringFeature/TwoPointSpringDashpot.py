from typing import Optional
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .SpringDashpot import SpringDashpot
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class TwoPointSpringDashpot(SpringDashpot):
    """The TwoPointSpringDashpot object defines springs and/or dashpots between two points on a
    part or an assembly.
    The TwoPointSpringDashpot object is derived from the SpringDashpot object.

    .. note:: 
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].engineeringFeatures.springDashpots[name]
            import assembly
            mdb.models[name].rootAssembly.engineeringFeatures.springDashpots[name]

        The corresponding analysis keywords are:

        - ELEMENT
        - SPRING
        - DASHPOT
    """

    #: A Boolean specifying whether the spring/dashpot is suppressed or not. The default value
    #: is OFF.
    suppressed: Boolean = OFF

    #: A String specifying the repository key.
    name: str

    #: A sequence of pairs of Region objects specifying the points between which the springs
    #: and/or dashpots are applied.
    regionPairs: tuple

    #: A SymbolicConstant specifying whether the axis of the springs and/or dashpots follows
    #: the rotation of the nodes or is in a specified direction. Possible values are NODAL_LINE
    #: and FIXED_DOF.
    axis: SymbolicConstant

    #: An Int specifying the degree of freedom with which the springs and/or dashpots are
    #: associated at their first points. The **dof1** argument applies only when
    #: **axis** = FIXED_DOFS. The default value is 0.
    dof1: int = 0

    #: An Int specifying the degree of freedom with which the springs and/or dashpots are
    #: associated at their second points. The **dof2** argument applies only when
    #: **axis** = FIXED_DOFS. The default value is 0.
    dof2: int = 0

    #: None or a DatumCsys object specifying the local directions for the spring and/or
    #: dashpot. If **orientation** = None, the spring and/or dashpot data are defined in the global
    #: coordinate system. The default value is None.The **orientation** argument applies only
    #: when **axis** = FIXED_DOFS.
    orientation: Optional[str] = None

    #: A Boolean specifying whether to apply spring behavior to the selected point pairs. The
    #: default value is OFF.At least one of the arguments **springBehavior** = ON or
    #: **dashpotBehavior** = ON must be specified.
    springBehavior: Boolean = OFF

    #: A Boolean specifying whether to apply dashpot behavior to the selected point pairs. The
    #: default value is OFF.At least one of the arguments **springBehavior** = ON or
    #: **dashpotBehavior** = ON must be specified.
    dashpotBehavior: Boolean = OFF

    #: A Float specifying the force per relative displacement for the springs. The default
    #: value is 0.0.
    springStiffness: float = 0

    #: A Float specifying the force per relative velocity for the dashpots. The default value
    #: is 0.0.
    dashpotCoefficient: float = 0

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        regionPairs: tuple,
        axis: SymbolicConstant,
        dof1: int = 0,
        dof2: int = 0,
        orientation: Optional[str] = None,
        springBehavior: Boolean = OFF,
        dashpotBehavior: Boolean = OFF,
        springStiffness: float = 0,
        dashpotCoefficient: float = 0,
    ):
        """This method creates a TwoPointSpringDashpot object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].engineeringFeatures.TwoPointSpringDashpot
                mdb.models[name].rootAssembly.engineeringFeatures.TwoPointSpringDashpot
            
        Parameters
        ----------
        name
            A String specifying the repository key. 
        regionPairs
            A sequence of pairs of Region objects specifying the points between which the springs 
            and/or dashpots are applied. 
        axis
            A SymbolicConstant specifying whether the axis of the springs and/or dashpots follows 
            the rotation of the nodes or is in a specified direction. Possible values are NODAL_LINE 
            and FIXED_DOF. 
        dof1
            An Int specifying the degree of freedom with which the springs and/or dashpots are 
            associated at their first points. The **dof1** argument applies only when 
            **axis** = FIXED_DOFS. The default value is 0. 
        dof2
            An Int specifying the degree of freedom with which the springs and/or dashpots are 
            associated at their second points. The **dof2** argument applies only when 
            **axis** = FIXED_DOFS. The default value is 0. 
        orientation
            None or a DatumCsys object specifying the local directions for the spring and/or 
            dashpot. If **orientation** = None, the spring and/or dashpot data are defined in the global 
            coordinate system. The default value is None.The **orientation** argument applies only 
            when **axis** = FIXED_DOFS. 
        springBehavior
            A Boolean specifying whether to apply spring behavior to the selected point pairs. The 
            default value is OFF.At least one of the arguments **springBehavior** = ON or 
            **dashpotBehavior** = ON must be specified. 
        dashpotBehavior
            A Boolean specifying whether to apply dashpot behavior to the selected point pairs. The 
            default value is OFF.At least one of the arguments **springBehavior** = ON or 
            **dashpotBehavior** = ON must be specified. 
        springStiffness
            A Float specifying the force per relative displacement for the springs. The default 
            value is 0.0. 
        dashpotCoefficient
            A Float specifying the force per relative velocity for the dashpots. The default value 
            is 0.0. 

        Returns
        -------
        TwoPointSpringDashpot
            A :py:class:`~abaqus.EngineeringFeature.TwoPointSpringDashpot.TwoPointSpringDashpot` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        dof1: int = 0,
        dof2: int = 0,
        orientation: Optional[str] = None,
        springBehavior: Boolean = OFF,
        dashpotBehavior: Boolean = OFF,
        springStiffness: float = 0,
        dashpotCoefficient: float = 0,
    ):
        """This method modifies the TwoPointSpringDashpot object.

        Parameters
        ----------
        dof1
            An Int specifying the degree of freedom with which the springs and/or dashpots are
            associated at their first points. The **dof1** argument applies only when
            **axis** = FIXED_DOFS. The default value is 0.
        dof2
            An Int specifying the degree of freedom with which the springs and/or dashpots are
            associated at their second points. The **dof2** argument applies only when
            **axis** = FIXED_DOFS. The default value is 0.
        orientation
            None or a DatumCsys object specifying the local directions for the spring and/or
            dashpot. If **orientation** = None, the spring and/or dashpot data are defined in the global
            coordinate system. The default value is None.The **orientation** argument applies only
            when **axis** = FIXED_DOFS.
        springBehavior
            A Boolean specifying whether to apply spring behavior to the selected point pairs. The
            default value is OFF.At least one of the arguments **springBehavior** = ON or
            **dashpotBehavior** = ON must be specified.
        dashpotBehavior
            A Boolean specifying whether to apply dashpot behavior to the selected point pairs. The
            default value is OFF.At least one of the arguments **springBehavior** = ON or
            **dashpotBehavior** = ON must be specified.
        springStiffness
            A Float specifying the force per relative displacement for the springs. The default
            value is 0.0.
        dashpotCoefficient
            A Float specifying the force per relative velocity for the dashpots. The default value
            is 0.0.
        """
        ...
