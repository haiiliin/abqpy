from typing import Union, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Constraint import Constraint
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import Boolean, OFF, ON, SymbolicConstant, UNIFORM


@abaqus_class_doc
class Coupling(Constraint):
    """The Coupling object defines a constraint between a group of coupling nodes located on a
    region and a reference point.
    The Coupling object is derived from the ConstrainedSketchConstraint object.

    .. note:: 
        This object can be accessed by::

            import interaction
            mdb.models[name].constraints[name]

        The corresponding analysis keywords are:

        - COUPLING
    """

    #: A Boolean specifying whether the constraint is suppressed or not. The default value is
    #: OFF.
    suppressed: Boolean = OFF

    #: A String specifying the constraint repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the surface on which the coupling nodes are located.
    surface: Region

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the constraint control point.
    controlPoint: Region

    #: The SymbolicConstant WHOLE_SURFACE or a Float specifying the influence radius.
    influenceRadius: Union[SymbolicConstant, float]

    #: A SymbolicConstant specifying the coupling constraint type. Possible values are
    #: KINEMATIC, DISTRIBUTING, and STRUCTURAL.
    couplingType: SymbolicConstant

    #: A Boolean specifying if the control point will be adjusted (moved) to the surface. The
    #: point will be adjusted in the direction normal to the specified surface. The default
    #: value is OFF.
    adjust: Boolean = OFF

    #: None or a DatumCsys object specifying the initial orientation of the local coordinate
    #: system for the coupling's degrees of freedom. If **localCsys** = None, the coupling is
    #: defined in the global coordinate system. The default value is None.
    localCsys: Optional[str] = None

    #: A Boolean specifying if the displacement component in the 1-direction is constrained to
    #: the reference node for a kinematic coupling constraint. The default value is ON.The **u1**
    #: argument applies only when **couplingType** = KINEMATIC.
    u1: Boolean = ON

    #: A Boolean specifying if the displacement component in the 2-direction is constrained to
    #: the reference node for a kinematic coupling constraint. The default value is ON.The **u2**
    #: argument applies only when **couplingType** = KINEMATIC.
    u2: Boolean = ON

    #: A Boolean specifying if the displacement component in the 3-direction is constrained to
    #: the reference node for a kinematic coupling constraint. The default value is ON.The **u3**
    #: argument applies only when **couplingType** = KINEMATIC.
    u3: Boolean = ON

    #: A Boolean specifying if the rotational displacement component about the 1-direction is
    #: constrained to the reference node for a kinematic coupling constraint. The default value
    #: is ON.The **ur1** argument applies only when **couplingType** = KINEMATIC.
    ur1: Boolean = ON

    #: A Boolean specifying if the rotational displacement component about the 2-direction is
    #: constrained to the reference node for a kinematic coupling constraint. The default value
    #: is ON.The **ur2** argument applies only when **couplingType** = KINEMATIC.
    ur2: Boolean = ON

    #: A Boolean specifying if the rotational displacement component about the 3-direction is
    #: constrained to the reference node for a kinematic coupling constraint. The default value
    #: is ON.The **ur3** argument applies only when **couplingType** = KINEMATIC.
    ur3: Boolean = ON

    #: A SymbolicConstant specifying an optional weighting method used for calculating the
    #: distributing weight factors. Possible values are UNIFORM, LINEAR, QUADRATIC, and CUBIC.
    #: The default value is UNIFORM.The **weightingMethod** argument applies only when
    #: **couplingType** = DISTRIBUTING.
    weightingMethod: SymbolicConstant = UNIFORM

    #: A Float specifying the value of the thermal expansion coefficient. The default value is 0.0.
    #: The alpha argument applies only when couplingType=KINEMATIC.
    #:
    #: .. versionadded:: 2022
    #:     The `alpha` attribute was added.
    alpha: float = 0.0

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        surface: Region,
        controlPoint: Region,
        influenceRadius: Union[SymbolicConstant, float],
        couplingType: SymbolicConstant,
        adjust: Boolean = OFF,
        localCsys: Optional[str] = None,
        u1: Boolean = ON,
        u2: Boolean = ON,
        u3: Boolean = ON,
        ur1: Boolean = ON,
        ur2: Boolean = ON,
        ur3: Boolean = ON,
        weightingMethod: SymbolicConstant = UNIFORM,
        alpha: float = 0.0,
    ):
        """This method creates a Coupling object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].Coupling

        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        surface
            A :py:class:`~abaqus.Region.Region.Region` object specifying the surface on which the coupling nodes are located.
        controlPoint
            A :py:class:`~abaqus.Region.Region.Region` object specifying the constraint control point.
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
            system for the coupling's degrees of freedom. If **localCsys** = None, the coupling is
            defined in the global coordinate system. The default value is None.
        u1
            A Boolean specifying if the displacement component in the 1-direction is constrained to
            the reference node for a kinematic coupling constraint. The default value is ON.The **u1**
            argument applies only when **couplingType** = KINEMATIC.
        u2
            A Boolean specifying if the displacement component in the 2-direction is constrained to
            the reference node for a kinematic coupling constraint. The default value is ON.The **u2**
            argument applies only when **couplingType** = KINEMATIC.
        u3
            A Boolean specifying if the displacement component in the 3-direction is constrained to
            the reference node for a kinematic coupling constraint. The default value is ON.The **u3**
            argument applies only when **couplingType** = KINEMATIC.
        ur1
            A Boolean specifying if the rotational displacement component about the 1-direction is
            constrained to the reference node for a kinematic coupling constraint. The default value
            is ON.The **ur1** argument applies only when **couplingType** = KINEMATIC.
        ur2
            A Boolean specifying if the rotational displacement component about the 2-direction is
            constrained to the reference node for a kinematic coupling constraint. The default value
            is ON.The **ur2** argument applies only when **couplingType** = KINEMATIC.
        ur3
            A Boolean specifying if the rotational displacement component about the 3-direction is
            constrained to the reference node for a kinematic coupling constraint. The default value
            is ON.The **ur3** argument applies only when **couplingType** = KINEMATIC.
        weightingMethod
            A SymbolicConstant specifying an optional weighting method used for calculating the
            distributing weight factors. Possible values are UNIFORM, LINEAR, QUADRATIC, and CUBIC.
            The default value is UNIFORM.The **weightingMethod** argument applies only when
            **couplingType** = DISTRIBUTING.
        alpha
            A Float specifying the value of the thermal expansion coefficient. The default value is 0.0.
            The alpha argument applies only when couplingType=KINEMATIC.

            .. versionadded:: 2022
                The `alpha` argument was added.

        Returns
        -------
        Coupling
            A :py:class:`~abaqus.Constraint.Coupling.Coupling` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        adjust: Boolean = OFF,
        localCsys: Optional[str] = None,
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
            system for the coupling's degrees of freedom. If **localCsys** = None, the coupling is
            defined in the global coordinate system. The default value is None.
        u1
            A Boolean specifying if the displacement component in the 1-direction is constrained to
            the reference node for a kinematic coupling constraint. The default value is ON.The **u1**
            argument applies only when **couplingType** = KINEMATIC.
        u2
            A Boolean specifying if the displacement component in the 2-direction is constrained to
            the reference node for a kinematic coupling constraint. The default value is ON.The **u2**
            argument applies only when **couplingType** = KINEMATIC.
        u3
            A Boolean specifying if the displacement component in the 3-direction is constrained to
            the reference node for a kinematic coupling constraint. The default value is ON.The **u3**
            argument applies only when **couplingType** = KINEMATIC.
        ur1
            A Boolean specifying if the rotational displacement component about the 1-direction is
            constrained to the reference node for a kinematic coupling constraint. The default value
            is ON.The **ur1** argument applies only when **couplingType** = KINEMATIC.
        ur2
            A Boolean specifying if the rotational displacement component about the 2-direction is
            constrained to the reference node for a kinematic coupling constraint. The default value
            is ON.The **ur2** argument applies only when **couplingType** = KINEMATIC.
        ur3
            A Boolean specifying if the rotational displacement component about the 3-direction is
            constrained to the reference node for a kinematic coupling constraint. The default value
            is ON.The **ur3** argument applies only when **couplingType** = KINEMATIC.
        weightingMethod
            A SymbolicConstant specifying an optional weighting method used for calculating the
            distributing weight factors. Possible values are UNIFORM, LINEAR, QUADRATIC, and CUBIC.
            The default value is UNIFORM.The **weightingMethod** argument applies only when
            **couplingType** = DISTRIBUTING.
        """
        ...
