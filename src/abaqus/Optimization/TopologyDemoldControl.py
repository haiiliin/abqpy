from abaqusConstants import *
from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


class TopologyDemoldControl(GeometricRestriction):
    """The TopologyDemoldControl object defines a topology demold control geometric
    restriction.
    The TopologyDemoldControl object is derived from the GeometricRestriction object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    def __init__(
        self,
        name: str,
        region: Region,
        csys: int = None,
        draftAngle: float = 0,
        collisionCheckRegion: SymbolicConstant = DEMOLD_REGION,
        pointRegion: Region = None,
        pullDirection: tuple = (),
        technique: SymbolicConstant = AUTO,
    ):
        """This method creates a TopologyDemoldControl object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

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
            A TopologyDemoldControl object.
        """
        super().__init__()
        pass

    def setValues(
        self,
        csys: int = None,
        draftAngle: float = 0,
        collisionCheckRegion: SymbolicConstant = DEMOLD_REGION,
        pointRegion: Region = None,
        pullDirection: tuple = (),
        technique: SymbolicConstant = AUTO,
    ):
        """This method modifies the TopologyDemoldControl object.

        Parameters
        ----------
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
        """
        pass
