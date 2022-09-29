from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import Boolean, DEMOLD_REGION, MAXIMUM, ON, SymbolicConstant


@abaqus_class_doc
class ShapeDemoldControl(GeometricRestriction):
    """The ShapeDemoldControl object defines a shape demold control geometric restriction.
    The ShapeDemoldControl object is derived from the GeometricRestriction object.

    .. note:: 
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object of length 2 specifying the demold pull direction. Instead of
    #: through a ConstrainedSketchVertex, each point might be specified through a tuple of coordinates.
    pullDirection: tuple

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
    #: When used with a TopologyTask, there is no default value. When used with a ShapeTask,
    #: the default value is MODEL.
    region: Region

    #: The SymbolicConstant DEMOLD_REGION or a Region object specifying the collision check
    #: region. If the value is DEMOLD_REGION, then the value of **region** is used as both the
    #: demold region and the collision check region. The default value is DEMOLD_REGION.
    collisionCheckRegion: SymbolicConstant = DEMOLD_REGION

    #: None or a DatumCsys object specifying the local coordinate system of the
    #: **pullDirection**. If **csys** = None, the global coordinate system is used. When this member
    #: is queried, it returns an Int indicating the identifier of the DatumCsys. The default
    #: value is None.
    csys: Optional[int] = None

    #: A Float specifying the draw angle. The default value is 0.0.
    drawAngle: float = 0

    #: A SymbolicConstant specifying the rule for assigning point priority. Possible values are
    #: MAXIMUM and MINIMUM. The default value is MAXIMUM.
    #:
    #: .. versionchanged:: 2022
    #:    The attribute `masterPointDetermination` was renamed to `mainPointDetermination`.
    mainPointDetermination: SymbolicConstant = MAXIMUM

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
        pullDirection: tuple,
        region: Region,
        collisionCheckRegion: SymbolicConstant = DEMOLD_REGION,
        csys: Optional[int] = None,
        drawAngle: float = 0,
        mainPointDetermination: SymbolicConstant = MAXIMUM,
        presumeFeasibleRegionAtStart: Boolean = ON,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
        undercutTolerance: float = 0,
    ):
        """This method creates a ShapeDemoldControl object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].ShapeDemoldControl

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        pullDirection
            A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object of length 2 specifying the demold pull direction. Instead of
            through a ConstrainedSketchVertex, each point might be specified through a tuple of coordinates.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
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
            A :py:class:`~abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        collisionCheckRegion: SymbolicConstant = DEMOLD_REGION,
        csys: Optional[int] = None,
        drawAngle: float = 0,
        mainPointDetermination: SymbolicConstant = MAXIMUM,
        presumeFeasibleRegionAtStart: Boolean = ON,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
        undercutTolerance: float = 0,
    ):
        """This method modifies the ShapeDemoldControl object.

        Parameters
        ----------
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
        """
        ...
