from typing import Union, Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .AdjustPoints import AdjustPoints
from .Coupling import Coupling
from .DisplayBody import DisplayBody
from .EmbeddedRegion import EmbeddedRegion
from .Equation import Equation
from .MultipointConstraint import MultipointConstraint
from .RigidBody import RigidBody
from .ShellSolidCoupling import ShellSolidCoupling
from .Tie import Tie
from ..Assembly.PartInstance import PartInstance
from ..BasicGeometry.ModelDotArray import ModelDotArray
from ..Model.ModelBase import ModelBase
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import (BOTH, Boolean, COMPUTED, DEFAULT, DOF_MODE_MPC, OFF,
                                              ON, SOLVER_DEFAULT, UNIFORM)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class ConstraintModel(ModelBase):
    """Abaqus creates a Model object named `Model-1` when a session is started.

    .. note:: 
        This object can be accessed by::

            mdb.models[name]
    """

    @abaqus_method_doc
    def AdjustPoints(
        self, name: str, surface: Region, controlPoints: Region
    ) -> AdjustPoints:
        """This method creates an AdjustPoints object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].AdjustPoints

        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        surface
            A :py:class:`~abaqus.Region.Region.Region` object specifying the surface to which the **controlPoints** are adjusted.
        controlPoints
            A :py:class:`~abaqus.Region.Region.Region` object specifying the constraint control points.

        Returns
        -------
        AdjustPoints
            An :py:class:`~abaqus.Constraint.AdjustPoints.AdjustPoints` object.
        """
        self.constraints[name] = constraint = AdjustPoints(name, surface, controlPoints)
        return constraint

    @abaqus_method_doc
    def Coupling(
        self,
        name: str,
        surface: Region,
        controlPoint: Region,
        influenceRadius: Union[Literal[C.WHOLE_SURFACE], float],
        couplingType: Literal[C.STRUCTURAL, C.DISTRIBUTING, C.KINEMATIC],
        adjust: Boolean = OFF,
        localCsys: Optional[str] = None,
        u1: Boolean = ON,
        u2: Boolean = ON,
        u3: Boolean = ON,
        ur1: Boolean = ON,
        ur2: Boolean = ON,
        ur3: Boolean = ON,
        weightingMethod: Literal[C.QUADRATIC, C.DISTRIBUTING, C.UNIFORM, C.LINEAR, C.CUBIC] = UNIFORM,
    ) -> Coupling:
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

        Returns
        -------
        Coupling
            A :py:class:`~abaqus.Constraint.Coupling.Coupling` object.
        """
        self.constraints[name] = constraint = Coupling(
            name,
            surface,
            controlPoint,
            influenceRadius,
            couplingType,
            adjust,
            localCsys,
            u1,
            u2,
            u3,
            ur1,
            ur2,
            ur3,
            weightingMethod,
        )
        return constraint

    @abaqus_method_doc
    def DisplayBody(
        self, name: str, instance: PartInstance, controlPoints: ModelDotArray
    ) -> DisplayBody:
        """This method creates a DisplayBody object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].DisplayBody

        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        instance
            A :py:class:`~abaqus.Assembly.PartInstance.PartInstance` object specifying the part instance that is to be used for display only.
        controlPoints
            A :py:class:`~abaqus.BasicGeometry.ModelDotArray.ModelDotArray` object specifying the motion of the PartInstance. The control points may
            be ConstrainedSketchVertex, ReferencePoint, or MeshNode objects. Their motion will control the motion of
            the PartInstance. If this argument is set to an empty sequence, the PartInstance will
            remain fixed in space during the analysis. The sequence can have either one object or
            three objects.

        Returns
        -------
        DisplayBody
            A :py:class:`~abaqus.Constraint.DisplayBody.DisplayBody` object.
        """
        self.constraints[name] = constraint = DisplayBody(name, instance, controlPoints)
        return constraint

    @abaqus_method_doc
    def EmbeddedRegion(
        self,
        name: str,
        embeddedRegion: Region,
        hostRegion: Region,
        weightFactorTolerance: Optional[float] = None,
        toleranceMethod: Literal[C.FRACTIONAL, C.BOTH, C.ABSOLUTE] = BOTH,
        absoluteTolerance: float = 0,
        fractionalTolerance: float = 0,
    ) -> EmbeddedRegion:
        """This method creates a EmbeddedRegion object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].EmbeddedRegion

        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        embeddedRegion
            A :py:class:`~abaqus.Region.Region.Region` object specifying the body region to be embedded.
        hostRegion
            A :py:class:`~abaqus.Region.Region.Region` object specifying the host region. A value of None indicates that the host
            region is the whole model.
        weightFactorTolerance
            A Float specifying a small value below which the weighting factors will be zeroed out.
            The default value is 10-6.
        toleranceMethod
            A SymbolicConstant specifying the method used to determine the embedded element
            tolerance. Possible values are ABSOLUTE, FRACTIONAL, and BOTH. The default value is
            BOTH.
        absoluteTolerance
            A Float specifying the absolute value by which a node on the embedded region may lie
            outside the host region. If **absoluteTolerance** = 0.0, the **fractionalTolerance** value
            will be used. The default value is 0.0.This argument applies only when
            **toleranceMethod** = ABSOLUTE or BOTH.
        fractionalTolerance
            A Float specifying the fractional value by which a node on the embedded region may lie
            outside the host region. The fractional value is based on the average element size
            within the host region. The default value is 0.05.If both tolerance arguments are
            specified, the smaller value will be used.This argument applies only when
            **toleranceMethod** = FRACTIONAL or BOTH.

        Returns
        -------
        EmbeddedRegion
            An :py:class:`~abaqus.Constraint.EmbeddedRegion.EmbeddedRegion` object.
        """
        self.constraints[name] = constraint = EmbeddedRegion(
            name,
            embeddedRegion,
            hostRegion,
            weightFactorTolerance,
            toleranceMethod,
            absoluteTolerance,
            fractionalTolerance,
        )
        return constraint

    @abaqus_method_doc
    def Equation(self, name: str, terms: tuple) -> Equation:
        """This method creates an Equation object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].Equation

        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        terms
            A sequence of (Float, String, Int, Int) sequences specifying a coefficient, Set name,
            degree of freedom, and coordinate system ID. The coordinate system ID is optional.

        Returns
        -------
        Equation
            An :py:class:`~abaqus.Constraint.Equation.Equation` object.

        Raises
        ------
        If **terms** does not contain more than one entry, Equation must have two or more terms.
        """
        self.constraints[name] = constraint = Equation(name, terms)
        return constraint

    @abaqus_method_doc
    def MultipointConstraint(
        self,
        name: str,
        surface: Region,
        controlPoint: Region,
        mpcType: Literal[C.USER_MPC, C.BEAM_MPC, C.ELBOW_MPC, C.TIE_MPC, C.MPC, C.PIN_MPC, C.LINK_MPC],
        csys: Optional[str] = None,
        userType: int = 0,
        userMode: Literal[C.DOF_MODE_MPC, C.USER_MPC, C.NODE_MODE_MPC] = DOF_MODE_MPC,
    ) -> MultipointConstraint:
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
        self.constraints[name] = constraint = MultipointConstraint(
            name, surface, controlPoint, mpcType, csys, userType, userMode
        )
        return constraint

    @abaqus_method_doc
    def RigidBody(
        self,
        name: str,
        refPointRegion: Region,
        bodyRegion: Optional[str] = None,
        tieRegion: Optional[str] = None,
        pinRegion: Optional[str] = None,
        surfaceRegion: Optional[str] = None,
        refPointAtCOM: Boolean = OFF,
        isothermal: Boolean = OFF,
    ) -> RigidBody:
        """This method creates a RigidBody object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].RigidBody

        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        refPointRegion
            A :py:class:`~abaqus.Region.Region.Region` object specifying the reference point.
        bodyRegion
            None or a Region object specifying the elements constrained to the movement of the
            reference point. The default value is None.
        tieRegion
            None or a Region object specifying the nodes tied to the movement of the reference
            point. The default value is None.
        pinRegion
            None or a Region object specifying the nodes pinned to the movement of the reference
            point. The default value is None.
        surfaceRegion
            None or a Region object specifying the analytic surface constrained to the movement of
            the reference point. The default value is None.
        refPointAtCOM
            A Boolean specifying whether the analysis product should recompute the reference point
            position to be at the center of mass. The default value is OFF.
        isothermal
            A Boolean specifying whether the temperature degree of freedom should be constrained.
            The default value is OFF.

        Returns
        -------
        RigidBody
            A :py:class:`~abaqus.Constraint.RigidBody.RigidBody` object.
        """
        self.constraints[name] = constraint = RigidBody(
            name,
            refPointRegion,
            bodyRegion,
            tieRegion,
            pinRegion,
            surfaceRegion,
            refPointAtCOM,
            isothermal,
        )
        return constraint

    @abaqus_method_doc
    def ShellSolidCoupling(
        self,
        name: str,
        shellEdge: Region,
        solidFace: Region,
        positionToleranceMethod: Literal[C.COMPUTED, C.SPECIFIED] = COMPUTED,
        positionTolerance: float = 0,
        influenceDistanceMethod: Literal[C.DEFAULT, C.SPECIFIED] = DEFAULT,
        influenceDistance: float = 0,
    ) -> ShellSolidCoupling:
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
        self.constraints[name] = constraint = ShellSolidCoupling(
            name,
            shellEdge,
            solidFace,
            positionToleranceMethod,
            positionTolerance,
            influenceDistanceMethod,
            influenceDistance,
        )
        return constraint

    @abaqus_method_doc
    def Tie(
        self,
        name: str,
        master: Region,
        slave: Region,
        adjust: Boolean = ON,
        positionToleranceMethod: Literal[C.COMPUTED, C.SPECIFIED] = COMPUTED,
        positionTolerance: float = 0,
        tieRotations: Boolean = ON,
        constraintRatioMethod: Literal[C.DEFAULT, C.SPECIFIED] = DEFAULT,
        constraintRatio: float = 0,
        constraintEnforcement: Literal[C.NODE_TO_SURFACE, C.SOLVER_DEFAULT, C.SURFACE_TO_SURFACE] = SOLVER_DEFAULT,
        thickness: Boolean = ON,
    ) -> Tie:
        """This method creates a Tie object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].Tie

        Parameters
        ----------
        name
            A String specifying the constraint repository key.
        master
            A :py:class:`~abaqus.Region.Region.Region` object specifying the name of the master surface.
        slave
            A :py:class:`~abaqus.Region.Region.Region` object specifying the name of the slave surface.
        adjust
            A Boolean specifying whether initial positions of tied slave nodes are adjusted to
            lie on the master surface. The default value is ON.
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
            A Float specifying the fractional distance between the master reference surface and the
            slave node at which the translational constraint should act. The **constraintRatio**
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
        self.constraints[name] = constraint = Tie(
            name,
            master,
            slave,
            adjust,
            positionToleranceMethod,
            positionTolerance,
            tieRotations,
            constraintRatioMethod,
            constraintRatio,
            constraintEnforcement,
            thickness,
        )
        return constraint
