from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class PenetrationCheck(GeometricRestriction):
    """The PenetrationCheck object defines a penetration check geometric restriction.
    The PenetrationCheck object is derived from the GeometricRestriction object.
    This page discusses:

    .. note:: 
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the penetration check region.
    penetrationCheckRegion: Region

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
    #: When used with a TopologyTask, there is no default value. When used with a ShapeTask,
    #: the default value is MODEL.
    region: Region

    #: A Boolean specifying whether to ignore the geometric restriction in the first design
    #: cycle. The default value is ON.
    presumeFeasibleRegionAtStart: Boolean = ON

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        penetrationCheckRegion: Region,
        region: Region,
        presumeFeasibleRegionAtStart: Boolean = ON,
    ):
        """This method creates a PenetrationCheck object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].PenetrationCheck

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        penetrationCheckRegion
            A :py:class:`~abaqus.Region.Region.Region` object specifying the penetration check region.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.

        Returns
        -------
        PenetrationCheck
            A :py:class:`~abaqus.Optimization.PenetrationCheck.PenetrationCheck` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, presumeFeasibleRegionAtStart: Boolean = ON):
        """This method modifies the PenetrationCheck object.

        Parameters
        ----------
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        """
        ...
