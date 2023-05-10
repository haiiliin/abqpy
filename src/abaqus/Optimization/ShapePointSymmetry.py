from typing import Optional

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import MAXIMUM, ON, Boolean, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .GeometricRestriction import GeometricRestriction


@abaqus_class_doc
class ShapePointSymmetry(GeometricRestriction):
    """The ShapePointSymmetry object defines a shape point symmetry geometric restriction. The
    ShapePointSymmetry object is derived from the GeometricRestriction object.

    .. note::
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A Region object specifying the region to which the geometric restriction is applied.
    #: When used with a TopologyTask, there is no default value. When used with a ShapeTask,
    #: the default value is MODEL.
    region: Region

    #: None or a DatumCsys object specifying the symmetry point represented as the origin of a
    #: local coordinate system. If **csys** = None, the global coordinate system is used. When this
    #: member is queried, it returns an Int. The default value is None.
    csys: Optional[int] = None

    #: A SymbolicConstant specifying the rule for determining the master node. Possible values
    #: are MAXIMUM and MINIMUM. The default value is MAXIMUM.
    masterPointDetermination: SymbolicConstant = MAXIMUM

    #: A Boolean specifying whether to ignore the geometric restriction in the first design
    #: cycle. The default value is ON.
    presumeFeasibleRegionAtStart: Boolean = ON

    #: A Float specifying the geometric tolerance in the 1-direction. The default value is
    #: 0.01.
    tolerance1: float = 0

    #: A Float specifying the geometric tolerance in the 2-direction. The default value is
    #: 0.01.
    tolerance2: float = 0

    #: A Float specifying the geometric tolerance in the 3-direction. The default value is
    #: 0.01.
    tolerance3: float = 0

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        csys: Optional[int] = None,
        masterPointDetermination: Literal[C.MINIMUM, C.MAXIMUM] = MAXIMUM,
        presumeFeasibleRegionAtStart: Boolean = ON,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
    ):
        """This method creates a ShapePointSymmetry object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].ShapePointSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        csys
            None or a DatumCsys object specifying the symmetry point represented as the origin of a
            local coordinate system. If **csys** = None, the global coordinate system is used. When this
            member is queried, it returns an Int. The default value is None.
        masterPointDetermination
            A SymbolicConstant specifying the rule for determining the master node. Possible values
            are MAXIMUM and MINIMUM. The default value is MAXIMUM.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        tolerance1
            A Float specifying the geometric tolerance in the 1-direction. The default value is
            0.01.
        tolerance2
            A Float specifying the geometric tolerance in the 2-direction. The default value is
            0.01.
        tolerance3
            A Float specifying the geometric tolerance in the 3-direction. The default value is
            0.01.

        Returns
        -------
        ShapePointSymmetry
            A ShapePointSymmetry object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        csys: Optional[int] = None,
        masterPointDetermination: Literal[C.MINIMUM, C.MAXIMUM] = MAXIMUM,
        presumeFeasibleRegionAtStart: Boolean = ON,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
    ):
        """This method modifies the ShapePointSymmetry object.

        Parameters
        ----------
        csys
            None or a DatumCsys object specifying the symmetry point represented as the origin of a
            local coordinate system. If **csys** = None, the global coordinate system is used. When this
            member is queried, it returns an Int. The default value is None.
        masterPointDetermination
            A SymbolicConstant specifying the rule for determining the master node. Possible values
            are MAXIMUM and MINIMUM. The default value is MAXIMUM.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        tolerance1
            A Float specifying the geometric tolerance in the 1-direction. The default value is
            0.01.
        tolerance2
            A Float specifying the geometric tolerance in the 2-direction. The default value is
            0.01.
        tolerance3
            A Float specifying the geometric tolerance in the 3-direction. The default value is
            0.01.
        """
        ...
