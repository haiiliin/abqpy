from typing import Optional

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import (
    MAXIMUM,
    ON,
    VECTOR,
    Boolean,
    SymbolicConstant,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .GeometricRestriction import GeometricRestriction


@abaqus_class_doc
class DesignDirection(GeometricRestriction):
    """The DesignDirection object defines a design direction geometric restriction. The DesignDirection object
    is derived from the GeometricRestriction object.

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

    #: None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
    #: global coordinate system is used. When this member is queried, it returns an Int. The
    #: default value is None.
    csys: Optional[int] = None

    #: None or a Region object specifying the master point used when **masterPointDetermination** is
    #: SPECIFY. The default value is None.
    masterPoint: Optional[str] = None

    #: A SymbolicConstant specifying the rule for assigning point priority. Possible values are
    #: MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.
    masterPointDetermination: SymbolicConstant = MAXIMUM

    #: A SymbolicConstant specifying whether movement in the region should follow only the
    #: direction of the **masterPoint**, only the magnitude, or both the magnitude of the
    #: **masterPoint** and the directions specified by **u1**, **u2** and **u3**. Possible values are
    #: DIRECTION, MAGNITUDE, and VECTOR. The default value is VECTOR.
    movementRestriction: SymbolicConstant = VECTOR

    #: A Boolean specifying whether to ignore the geometric restriction in the first design
    #: cycle. The default value is ON.
    presumeFeasibleRegionAtStart: Boolean = ON

    #: A Boolean specifying whether movement in the region should follow the **masterPoint** in
    #: the 1-direction. This is used when **movementRestriction** is VECTOR. The default value is
    #: ON.
    u1: Boolean = ON

    #: A Boolean specifying whether movement in the region should follow the **masterPoint** in
    #: the 2-direction. This is used when **movementRestriction** is VECTOR. The default value is
    #: ON.
    u2: Boolean = ON

    #: A Boolean specifying whether movement in the region should follow the **masterPoint** in
    #: the 3-direction. This is used when **movementRestriction** is VECTOR. The default value is
    #: ON.
    u3: Boolean = ON

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        region: Region,
        csys: Optional[int] = None,
        masterPoint: Optional[str] = None,
        masterPointDetermination: Literal[C.SPECIFY, C.MINIMUM, C.MAXIMUM] = MAXIMUM,
        movementRestriction: Literal[C.MAGNITUDE, C.DIRECTION, C.VECTOR] = VECTOR,
        presumeFeasibleRegionAtStart: Boolean = ON,
        u1: Boolean = ON,
        u2: Boolean = ON,
        u3: Boolean = ON,
    ):
        """This method creates a DesignDirection object.

        .. note::
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].DesignDirection

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        region
            A Region object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        masterPoint
            None or a Region object specifying the master point used when **masterPointDetermination** is
            SPECIFY. The default value is None.
        masterPointDetermination
            A SymbolicConstant specifying the rule for assigning point priority. Possible values are
            MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.
        movementRestriction
            A SymbolicConstant specifying whether movement in the region should follow only the
            direction of the **masterPoint**, only the magnitude, or both the magnitude of the
            **masterPoint** and the directions specified by **u1**, **u2** and **u3**. Possible values are
            DIRECTION, MAGNITUDE, and VECTOR. The default value is VECTOR.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        u1
            A Boolean specifying whether movement in the region should follow the **masterPoint** in
            the 1-direction. This is used when **movementRestriction** is VECTOR. The default value is
            ON.
        u2
            A Boolean specifying whether movement in the region should follow the **masterPoint** in
            the 2-direction. This is used when **movementRestriction** is VECTOR. The default value is
            ON.
        u3
            A Boolean specifying whether movement in the region should follow the **masterPoint** in
            the 3-direction. This is used when **movementRestriction** is VECTOR. The default value is
            ON.

        Returns
        -------
        DesignDirection
            A DesignDirection object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        csys: Optional[int] = None,
        masterPoint: Optional[str] = None,
        masterPointDetermination: Literal[C.SPECIFY, C.MINIMUM, C.MAXIMUM] = MAXIMUM,
        movementRestriction: Literal[C.MAGNITUDE, C.DIRECTION, C.VECTOR] = VECTOR,
        presumeFeasibleRegionAtStart: Boolean = ON,
        u1: Boolean = ON,
        u2: Boolean = ON,
        u3: Boolean = ON,
    ):
        """This method modifies the DesignDirection object.

        Parameters
        ----------
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        masterPoint
            None or a Region object specifying the master point used when **masterPointDetermination** is
            SPECIFY. The default value is None.
        masterPointDetermination
            A SymbolicConstant specifying the rule for assigning point priority. Possible values are
            MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.
        movementRestriction
            A SymbolicConstant specifying whether movement in the region should follow only the
            direction of the **masterPoint**, only the magnitude, or both the magnitude of the
            **masterPoint** and the directions specified by **u1**, **u2** and **u3**. Possible values are
            DIRECTION, MAGNITUDE, and VECTOR. The default value is VECTOR.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        u1
            A Boolean specifying whether movement in the region should follow the **masterPoint** in
            the 1-direction. This is used when **movementRestriction** is VECTOR. The default value is
            ON.
        u2
            A Boolean specifying whether movement in the region should follow the **masterPoint** in
            the 2-direction. This is used when **movementRestriction** is VECTOR. The default value is
            ON.
        u3
            A Boolean specifying whether movement in the region should follow the **masterPoint** in
            the 3-direction. This is used when **movementRestriction** is VECTOR. The default value is
            ON.
        """
        ...
