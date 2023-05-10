from typing import Optional

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import MAXIMUM, ON, Boolean, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .GeometricRestriction import GeometricRestriction


@abaqus_class_doc
class DrillControl(GeometricRestriction):
    """The DrillControl object defines a drill control geometric restriction. The DrillControl object is derived
    from the GeometricRestriction object.

    .. note::
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A VertexArray object of length 2 specifying the direction of the drill axis positioned
    #: at the **csys** origin. Instead of through a ConstrainedSketchVertex, each point may be specified through a
    #: tuple of coordinates.
    clientDirection: tuple

    #: A Region object specifying the region to which the geometric restriction is applied.
    #: When used with a TopologyTask, there is no default value. When used with a ShapeTask,
    #: the default value is MODEL.
    region: Region

    #: None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
    #: global coordinate system is used. When this member is queried, it returns an Int. The
    #: default value is None.
    csys: Optional[int] = None

    #: A Float specifying the draw angle. The default value is 0.0.
    drawAngle: float = 0

    #: None or a Region object specifying the master point used when **masterPointDetermination** is
    #: SPECIFY. The default value is None.
    masterPoint: Optional[str] = None

    #: A SymbolicConstant specifying the rule for assigning point priority. Possible values are
    #: MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.
    masterPointDetermination: SymbolicConstant = MAXIMUM

    #: A Boolean specifying whether to ignore the geometric restriction in the first design
    #: cycle. The default value is ON.
    presumeFeasibleRegionAtStart: Boolean = ON

    #: A Float specifying the geometric tolerance in the 1-direction. The default value is
    #: 0.01.
    tolerance1: float = 0

    #: A Float specifying the geometric tolerance in the 2-direction. The default value is
    #: 0.01.
    tolerance2: float = 0

    #: A Float specifying the geometric tolerance in the 3-direction. The default value is
    #: 0.01.
    tolerance3: float = 0

    #: A Float specifying the undercut tolerance. The default value is 0.0.
    undercutTolerance: float = 0

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        clientDirection: tuple,
        region: Region,
        csys: Optional[int] = None,
        drawAngle: float = 0,
        masterPoint: Optional[str] = None,
        masterPointDetermination: Literal[C.SPECIFY, C.MINIMUM, C.MAXIMUM] = MAXIMUM,
        presumeFeasibleRegionAtStart: Boolean = ON,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
        undercutTolerance: float = 0,
    ):
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
        masterPoint
            None or a Region object specifying the master point used when **masterPointDetermination** is
            SPECIFY. The default value is None.
        masterPointDetermination
            A SymbolicConstant specifying the rule for assigning point priority. Possible values are
            MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.
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
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        csys: Optional[int] = None,
        drawAngle: float = 0,
        masterPoint: Optional[str] = None,
        masterPointDetermination: Literal[C.SPECIFY, C.MINIMUM, C.MAXIMUM] = MAXIMUM,
        presumeFeasibleRegionAtStart: Boolean = ON,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
        undercutTolerance: float = 0,
    ):
        """This method modifies the DrillControl object.

        Parameters
        ----------
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        drawAngle
            A Float specifying the draw angle. The default value is 0.0.
        masterPoint
            None or a Region object specifying the master point used when **masterPointDetermination** is
            SPECIFY. The default value is None.
        masterPointDetermination
            A SymbolicConstant specifying the rule for assigning point priority. Possible values are
            MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.
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
        """
        ...
