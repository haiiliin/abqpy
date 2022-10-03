from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Area import Area
from .AreaStyle import AreaStyle
from .Axis import Axis
from .Legend import Legend
from .LineStyle import LineStyle
from .TextStyle import TextStyle
from ..UtilityAndView.abaqusConstants import Boolean, ON


@abaqus_class_doc
class DefaultChartOptions:
    """The DefaultChartOptions object is used to hold on default chart and axis attributes. The
    DefaultChartOptions object attributes are used whenever Chart or Axis are created. A
    DefaultChartOptions object is automatically created when opening a session.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.defaultChartOptions
    """

    areaStyle: AreaStyle = AreaStyle()

    @abaqus_method_doc
    def setValues(
        self,
        areaStyle: AreaStyle,
        aspectRatio: Optional[float] = None,
        defaultAxis1Options: Optional[Axis] = None, 
        defaultAxis2Options: Optional[Axis] = None, 
        gridArea: Optional[Area] = None, 
        legend: Optional[Legend] = None, 
        majorAxis1GridStyle: Optional[LineStyle] = None, 
        majorAxis2GridStyle: Optional[LineStyle] = None, 
        minorAxis1GridStyle: Optional[LineStyle] = None, 
        minorAxis2GridStyle: Optional[LineStyle] = None, 
        tagAreaStyle: Optional[AreaStyle] = None, 
        tagBorder: Optional[LineStyle] = None, 
        tagTextStyle: Optional[TextStyle] = None, 
        useQuantityType: Boolean = ON,
    ):
        """This method modifies the DefaultChartOptions object.

        Parameters
        ----------
        areaStyle
            An :py:class:`~abaqus.XY.AreaStyle.AreaStyle` object specifying an AreaStyle used to hold on to the default display
            properties for the chart area.
        aspectRatio
            A Float specifying the default aspect ratio of the grid area. A value of -1 specifies
            that the gridArea will take up all available space. The default value is −1.
        defaultAxis1Options
            An :py:class:`~abaqus.XY.Axis.Axis` object specifying an Axis object used to hold on to the default properties for
            direction 1 axes—the abscissa for a Cartesian chart.
        defaultAxis2Options
            An :py:class:`~abaqus.XY.Axis.Axis` object specifying an Axis object used to hold on to the default properties for
            direction 2 axes—the ordinate for a Cartesian chart.
        gridArea
            An :py:class:`~abaqus.XY.Area.Area` object specifying how to display the grid area by default.
        legend
            A :py:class:`~abaqus.XY.Legend.Legend` object specifying the default attributes for the legend of the chart.
        majorAxis1GridStyle
            A :py:class:`~abaqus.XY.LineStyle.LineStyle` object specifying the default line properties to be used when drawing major
            gridlines along axis 1.
        majorAxis2GridStyle
            A :py:class:`~abaqus.XY.LineStyle.LineStyle` object specifying the default line properties to be used when drawing major
            gridlines along axis 2.
        minorAxis1GridStyle
            A :py:class:`~abaqus.XY.LineStyle.LineStyle` object specifying the default line properties to be used when drawing minor
            gridlines along axis 1.
        minorAxis2GridStyle
            A :py:class:`~abaqus.XY.LineStyle.LineStyle` object specifying the default line properties to be used when drawing minor
            gridlines along axis 2.
        tagAreaStyle
            An :py:class:`~abaqus.XY.AreaStyle.AreaStyle` object specifying the default area properties to be used when creating
            tags.
        tagBorder
            A :py:class:`~abaqus.XY.LineStyle.LineStyle` object specifying the default tag area border properties to be used when
            creating tags.
        tagTextStyle
            A :py:class:`~abaqus.XY.TextStyle.TextStyle` object specifying the default text properties to be used when creating tags.
        useQuantityType
            A Boolean specifying whether to use the QuantityType to associate curves with axes. The
            default value is ON.
        """
        ...
