from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Area import Area
from .TextStyle import TextStyle
from ..UtilityAndView.abaqusConstants import AUTOMATIC, Boolean, OFF, ON, SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class Legend:
    """The Legend object is used to store the display attributes of the chart legend. A legend
    object is automatically created when creating a Chart object.

    .. note::
        This object can be accessed by::

            import visualization
            session.charts[name].legend
            session.defaultChartOptions.legend
            session.xyPlots[name].charts[name].legend
    """

    #: A SymbolicConstant specifying how the minimum and maximum values are formatted. Possible
    #: values are AUTOMATIC, DECIMAL, SCIENTIFIC, and ENGINEERING. The default value is
    #: AUTOMATIC.
    numberFormat: SymbolicConstant = AUTOMATIC

    #: An Int specifying the number of significant digits displayed for the minimum and maximum
    #: values. Possible values are 1 to 7. The default value is 2.
    numDigits: int = 2

    #: A Boolean specifying whether to show the legend. The default value is ON.
    show: Boolean = ON

    #: A Boolean specifying whether to display the minimum and maximum values. The default
    #: value is OFF.
    showMinMax: Boolean = OFF

    #: An Area object specifying the area of the legend.
    area: Area = Area()

    #: A TextStyle object specifying the text properties used to display the legend text.
    textStyle: TextStyle = TextStyle()

    #: A String specifying the title to appear on the legend. The default value is an empty
    #: string.
    title: str = ""

    #: A TextStyle object specifying the text properties used to display the legend title.
    titleStyle: TextStyle = TextStyle()

    @abaqus_method_doc
    def setValues(
        self,
        legend: "Legend",
        show: Boolean = ON,
        showMinMax: Boolean = OFF,
        title: str = "",
        numberFormat: Literal[C.SCIENTIFIC, C.AUTOMATIC, C.ENGINEERING, C.DECIMAL] = AUTOMATIC,
        numDigits: int = 2,
        textStyle: Optional[TextStyle] = None,
        titleStyle: Optional[TextStyle] = None,
    ):
        """This method modifies the Legend object.

        Parameters
        ----------
        legend
            A Legend object from which attributes are to be copied.
        show
            A Boolean specifying whether to show the legend. The default value is ON.
        showMinMax
            A Boolean specifying whether to display the minimum and maximum values. The default
            value is OFF.
        title
            A String specifying the title to appear on the legend. The default value is an empty
            string.
        numberFormat
            A SymbolicConstant specifying how the minimum and maximum values are formatted. Possible
            values are AUTOMATIC, DECIMAL, SCIENTIFIC, and ENGINEERING. The default value is
            AUTOMATIC.
        numDigits
            An Int specifying the number of significant digits displayed for the minimum and maximum
            values. Possible values are 1 to 7. The default value is 2.
        textStyle
            A TextStyle object specifying the text properties used to display the legend text.
        titleStyle
            A TextStyle object specifying the text properties used to display the legend title.
        """
        ...
