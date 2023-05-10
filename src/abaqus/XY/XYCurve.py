from typing import Optional

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import CURVE_LEGEND, ON, Boolean, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .LineStyle import LineStyle
from .SymbolStyle import SymbolStyle
from .XYData import XYData


@abaqus_class_doc
class XYCurve:
    """The XYCurve object is used to plot **X - Y** data and to store its display attributes.

    .. note::
        This object can be accessed by::

            import visualization
            session.charts[name].axes1[i].axisData.curves[i]
            session.charts[name].axes2[i].axisData.curves[i]
            session.charts[name].curves[name]
            session.curves[name]
            session.defaultChartOptions.defaultAxis1Options.axisData.curves[i]
            session.defaultChartOptions.defaultAxis2Options.axisData.curves[i]
            session.xyPlots[name].charts[name].axes1[i].axisData.curves[i]
            session.xyPlots[name].charts[name].axes2[i].axisData.curves[i]
            session.xyPlots[name].charts[name].curves[name]
            session.xyPlots[name].curves[name]
    """

    #: A String specifying the repository key.
    name: str = ""

    #: An Int specifying the frequency of plotting the markers. Possible values are
    #: **symbolFrequency** > 0. If **symbolFrequency** = 1, then markers are plotted at every point.
    #: The default value is 1.
    symbolFrequency: int = 1

    #: A Boolean specifying whether to use the system supplied legend label. The default value
    #: is ON.
    useDefault: Boolean = ON

    #: A SymbolicConstant specifying how the system supplied, default legend label is to be
    #: generated. Possible values are CURVE_LEGEND, CURVE_NAME, and CURVE_NAME_LEGEND. The
    #: default value is CURVE_LEGEND.
    legendSource: SymbolicConstant = CURVE_LEGEND

    #: An XYData object specifying the data for the curve.
    data: Optional[XYData] = None

    #: A LineStyle object specifying the line properties used to display the curve.
    lineStyle: LineStyle = LineStyle()

    #: A SymbolStyle object specifying the symbol properties used to display the curve.
    symbolStyle: SymbolStyle = SymbolStyle()

    #: A String specifying the label to be displayed in the legend. By default, the label is
    #: system defined.
    legendLabel: str = ""

    #: A tuple of SymbolicConstants specifying that describe how curves are to be displayed.
    #: Possible values are LINE and SYMBOL. The default value is (LINE).
    displayTypes: Optional[SymbolicConstant] = None

    @abaqus_method_doc
    def Curve(self, name: str, data: XYData):
        """This method creates an XYCurve object from an XYData object.

        .. note::
            This function can be accessed by::

                session.Curve

        Parameters
        ----------
        name
            A String specifying the repository key.
        data
            An XYData object specifying the data for the curve.

        Returns
        -------
        XYCurve
            An XYCurve object.
        """
        ...

    @abaqus_method_doc
    def setValues(
        self,
        displayTypes: Optional[Literal[C.SYMBOL, C.LINE]] = None,
        legendLabel: str = "",
        symbolFrequency: int = 1,
        useDefault: Boolean = ON,
    ):
        """This method modifies the XYCurve object.

        Parameters
        ----------
        displayTypes
            A sequence of SymbolicConstants specifying that describe how curves are to be displayed.
            Possible values are LINE and SYMBOL. The default value is (LINE).
        legendLabel
            A String specifying the label to be displayed in the legend. By default, the label is
            system defined.
        symbolFrequency
            An Int specifying the frequency of plotting the markers. Possible values are
            **symbolFrequency** > 0. If **symbolFrequency** = 1, then markers are plotted at every point.
            The default value is 1.
        useDefault
            A Boolean specifying whether to use the system supplied legend label. The default value
            is ON.
        """
        ...
