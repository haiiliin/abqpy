from typing import Optional
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region


@abaqus_class_doc
class BeadPointSymmetry(GeometricRestriction):
    """The BeadPointSymmetry object defines a point symmetry geometric restriction.
    The BeadPointSymmetry object is derived from the GeometricRestriction object.

    .. note:: 
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
    region: Region

    #: None or a DatumCsys object specifying the position of the symmetry point defined as the
    #: origin of a local coordinate system. If **csys** = None, the global coordinate system is
    #: used. When this member is queried, it returns an Int. The default value is None.
    csys: Optional[int] = None

    @abaqus_method_doc
    def __init__(self, name: str, region: Region, csys: Optional[int] = None):
        """This method creates a BeadPointSymmetry object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].BeadPointSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
        csys
            None or a DatumCsys object specifying the position of the symmetry point defined as the
            origin of a local coordinate system. If **csys** = None, the global coordinate system is
            used. When this member is queried, it returns an Int. The default value is None.

        Returns
        -------
        BeadPointSymmetry
            A :py:class:`~abaqus.Optimization.BeadPointSymmetry.BeadPointSymmetry` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, csys: Optional[int] = None):
        """This method modifies the BeadPointSymmetry object.

        Parameters
        ----------
        csys
            None or a DatumCsys object specifying the position of the symmetry point defined as the
            origin of a local coordinate system. If **csys** = None, the global coordinate system is
            used. When this member is queried, it returns an Int. The default value is None.
        """
        ...
