from typing import Optional, Union

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..BasicGeometry.VertexArray import VertexArray
from ..Datum.DatumCsys import DatumCsys
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import RIBDESIGN_REGION
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .GeometricRestriction import GeometricRestriction


@abaqus_class_doc
class TopologyRibDesign(GeometricRestriction):
    """The TopologyRibDesign object defines a topology rib design geometric restriction. The TopologyRibDesign
    object is derived from the GeometricRestriction object.

    .. note::
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]

    .. versionadded:: 2023

        The ``TopologyRibDesign`` class was added.
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A VertexArray object of length 2 specifying the out-of-plane growth direction of the ribs. Instead of
    #: through a Vertex, each point can be specified through a tuple of coordinates.
    ribDirection: VertexArray

    #: A Float specifying the average thickness of the ribs.
    ribThickness: float

    #: A Float specifying the average distance between the rib centers. The distance must be larger than twice
    #: the average element edge length.
    ribDistance: float

    #: A Region object specifying the region to which the geometric restriction is applied.
    #: When used with a TopologyTask, there is no default value. When used with a ShapeTask,
    #: the default value is MODEL.
    region: Region

    #: None or a DatumCsys object specifying the position of the symmetry point defined as the
    #: origin of a local coordinate system. If **csys** = None, the global coordinate system is
    #: used. When this member is queried, it returns an Int. The default value is None.
    csys: Optional[DatumCsys] = None

    #: The SymbolicConstant RIBDESIGN_REGION or a Region object specifying the overhang check region. If the value
    #: is OVERHANG_REGION, the value of region is used as both the overhang control region and the overhang check
    #: region. The default value is RIBDESIGN_REGION.
    ribDesignCheckRegion: Union[Literal[C.RIBDESIGN_REGION], Region] = RIBDESIGN_REGION

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        ribDirection: VertexArray,
        ribThickness: float,
        ribDistance: float,
        region: Region,
        csys: Optional[DatumCsys] = None,
        ribDesignCheckRegion: Union[Literal[C.RIBDESIGN_REGION], Region] = RIBDESIGN_REGION,
    ):
        """This method creates a TopologyRibDesign object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].TopologyRibDesign

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        ribDirection
            A VertexArray object of length 2 specifying the out-of-plane growth direction of the ribs. Instead of
            through a Vertex, each point can be specified through a tuple of coordinates.
        ribThickness
            A Float specifying the average thickness of the ribs.
        ribDistance
            A Float specifying the average distance between the rib centers. The distance must be larger than twice
            the average element edge length.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        csys
            None or a DatumCsys object specifying the position of the symmetry point defined as the
            origin of a local coordinate system. If **csys** = None, the global coordinate system is
            used. When this member is queried, it returns an Int. The default value is None.
        ribDesignCheckRegion
            The SymbolicConstant RIBDESIGN_REGION or a Region object specifying the overhang check region. If the value
            is OVERHANG_REGION, the value of region is used as both the overhang control region and the overhang check
            region. The default value is RIBDESIGN_REGION.

        Returns
        -------
        TopologyRibDesign
            A TopologyRibDesign object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        ribDirection: VertexArray,
        ribThickness: float,
        ribDistance: float,
        region: Region,
        csys: Optional[DatumCsys] = None,
        ribDesignCheckRegion: Union[Literal[C.RIBDESIGN_REGION], Region] = RIBDESIGN_REGION,
    ):
        """This method modifies the TopologyRibDesign object.

        Parameters
        ----------
        ribDirection
            A VertexArray object of length 2 specifying the out-of-plane growth direction of the ribs. Instead of
            through a Vertex, each point can be specified through a tuple of coordinates.
        ribThickness
            A Float specifying the average thickness of the ribs.
        ribDistance
            A Float specifying the average distance between the rib centers. The distance must be larger than twice
            the average element edge length.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        csys
            None or a DatumCsys object specifying the position of the symmetry point defined as the
            origin of a local coordinate system. If **csys** = None, the global coordinate system is
            used. When this member is queried, it returns an Int. The default value is None.
        ribDesignCheckRegion
            The SymbolicConstant RIBDESIGN_REGION or a Region object specifying the overhang check region. If the value
            is OVERHANG_REGION, the value of region is used as both the overhang control region and the overhang check
            region. The default value is RIBDESIGN_REGION.
        """
        ...
