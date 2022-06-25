from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


class BeadGrowth(GeometricRestriction):
    """The BeadGrowth object defines a growth geometric restriction.
    The BeadGrowth object is derived from the GeometricRestriction object.

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

    #: A Float specifying the maximum optimization displacement in the growth direction. Either
    #: **beadGrowth** or **shrink** or both must be specified. The default value is 0.0.
    beadGrowth: float = 0

    #: A Float specifying the maximum optimization displacement in the shrink direction. Either
    #: **beadGrowth** or **shrink** or both must be specified The default value is 0.0.
    shrink: float = 0

    def __init__(
        self, name: str, region: Region, beadGrowth: float = 0, shrink: float = 0
    ):
        """This method creates a BeadGrowth object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].optimizationTasks[name].BeadGrowth

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
        beadGrowth
            A Float specifying the maximum optimization displacement in the growth direction. Either
            **beadGrowth** or **shrink** or both must be specified. The default value is 0.0.
        shrink
            A Float specifying the maximum optimization displacement in the shrink direction. Either
            **beadGrowth** or **shrink** or both must be specified The default value is 0.0.

        Returns
        -------
        BeadGrowth
            A :py:class:`~abaqus.Optimization.BeadGrowth.BeadGrowth` object.
        """
        super().__init__()
        pass

    def setValues(self, beadGrowth: float = 0, shrink: float = 0):
        """This method modifies the BeadGrowth object.

        Parameters
        ----------
        beadGrowth
            A Float specifying the maximum optimization displacement in the growth direction. Either
            **beadGrowth** or **shrink** or both must be specified. The default value is 0.0.
        shrink
            A Float specifying the maximum optimization displacement in the shrink direction. Either
            **beadGrowth** or **shrink** or both must be specified The default value is 0.0.
        """
        pass
