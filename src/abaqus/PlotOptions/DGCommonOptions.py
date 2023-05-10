from typing import Optional

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import (
    ELEMENT,
    EXTERIOR,
    HOLLOW_CIRCLE,
    MEDIUM,
    OFF,
    ON,
    SHADED,
    SMALL,
    SOLID,
    VERY_THIN,
    WIRE,
    Boolean,
    SymbolicConstant,
)


@abaqus_class_doc
class DGCommonOptions:
    """The DGCommonOptions object stores values and attributes that are common to all plot
    states. The DGCommonOptions object has no constructor command. Abaqus creates an
    *odbDisplayOptions.commonOptions* member when a display group instance is created, using
    values from *odbDisplay.commonOptions*.

    .. note::
        This object can be accessed by::

            session.viewports[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions.commonOptions
            session.viewports[name].layers[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions.commonOptions
            session.viewports[name].layers[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions.commonOptions
            session.viewports[name].layers[name].partDisplay.displayGroupInstances[name].odbDisplayOptions.commonOptions
            session.viewports[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions.commonOptions
            session.viewports[name].partDisplay.displayGroupInstances[name].odbDisplayOptions.commonOptions
    """

    #: A SymbolicConstant specifying the render style of the plot. Possible values are
    #: WIREFRAME, FILLED, HIDDEN, and SHADED. The default value is SHADED.
    renderStyle: SymbolicConstant = SHADED

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

    #: A Boolean specifying whether to plot the element labels. The default value is OFF.
    elemLabels: Boolean = OFF

    #: A Boolean specifying whether to plot the face labels. The default value is OFF.
    faceLabels: Boolean = OFF

    #: A Boolean specifying whether to plot the node labels. The default value is OFF.
    nodeLabels: Boolean = OFF

    #: A Boolean specifying whether to plot the node symbols. The default value is OFF.
    nodeSymbols: Boolean = OFF

    #: A SymbolicConstant specifying the node symbol types. Possible values
    #: are:FILLED_CIRCLEFILLED_SQUAREFILLED_DIAMONDFILLED_TRIHOLLOW_CIRCLEHOLLOW_SQUAREHOLLOW_DIAMONDHOLLOW_TRICROSSXMARKERThe
    #: default value is HOLLOW_CIRCLE.
    nodeSymbolType: SymbolicConstant = HOLLOW_CIRCLE

    #: A SymbolicConstant specifying the node symbol size. Possible values are SMALL, MEDIUM,
    #: and LARGE. The default value is SMALL.
    nodeSymbolSize: SymbolicConstant = SMALL

    #: A Boolean specifying whether elements are displayed in a shrunk format. The default
    #: value is OFF.
    elementShrink: Boolean = OFF

    #: An Int specifying the percentage to shrink the elements when **elementShrink** = ON.
    #: Possible values are 0≤ **elementShrinkPercentage** ≤ 90. The default value is 5.
    elementShrinkFactor: int = 5

    #: A Boolean specifying whether to scale coordinates. The default value is OFF.
    coordinateScale: Boolean = OFF

    #: A Boolean specifying whether to draw arrows that indicate the directions of element and
    #: surface normals. The default value is OFF.
    normals: Boolean = OFF

    #: A SymbolicConstant specifying whether to draw element normals or surface normals.
    #: Possible values are ELEMENT and SURFACE. The default value is ELEMENT.
    normalDisplay: SymbolicConstant = ELEMENT

    #: A SymbolicConstant specifying the length of the normal arrows. Possible values are
    #: SHORT, MEDIUM, and LONG. The default value is MEDIUM.
    normalArrowLength: SymbolicConstant = MEDIUM

    #: A SymbolicConstant specifying the thickness of the normal arrows. Possible values are
    #: VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.
    normalLineThickness: SymbolicConstant = VERY_THIN

    #: A SymbolicConstant specifying the arrowhead style of the normal arrows. Possible values
    #: are NONE, FILLED, and WIRE. The default value is WIRE.
    normalArrowheadStyle: SymbolicConstant = WIRE

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

    #: A String specifying the label font to be used for all model labels. The default value is
    #: "-*-courier-medium-r-normal-*-*-120-*-*-m-*-*-*".
    labelFont: str = ""

    #: A String specifying the color to be used to plot the element labels. The default value
    #: is "Cyan".
    elemLabelColor: str = ""

    #: A String specifying the color to be used to plot the face labels. The default value is
    #: "Red".
    faceLabelColor: str = ""

    #: A String specifying the color to be used to plot the node labels. The default value is
    #: "Yellow".
    nodeLabelColor: str = ""

    #: A String specifying the color to be used to plot the node symbols. The default value is
    #: "Yellow".
    nodeSymbolColor: str = ""

    #: A String specifying the color to be used to plot the normal to a nonbeam element or to a
    #: surface. The default value is "Red".
    faceNormalColor: str = ""

    #: A String specifying the color to be used to plot an arrow along the beam n1n1-direction.
    #: The default value is "Blue".
    beamN1Color: str = ""

    #: A String specifying the color to be used to plot an arrow along the beam n2n2-direction.
    #: The default value is "Red".
    beamN2Color: str = ""

    #: A String specifying the color to be used to plot an arrow along the tangent to a beam.
    #: The default value is "White".
    beamTangentColor: str = ""

    #: A tuple of three Floats specifying the coordinate scaling in each of the three
    #: coordinate directions when **coordinateScale** = ON. The default value is (1, 1, 1).
    coordinateScaleFactors: Optional[float] = None
