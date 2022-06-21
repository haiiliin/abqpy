from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


class FrozenArea(GeometricRestriction):
    """The FrozenArea object defines a frozen area geometric restriction.
    The FrozenArea object is derived from the GeometricRestriction object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    def __init__(self, name: str, region: Region = Region()):
        """This method creates a FrozenArea object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

                      mdb.models[name].optimizationTasks[name].FrozenArea

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.

        Returns
        -------
        A :py:class:`~abaqus.Optimization.FrozenArea.FrozenArea` object.
        """
        super().__init__()
        pass

    def setValues(self, region: Region = Region()):
        """This method modifies the FrozenArea object.

        Parameters
        ----------
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        """
        pass
