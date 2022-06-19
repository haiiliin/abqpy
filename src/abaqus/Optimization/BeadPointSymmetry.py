from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


class BeadPointSymmetry(GeometricRestriction):
    """The BeadPointSymmetry object defines a point symmetry geometric restriction.
    The BeadPointSymmetry object is derived from the GeometricRestriction object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import optimization
        mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    def __init__(self, name: str, region: Region, csys: int = None):
        """This method creates a BeadPointSymmetry object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

                      mdb.models[name].optimizationTasks[name].BeadPointSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
        csys
            None or a DatumCsys object specifying the position of the symmetry point defined as the
            origin of a local coordinate system. If **csys**=None, the global coordinate system is
            used. When this member is queried, it returns an Int. The default value is None.

        Returns
        -------
            A BeadPointSymmetry object.
        """
        super().__init__()
        pass

    def setValues(self, csys: int = None):
        """This method modifies the BeadPointSymmetry object.

        Parameters
        ----------
        csys
            None or a DatumCsys object specifying the position of the symmetry point defined as the
            origin of a local coordinate system. If **csys**=None, the global coordinate system is
            used. When this member is queried, it returns an Int. The default value is None.
        """
        pass
