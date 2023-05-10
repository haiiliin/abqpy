from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import OFF, Boolean
from .GeometricRestriction import GeometricRestriction


@abaqus_class_doc
class SizingPointSymmetry(GeometricRestriction):
    """The SizingPointSymmetry object defines a sizing point symmetry geometric restriction. The
    SizingPointSymmetry object is derived from the GeometricRestriction object.

    .. note::
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A Region object specifying the region to which the geometric restriction is applied.
    region: Region

    #: None or a DatumCsys object specifying the position of the symmetry point defined as the
    #: origin of a local coordinate system. If **csys** = None, the global coordinate system is
    #: used. When this member is queried, it returns an Int. The default value is None.
    csys: Optional[int] = None

    #: A Boolean specifying whether to ignore frozen areas. The default value is OFF.
    ignoreFrozenArea: Boolean = OFF

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        csys: Optional[int] = None,
        ignoreFrozenArea: Boolean = OFF,
    ):
        """This method creates a SizingPointSymmetry object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].SizingPointSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
        csys
            None or a DatumCsys object specifying the position of the symmetry point defined as the
            origin of a local coordinate system. If **csys** = None, the global coordinate system is
            used. When this member is queried, it returns an Int. The default value is None.
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns
        -------
        SizingPointSymmetry
            A SizingPointSymmetry object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, csys: Optional[int] = None, ignoreFrozenArea: Boolean = OFF):
        """This method modifies the SizingPointSymmetry object.

        Parameters
        ----------
        csys
            None or a DatumCsys object specifying the position of the symmetry point defined as the
            origin of a local coordinate system. If **csys** = None, the global coordinate system is
            used. When this member is queried, it returns an Int. The default value is None.
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF.
        """
        ...
