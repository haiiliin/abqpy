from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import AXIS_1, Boolean, OFF, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class TopologyPlanarSymmetry(GeometricRestriction):
    """The TopologyPlanarSymmetry object defines a topology planar symmetry geometric
    restriction.
    The TopologyPlanarSymmetry object is derived from the GeometricRestriction object.

    .. note:: 
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
    #: When used with a TopologyTask, there is no default value. When used with a ShapeTask,
    #: the default value is MODEL.
    region: Region

    #: A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2,
    #: and AXIS_3. The default value is AXIS_1.
    axis: SymbolicConstant = AXIS_1

    #: None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
    #: global coordinate system is used. When this member is queried, it returns an Int. The
    #: default value is None.
    csys: Optional[int] = None

    #: A Boolean specifying whether to ignore frozen areas. The default value is OFF.
    ignoreFrozenArea: Boolean = OFF

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        axis: Literal[C.AXIS_1, C.AXIS_3, C.AXIS_2] = AXIS_1,
        csys: Optional[int] = None,
        ignoreFrozenArea: Boolean = OFF,
    ):
        """This method creates a TopologyPlanarSymmetry object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].TopologyPlanarSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        axis
            A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2,
            and AXIS_3. The default value is AXIS_1.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns
        -------
        TopologyPlanarSymmetry
            A :py:class:`~abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        axis: Literal[C.AXIS_1, C.AXIS_3, C.AXIS_2] = AXIS_1,
        csys: Optional[int] = None,
        ignoreFrozenArea: Boolean = OFF,
    ):
        """This method modifies the TopologyPlanarSymmetry object.

        Parameters
        ----------
        axis
            A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS_1, AXIS_2,
            and AXIS_3. The default value is AXIS_1.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        ignoreFrozenArea
            A Boolean specifying whether to ignore frozen areas. The default value is OFF.
        """
        ...
