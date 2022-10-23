from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .GeometricRestriction import GeometricRestriction


@abaqus_class_doc
class SizingClusterAreas(GeometricRestriction):
    """The SizingClusterAreas object defines a sizing cluster areas geometric restriction.
    The SizingClusterAreas object is derived from the GeometricRestriction object.

    .. note::
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: Tuple of Region objects specifying the regions to which the geometric restriction is
    #: applied.
    regions: tuple

    @abaqus_method_doc
    def __init__(self, name: str, regions: tuple):
        """This method creates a SizingClusterAreas object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].SizingClusterAreas

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        regions
            Tuple of Region objects specifying the regions to which the geometric restriction is
            applied.

        Returns
        -------
        SizingClusterAreas
            A :py:class:`~abaqus.Optimization.SizingClusterAreas.SizingClusterAreas` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, *args, **kwargs):
        """This method modifies the SizingClusterAreas object."""
        ...
