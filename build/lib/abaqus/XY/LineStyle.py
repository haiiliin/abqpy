from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import Boolean, ON, SOLID, SymbolicConstant


@abaqus_class_doc
class LineStyle:
    """The LineStyle object is used to define the line style to be used for drawing XY-Plot
    objects.
    LineStyle objects can be created using the methods described below.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.charts[name].area.border
            session.charts[name].axes1[i].axisData.curves[i].lineStyle
            session.charts[name].axes1[i].lineStyle
            session.charts[name].axes1[i].tickStyle
            session.charts[name].axes2[i].axisData.curves[i].lineStyle
            session.charts[name].axes2[i].lineStyle
            session.charts[name].axes2[i].tickStyle
            session.charts[name].curves[name].lineStyle
            session.charts[name].gridArea.border
            session.charts[name].legend.area.border
            session.charts[name].majorAxis1GridStyle
            session.charts[name].majorAxis2GridStyle
            session.charts[name].minorAxis1GridStyle
            session.charts[name].minorAxis2GridStyle
            session.charts[name].tagBorder
            session.curves[name].lineStyle
            session.defaultChartOptions.defaultAxis1Options.axisData.curves[i].lineStyle
            session.defaultChartOptions.defaultAxis1Options.lineStyle
            session.defaultChartOptions.defaultAxis1Options.tickStyle
            session.defaultChartOptions.defaultAxis2Options.axisData.curves[i].lineStyle
            session.defaultChartOptions.defaultAxis2Options.lineStyle
            session.defaultChartOptions.defaultAxis2Options.tickStyle
            session.defaultChartOptions.gridArea.border
            session.defaultChartOptions.legend.area.border
            session.defaultChartOptions.majorAxis1GridStyle
            session.defaultChartOptions.majorAxis2GridStyle
            session.defaultChartOptions.minorAxis1GridStyle
            session.defaultChartOptions.minorAxis2GridStyle
            session.defaultChartOptions.tagBorder
            session.defaultPlot.area.border
            session.defaultPlot.title.area.border
            session.xyPlots[name].area.border
            session.xyPlots[name].charts[name].area.border
            session.xyPlots[name].charts[name].axes1[i].axisData.curves[i].lineStyle
            session.xyPlots[name].charts[name].axes1[i].lineStyle
            session.xyPlots[name].charts[name].axes1[i].tickStyle
            session.xyPlots[name].charts[name].axes2[i].axisData.curves[i].lineStyle
            session.xyPlots[name].charts[name].axes2[i].lineStyle
            session.xyPlots[name].charts[name].axes2[i].tickStyle
            session.xyPlots[name].charts[name].curves[name].lineStyle
            session.xyPlots[name].charts[name].gridArea.border
            session.xyPlots[name].charts[name].legend.area.border
            session.xyPlots[name].charts[name].majorAxis1GridStyle
            session.xyPlots[name].charts[name].majorAxis2GridStyle
            session.xyPlots[name].charts[name].minorAxis1GridStyle
            session.xyPlots[name].charts[name].minorAxis2GridStyle
            session.xyPlots[name].charts[name].tagBorder
            session.xyPlots[name].curves[name].lineStyle
            session.xyPlots[name].title.area.border
    """

    #: A String specifying the color to be used when drawing a line with this LineStyle object.
    #: The default value is "White".
    color: str = ""

    #: A Boolean specifying whether to draw the line when using this LineStyle. The default
    #: value is ON.
    show: Boolean = ON

    #: A SymbolicConstant specifying the line style to be used when drawing lines using this
    #: LineStyle. Possible values are SOLID, DASHED, DOTTED, and DOT_DASH. The default value is
    #: SOLID.
    style: SymbolicConstant = SOLID

    #: A Float specifying the line thickness in mm to be used when drawing lines using this
    #: LineStyle. The default value is 0.2.
    thickness: float = 0

    @abaqus_method_doc
    def __init__(
        self,
        color: str = "",
        show: Boolean = ON,
        style: SymbolicConstant = SOLID,
        thickness: float = 0,
    ):
        """This method creates a LineStyle.

        .. note:: 
            This function can be accessed by::

                session.LineStyle
                xyPlot.LineStyle

        Parameters
        ----------
        color
            A String specifying the color to be used when drawing a line with this LineStyle object.
            The default value is "White".
        show
            A Boolean specifying whether to draw the line when using this LineStyle. The default
            value is ON.
        style
            A SymbolicConstant specifying the line style to be used when drawing lines using this
            LineStyle. Possible values are SOLID, DASHED, DOTTED, and DOT_DASH. The default value is
            SOLID.
        thickness
            A Float specifying the line thickness in mm to be used when drawing lines using this
            LineStyle. The default value is 0.2.

        Returns
        -------
        LineStyle
            A :py:class:`~abaqus.XY.LineStyle.LineStyle` object.

        Raises
        ------
        ColorError
        """
        ...

    @abaqus_method_doc
    def setValues(
        self,
        color: str = "",
        show: Boolean = ON,
        style: SymbolicConstant = SOLID,
        thickness: float = 0,
    ):
        """This method modifies the LineStyle object.

        Parameters
        ----------
        color
            A String specifying the color to be used when drawing a line with this LineStyle object.
            The default value is "White".
        show
            A Boolean specifying whether to draw the line when using this LineStyle. The default
            value is ON.
        style
            A SymbolicConstant specifying the line style to be used when drawing lines using this
            LineStyle. Possible values are SOLID, DASHED, DOTTED, and DOT_DASH. The default value is
            SOLID.
        thickness
            A Float specifying the line thickness in mm to be used when drawing lines using this
            LineStyle. The default value is 0.2.
        """
        ...
