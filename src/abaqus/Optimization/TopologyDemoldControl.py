from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import AUTO, DEMOLD_REGION, SymbolicConstant


@abaqus_class_doc
class TopologyDemoldControl(GeometricRestriction):
    """The TopologyDemoldControl object defines a topology demold control geometric
    restriction.
    The TopologyDemoldControl object is derived from the GeometricRestriction object.

    .. note:: 
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
    #: When used with a TopologyTask, there is no default value. When used with a ShapeTask,
    #: the default value is MODEL.
    region: Region

    #: None or a DatumCsys object specifying the local coordinate system of the
    #: **pullDirection**. If **csys** = None, the global coordinate system is used. When this member
    #: is queried, it returns an Int indicating the identifier of the DatumCsys. The default
    #: value is None.
    csys: Optional[int] = None

    #: A Float specifying the draft angle. The default value is 0.0.
    draftAngle: float = 0

    #: The SymbolicConstant DEMOLD_REGION or a Region object specifying the collision check
    #: region. If the value is DEMOLD_REGION, then the value of **region** is used as both the
    #: demold region and the collision check region. The default value is DEMOLD_REGION.
    collisionCheckRegion: SymbolicConstant = DEMOLD_REGION

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the point on a plane perpendicular to the pull direction,
    #: used to specify the central plane when **technique** is POINT.
    pointRegion: Optional[Region] = None

    #: A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object of length 2 specifying the demold pull direction. Instead of
    #: through a ConstrainedSketchVertex, each point may be specified through a tuple of coordinates.
    pullDirection: tuple = ()

    #: A SymbolicConstant specifying the demold technique. Possible values are AUTO,
    #: AUTO_TIGHT, POINT, SURFACE, and STAMP. The default value is AUTO.
    technique: SymbolicConstant = AUTO

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        csys: Optional[int] = None,
        draftAngle: float = 0,
        collisionCheckRegion: SymbolicConstant = DEMOLD_REGION,
        pointRegion: Optional[Region] = None,
        pullDirection: tuple = (),
        technique: SymbolicConstant = AUTO,
    ):
        """This method creates a TopologyDemoldControl object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].TopologyDemoldControl

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
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
            A :py:class:`~abaqus.Region.Region.Region` object specifying the point on a plane perpendicular to the pull direction,
            used to specify the central plane when **technique** is POINT.
        pullDirection
            A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object of length 2 specifying the demold pull direction. Instead of
            through a ConstrainedSketchVertex, each point may be specified through a tuple of coordinates.
        technique
            A SymbolicConstant specifying the demold technique. Possible values are AUTO,
            AUTO_TIGHT, POINT, SURFACE, and STAMP. The default value is AUTO.

        Returns
        -------
        TopologyDemoldControl
            A :py:class:`~abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        csys: Optional[int] = None,
        draftAngle: float = 0,
        collisionCheckRegion: SymbolicConstant = DEMOLD_REGION,
        pointRegion: Optional[Region] = None,
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
            A :py:class:`~abaqus.Region.Region.Region` object specifying the point on a plane perpendicular to the pull direction,
            used to specify the central plane when **technique** is POINT.
        pullDirection
            A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object of length 2 specifying the demold pull direction. Instead of
            through a ConstrainedSketchVertex, each point may be specified through a tuple of coordinates.
        technique
            A SymbolicConstant specifying the demold technique. Possible values are AUTO,
            AUTO_TIGHT, POINT, SURFACE, and STAMP. The default value is AUTO.
        """
        ...
