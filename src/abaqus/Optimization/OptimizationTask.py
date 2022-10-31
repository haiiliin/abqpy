from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .BeadFixedRegion import BeadFixedRegion
from .BeadGrowth import BeadGrowth
from .BeadPenetrationCheck import BeadPenetrationCheck
from .BeadPlanarSymmetry import BeadPlanarSymmetry
from .BeadPointSymmetry import BeadPointSymmetry
from .BeadRotationalSymmetry import BeadRotationalSymmetry
from .DesignDirection import DesignDirection
from .DrillControl import DrillControl
from .FixedRegion import FixedRegion
from .FrozenArea import FrozenArea
from .Growth import Growth
from .ObjectiveFunction import ObjectiveFunction
from .OptimizationConstraint import OptimizationConstraint
from .OptimizationObjectiveArray import OptimizationObjectiveArray
from .OptimizationTaskBase import OptimizationTaskBase
from .PenetrationCheck import PenetrationCheck
from .ShapeDemoldControl import ShapeDemoldControl
from .ShapeMemberSize import ShapeMemberSize
from .ShapePlanarSymmetry import ShapePlanarSymmetry
from .ShapePointSymmetry import ShapePointSymmetry
from .ShapeRotationalSymmetry import ShapeRotationalSymmetry
from .SingleTermDesignResponse import SingleTermDesignResponse
from .SizingClusterAreas import SizingClusterAreas
from .SizingCyclicSymmetry import SizingCyclicSymmetry
from .SizingFrozenArea import SizingFrozenArea
from .SizingMemberSize import SizingMemberSize
from .SizingPlanarSymmetry import SizingPlanarSymmetry
from .SizingPointSymmetry import SizingPointSymmetry
from .SizingRotationalSymmetry import SizingRotationalSymmetry
from .SlideRegionControl import SlideRegionControl
from .StampControl import StampControl
from .StepOptionArray import StepOptionArray
from .TopologyCyclicSymmetry import TopologyCyclicSymmetry
from .TopologyDemoldControl import TopologyDemoldControl
from .TopologyMemberSize import TopologyMemberSize
from .TopologyMillingControl import TopologyMillingControl
from .TopologyOverhangControl import TopologyOverhangControl
from .TopologyPlanarSymmetry import TopologyPlanarSymmetry
from .TopologyPointSymmetry import TopologyPointSymmetry
from .TopologyRotationalSymmetry import TopologyRotationalSymmetry
from .TurnControl import TurnControl
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import (
    ABSOLUTE_EQUAL,
    AUTO,
    AXIS_1,
    Boolean,
    DEMOLD_REGION,
    FREE_FORM,
    MAXIMUM,
    MILLING_REGION,
    MINIMIZE,
    MINIMUM,
    MODEL,
    OFF,
    ON,
    OVERHANG_REGION,
    SUM,
    TRUE,
    VECTOR,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class OptimizationTask(OptimizationTaskBase):
    @abaqus_method_doc
    def SingleTermDesignResponse(
        self,
        name: str,
        identifier: str,
        csys: Optional[int] = None,
        drivingRegion: Optional[str] = None,
        operation: Literal[C.SUM, C.MINIMUM, C.MAXIMUM] = SUM,
        region: Literal[C.MODEL] = MODEL,
        shellLayer: Literal[C.BOTTOM, C.TOP, C.MAXIMUM, C.MINIMUM, C.MIDDLE] = MAXIMUM,
        stepOperation: Literal[C.SUM, C.MINIMUM, C.MAXIMUM] = SUM,
        stepOptions: Optional[StepOptionArray] = None,
    ) -> SingleTermDesignResponse:
        """This method creates a SingleTermDesignResponse object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].SingleTermDesignResponse

        Parameters
        ----------
        name
            A String specifying the design response repository key.
        identifier
            A String specifying the name of the variable identifier.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        drivingRegion
            None or a sequence of Floats specifying the driving region used when **identifier** is an
            internal nodal variable. The default value is None.
        operation
            A SymbolicConstant specifying the operation used on values in the region. Possible
            values are MAXIMUM, MINIMUM, and SUM. The default value is SUM.
        region
            The SymbolicConstant MODEL or a Region object specifying the region of the design
            response variable. The default value is MODEL.
        shellLayer
            A SymbolicConstant specifying the location used for shell layer values. Possible values
            are BOTTOM, MAXIMUM, MIDDLE, MINIMUM, and TOP. The default value is MAXIMUM.
        stepOperation
            A SymbolicConstant specifying the operation used on values across steps and load cases.
            Possible values are MAXIMUM, MINIMUM, and SUM. The default value is SUM.
        stepOptions
            A StepOptionArray object.

        Returns
        -------
        SingleTermDesignResponse
            A SingleTermDesignResponse object.
        """
        self.designResponses[name] = singleTermDesignResponse = SingleTermDesignResponse(
            name,
            identifier,
            csys,
            drivingRegion,
            operation,
            region,
            shellLayer,
            stepOperation,
            stepOptions,
        )
        return singleTermDesignResponse

    @abaqus_method_doc
    def ObjectiveFunction(
        self,
        name: str,
        objectives: OptimizationObjectiveArray,
        target: Literal[C.MINIMIZE_MAXIMUM, C.MINIMIZE, C.MAXIMIZE] = MINIMIZE,
    ) -> ObjectiveFunction:
        """This method creates an ObjectiveFunction object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].ObjectiveFunction

        Parameters
        ----------
        name
            A String specifying the objective function repository key.
        objectives
            An OptimizationObjectiveArray object.
        target
            A SymbolicConstant specifying the target of the objective function. Possible values are
            MINIMIZE, MAXIMIZE, and MINIMIZE_MAXIMUM. The default value is MINIMIZE.

        Returns
        -------
        ObjectiveFunction
            An ObjectiveFunction object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.objectiveFunctions[name] = objectiveFunction = ObjectiveFunction(name, objectives, target)
        return objectiveFunction

    @abaqus_method_doc
    def OptimizationConstraint(
        self,
        name: str,
        designResponse: str,
        restrictionValue: float,
        restrictionMethod: Literal[
            C.ABSOLUTE_LESS_THAN_EQUAL,
            C.RELATIVE_GREATER_THAN_EQUAL,
            C.ABSOLUTE_GREATER_THAN_EQUAL,
            C.RELATIVE_EQUAL,
            C.ABSOLUTE_EQUAL,
            C.RELATIVE_LESS_THAN_EQUAL,
        ] = ABSOLUTE_EQUAL,
    ) -> OptimizationConstraint:
        """This method creates an OptimizationConstraint object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].OptimizationConstraint

        Parameters
        ----------
        name
            A String specifying the optimization constraint repository key.
        designResponse
            A String specifying the name of the design response to constrain.
        restrictionValue
            A Float specifying the value to which the design response should be constrained.
        restrictionMethod
            A SymbolicConstant specifying the method used to constrain the design response. Possible
            values are ABSOLUTE_EQUAL, ABSOLUTE_GREATER_THAN_EQUAL, ABSOLUTE_LESS_THAN_EQUAL,
            RELATIVE_EQUAL, RELATIVE_GREATER_THAN_EQUAL, and RELATIVE_LESS_THAN_EQUAL. The default
            value is ABSOLUTE_EQUAL.

        Returns
        -------
        OptimizationConstraint
            An OptimizationConstraint object.

        Raises
        ------
        InvalidNameError
        RangeError
        """
        self.optimizationConstraints[name] = optimizationConstraint = OptimizationConstraint(
            name, designResponse, restrictionValue, restrictionMethod
        )
        return optimizationConstraint

    @abaqus_method_doc
    def BeadFixedRegion(
        self,
        name: str,
        region: Region,
        csys: Optional[int] = None,
        u1: Boolean = OFF,
        u2: Boolean = OFF,
        u3: Boolean = OFF,
    ) -> BeadFixedRegion:
        """This method creates a BeadFixedRegion object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].BeadFixedRegion

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        u1
            A Boolean specifying whether to fix the region in the 1-direction. The default value is
            OFF.
        u2
            A Boolean specifying whether to fix the region in the 2-direction. The default value is
            OFF.
        u3
            A Boolean specifying whether to fix the region in the 3-direction. The default value is
            OFF.

        Returns
        -------
        BeadFixedRegion
            A BeadFixedRegion object.
        """
        self.geometricRestrictions[name] = geometricRestriction = BeadFixedRegion(name, region, csys, u1, u2, u3)
        return geometricRestriction

    @abaqus_method_doc
    def BeadGrowth(self, name: str, region: Region, beadGrowth: float = 0, shrink: float = 0) -> BeadGrowth:
        """This method creates a BeadGrowth object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].BeadGrowth

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
        beadGrowth
            A Float specifying the maximum optimization displacement in the growth direction. Either
            **beadGrowth** or **shrink** or both must be specified. The default value is 0.0.
        shrink
            A Float specifying the maximum optimization displacement in the shrink direction. Either
            **beadGrowth** or **shrink** or both must be specified The default value is 0.0.

        Returns
        -------
        BeadGrowth
            A BeadGrowth object.
        """
        self.geometricRestrictions[name] = geometricRestriction = BeadGrowth(name, region, beadGrowth, shrink)
        return geometricRestriction

    @abaqus_method_doc
    def BeadPenetrationCheck(
        self, name: str, beadPenetrationCheckRegion: Region, region: Region
    ) -> BeadPenetrationCheck:
        """This method creates a BeadPenetrationCheck object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].BeadPenetrationCheck

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        beadPenetrationCheckRegion
            A Region object specifying the penetration check region.
        region
            A Region object specifying the region to which the geometric restriction is applied.

        Returns
        -------
        BeadPenetrationCheck
            A BeadPenetrationCheck object.
        """
        self.geometricRestrictions[name] = geometricRestriction = BeadPenetrationCheck(
            name, beadPenetrationCheckRegion, region
        )
        return geometricRestriction

    @abaqus_method_doc
    def BeadPlanarSymmetry(
        self,
        name: str,
        region: Region,
        axis: Literal[C.AXIS_1, C.AXIS_3, C.AXIS_2] = AXIS_1,
        csys: Optional[int] = None,
    ) -> BeadPlanarSymmetry:
        """This method creates a BeadPlanarSymmetry object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].BeadPlanarSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
        axis
            A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2,
            and AXIS_3. The default value is AXIS_1.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.

        Returns
        -------
        BeadPlanarSymmetry
            A BeadPlanarSymmetry object.
        """
        self.geometricRestrictions[name] = geometricRestriction = BeadPlanarSymmetry(name, region, axis, csys)
        return geometricRestriction

    @abaqus_method_doc
    def BeadPointSymmetry(self, name: str, region: Region, csys: Optional[int] = None) -> BeadPointSymmetry:
        """This method creates a BeadPointSymmetry object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].BeadPointSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
        csys
            None or a DatumCsys object specifying the position of the symmetry point defined as the
            origin of a local coordinate system. If **csys** = None, the global coordinate system is
            used. When this member is queried, it returns an Int. The default value is None.

        Returns
        -------
        BeadPointSymmetry
            A BeadPointSymmetry object.
        """
        self.geometricRestrictions[name] = geometricRestriction = BeadPointSymmetry(name, region, csys)
        return geometricRestriction

    @abaqus_method_doc
    def BeadRotationalSymmetry(
        self,
        name: str,
        angle: float,
        region: Region,
        axis: Literal[C.AXIS_1, C.AXIS_3, C.AXIS_2] = AXIS_1,
        csys: Optional[int] = None,
    ) -> BeadRotationalSymmetry:
        """This method creates a BeadRotationalSymmetry object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].BeadRotationalSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        angle
            A Float specifying the repeating segment size, an angle in degrees.
        region
            A Region object specifying the region to which the geometric restriction is applied.
        axis
            A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2,
            and AXIS_3. The default value is AXIS_1.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.

        Returns
        -------
        BeadRotationalSymmetry
            A BeadRotationalSymmetry object.
        """
        self.geometricRestrictions[name] = geometricRestriction = BeadRotationalSymmetry(
            name, angle, region, axis, csys
        )
        return geometricRestriction

    @abaqus_method_doc
    def DesignDirection(
        self,
        name: str,
        region: Region,
        csys: Optional[int] = None,
        mainPoint: Optional[str] = None,
        mainPointDetermination: Literal[C.SPECIFY, C.MINIMUM, C.MAXIMUM] = MAXIMUM,
        movementRestriction: Literal[C.MAGNITUDE, C.DIRECTION, C.VECTOR] = VECTOR,
        presumeFeasibleRegionAtStart: Boolean = ON,
        u1: Boolean = ON,
        u2: Boolean = ON,
        u3: Boolean = ON,
    ) -> DesignDirection:
        """This method creates a DesignDirection object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].DesignDirection

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        mainPoint
            None or a Region object specifying the main point used when **mainPointDetermination** is
            SPECIFY. The default value is None.

            .. versionchanged:: 2022
                The argument `masterPoint` was renamed to `mainPoint`.
        mainPointDetermination
            A SymbolicConstant specifying the rule for assigning point priority. Possible values are
            MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

            .. versionchanged:: 2022
                The argument `masterPointDetermination` was renamed to `mainPointDetermination`.
        movementRestriction
            A SymbolicConstant specifying whether movement in the region should follow only the
            direction of the **mainPoint**, only the magnitude, or both the magnitude of the
            **mainPoint** and the directions specified by **u1**, **u2** and **u3**. Possible values are
            DIRECTION, MAGNITUDE, and VECTOR. The default value is VECTOR.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        u1
            A Boolean specifying whether movement in the region should follow the **masterPoint** in
            the 1-direction. This is used when **movementRestriction** is VECTOR. The default value is
            ON.
        u2
            A Boolean specifying whether movement in the region should follow the **masterPoint** in
            the 2-direction. This is used when **movementRestriction** is VECTOR. The default value is
            ON.
        u3
            A Boolean specifying whether movement in the region should follow the **masterPoint** in
            the 3-direction. This is used when **movementRestriction** is VECTOR. The default value is
            ON.

        Returns
        -------
        DesignDirection
            A DesignDirection object.
        """
        self.geometricRestrictions[name] = geometricRestriction = DesignDirection(
            name,
            region,
            csys,
            mainPoint,
            mainPointDetermination,
            movementRestriction,
            presumeFeasibleRegionAtStart,
            u1,
            u2,
            u3,
        )
        return geometricRestriction

    @abaqus_method_doc
    def DrillControl(
        self,
        name: str,
        clientDirection: tuple,
        region: Region,
        csys: Optional[int] = None,
        drawAngle: float = 0,
        mainPoint: Optional[str] = None,
        mainPointDetermination: Literal[C.SPECIFY, C.MINIMUM, C.MAXIMUM] = MAXIMUM,
        presumeFeasibleRegionAtStart: Boolean = ON,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
        undercutTolerance: float = 0,
    ) -> DrillControl:
        """This method creates a DrillControl object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].DrillControl

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        clientDirection
            A VertexArray object of length 2 specifying the direction of the drill axis positioned
            at the **csys** origin. Instead of through a ConstrainedSketchVertex, each point may be specified through a
            tuple of coordinates.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        drawAngle
            A Float specifying the draw angle. The default value is 0.0.
        mainPoint
            None or a Region object specifying the main point used when **mainPointDetermination** is
            SPECIFY. The default value is None.

            .. versionchanged:: 2022
                The argument `masterPoint` was renamed to `mainPoint`.
        mainPointDetermination
            A SymbolicConstant specifying the rule for assigning point priority. Possible values are
            MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

            .. versionchanged:: 2022
                The argument `masterPointDetermination` was renamed to `mainPointDetermination`.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        tolerance1
            A Float specifying the geometric tolerance in the 1-direction. The default value is
            0.01.
        tolerance2
            A Float specifying the geometric tolerance in the 2-direction. The default value is
            0.01.
        tolerance3
            A Float specifying the geometric tolerance in the 3-direction. The default value is
            0.01.
        undercutTolerance
            A Float specifying the undercut tolerance. The default value is 0.0.

        Returns
        -------
        DrillControl
            A DrillControl object.
        """
        self.geometricRestrictions[name] = geometricRestriction = DrillControl(
            name,
            clientDirection,
            region,
            csys,
            drawAngle,
            mainPoint,
            mainPointDetermination,
            presumeFeasibleRegionAtStart,
            tolerance1,
            tolerance2,
            tolerance3,
            undercutTolerance,
        )
        return geometricRestriction

    @abaqus_method_doc
    def FixedRegion(
        self,
        name: str,
        region: Region,
        csys: Optional[int] = None,
        presumeFeasibleRegionAtStart: Boolean = ON,
        u1: Boolean = OFF,
        u2: Boolean = OFF,
        u3: Boolean = OFF,
    ) -> FixedRegion:
        """This method creates a FixedRegion object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].FixedRegion

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        u1
            A Boolean specifying whether to fix the region in the 1-direction. The default value is
            OFF.
        u2
            A Boolean specifying whether to fix the region in the 2-direction. The default value is
            OFF.
        u3
            A Boolean specifying whether to fix the region in the 3-direction. The default value is
            OFF.

        Returns
        -------
        FixedRegion
            A FixedRegion object.
        """
        self.geometricRestrictions[name] = geometricRestriction = FixedRegion(
            name, region, csys, presumeFeasibleRegionAtStart, u1, u2, u3
        )
        return geometricRestriction

    @abaqus_method_doc
    def FrozenArea(self, name: str, region: Region = Region()) -> FrozenArea:
        """This method creates a FrozenArea object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].FrozenArea

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.

        Returns
        -------
        FrozenArea
            A FrozenArea object.
        """
        self.geometricRestrictions[name] = geometricRestriction = FrozenArea(name, region)
        return geometricRestriction

    @abaqus_method_doc
    def Growth(
        self,
        name: str,
        region: Region,
        growth: float = 0,
        presumeFeasibleRegionAtStart: Boolean = ON,
        shrink: float = 0,
    ) -> Growth:
        """This method creates a Growth object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].Growth

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        growth
            A Float specifying the maximum optimization displacement in the growth direction. Either
            **growth** or **shrink** or both must be specified. The default value is 0.0.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        shrink
            A Float specifying the maximum optimization displacement in the shrink direction. Either
            **growth** or **shrink** or both must be specified The default value is 0.0.

        Returns
        -------
        Growth
            A Growth object.
        """
        self.geometricRestrictions[name] = geometricRestriction = Growth(
            name, region, growth, presumeFeasibleRegionAtStart, shrink
        )
        return geometricRestriction

    @abaqus_method_doc
    def PenetrationCheck(
        self,
        name: str,
        penetrationCheckRegion: Region,
        region: Region,
        presumeFeasibleRegionAtStart: Boolean = ON,
    ) -> PenetrationCheck:
        """This method creates a PenetrationCheck object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].PenetrationCheck

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        penetrationCheckRegion
            A Region object specifying the penetration check region.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.

        Returns
        -------
        PenetrationCheck
            A PenetrationCheck object.
        """
        self.geometricRestrictions[name] = geometricRestriction = PenetrationCheck(
            name, penetrationCheckRegion, region, presumeFeasibleRegionAtStart
        )
        return geometricRestriction

    @abaqus_method_doc
    def ShapeDemoldControl(
        self,
        name: str,
        pullDirection: tuple,
        region: Region,
        collisionCheckRegion: Literal[C.DEMOLD_REGION] = DEMOLD_REGION,
        csys: Optional[int] = None,
        drawAngle: float = 0,
        mainPointDetermination: Literal[C.MINIMUM, C.MAXIMUM] = MAXIMUM,
        presumeFeasibleRegionAtStart: Boolean = ON,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
        undercutTolerance: float = 0,
    ) -> ShapeDemoldControl:
        """This method creates a ShapeDemoldControl object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].ShapeDemoldControl

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        pullDirection
            A VertexArray object of length 2 specifying the demold pull direction. Instead of
            through a ConstrainedSketchVertex, each point might be specified through a tuple of coordinates.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        collisionCheckRegion
            The SymbolicConstant DEMOLD_REGION or a Region object specifying the collision check
            region. If the value is DEMOLD_REGION, then the value of **region** is used as both the
            demold region and the collision check region. The default value is DEMOLD_REGION.
        csys
            None or a DatumCsys object specifying the local coordinate system of the
            **pullDirection**. If **csys** = None, the global coordinate system is used. When this member
            is queried, it returns an Int indicating the identifier of the DatumCsys. The default
            value is None.
        drawAngle
            A Float specifying the draw angle. The default value is 0.0.
        mainPointDetermination
            A SymbolicConstant specifying the rule for assigning point priority. Possible values are
            MAXIMUM and MINIMUM. The default value is MAXIMUM.

            .. versionchanged:: 2022
                The argument `masterPointDetermination` was renamed to `mainPointDetermination`.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        tolerance1
            A Float specifying the geometric tolerance in the 1-direction. The default value is
            0.01.
        tolerance2
            A Float specifying the geometric tolerance in the 2-direction. The default value is
            0.01.
        tolerance3
            A Float specifying the geometric tolerance in the 3-direction. The default value is
            0.01.
        undercutTolerance
            A Float specifying the undercut tolerance. The default value is 0.0.

        Returns
        -------
        ShapeDemoldControl
            A ShapeDemoldControl object.
        """
        self.geometricRestrictions[name] = geometricRestriction = ShapeDemoldControl(
            name,
            pullDirection,
            region,
            collisionCheckRegion,
            csys,
            drawAngle,
            mainPointDetermination,
            presumeFeasibleRegionAtStart,
            tolerance1,
            tolerance2,
            tolerance3,
            undercutTolerance,
        )
        return geometricRestriction

    @abaqus_method_doc
    def ShapeMemberSize(
        self,
        name: str,
        region: Region,
        maxThickness: float = 0,
        minThickness: float = 0,
        sizeRestriction: Literal[C.MINIMUM, C.MAXIMUM] = MINIMUM,
        assignNodeGroupRegion: str = OFF,
        nodeGroupRegion: str = "",
    ) -> ShapeMemberSize:
        """This method creates a ShapeMemberSize object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].ShapeMemberSize

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        maxThickness
            A Float specifying the maximum thickness. The default value is 0.0.
        minThickness
            A Float specifying the minimum thickness. The default value is 0.0.
        sizeRestriction
            A SymbolicConstant specifying whether to restrict the minimum or maximum thickness.
            Possible values are MAXIMUM and MINIMUM. The default value is MINIMUM.
        assignNodeGroupRegion
            A bool specifying whether to use the node group region. The default value is OFF.

            .. versionadded:: 2022
                The `assignNodeGroupRegion` argument was added.
        nodeGroupRegion
            A Node Region object specifying the check node group.

            .. versionadded:: 2022
                The `nodeGroupRegion` argument was added.

        Returns
        -------
        ShapeMemberSize
            A ShapeMemberSize object.
        """
        self.geometricRestrictions[name] = geometricRestriction = ShapeMemberSize(
            name,
            region,
            maxThickness,
            minThickness,
            sizeRestriction,
            assignNodeGroupRegion,
            nodeGroupRegion,
        )
        return geometricRestriction

    @abaqus_method_doc
    def ShapePlanarSymmetry(
        self,
        name: str,
        clientDirection: tuple,
        region: Region,
        allowNonSymmetricMesh: Boolean = TRUE,
        csys: Optional[int] = None,
        mainPointDetermination: Literal[C.MINIMUM, C.MAXIMUM] = MAXIMUM,
        presumeFeasibleRegionAtStart: Boolean = ON,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
    ) -> ShapePlanarSymmetry:
        """This method creates a ShapePlanarSymmetry object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].ShapePlanarSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        clientDirection
            A VertexArray object of length 2 specifying the vector positioned at the **csys** origin
            that is normal to the symmetry plane. Instead of through a ConstrainedSketchVertex, each point may be
            specified through a tuple of coordinates.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        allowNonSymmetricMesh
            A Boolean specifying whether to allow a nonsymmetric mesh for this geometric
            restriction. The default value is TRUE.

            .. versionadded:: 2021
                The `alloowNonSymmetricMesh` argument was added.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        mainPointDetermination
            A SymbolicConstant specifying the rule for determining the main node. Possible values
            are MAXIMUM and MINIMUM. The default value is MAXIMUM.

            .. versionchanged:: 2022
                The argument `masterPointDetermination` was renamed to `mainPointDetermination`.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        tolerance1
            A Float specifying the geometric tolerance in the 1-direction. The default value is
            0.01.
        tolerance2
            A Float specifying the geometric tolerance in the 2-direction. The default value is
            0.01.
        tolerance3
            A Float specifying the geometric tolerance in the 3-direction. The default value is
            0.01.

        Returns
        -------
        ShapePlanarSymmetry
            A ShapePlanarSymmetry object.
        """
        self.geometricRestrictions[name] = geometricRestriction = ShapePlanarSymmetry(
            name,
            clientDirection,
            region,
            allowNonSymmetricMesh,
            csys,
            mainPointDetermination,
            presumeFeasibleRegionAtStart,
            tolerance1,
            tolerance2,
            tolerance3,
        )
        return geometricRestriction

    @abaqus_method_doc
    def ShapePointSymmetry(
        self,
        name: str,
        region: Region,
        csys: Optional[int] = None,
        mainPointDetermination: Literal[C.MINIMUM, C.MAXIMUM] = MAXIMUM,
        presumeFeasibleRegionAtStart: Boolean = ON,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
    ) -> ShapePointSymmetry:
        """This method creates a ShapePointSymmetry object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].ShapePointSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        csys
            None or a DatumCsys object specifying the symmetry point represented as the origin of a
            local coordinate system. If **csys** = None, the global coordinate system is used. When this
            member is queried, it returns an Int. The default value is None.
        mainPointDetermination
            A SymbolicConstant specifying the rule for determining the main node. Possible values
            are MAXIMUM and MINIMUM. The default value is MAXIMUM.

            .. versionchanged:: 2022
                The argument `masterPointDetermination` was renamed to `mainPointDetermination`.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        tolerance1
            A Float specifying the geometric tolerance in the 1-direction. The default value is
            0.01.
        tolerance2
            A Float specifying the geometric tolerance in the 2-direction. The default value is
            0.01.
        tolerance3
            A Float specifying the geometric tolerance in the 3-direction. The default value is
            0.01.

        Returns
        -------
        ShapePointSymmetry
            A ShapePointSymmetry object.
        """
        self.geometricRestrictions[name] = geometricRestriction = ShapePointSymmetry(
            name,
            region,
            csys,
            mainPointDetermination,
            presumeFeasibleRegionAtStart,
            tolerance1,
            tolerance2,
            tolerance3,
        )
        return geometricRestriction

    @abaqus_method_doc
    def ShapeRotationalSymmetry(
        self,
        name: str,
        clientDirection: tuple,
        region: Region,
        allowNonSymmetricMesh: Boolean = TRUE,
        angle: float = 0,
        csys: Optional[int] = None,
        mainPoint: Optional[str] = None,
        mainPointDetermination: Literal[C.SPECIFY, C.MINIMUM, C.MAXIMUM] = MAXIMUM,
        presumeFeasibleRegionAtStart: Boolean = ON,
        startPoint: Optional[float] = None,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
    ) -> ShapeRotationalSymmetry:
        """This method creates a ShapeRotationalSymmetry object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].ShapeRotationalSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        clientDirection
            A VertexArray object of length 2 specifying the vector positioned at the **csys** origin,
            used as the axis of symmetry. Instead of through a ConstrainedSketchVertex, each point might be specified
            through a tuple of coordinates.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        allowNonSymmetricMesh
            A Boolean specifying whether to allow a nonsymmetric mesh for this geometric
            restriction. The default value is TRUE.

            .. versionadded:: 2021
                The `alloowNonSymmetricMesh` argument was added.
        angle
            A Float specifying the segment size of the repeating pattern in degrees. If the **angle**
            value is 0, no repeating pattern is created. The default value is 0.0.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        mainPoint
            None or a Region object specifying the main point used when **mainPointDetermination** is
            SPECIFY. The default value is None.

            .. versionchanged:: 2022
                The argument `masterPoint` was renamed to `mainPoint`.
        mainPointDetermination
            A SymbolicConstant specifying the rule for determining the main node. Possible values
            are MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

            .. versionchanged:: 2022
                The argument `masterPointDetermination` was renamed to `mainPointDetermination`.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        startPoint
            A tuple of Floats representing the coordinates of a start point of the rotational
            symmetry.
        tolerance1
            A Float specifying the geometric tolerance in the 1-direction. The default value is
            0.01.
        tolerance2
            A Float specifying the geometric tolerance in the 2-direction. The default value is
            0.01.
        tolerance3
            A Float specifying the geometric tolerance in the 3-direction. The default value is
            0.01.

        Returns
        -------
        ShapeRotationalSymmetry
            A ShapeRotationalSymmetry object.
        """
        self.geometricRestrictions[name] = geometricRestriction = ShapeRotationalSymmetry(
            name,
            clientDirection,
            region,
            allowNonSymmetricMesh,
            angle,
            csys,
            mainPoint,
            mainPointDetermination,
            presumeFeasibleRegionAtStart,
            startPoint,
            tolerance1,
            tolerance2,
            tolerance3,
        )
        return geometricRestriction

    @abaqus_method_doc
    def SizingClusterAreas(self, name: str, regions: tuple) -> SizingClusterAreas:
        """This method creates a SizingClusterAreas object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].SizingClusterAreas

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        regions
            Tuple of Region objects specifying the regions to which the geometric restriction is
            applied.

        Returns
        -------
        SizingClusterAreas
            A SizingClusterAreas object.
        """
        self.geometricRestrictions[name] = geometricRestriction = SizingClusterAreas(name, regions)
        return geometricRestriction

    @abaqus_method_doc
    def SizingCyclicSymmetry(
        self,
        name: str,
        region: Region,
        translation: float,
        axis: Literal[C.AXIS_1, C.AXIS_3, C.AXIS_2] = AXIS_1,
        csys: Optional[int] = None,
        ignoreFrozenArea: Boolean = OFF,
    ) -> SizingCyclicSymmetry:
        """This method creates a SizingCyclicSymmetry object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].SizingCyclicSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
        translation
            A Float specifying the translation distance.
        axis
            A SymbolicConstant specifying the translation direction defined along an axis positioned
            at the **csys** origin. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value
            is AXIS_1.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns
        -------
        SizingCyclicSymmetry
            A SizingCyclicSymmetry object.
        """
        self.geometricRestrictions[name] = geometricRestriction = SizingCyclicSymmetry(
            name, region, translation, axis, csys, ignoreFrozenArea
        )
        return geometricRestriction

    @abaqus_method_doc
    def SizingFrozenArea(self, name: str, region: Region) -> SizingFrozenArea:
        """This method creates a SizingFrozenArea object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].SizingFrozenArea

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.

        Returns
        -------
        SizingFrozenArea
            A SizingFrozenArea object.
        """
        self.geometricRestrictions[name] = geometricRestriction = SizingFrozenArea(name, region)
        return geometricRestriction

    @abaqus_method_doc
    def SizingMemberSize(self, name: str, region: Region, minWidth: float) -> SizingMemberSize:
        """This method creates a SizingMemberSize object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].SizingMemberSize

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
        minWidth
            A Float specifying the min width.

        Returns
        -------

        Raises
        ------
        """
        self.geometricRestrictions[name] = geometricRestriction = SizingMemberSize(name, region, minWidth)
        return geometricRestriction

    @abaqus_method_doc
    def SizingPlanarSymmetry(
        self,
        name: str,
        region: Region,
        axis: Literal[C.AXIS_1, C.AXIS_3, C.AXIS_2] = AXIS_1,
        csys: Optional[int] = None,
        ignoreFrozenArea: Boolean = OFF,
    ) -> SizingPlanarSymmetry:
        """This method creates a SizingPlanarSymmetry object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].SizingPlanarSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
        axis
            A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2,
            and AXIS_3. The default value is AXIS_1.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns
        -------
        SizingPlanarSymmetry
            A SizingPlanarSymmetry object.
        """
        self.geometricRestrictions[name] = geometricRestriction = SizingPlanarSymmetry(
            name, region, axis, csys, ignoreFrozenArea
        )
        return geometricRestriction

    @abaqus_method_doc
    def SizingPointSymmetry(
        self,
        name: str,
        region: Region,
        csys: Optional[int] = None,
        ignoreFrozenArea: Boolean = OFF,
    ) -> SizingPointSymmetry:
        """This method creates a SizingPointSymmetry object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].SizingPointSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
        csys
            None or a DatumCsys object specifying the position of the symmetry point defined as the
            origin of a local coordinate system. If **csys** = None, the global coordinate system is
            used. When this member is queried, it returns an Int. The default value is None.
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns
        -------
        SizingPointSymmetry
            A SizingPointSymmetry object.
        """
        self.geometricRestrictions[name] = geometricRestriction = SizingPointSymmetry(
            name, region, csys, ignoreFrozenArea
        )
        return geometricRestriction

    @abaqus_method_doc
    def SizingRotationalSymmetry(
        self,
        name: str,
        angle: float,
        region: Region,
        axis: Literal[C.AXIS_1, C.AXIS_3, C.AXIS_2] = AXIS_1,
        csys: Optional[int] = None,
        ignoreFrozenArea: Boolean = OFF,
    ) -> SizingRotationalSymmetry:
        """This method creates a SizingRotationalSymmetry object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].SizingRotationalSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        angle
            A Float specifying the repeating segment size, an angle in degrees.
        region
            A Region object specifying the region to which the geometric restriction is applied.
        axis
            A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2,
            and AXIS_3. The default value is AXIS_1.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns
        -------
        SizingRotationalSymmetry
            A SizingRotationalSymmetry object.
        """
        self.geometricRestrictions[name] = geometricRestriction = SizingRotationalSymmetry(
            name, angle, region, axis, csys, ignoreFrozenArea
        )
        return geometricRestriction

    @abaqus_method_doc
    def SlideRegionControl(
        self,
        name: str,
        clientDirection: tuple,
        region: Region,
        approach: Literal[C.FREE_FORM, C.TURN] = FREE_FORM,
        csys: Optional[int] = None,
        freeFormRegion: Optional[str] = None,
        presumeFeasibleRegionAtStart: Boolean = ON,
        revolvedRegion: Optional[str] = None,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
    ) -> SlideRegionControl:
        """This method creates a SlideRegionControl object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].SlideRegionControl

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        clientDirection
            A VertexArray object of length 2 specifying the axis of revolution. Instead of through a
            ConstrainedSketchVertex, each point may be specified through a tuple of coordinates. This is used when
            **approach** is TURN.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        approach
            A SymbolicConstant specifying the restriction approach. The SymbolicConstant FREE_FORM
            indicates a free-form slide region, and the SymbolicConstant TURN indicates that the
            restriction should conserve a turnable surface. Possible values are FREE_FORM and TURN.
            The default value is FREE_FORM.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. This
            is used when **approach** is TURN. The default value is None.
        freeFormRegion
            None or a Region object specifying the free-form region. This is used when **approach** is
            FREE_FORM. The default value is None.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        revolvedRegion
            None or a Region object specifying the region to revolve into a slide region. This is
            used when **approach** is TURN. The default value is None.
        tolerance1
            A Float specifying the geometric tolerance in the 1-direction. This is used when
            **approach** is TURN. The default value is 0.01.
        tolerance2
            A Float specifying the geometric tolerance in the 2-direction. This is used when
            **approach** is TURN. The default value is 0.01.
        tolerance3
            A Float specifying the geometric tolerance in the 3-direction. This is used when
            **approach** is TURN. The default value is 0.01.

        Returns
        -------
        SlideRegionControl
            A SlideRegionControl object.
        """
        self.geometricRestrictions[name] = geometricRestriction = SlideRegionControl(
            name,
            clientDirection,
            region,
            approach,
            csys,
            freeFormRegion,
            presumeFeasibleRegionAtStart,
            revolvedRegion,
            tolerance1,
            tolerance2,
            tolerance3,
        )
        return geometricRestriction

    @abaqus_method_doc
    def StampControl(
        self,
        name: str,
        clientDirection: tuple,
        region: Region,
        csys: Optional[int] = None,
        drawAngle: float = 0,
        mainPoint: Optional[str] = None,
        mainPointDetermination: Literal[C.SPECIFY, C.MINIMUM, C.MAXIMUM] = MAXIMUM,
        presumeFeasibleRegionAtStart: Boolean = ON,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
        undercutTolerance: float = 0,
    ) -> StampControl:
        """This method creates a StampControl object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].StampControl

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        clientDirection
            A VertexArray object of length 2 specifying the stamping direction. Instead of through a
            ConstrainedSketchVertex, each point may be specified through a tuple of coordinates.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        drawAngle
            A Float specifying the draw angle. The default value is 0.0.
        mainPoint
            None or a Region object specifying the main point used when **mainPointDetermination** is
            SPECIFY. The default value is None.

            .. versionchanged:: 2022
                The argument `masterPoint` was renamed to `mainPoint`.
        mainPointDetermination
            A SymbolicConstant specifying the rule for assigning point priority. Possible values are
            MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

            .. versionchanged:: 2022
                The argument `masterPointDetermination` was renamed to `mainPointDetermination`.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        tolerance1
            A Float specifying the geometric tolerance in the 1-direction. The default value is
            0.01.
        tolerance2
            A Float specifying the geometric tolerance in the 2-direction. The default value is
            0.01.
        tolerance3
            A Float specifying the geometric tolerance in the 3-direction. The default value is
            0.01.
        undercutTolerance
            A Float specifying the undercut tolerance. The default value is 0.0.

        Returns
        -------
        StampControl
            A StampControl object.
        """
        self.geometricRestrictions[name] = geometricRestriction = StampControl(
            name,
            clientDirection,
            region,
            csys,
            drawAngle,
            mainPoint,
            mainPointDetermination,
            presumeFeasibleRegionAtStart,
            tolerance1,
            tolerance2,
            tolerance3,
            undercutTolerance,
        )
        return geometricRestriction

    @abaqus_method_doc
    def TopologyCyclicSymmetry(
        self,
        name: str,
        region: Region,
        translation: float,
        axis: Literal[C.AXIS_1, C.AXIS_3, C.AXIS_2] = AXIS_1,
        csys: Optional[int] = None,
        ignoreFrozenArea: Boolean = OFF,
    ) -> TopologyCyclicSymmetry:
        """This method creates a TopologyCyclicSymmetry object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].TopologyCyclicSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        translation
            A Float specifying the translation distance.
        axis
            A SymbolicConstant specifying the translation direction defined along an axis positioned
            at the **csys** origin. Possible values are AXIS_1, AXIS_2, and AXIS_3. The default value
            is AXIS_1.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns
        -------
        TopologyCyclicSymmetry
            A TopologyCyclicSymmetry object.
        """
        self.geometricRestrictions[name] = geometricRestriction = TopologyCyclicSymmetry(
            name, region, translation, axis, csys, ignoreFrozenArea
        )
        return geometricRestriction

    @abaqus_method_doc
    def TopologyDemoldControl(
        self,
        name: str,
        region: Region,
        csys: Optional[int] = None,
        draftAngle: float = 0,
        collisionCheckRegion: Literal[C.DEMOLD_REGION] = DEMOLD_REGION,
        pointRegion: Optional[Region] = None,
        pullDirection: tuple = (),
        technique: Literal[C.POINT, C.AUTO_TIGHT, C.SURFACE, C.STAMP, C.AUTO] = AUTO,
    ) -> TopologyDemoldControl:
        """This method creates a TopologyDemoldControl object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].TopologyDemoldControl

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        csys
            None or a DatumCsys object specifying the local coordinate system of the
            **pullDirection**. If **csys** = None, the global coordinate system is used. When this member
            is queried, it returns an Int indicating the identifier of the DatumCsys. The default
            value is None.
        draftAngle
            A Float specifying the draft angle. The default value is 0.0.
        collisionCheckRegion
            The SymbolicConstant DEMOLD_REGION or a Region object specifying the collision check
            region. If the value is DEMOLD_REGION, then the value of **region** is used as both the
            demold region and the collision check region. The default value is DEMOLD_REGION.
        pointRegion
            A Region object specifying the point on a plane perpendicular to the pull direction,
            used to specify the central plane when **technique** is POINT.
        pullDirection
            A VertexArray object of length 2 specifying the demold pull direction. Instead of
            through a ConstrainedSketchVertex, each point may be specified through a tuple of coordinates.
        technique
            A SymbolicConstant specifying the demold technique. Possible values are AUTO,
            AUTO_TIGHT, POINT, SURFACE, and STAMP. The default value is AUTO.

        Returns
        -------
        TopologyDemoldControl
            A TopologyDemoldControl object.
        """
        self.geometricRestrictions[name] = geometricRestriction = TopologyDemoldControl(
            name,
            region,
            csys,
            draftAngle,
            collisionCheckRegion,
            pointRegion,
            pullDirection,
            technique,
        )
        return geometricRestriction

    @abaqus_method_doc
    def TopologyMemberSize(
        self,
        name: str,
        region: Region,
        maxThickness: float = 0,
        minThickness: float = 0,
        separation: float = 0,
        sizeRestriction: Literal[C.ENVELOPE, C.MINIMUM, C.MAXIMUM] = MINIMUM,
    ) -> TopologyMemberSize:
        """This method creates a TopologyMemberSize object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].TopologyMemberSize

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        maxThickness
            A Float specifying the maximum thickness. The default value is 0.0.
        minThickness
            A Float specifying the minimum thickness. The default value is 0.0.
        separation
            A Float specifying the minimum gap. The default value is 0.0.
        sizeRestriction
            A SymbolicConstant specifying whether to restrict the minimum or maximum thickness or an
            envelope of both. Possible values are ENVELOPE, MAXIMUM, and MINIMUM. The default value
            is MINIMUM.

        Returns
        -------
        TopologyMemberSize
            A TopologyMemberSize object.
        """
        self.geometricRestrictions[name] = geometricRestriction = TopologyMemberSize(
            name, region, maxThickness, minThickness, separation, sizeRestriction
        )
        return geometricRestriction

    @abaqus_method_doc
    def TopologyMillingControl(
        self,
        name: str,
        millingDirections: tuple,
        region: Region,
        csys: Optional[int] = None,
        millingCheckRegion: Literal[C.MILLING_REGION] = MILLING_REGION,
        radius: Optional[float] = None,
    ) -> TopologyMillingControl:
        """This method creates a TopologyMillingControl object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].TopologyMillingControl

        .. versionadded:: 2022
            The `TopologyMillingControl` method was added.

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        millingDirections
            A tuple of VertexArray objects of length 2 specifying the milling directions. Each point
            can be specified through a tuple of coordinates instead of through a ConstrainedSketchVertex.
        region
            A Region object specifying the region to which the geometric restriction is applied.
        csys
            None or a DatumCsys object specifying the local coordinate system of the
            **millingDirections**. If **csys** = None, the global coordinate system is used. When this
            member is queried, it returns an Int indicating the identifier of the DatumCsys. The
            default value is None.
        millingCheckRegion
            The SymbolicConstant MILLING_REGION or a Region object specifying the milling check
            region. If the value is MILLING_REGION, the value of **region** is used as both the
            milling control region and the milling check region. The default value is
            MILLING_REGION.
        radius
            A Float specifying the radius for the collision check during the removal of the elements
            for the milling criteria.

        Returns
        -------
        TopologyMillingControl
            A TopologyMillingControl object.
        """
        self.geometricRestrictions[name] = geometricRestriction = TopologyMillingControl(
            name, millingDirections, region, csys, millingCheckRegion, radius
        )
        return geometricRestriction

    @abaqus_method_doc
    def TopologyOverhangControl(
        self,
        name: str,
        pullDirection: tuple,
        region: Region,
        csys: Optional[int] = None,
        draftAngle: float = 45,
        overhangCheckRegion: Literal[C.OVERHANG_REGION] = OVERHANG_REGION,
        pointRegion: Region = Region(),
        radius: Optional[float] = None,
        technique: Literal[C.POINT, C.NONE, C.AUTO] = AUTO,
    ) -> TopologyOverhangControl:
        """This method creates a TopologyOverhangControl object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].TopologyOverhangControl

        .. versionadded:: 2019
            The `TopologyOverhangControl` method was added.

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        pullDirection
            A VertexArray object of length 2 specifying the overhang control print direction.
            Instead of through a ConstrainedSketchVertex, each point can be specified through a tuple of coordinates.
        region
            A Region object specifying the region to which the geometric restriction is applied.
        csys
            None or a DatumCsys object specifying the local coordinate system of the
            **pullDirection**. If **csys** = None, the global coordinate system is used. When this member
            is queried, it returns an Int indicating the identifier of the DatumCsys. The default
            value is None.
        draftAngle
            A Float specifying the overhang angle. The default value is 45.0.
        overhangCheckRegion
            The SymbolicConstant OVERHANG_REGION or a Region object specifying the overhang check
            region. If the value is OVERHANG_REGION, the value of **region** is used as both the
            overhang control region and the overhang check region. The default value is
            OVERHANG_REGION.
        pointRegion
            A Region object specifying the point on a plane perpendicular to the **pullDirection**
            that is used to specify the base plane when **technique** is POINT.
        radius
            A Float specifying the radius to define the size of the cones that are used in the
            internal check for the overhang criteria.
        technique
            A SymbolicConstant specifying the overhang control technique used to define the base
            plane. Possible values are AUTO, POINT, and NONE. The default value is AUTO.

        Returns
        -------
            A TopologyOverhangControl object.
        """
        self.geometricRestrictions[name] = geometricRestriction = TopologyOverhangControl(
            name,
            pullDirection,
            region,
            csys,
            draftAngle,
            overhangCheckRegion,
            pointRegion,
            radius,
            technique,
        )
        return geometricRestriction

    @abaqus_method_doc
    def TopologyPlanarSymmetry(
        self,
        name: str,
        region: Region,
        axis: Literal[C.AXIS_1, C.AXIS_3, C.AXIS_2] = AXIS_1,
        csys: Optional[int] = None,
        ignoreFrozenArea: Boolean = OFF,
    ) -> TopologyPlanarSymmetry:
        """This method creates a TopologyPlanarSymmetry object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].TopologyPlanarSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        axis
            A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2,
            and AXIS_3. The default value is AXIS_1.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns
        -------
        TopologyPlanarSymmetry
            A TopologyPlanarSymmetry object.
        """
        self.geometricRestrictions[name] = geometricRestriction = TopologyPlanarSymmetry(
            name, region, axis, csys, ignoreFrozenArea
        )
        return geometricRestriction

    @abaqus_method_doc
    def TopologyPointSymmetry(
        self,
        name: str,
        region: Region,
        csys: Optional[int] = None,
        ignoreFrozenArea: Boolean = OFF,
    ) -> TopologyPointSymmetry:
        """This method creates a TopologyPointSymmetry object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].TopologyPointSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        csys
            None or a DatumCsys object specifying the position of the symmetry point defined as the
            origin of a local coordinate system. If **csys** = None, the global coordinate system is
            used. When this member is queried, it returns an Int. The default value is None.
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns
        -------
        TopologyPointSymmetry
            A TopologyPointSymmetry object.
        """
        self.geometricRestrictions[name] = geometricRestriction = TopologyPointSymmetry(
            name, region, csys, ignoreFrozenArea
        )
        return geometricRestriction

    @abaqus_method_doc
    def TopologyRotationalSymmetry(
        self,
        name: str,
        angle: float,
        region: Region,
        axis: Literal[C.AXIS_1, C.AXIS_3, C.AXIS_2] = AXIS_1,
        csys: Optional[int] = None,
        ignoreFrozenArea: Boolean = OFF,
    ) -> TopologyRotationalSymmetry:
        """This method creates a TopologyRotationalSymmetry object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].TopologyRotationalSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        angle
            A Float specifying the repeating segment size, an angle in degrees.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        axis
            A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2,
            and AXIS_3. The default value is AXIS_1.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns
        -------
        TopologyRotationalSymmetry
            A TopologyRotationalSymmetry object.
        """
        self.geometricRestrictions[name] = geometricRestriction = TopologyRotationalSymmetry(
            name, angle, region, axis, csys, ignoreFrozenArea
        )
        return geometricRestriction

    @abaqus_method_doc
    def TurnControl(
        self,
        name: str,
        clientDirection: tuple,
        region: Region,
        csys: Optional[int] = None,
        mainPoint: Optional[str] = None,
        mainPointDetermination: Literal[C.SPECIFY, C.MINIMUM, C.MAXIMUM] = MAXIMUM,
        presumeFeasibleRegionAtStart: Boolean = ON,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
    ) -> TurnControl:
        """This method creates a TurnControl object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].TurnControl

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        clientDirection
            A VertexArray object of length 2 specifying the direction of the rotation axis as a
            vector positioned at the **csys** origin. Instead of through a ConstrainedSketchVertex, each point might be
            specified through a tuple of coordinates.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        mainPoint
            None or a Region object specifying the main point used when **mainPointDetermination** is
            SPECIFY. The default value is None.

            .. versionchanged:: 2022
                The argument `masterPoint` was renamed to `mainPoint`.
        mainPointDetermination
            A SymbolicConstant specifying the rule for assigning point priority. Possible values are
            MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

            .. versionchanged:: 2022
                The argument `masterPointDetermination` was renamed to `mainPointDetermination`.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        tolerance1
            A Float specifying the geometric tolerance in the 1-direction. The default value is
            0.01.
        tolerance2
            A Float specifying the geometric tolerance in the 2-direction. The default value is
            0.01.
        tolerance3
            A Float specifying the geometric tolerance in the 3-direction. The default value is
            0.01.

        Returns
        -------
        TurnControl
            A TurnControl object.
        """
        self.geometricRestrictions[name] = geometricRestriction = TurnControl(
            name,
            clientDirection,
            region,
            csys,
            mainPoint,
            mainPointDetermination,
            presumeFeasibleRegionAtStart,
            tolerance1,
            tolerance2,
            tolerance3,
        )
        return geometricRestriction
