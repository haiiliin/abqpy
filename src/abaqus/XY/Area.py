from typing import Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .AreaStyle import AreaStyle
from .LineStyle import LineStyle
from ..UtilityAndView.abaqusConstants import AUTOMATIC, AUTO_ALIGN, BOTTOM_LEFT, Boolean, OFF, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class Area:
    """The Area object is used to display a rectangular area in an XYPlot. The Area object has
    no constructor. Area objects are automatically created whenever a XYPlot, Chart,
    PlotTitle, or Legend objects are created.

    .. note::
        This object can be accessed by::

            import visualization
            session.charts[name].area
            session.charts[name].gridArea
            session.charts[name].legend.area
            session.defaultChartOptions.gridArea
            session.defaultChartOptions.legend.area
            session.defaultPlot.area
            session.defaultPlot.title.area
            session.xyPlots[name].area
            session.xyPlots[name].charts[name].area
            session.xyPlots[name].charts[name].gridArea
            session.xyPlots[name].charts[name].legend.area
            session.xyPlots[name].title.area
    """

    #: A Boolean specifying whether the area is inset or occupies a reserved area. The default
    #: value is OFF.
    inset: Boolean = OFF

    #: A SymbolicConstant specifying how the area is positioned. Possible values are AUTO_ALIGN
    #: and MANUAL. The default value is AUTO_ALIGN.
    positionMethod: SymbolicConstant = AUTO_ALIGN

    #: A SymbolicConstant specifying the relative position of the area in its parent when
    #: **positionMethod** = AUTO_ALIGN. Possible values are:
    #:
    #: - BOTTOM_LEFT
    #: - BOTTOM_CENTER
    #: - BOTTOM_RIGHT
    #: - CENTER_LEFT
    #: - CENTER
    #: - CENTER_RIGHT
    #: - TOP_LEFT
    #: - TOP_CENTER
    #: - TOP_RIGHT
    #:
    #: The default value is BOTTOM_LEFT.
    alignment: SymbolicConstant = BOTTOM_LEFT

    #: A SymbolicConstant specifying how the area size is defined. Possible values are
    #: AUTOMATIC and MANUAL. The default value is AUTOMATIC.
    sizeMethod: SymbolicConstant = AUTOMATIC

    #: A Float specifying the width of the area in mm. The default value is 1.0.
    width: float = 1

    #: A Float specifying the height of the area in mm. The default value is 1.0.
    height: float = 1

    #: A Float specifying the scale as a fraction of the width of the available area when the
    #: sizeMethod=MANUAL. The valid range is (0, 1). The default value is 1.0.
    widthScale: float = 1

    #: A Float specifying the scale as a fraction of the height of the available area when the
    #: **sizeMethod** = MANUAL. The valid range is (0, 1). The default value is 1.0.
    heightScale: float = 1

    #: A Float specifying the left padding of the area in mm. The default value is 1.0.
    pl: float = 1

    #: A Float specifying the right padding of the area in mm. The default value is 1.0.
    pr: float = 1

    #: A Float specifying the top padding of the area in mm. The default value is 1.0.
    pt: float = 1

    #: A Float specifying the bottom padding of the area in mm. The default value is 1.0.
    pb: float = 1

    #: An :py:class:`~abaqus.XY.AreaStyle.AreaStyle` object specifying whether and how to fill the area.
    style: AreaStyle = AreaStyle()

    #: A :py:class:`~abaqus.XY.LineStyle.LineStyle` object specifying whether and how to draw the border of the area.
    border: LineStyle = LineStyle()

    #: A pair of Floats specifying the X- and Y-offsets in millimeters from the lower-left
    #: corner of the XYPlot.
    origin: Sequence[float] = ()

    #: A pair of Floats specifying the X- and Y-offsets of the origin as a fraction of the
    #: available area. The **originOffset** argument is ignored unless **positionMethod** = MANUAL.
    #: The default value is (-1, 0). The valid range for each float is (0, 1).
    originOffset: Sequence[float] = ()

    @abaqus_method_doc
    def setValues(
        self,
        area: "Area",
        style: AreaStyle,
        border: LineStyle,
        positionMethod: Literal[C.MANUAL, C.AUTO_ALIGN] = AUTO_ALIGN,
        alignment: Literal[
            C.CENTER_RIGHT,
            C.TOP_CENTER,
            C.BOTTOM_RIGHT,
            C.BOTTOM_LEFT,
            C.CENTER,
            C.AUTO_ALIGN,
            C.TOP_RIGHT,
            C.CENTER_LEFT,
            C.TOP_LEFT,
            C.BOTTOM_CENTER,
        ] = BOTTOM_LEFT,
        sizeMethod: Literal[C.AUTOMATIC, C.MANUAL] = AUTOMATIC,
        originOffset: Sequence[float] = (),
        widthScale: float = 1,
        heightScale: float = 1,
        inset: Boolean = OFF,
        pl: float = 1,
        pr: float = 1,
        pt: float = 1,
        pb: float = 1,
    ):
        """This method modifies the Area object.

        Parameters
        ----------
        area
            An :py:class:`~abaqus.XY.Area.Area` object from which attributes are to be copied.
        style
            An :py:class:`~abaqus.XY.AreaStyle.AreaStyle` object.
        border
            A :py:class:`~abaqus.XY.LineStyle.LineStyle` object.
        positionMethod
            A SymbolicConstant specifying how the area is positioned. Possible values are AUTO_ALIGN
            and MANUAL. The default value is AUTO_ALIGN.
        alignment
            A SymbolicConstant specifying the relative position of the area in its parent when
            **positionMethod** = AUTO_ALIGN. Possible values are:

            - BOTTOM_LEFT
            - BOTTOM_CENTER
            - BOTTOM_RIGHT
            - CENTER_LEFT
            - CENTER
            - CENTER_RIGHT
            - TOP_LEFT
            - TOP_CENTER
            - TOP_RIGHT

            The default value is BOTTOM_LEFT.
        sizeMethod
            A SymbolicConstant specifying how the area size is defined. Possible values are
            AUTOMATIC and MANUAL. The default value is AUTOMATIC.
        originOffset
            A pair of Floats specifying the X- and Y-offsets of the origin as a fraction of the
            available area. The **originOffset** argument is ignored unless **positionMethod** = MANUAL.
            The default value is (-1, 0). The valid range for each float is (0, 1).
        widthScale
            A Float specifying the scale as a fraction of the width of the available area when the
            sizeMethod=MANUAL. The valid range is (0, 1). The default value is 1.0.
        heightScale
            A Float specifying the scale as a fraction of the height of the available area when the
            **sizeMethod** = MANUAL. The valid range is (0, 1). The default value is 1.0.
        inset
            A Boolean specifying whether the area is inset or occupies a reserved area. The default
            value is OFF.
        pl
            A Float specifying the left padding of the area in mm. The default value is 1.0.
        pr
            A Float specifying the right padding of the area in mm. The default value is 1.0.
        pt
            A Float specifying the top padding of the area in mm. The default value is 1.0.
        pb
            A Float specifying the bottom padding of the area in mm. The default value is 1.0.

        Raises
        ------
        RangeError
        """
        ...
