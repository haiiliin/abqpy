from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


@abaqus_class_doc
class BeadPenetrationCheck(GeometricRestriction):
    """The BeadPenetrationCheck object defines a penetration check geometric restriction.
    The BeadPenetrationCheck object is derived from the GeometricRestriction object.

    .. note:: 
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the penetration check region.
    beadPenetrationCheckRegion: Region

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
    region: Region

    @abaqus_method_doc
    def __init__(self, name: str, beadPenetrationCheckRegion: Region, region: Region):
        """This method creates a BeadPenetrationCheck object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].BeadPenetrationCheck

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        beadPenetrationCheckRegion
            A :py:class:`~abaqus.Region.Region.Region` object specifying the penetration check region.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.

        Returns
        -------
        BeadPenetrationCheck
            A :py:class:`~abaqus.Optimization.BeadPenetrationCheck.BeadPenetrationCheck` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the BeadPenetrationCheck object."""
        ...
