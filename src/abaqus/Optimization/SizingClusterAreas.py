from .GeometricRestriction import GeometricRestriction


class SizingClusterAreas(GeometricRestriction):
    """The SizingClusterAreas object defines a sizing cluster areas geometric restriction.
    The SizingClusterAreas object is derived from the GeometricRestriction object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: Tuple of Region objects specifying the regions to which the geometric restriction is
    #: applied.
    regions: tuple

    def __init__(self, name: str, regions: tuple):
        """This method creates a SizingClusterAreas object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

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
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the SizingClusterAreas object."""
        pass
