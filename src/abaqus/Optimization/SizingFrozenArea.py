from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


class SizingFrozenArea(GeometricRestriction):
    """The SizingFrozenArea object defines a sizing frozen area geometric restriction.
    The SizingFrozenArea object is derived from the GeometricRestriction object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
    region: Region

    def __init__(self, name: str, region: Region):
        """This method creates a SizingFrozenArea object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].optimizationTasks[name].SizingFrozenArea

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.

        Returns
        -------
        SizingFrozenArea
            A :py:class:`~abaqus.Optimization.SizingFrozenArea.SizingFrozenArea` object.
        """
        super().__init__()
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the SizingFrozenArea object."""
        pass
