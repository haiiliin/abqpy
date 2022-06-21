from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


class SizingMemberSize(GeometricRestriction):
    """The SizingMemberSize object defines a sizing member size geometric restriction.
    The SizingMemberSize object is derived from the GeometricRestriction object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    def __init__(self, name: str, region: Region, minWidth: float):
        """This method creates a SizingMemberSize object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

                      mdb.models[name].optimizationTasks[name].SizingMemberSize

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
        minWidth
            A Float specifying the min width.

        Returns
        -------

        Raises
        ------
        """
        super().__init__()
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the sizingMemberSize object."""
        pass
