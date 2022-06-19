import typing

from abaqusConstants import *
from .Constraint import Constraint
from ..Region.Region import Region


class Coupling(Constraint):
    """The Coupling object defines a constraint between a group of coupling nodes located on a
    region and a reference point.
    The Coupling object is derived from the ConstrainedSketchConstraint object.

    Attributes
    ----------
    suppressed: Boolean
        A Boolean specifying whether the constraint is suppressed or not. The default value is
        OFF.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].constraints[name]

    The corresponding analysis keywords are:

    - COUPLING

    """

    # A Boolean specifying whether the constraint is suppressed or not. The default value is
    # OFF.
    suppressed: Boolean = OFF

    def __init__(
        self,
        name: str,
        surface: Region,
        controlPoint: Region,
        influenceRadius: typing.Union[SymbolicConstant, float],
        couplingType: SymbolicConstant,
        adjust: Boolean = OFF,
        localCsys: str = None,
        u1: Boolean = ON,
        u2: Boolean = ON,
        u3: Boolean = ON,
        ur1: Boolean = ON,
        ur2: Boolean = ON,
        ur3: Boolean = ON,
        weightingMethod: SymbolicConstant = UNIFORM,
    ):
        """This method creates a Coupling object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Coupling

        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        surface
            A Region object specifying the surface on which the coupling nodes are located.
        controlPoint
            A Region object specifying the constraint control point.
        influenceRadius
            The SymbolicConstant WHOLE_SURFACE or a Float specifying the influence radius.
        couplingType
            A SymbolicConstant specifying the coupling constraint type. Possible values are
            KINEMATIC, DISTRIBUTING, and STRUCTURAL.
        adjust
            A Boolean specifying if the control point will be adjusted (moved) to the surface. The
            point will be adjusted in the direction normal to the specified surface. The default
            value is OFF.
        localCsys
            None or a DatumCsys object specifying the initial orientation of the local coordinate
            system for the coupling's degrees of freedom. If **localCsys**=None, the coupling is
            defined in the global coordinate system. The default value is None.
        u1
            A Boolean specifying if the displacement component in the 1-direction is constrained to
            the reference node for a kinematic coupling constraint. The default value is ON.The **u1**
            argument applies only when **couplingType**=KINEMATIC.
        u2
            A Boolean specifying if the displacement component in the 2-direction is constrained to
            the reference node for a kinematic coupling constraint. The default value is ON.The **u2**
            argument applies only when **couplingType**=KINEMATIC.
        u3
            A Boolean specifying if the displacement component in the 3-direction is constrained to
            the reference node for a kinematic coupling constraint. The default value is ON.The **u3**
            argument applies only when **couplingType**=KINEMATIC.
        ur1
            A Boolean specifying if the rotational displacement component about the 1-direction is
            constrained to the reference node for a kinematic coupling constraint. The default value
            is ON.The **ur1** argument applies only when **couplingType**=KINEMATIC.
        ur2
            A Boolean specifying if the rotational displacement component about the 2-direction is
            constrained to the reference node for a kinematic coupling constraint. The default value
            is ON.The **ur2** argument applies only when **couplingType**=KINEMATIC.
        ur3
            A Boolean specifying if the rotational displacement component about the 3-direction is
            constrained to the reference node for a kinematic coupling constraint. The default value
            is ON.The **ur3** argument applies only when **couplingType**=KINEMATIC.
        weightingMethod
            A SymbolicConstant specifying an optional weighting method used for calculating the
            distributing weight factors. Possible values are UNIFORM, LINEAR, QUADRATIC, and CUBIC.
            The default value is UNIFORM.The **weightingMethod** argument applies only when
            **couplingType**=DISTRIBUTING.

        Returns
        -------
            A Coupling object.
        """
        super().__init__()
        pass

    def setValues(
        self,
        adjust: Boolean = OFF,
        localCsys: str = None,
        u1: Boolean = ON,
        u2: Boolean = ON,
        u3: Boolean = ON,
        ur1: Boolean = ON,
        ur2: Boolean = ON,
        ur3: Boolean = ON,
        weightingMethod: SymbolicConstant = UNIFORM,
    ):
        """This method modifies the Coupling object.

        Parameters
        ----------
        adjust
            A Boolean specifying if the control point will be adjusted (moved) to the surface. The
            point will be adjusted in the direction normal to the specified surface. The default
            value is OFF.
        localCsys
            None or a DatumCsys object specifying the initial orientation of the local coordinate
            system for the coupling's degrees of freedom. If **localCsys**=None, the coupling is
            defined in the global coordinate system. The default value is None.
        u1
            A Boolean specifying if the displacement component in the 1-direction is constrained to
            the reference node for a kinematic coupling constraint. The default value is ON.The **u1**
            argument applies only when **couplingType**=KINEMATIC.
        u2
            A Boolean specifying if the displacement component in the 2-direction is constrained to
            the reference node for a kinematic coupling constraint. The default value is ON.The **u2**
            argument applies only when **couplingType**=KINEMATIC.
        u3
            A Boolean specifying if the displacement component in the 3-direction is constrained to
            the reference node for a kinematic coupling constraint. The default value is ON.The **u3**
            argument applies only when **couplingType**=KINEMATIC.
        ur1
            A Boolean specifying if the rotational displacement component about the 1-direction is
            constrained to the reference node for a kinematic coupling constraint. The default value
            is ON.The **ur1** argument applies only when **couplingType**=KINEMATIC.
        ur2
            A Boolean specifying if the rotational displacement component about the 2-direction is
            constrained to the reference node for a kinematic coupling constraint. The default value
            is ON.The **ur2** argument applies only when **couplingType**=KINEMATIC.
        ur3
            A Boolean specifying if the rotational displacement component about the 3-direction is
            constrained to the reference node for a kinematic coupling constraint. The default value
            is ON.The **ur3** argument applies only when **couplingType**=KINEMATIC.
        weightingMethod
            A SymbolicConstant specifying an optional weighting method used for calculating the
            distributing weight factors. Possible values are UNIFORM, LINEAR, QUADRATIC, and CUBIC.
            The default value is UNIFORM.The **weightingMethod** argument applies only when
            **couplingType**=DISTRIBUTING.
        """
        pass
