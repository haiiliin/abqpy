from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import Boolean, OFF, ON


@abaqus_class_doc
class FixedRegion(GeometricRestriction):
    """The FixedRegion object defines a fixed region geometric restriction.
    The FixedRegion object is derived from the GeometricRestriction object.

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

    #: None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
    #: global coordinate system is used. When this member is queried, it returns an Int. The
    #: default value is None.
    csys: Optional[int] = None

    #: A Boolean specifying whether to ignore the geometric restriction in the first design
    #: cycle. The default value is ON.
    presumeFeasibleRegionAtStart: Boolean = ON

    #: A Boolean specifying whether to fix the region in the 1-direction. The default value is
    #: OFF.
    u1: Boolean = OFF

    #: A Boolean specifying whether to fix the region in the 2-direction. The default value is
    #: OFF.
    u2: Boolean = OFF

    #: A Boolean specifying whether to fix the region in the 3-direction. The default value is
    #: OFF.
    u3: Boolean = OFF

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        csys: Optional[int] = None,
        presumeFeasibleRegionAtStart: Boolean = ON,
        u1: Boolean = OFF,
        u2: Boolean = OFF,
        u3: Boolean = OFF,
    ):
        """This method creates a FixedRegion object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].FixedRegion

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
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
            A :py:class:`~abaqus.Optimization.FixedRegion.FixedRegion` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        csys: Optional[int] = None,
        presumeFeasibleRegionAtStart: Boolean = ON,
        u1: Boolean = OFF,
        u2: Boolean = OFF,
        u3: Boolean = OFF,
    ):
        """This method modifies the FixedRegion object.

        Parameters
        ----------
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
        """
        ...
