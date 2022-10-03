from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .SpringDashpot import SpringDashpot
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class SpringDashpotToGround(SpringDashpot):
    """The SpringDashpotToGround object defines springs and/or dashpots between points and
    ground on a part or an assembly region.
    The SpringDashpotToGround object is derived from the SpringDashpot object.

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

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the springs and/or dashpots are applied.
    region: Region

    #: An Int specifying the degree of freedom associated with the spring and dashpot
    #: behaviors.
    dof: int

    #: None or a DatumCsys object specifying the local directions for the spring and/or
    #: dashpot. If **orientation** = None, the spring and/or dashpot data are defined in the global
    #: coordinate system. The default value is None.
    orientation: Optional[str] = None

    #: A Boolean specifying whether to apply spring behavior to the selected points. The
    #: default value is OFF.At least one of the arguments **springBehavior** = ON or
    #: **dashpotBehavior** = ON must be specified.
    springBehavior: Boolean = OFF

    #: A Boolean specifying whether to apply dashpot behavior to the selected points. The
    #: default value is OFF.At least one of the arguments **springBehavior** = ON or
    #: **dashpotBehavior** = ON must be specified.
    dashpotBehavior: Boolean = OFF

    #: A Float specifying the force per relative displacement for the spring. The default value
    #: is 0.0.
    springStiffness: float = 0

    #: A Float specifying the force per relative velocity for the dashpot. The default value is
    #: 0.0.
    dashpotCoefficient: float = 0

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        dof: int,
        orientation: Optional[str] = None,
        springBehavior: Boolean = OFF,
        dashpotBehavior: Boolean = OFF,
        springStiffness: float = 0,
        dashpotCoefficient: float = 0,
    ):
        """This method creates a SpringDashpotToGround object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].engineeringFeatures.SpringDashpotToGround
                mdb.models[name].rootAssembly.engineeringFeatures.SpringDashpotToGround
            
        Parameters
        ----------
        name
            A String specifying the repository key. 
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the springs and/or dashpots are applied. 
        dof
            An Int specifying the degree of freedom associated with the spring and dashpot 
            behaviors. 
        orientation
            None or a DatumCsys object specifying the local directions for the spring and/or 
            dashpot. If **orientation** = None, the spring and/or dashpot data are defined in the global 
            coordinate system. The default value is None. 
        springBehavior
            A Boolean specifying whether to apply spring behavior to the selected points. The 
            default value is OFF.At least one of the arguments **springBehavior** = ON or 
            **dashpotBehavior** = ON must be specified. 
        dashpotBehavior
            A Boolean specifying whether to apply dashpot behavior to the selected points. The 
            default value is OFF.At least one of the arguments **springBehavior** = ON or 
            **dashpotBehavior** = ON must be specified. 
        springStiffness
            A Float specifying the force per relative displacement for the spring. The default value 
            is 0.0. 
        dashpotCoefficient
            A Float specifying the force per relative velocity for the dashpot. The default value is 
            0.0. 

        Returns
        -------
        SpringDashpotToGround
            A :py:class:`~abaqus.EngineeringFeature.SpringDashpotToGround.SpringDashpotToGround` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        orientation: Optional[str] = None,
        springBehavior: Boolean = OFF,
        dashpotBehavior: Boolean = OFF,
        springStiffness: float = 0,
        dashpotCoefficient: float = 0,
    ):
        """This method modifies the SpringDashpotToGround object.

        Parameters
        ----------
        orientation
            None or a DatumCsys object specifying the local directions for the spring and/or
            dashpot. If **orientation** = None, the spring and/or dashpot data are defined in the global
            coordinate system. The default value is None.
        springBehavior
            A Boolean specifying whether to apply spring behavior to the selected points. The
            default value is OFF.At least one of the arguments **springBehavior** = ON or
            **dashpotBehavior** = ON must be specified.
        dashpotBehavior
            A Boolean specifying whether to apply dashpot behavior to the selected points. The
            default value is OFF.At least one of the arguments **springBehavior** = ON or
            **dashpotBehavior** = ON must be specified.
        springStiffness
            A Float specifying the force per relative displacement for the spring. The default value
            is 0.0.
        dashpotCoefficient
            A Float specifying the force per relative velocity for the dashpot. The default value is
            0.0.
        """
        ...
