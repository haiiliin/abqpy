from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Constraint import Constraint
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class MultipointConstraint(Constraint):
    """The MultipointConstraint object defines a constraint between a group of
    MultipointConstraint nodes located on a region and a reference point.
    The MultipointConstraint object is derived from the ConstrainedSketchConstraint object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].constraints[name]

        The corresponding analysis keywords are:

        - MPC
    """

    #: A Boolean specifying whether the constraint is suppressed or not. The default value is
    #: OFF.
    suppressed: Boolean = OFF

    #: A String specifying the constraint repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the surface on which the MultipointConstraint nodes are
    #: located.
    surface: Region

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the constraint control point.
    controlPoint: Region

    #: A SymbolicConstant specifying the MPC type of the constraint. Possible values are
    #: BEAM_MPC, ELBOW_MPC, PIN_MPC, LINK_MPC, TIE_MPC, and USER_MPC.
    mpcType: SymbolicConstant

    #: None or a DatumCsys object specifying the initial orientation of the local coordinate
    #: system for the MultipointConstraint's degrees of freedom. If **localCsys** = None, the
    #: MultipointConstraint is defined in the global coordinate system. The default value is
    #: None.
    csys: Optional[str] = None

    #: An Int specifying to differentiate between different constraint types in a user-defined
    #: MultipointConstraint. The default value is 0.The **userType** argument applies only when
    #: **mpcType** = USER_MPC.
    userType: int = 0

    #: A SymbolicConstant specifying the mode of the constraint when it is user-defined.
    #: Possible values are DOF_MODE_MPC and NODE_MODE_MPC. The default value is
    #: DOF_MODE_MPC.The **userMode** argument applies only when **mpcType** = USER_MPC.
    userMode: SymbolicConstant = DOF_MODE_MPC

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        surface: Region,
        controlPoint: Region,
        mpcType: SymbolicConstant,
        csys: Optional[str] = None,
        userType: int = 0,
        userMode: SymbolicConstant = DOF_MODE_MPC,
    ):
        """This method creates a MultipointConstraint object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].MultipointConstraint

        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        surface
            A :py:class:`~abaqus.Region.Region.Region` object specifying the surface on which the MultipointConstraint nodes are
            located.
        controlPoint
            A :py:class:`~abaqus.Region.Region.Region` object specifying the constraint control point.
        mpcType
            A SymbolicConstant specifying the MPC type of the constraint. Possible values are
            BEAM_MPC, ELBOW_MPC, PIN_MPC, LINK_MPC, TIE_MPC, and USER_MPC.
        csys
            None or a DatumCsys object specifying the initial orientation of the local coordinate
            system for the MultipointConstraint's degrees of freedom. If **localCsys** = None, the
            MultipointConstraint is defined in the global coordinate system. The default value is
            None.
        userType
            An Int specifying to differentiate between different constraint types in a user-defined
            MultipointConstraint. The default value is 0.The **userType** argument applies only when
            **mpcType** = USER_MPC.
        userMode
            A SymbolicConstant specifying the mode of the constraint when it is user-defined.
            Possible values are DOF_MODE_MPC and NODE_MODE_MPC. The default value is
            DOF_MODE_MPC.The **userMode** argument applies only when **mpcType** = USER_MPC.

        Returns
        -------
        MultipointConstraint
            A :py:class:`~abaqus.Constraint.MultipointConstraint.MultipointConstraint` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        csys: Optional[str] = None,
        userType: int = 0,
        userMode: SymbolicConstant = DOF_MODE_MPC,
    ):
        """This method modifies the MultipointConstraint object.

        Parameters
        ----------
        csys
            None or a DatumCsys object specifying the initial orientation of the local coordinate
            system for the MultipointConstraint's degrees of freedom. If **localCsys** = None, the
            MultipointConstraint is defined in the global coordinate system. The default value is
            None.
        userType
            An Int specifying to differentiate between different constraint types in a user-defined
            MultipointConstraint. The default value is 0.The **userType** argument applies only when
            **mpcType** = USER_MPC.
        userMode
            A SymbolicConstant specifying the mode of the constraint when it is user-defined.
            Possible values are DOF_MODE_MPC and NODE_MODE_MPC. The default value is
            DOF_MODE_MPC.The **userMode** argument applies only when **mpcType** = USER_MPC.
        """
        ...
