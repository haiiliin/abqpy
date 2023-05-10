from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import (
    FILLED_CIRCLE,
    ON,
    Boolean,
    SymbolicConstant,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class SymbolStyle:
    """The SymbolStyle object is used to define the marker properties to be used when drawing curves.
    SymbolStyle objects can be created using the methods described below.

    .. note::
        This object can be accessed by::

            import visualization
            session.charts[name].axes1[i].axisData.curves[i].symbolStyle
            session.charts[name].axes2[i].axisData.curves[i].symbolStyle
            session.charts[name].curves[name].symbolStyle
            session.curves[name].symbolStyle
            session.defaultChartOptions.defaultAxis1Options.axisData.curves[i].symbolStyle
            session.defaultChartOptions.defaultAxis2Options.axisData.curves[i].symbolStyle
            session.xyPlots[name].charts[name].axes1[i].axisData.curves[i].symbolStyle
            session.xyPlots[name].charts[name].axes2[i].axisData.curves[i].symbolStyle
            session.xyPlots[name].charts[name].curves[name].symbolStyle
            session.xyPlots[name].curves[name].symbolStyle
    """

    #: A String specifying the color to be used when drawing a marker with this SymbolStyle
    #: object. The default value is "White".
    color: str = ""

    #: A Boolean specifying whether to draw the marker when using this SymbolStyle object. The
    #: default value is ON.
    show: Boolean = ON

    #: A SymbolicConstant specifying the marker type be used when drawing symbols using this
    #: SymbolStyle object. Possible values are:

    #: - FILLED_CIRCLE
    #: - FILLED_SQUARE
    #: - FILLED_DIAMOND
    #: - FILLED_TRI
    #: - HOLLOW_CIRCLE
    #: - HOLLOW_SQUARE
    #: - HOLLOW_DIAMOND
    #: - HOLLOW_TRI
    #: - CROSS
    #: - XMARKER
    #: - POINT
    #:
    #: The default value is FILLED_CIRCLE.
    marker: SymbolicConstant = FILLED_CIRCLE

    #: A Float specifying the marker size to be used when drawing markers using this
    #: SymbolStyle object. The default value is 2.0.
    size: float = 2

    @abaqus_method_doc
    def __init__(
        self,
        color: str = "",
        show: Boolean = ON,
        marker: Literal[
            C.CROSS,
            C.FILLED_DIAMOND,
            C.FILLED_SQUARE,
            C.POINT,
            C.HOLLOW_CIRCLE,
            C.HOLLOW_TRI,
            C.HOLLOW_SQUARE,
            C.FILLED_TRI,
            C.HOLLOW_DIAMOND,
            C.FILLED_CIRCLE,
            C.XMARKER,
        ] = FILLED_CIRCLE,
        size: float = 2,
    ):
        """This method creates a SymbolStyle object.

        .. note::
            This function can be accessed by::

                session.SymbolStyle
                xyPlot.SymbolStyle

        Parameters
        ----------
        color
            A String specifying the color to be used when drawing a marker with this SymbolStyle
            object. The default value is "White".
        show
            A Boolean specifying whether to draw the marker when using this SymbolStyle object. The
            default value is ON.
        marker
            A SymbolicConstant specifying the marker type be used when drawing symbols using this
            SymbolStyle object. Possible values are:

            - FILLED_CIRCLE
            - FILLED_SQUARE
            - FILLED_DIAMOND
            - FILLED_TRI
            - HOLLOW_CIRCLE
            - HOLLOW_SQUARE
            - HOLLOW_DIAMOND
            - HOLLOW_TRI
            - CROSS
            - XMARKER
            - POINT

            The default value is FILLED_CIRCLE.
        size
            A Float specifying the marker size to be used when drawing markers using this
            SymbolStyle object. The default value is 2.0.

        Returns
        -------
        SymbolStyle
            A SymbolStyle object.

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
        marker: Literal[
            C.CROSS,
            C.FILLED_DIAMOND,
            C.FILLED_SQUARE,
            C.POINT,
            C.HOLLOW_CIRCLE,
            C.HOLLOW_TRI,
            C.HOLLOW_SQUARE,
            C.FILLED_TRI,
            C.HOLLOW_DIAMOND,
            C.FILLED_CIRCLE,
            C.XMARKER,
        ] = FILLED_CIRCLE,
        size: float = 2,
    ):
        """This method modifies the SymbolStyle object.

        Parameters
        ----------
        color
            A String specifying the color to be used when drawing a marker with this SymbolStyle
            object. The default value is "White".
        show
            A Boolean specifying whether to draw the marker when using this SymbolStyle object. The
            default value is ON.
        marker
            A SymbolicConstant specifying the marker type be used when drawing symbols using this
            SymbolStyle object. Possible values are:

            - FILLED_CIRCLE
            - FILLED_SQUARE
            - FILLED_DIAMOND
            - FILLED_TRI
            - HOLLOW_CIRCLE
            - HOLLOW_SQUARE
            - HOLLOW_DIAMOND
            - HOLLOW_TRI
            - CROSS
            - XMARKER
            - POINT

            The default value is FILLED_CIRCLE.
        size
            A Float specifying the marker size to be used when drawing markers using this
            SymbolStyle object. The default value is 2.0.
        """
        ...
