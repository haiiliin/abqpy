from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class BeadFixedRegion(GeometricRestriction):
    """The BeadFixedRegion object defines a fixed region geometric restriction.
    The BeadFixedRegion object is derived from the GeometricRestriction object.

    .. note::
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
    region: Region

    #: None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
    #: global coordinate system is used. When this member is queried, it returns an Int. The
    #: default value is None.
    csys: Optional[int] = None

    #: A Boolean specifying whether to fix the region in the 1-direction. The default value is
    #: OFF.
    u1: Boolean = OFF

    #: A Boolean specifying whether to fix the region in the 2-direction. The default value is
    #: OFF.
    u2: Boolean = OFF

    #: A Boolean specifying whether to fix the region in the 3-direction. The default value is
    #: OFF.
    u3: Boolean = OFF

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        csys: Optional[int] = None,
        u1: Boolean = OFF,
        u2: Boolean = OFF,
        u3: Boolean = OFF,
    ):
        """This method creates a BeadFixedRegion object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].BeadFixedRegion

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        u1
            A Boolean specifying whether to fix the region in the 1-direction. The default value is
            OFF.
        u2
            A Boolean specifying whether to fix the region in the 2-direction. The default value is
            OFF.
        u3
            A Boolean specifying whether to fix the region in the 3-direction. The default value is
            OFF.

        Returns
        -------
        BeadFixedRegion
            A :py:class:`~abaqus.Optimization.BeadFixedRegion.BeadFixedRegion` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, csys: Optional[int] = None, u1: Boolean = OFF, u2: Boolean = OFF, u3: Boolean = OFF):
        """This method modifies the BeadFixedRegion object.

        Parameters
        ----------
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        u1
            A Boolean specifying whether to fix the region in the 1-direction. The default value is
            OFF.
        u2
            A Boolean specifying whether to fix the region in the 2-direction. The default value is
            OFF.
        u3
            A Boolean specifying whether to fix the region in the 3-direction. The default value is
            OFF.
        """
        ...
