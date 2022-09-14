from abqpy.decorators import abaqus_class_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class DGSymbolOptions:
    """The DGSymbolOptions object stores values and attributes associated with a symbol plot.
    The DGSymbolOptions object has no constructor command. Abaqus creates an
    *odbDisplayOptions.symbolOptions* member when a display group instance is created, using
    values from *odbDisplay.symbolOptions*.

    .. note:: 
        This object can be accessed by::

            session.viewports[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions.symbolOptions
            session.viewports[name].layers[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions.symbolOptions
            session.viewports[name].layers[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions.symbolOptions
            session.viewports[name].layers[name].partDisplay.displayGroupInstances[name].odbDisplayOptions.symbolOptions
            session.viewports[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions.symbolOptions
            session.viewports[name].partDisplay.displayGroupInstances[name].odbDisplayOptions.symbolOptions
    """

    #: A SymbolicConstant specifying the vector line thickness. Possible values are VERY_THIN,
    #: THIN, MEDIUM, and THICK. The default value is VERY_THIN.
    vectorLineThickness: SymbolicConstant = VERY_THIN

    #: A SymbolicConstant specifying the vector color method. Possible values are UNIFORM and
    #: SPECTRUM. The default value is SPECTRUM.
    vectorColorMethod: SymbolicConstant = SPECTRUM

    #: A SymbolicConstant specifying the tensor color method. Possible values are UNIFORM and
    #: SPECTRUM. The default value is SPECTRUM.
    tensorColorMethod: SymbolicConstant = SPECTRUM

    #: A SymbolicConstant specifying the vector arrowhead style. Possible values are NONE,
    #: FILLED, and WIRE. The default value is WIRE.
    vectorArrowheadStyle: SymbolicConstant = WIRE

    #: An Int specifying the length of vector and tensor symbols. The default value is 6.
    arrowSymbolSize: int = 6

    #: An Int specifying the number of color intervals for vector symbols. The default value is
    #: 12.
    vectorIntervalNumber: int = 12

    #: A Float specifying the factor for randomized sampling. The default value is 1.0.
    symbolDensity: float = 1

    #: A Boolean specifying whether to use constant-length arrows for vector symbols. The
    #: default value is OFF.
    constantLengthArrows: Boolean = OFF

    #: An Int specifying the number of color intervals for tensor symbols. The default value is
    #: 12.
    tensorIntervalNumber: int = 12

    #: A SymbolicConstant specifying the line thickness of the tensor symbols. Possible values
    #: are VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.
    tensorLineThickness: SymbolicConstant = VERY_THIN

    #: A SymbolicConstant specifying the arrowhead style of the tensor symbols. Possible values
    #: are NONE, FILLED, and WIRE. The default value is WIRE.
    tensorArrowheadStyle: SymbolicConstant = WIRE

    #: A SymbolicConstant specifying the number format for tensor. Possible values are
    #: SCIENTIFIC, FIXED, and ENGINEERING. The default value is SCIENTIFIC.
    numberFormatT: SymbolicConstant = SCIENTIFIC

    #: A SymbolicConstant specifying the number format for vector. Possible values are
    #: SCIENTIFIC, FIXED, and ENGINEERING. The default value is SCIENTIFIC.
    numberFormatV: SymbolicConstant = SCIENTIFIC

    #: A SymbolicConstant specifying the arrow scaling mode. Possible values are MODEL_SIZE and
    #: SCREEN_SIZE. The default value is MODEL_SIZE.
    arrowScaleMode: SymbolicConstant = MODEL_SIZE

    #: A Boolean specifying whether to draw tensor labels. The default value is OFF.
    drawLabelT: Boolean = OFF

    #: A Boolean specifying whether to draw vector labels. The default value is OFF.
    drawLabelV: Boolean = OFF

    #: An Int specifying the number of digits in the tensor label. The default value is 2.
    numDigitsT: int = 2

    #: An Int specifying the number of digits in the vector label. The default value is 2.
    numDigitsV: int = 2

    #: A String specifying the vector color. The default value is "Red".
    vectorColor: str = ""

    #: A String specifying the vector color spectrum name. The default value is "Rainbow".
    vectorColorSpectrum: str = ""

    #: A String specifying the tensor color spectrum name. The default value is "Rainbow".
    tensorColorSpectrum: str = ""

    #: A String specifying the text color for tensor. The default value is "Yellow".
    textColorT: str = ""

    #: A String specifying the text color for vector. The default value is "Yellow".
    textColorV: str = ""

    #: A String specifying the text font for tensor. The default value is "verdana".
    textFontT: str = ""

    #: A String specifying the text font for vector. The default value is "verdana".
    textFontV: str = ""

    #: A String specifying the color of the maximum principal tensor symbols. The default value
    #: is "Red".
    tensorMaxPrinColor: str = ""

    #: A String specifying the color of the minimum principal tensor symbols. The default value
    #: is "Cyan".
    tensorMinPrinColor: str = ""

    #: A String specifying the color of the intermediate principal tensor symbols. The default
    #: value is "Yellow".
    tensorMidPrinColor: str = ""

    #: A String specifying the color of the selected principal tensor symbols. The default
    #: value is "Red".
    tensorSelectedPrinColor: str = ""
