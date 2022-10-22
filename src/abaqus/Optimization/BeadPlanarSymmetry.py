from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import AXIS_1, SymbolicConstant


@abaqus_class_doc
class BeadPlanarSymmetry(GeometricRestriction):
    """The BeadPlanarSymmetry object defines a bead planar symmetry geometric restriction.
    The BeadPlanarSymmetry object is derived from the GeometricRestriction object.

    .. note:: 
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
    region: Region

    #: A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2,
    #: and AXIS_3. The default value is AXIS_1.
    axis: SymbolicConstant = AXIS_1

    #: None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
    #: global coordinate system is used. When this member is queried, it returns an Int. The
    #: default value is None.
    csys: Optional[int] = None

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        axis: SymbolicConstant = AXIS_1,
        csys: Optional[int] = None,
    ):
        """This method creates a BeadPlanarSymmetry object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].BeadPlanarSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
        axis
            A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2,
            and AXIS_3. The default value is AXIS_1.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.

        Returns
        -------
        BeadPlanarSymmetry
            A :py:class:`~abaqus.Optimization.BeadPlanarSymmetry.BeadPlanarSymmetry` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(self, axis: SymbolicConstant = AXIS_1, csys: Optional[int] = None):
        """This method modifies the BeadPlanarSymmetry object.

        Parameters
        ----------
        axis
            A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2,
            and AXIS_3. The default value is AXIS_1.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        """
        ...
