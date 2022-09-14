from abqpy.decorators import abaqus_class_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class DGDisplayBodyOptions:
    """The DGDisplayBodyOptions object stores values and attributes applied to display bodies.
    The DGDisplayBodyOptions object has no constructor command. Abaqus creates an
    *odbDisplayOptions.displayBodyOptions* member when a display group instance is created,
    using values from *odbDisplay.displayBodyOptions*.

    .. note:: 
        This object can be accessed by::

            session.viewports[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions.displayBodyOptions
            session.viewports[name].layers[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions.displayBodyOptions
            session.viewports[name].layers[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions.displayBodyOptions
            session.viewports[name].layers[name].partDisplay.displayGroupInstances[name].odbDisplayOptions.displayBodyOptions
            session.viewports[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions.displayBodyOptions
            session.viewports[name].partDisplay.displayGroupInstances[name].odbDisplayOptions.displayBodyOptions
    """

    #: A SymbolicConstant specifying which edges to plot. Possible values are ALL, EXTERIOR,
    #: FEATURE, FREE, and NONE. The default value is EXTERIOR.NONE can be used only when
    #: **renderStyle** = SHADED.
    visibleEdges: SymbolicConstant = EXTERIOR

    #: A SymbolicConstant specifying the edge line style. Possible values are SOLID, DASHED,
    #: DOTTED, and DOT_DASH. The default value is SOLID.
    edgeLineStyle: SymbolicConstant = SOLID

    #: A SymbolicConstant specifying the edge line thickness. Possible values are VERY_THIN,
    #: THIN, MEDIUM, and THICK. The default value is VERY_THIN.
    edgeLineThickness: SymbolicConstant = VERY_THIN

    #: A Boolean specifying whether to allow color coded items in the output database to
    #: override the edge and fill color settings. The default value is ON.
    colorCodeOverride: Boolean = ON

    #: A Boolean specifying whether elements are displayed in a shrunk format. The default
    #: value is OFF.
    elementShrink: Boolean = OFF

    #: An Int specifying the percentage to shrink the elements when **elementShrink** = ON.
    #: Possible values are 0≤ **elementShrinkPercentage** ≤ 90. The default value is 5.
    elementShrinkFactor: int = 5

    #: A Boolean specifying whether to scale coordinates. The default value is OFF.
    coordinateScale: Boolean = OFF

    #: A Boolean specifying whether to set translucency. The default value is OFF.
    translucency: Boolean = OFF

    #: A Float specifying the translucency factor when **translucency** = ON. Possible values are
    #: 0.0≤ **translucencyFactor** ≤ 1.0. The default value is 0.3.
    translucencyFactor: float = 0

    #: A String specifying the color to be used to plot the edges of the model when
    #: **renderStyle** = WIREFRAME or HIDDEN. The default value is "White".
    edgeColorWireHide: str = ""

    #: A String specifying the color to be used to plot the edges of the model when
    #: **renderStyle** = FILLED or SHADED. The default value is "Black".
    edgeColorFillShade: str = ""

    #: A String specifying the color to be used to fill elements when **renderStyle** = FILLED or
    #: SHADED. The default value is "White".
    fillColor: str = ""

    #: A tuple of three Floats specifying the coordinate scaling in each of the three
    #: coordinate directions when **coordinateScale** = ON. The default value is (1, 1, 1).
    coordinateScaleFactors: float = None
