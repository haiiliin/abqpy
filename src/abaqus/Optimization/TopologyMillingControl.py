from abaqusConstants import *
from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


class TopologyMillingControl(GeometricRestriction):
    """The TopologyMillingControl object defines a topology milling control geometric
    restriction.
    The TopologyMillingControl object is derived from the GeometricRestriction object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A tuple of VertexArray objects of length 2 specifying the milling directions. Each point
    #: can be specified through a tuple of coordinates instead of through a ConstrainedSketchVertex.
    millingDirections: tuple

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
    region: Region

    #: None or a DatumCsys object specifying the local coordinate system of the
    #: **millingDirections**. If **csys** = None, the global coordinate system is used. When this
    #: member is queried, it returns an Int indicating the identifier of the DatumCsys. The
    #: default value is None.
    csys: int = None

    #: The SymbolicConstant MILLING_REGION or a Region object specifying the milling check
    #: region. If the value is MILLING_REGION, the value of **region** is used as both the
    #: milling control region and the milling check region. The default value is
    #: MILLING_REGION.
    millingCheckRegion: SymbolicConstant = MILLING_REGION

    #: A Float specifying the radius for the collision check during the removal of the elements
    #: for the milling criteria.
    radius: float = None

    def __init__(
        self,
        name: str,
        millingDirections: tuple,
        region: Region,
        csys: int = None,
        millingCheckRegion: SymbolicConstant = MILLING_REGION,
        radius: float = None,
    ):
        """This method creates a TopologyMillingControl object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].optimizationTasks[name].TopologyMillingControl

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        millingDirections
            A tuple of VertexArray objects of length 2 specifying the milling directions. Each point
            can be specified through a tuple of coordinates instead of through a ConstrainedSketchVertex.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
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
            A :py:class:`~abaqus.Optimization.TopologyMillingControl.TopologyMillingControl` object.
        """
        super().__init__()
        pass

    def setValues(
        self,
        csys: int = None,
        millingCheckRegion: SymbolicConstant = MILLING_REGION,
        radius: float = None,
    ):
        """This method modifies the TopologyMillingControl object.

        Parameters
        ----------
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
        """
        pass
