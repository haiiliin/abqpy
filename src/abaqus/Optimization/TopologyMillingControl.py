from __future__ import annotations

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import MILLING_REGION, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .GeometricRestriction import GeometricRestriction


@abaqus_class_doc
class TopologyMillingControl(GeometricRestriction):
    """The TopologyMillingControl object defines a topology milling control geometric restriction. The
    TopologyMillingControl object is derived from the GeometricRestriction object.

    .. note::
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]

    .. versionadded:: 2022
        The ``TopologyMillingControl`` class was added.
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A tuple of VertexArray objects of length 2 specifying the milling directions. Each point
    #: can be specified through a tuple of coordinates instead of through a ConstrainedSketchVertex.
    millingDirections: tuple

    #: A Region object specifying the region to which the geometric restriction is applied.
    region: Region

    #: None or a DatumCsys object specifying the local coordinate system of the
    #: **millingDirections**. If **csys** = None, the global coordinate system is used. When this
    #: member is queried, it returns an Int indicating the identifier of the DatumCsys. The
    #: default value is None.
    csys: int | None = None

    #: The SymbolicConstant MILLING_REGION or a Region object specifying the milling check
    #: region. If the value is MILLING_REGION, the value of **region** is used as both the
    #: milling control region and the milling check region. The default value is
    #: MILLING_REGION.
    millingCheckRegion: SymbolicConstant = MILLING_REGION

    #: A Float specifying the radius for the collision check during the removal of the elements
    #: for the milling criteria.
    radius: float | None = None

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        millingDirections: tuple,
        region: Region,
        csys: int | None = None,
        millingCheckRegion: Literal[C.MILLING_REGION] = MILLING_REGION,
        radius: float | None = None,
    ):
        """This method creates a TopologyMillingControl object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].TopologyMillingControl

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
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        csys: int | None = None,
        millingCheckRegion: Literal[C.MILLING_REGION] = MILLING_REGION,
        radius: float | None = None,
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
        ...
