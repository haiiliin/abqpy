from typing_extensions import Literal
from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import Boolean, FREE_FORM, ON, SymbolicConstant


@abaqus_class_doc
class SlideRegionControl(GeometricRestriction):
    """The SlideRegionControl object defines a slide region control geometric restriction.
    The SlideRegionControl object is derived from the GeometricRestriction object.

    .. note:: 
        This object can be accessed by::

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object of length 2 specifying the axis of revolution. Instead of through a
    #: ConstrainedSketchVertex, each point may be specified through a tuple of coordinates. This is used when
    #: **approach** is TURN.
    clientDirection: tuple

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
    #: When used with a TopologyTask, there is no default value. When used with a ShapeTask,
    #: the default value is MODEL.
    region: Region

    #: A SymbolicConstant specifying the restriction approach. The SymbolicConstant FREE_FORM
    #: indicates a free-form slide region, and the SymbolicConstant TURN indicates that the
    #: restriction should conserve a turnable surface. Possible values are FREE_FORM and TURN.
    #: The default value is FREE_FORM.
    approach: SymbolicConstant = FREE_FORM

    #: None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
    #: global coordinate system is used. When this member is queried, it returns an Int. This
    #: is used when **approach** is TURN. The default value is None.
    csys: Optional[int] = None

    #: None or a Region object specifying the free-form region. This is used when **approach** is
    #: FREE_FORM. The default value is None.
    freeFormRegion: Optional[str] = None

    #: A Boolean specifying whether to ignore the geometric restriction in the first design
    #: cycle. The default value is ON.
    presumeFeasibleRegionAtStart: Boolean = ON

    #: None or a Region object specifying the region to revolve into a slide region. This is
    #: used when **approach** is TURN. The default value is None.
    revolvedRegion: Optional[str] = None

    #: A Float specifying the geometric tolerance in the 1-direction. This is used when
    #: **approach** is TURN. The default value is 0.01.
    tolerance1: float = 0

    #: A Float specifying the geometric tolerance in the 2-direction. This is used when
    #: **approach** is TURN. The default value is 0.01.
    tolerance2: float = 0

    #: A Float specifying the geometric tolerance in the 3-direction. This is used when
    #: **approach** is TURN. The default value is 0.01.
    tolerance3: float = 0

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        clientDirection: tuple,
        region: Region,
        approach: Literal[C.FREE_FORM, C.TURN] = FREE_FORM,
        csys: Optional[int] = None,
        freeFormRegion: Optional[str] = None,
        presumeFeasibleRegionAtStart: Boolean = ON,
        revolvedRegion: Optional[str] = None,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
    ):
        """This method creates a SlideRegionControl object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].optimizationTasks[name].SlideRegionControl

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        clientDirection
            A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object of length 2 specifying the axis of revolution. Instead of through a
            ConstrainedSketchVertex, each point may be specified through a tuple of coordinates. This is used when
            **approach** is TURN.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        approach
            A SymbolicConstant specifying the restriction approach. The SymbolicConstant FREE_FORM
            indicates a free-form slide region, and the SymbolicConstant TURN indicates that the
            restriction should conserve a turnable surface. Possible values are FREE_FORM and TURN.
            The default value is FREE_FORM.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. This
            is used when **approach** is TURN. The default value is None.
        freeFormRegion
            None or a Region object specifying the free-form region. This is used when **approach** is
            FREE_FORM. The default value is None.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        revolvedRegion
            None or a Region object specifying the region to revolve into a slide region. This is
            used when **approach** is TURN. The default value is None.
        tolerance1
            A Float specifying the geometric tolerance in the 1-direction. This is used when
            **approach** is TURN. The default value is 0.01.
        tolerance2
            A Float specifying the geometric tolerance in the 2-direction. This is used when
            **approach** is TURN. The default value is 0.01.
        tolerance3
            A Float specifying the geometric tolerance in the 3-direction. This is used when
            **approach** is TURN. The default value is 0.01.

        Returns
        -------
        SlideRegionControl
            A :py:class:`~abaqus.Optimization.SlideRegionControl.SlideRegionControl` object.
        """
        super().__init__()

    @abaqus_method_doc
    def setValues(
        self,
        approach: Literal[C.FREE_FORM, C.TURN] = FREE_FORM,
        csys: Optional[int] = None,
        freeFormRegion: Optional[str] = None,
        presumeFeasibleRegionAtStart: Boolean = ON,
        revolvedRegion: Optional[str] = None,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
    ):
        """This method modifies the SlideRegionControl object.

        Parameters
        ----------
        approach
            A SymbolicConstant specifying the restriction approach. The SymbolicConstant FREE_FORM
            indicates a free-form slide region, and the SymbolicConstant TURN indicates that the
            restriction should conserve a turnable surface. Possible values are FREE_FORM and TURN.
            The default value is FREE_FORM.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. This
            is used when **approach** is TURN. The default value is None.
        freeFormRegion
            None or a Region object specifying the free-form region. This is used when **approach** is
            FREE_FORM. The default value is None.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        revolvedRegion
            None or a Region object specifying the region to revolve into a slide region. This is
            used when **approach** is TURN. The default value is None.
        tolerance1
            A Float specifying the geometric tolerance in the 1-direction. This is used when
            **approach** is TURN. The default value is 0.01.
        tolerance2
            A Float specifying the geometric tolerance in the 2-direction. This is used when
            **approach** is TURN. The default value is 0.01.
        tolerance3
            A Float specifying the geometric tolerance in the 3-direction. This is used when
            **approach** is TURN. The default value is 0.01.
        """
        ...
