from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ..UtilityAndView.abaqusConstants import Boolean, FEATURE, OFF, ON, SOLID, SymbolicConstant, VERY_THIN, WIREFRAME
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class OptionArg:
    """The OptionArg object is used to store values and attributes as a temporary object to be
    associated with a viewCutOptions object. The OptionArg object has only a constructor
    command.

    .. note::
        This object can be accessed by::

            import visualization
            session.defaultOdbDisplay.viewCutOptions.aboveOptions
            session.defaultOdbDisplay.viewCutOptions.belowOptions
            session.defaultOdbDisplay.viewCutOptions.onOptions
            session.viewports[name].layers[name].odbDisplay.viewCutOptions.aboveOptions
            session.viewports[name].layers[name].odbDisplay.viewCutOptions.belowOptions
            session.viewports[name].layers[name].odbDisplay.viewCutOptions.onOptions
            session.viewports[name].odbDisplay.viewCutOptions.aboveOptions
            session.viewports[name].odbDisplay.viewCutOptions.belowOptions
            session.viewports[name].odbDisplay.viewCutOptions.onOptions
    """

    #: A SymbolicConstant specifying the render style of the plot. Possible values are
    #: WIREFRAME, FILLED, HIDDEN, and SHADED. The default value is WIREFRAME.
    renderStyle: SymbolicConstant = WIREFRAME

    #: A SymbolicConstant specifying which edges to plot. Possible values are ALL, EXTERIOR,
    #: FEATURE, FREE, and NONE. The default value is FEATURE.NONE can be used only when
    #: **renderStyle** = SHADED.
    visibleEdges: SymbolicConstant = FEATURE

    #: A String specifying the color to be used to plot the edges of the undeformed plot when
    #: **renderStyle** = WIREFRAME or HIDDEN. The default value is "Green".
    edgeColorWireHide: str = ""

    #: A String specifying the color to be used to plot the edges of the undeformed plot when
    #: **renderStyle** = FILLED or SHADED. The default value is "Black".
    edgeColorFillShade: str = ""

    #: A SymbolicConstant specifying the edge line style. Possible values are SOLID, DASHED,
    #: DOTTED, and DOT_DASH. The default value is SOLID.
    edgeLineStyle: SymbolicConstant = SOLID

    #: A SymbolicConstant specifying the edge line thickness. Possible values are VERY_THIN,
    #: THIN, MEDIUM, and THICK. The default value is VERY_THIN.
    edgeLineThickness: SymbolicConstant = VERY_THIN

    #: A Boolean specifying whether to allow color coded items in the output database to
    #: override the edge and fill color settings. The default value is ON.
    colorCodeOverride: Boolean = ON

    #: A String specifying the color to be used to fill elements when **renderStyle** = FILLED or
    #: SHADED. The default value is "Green".
    fillColor: str = ""

    #: A Boolean specifying whether to set translucency. The default value is OFF.
    translucency: Boolean = OFF

    #: A Float specifying the translucency factor when **translucency** = ON. Possible values are
    #: 0.0 ≤ **translucencyFactor** ≤ 1.0. The default value is 0.3.
    translucencyFactor: float = 0

    @abaqus_method_doc
    def __init__(
        self,
        renderStyle: Literal[C.SHADED, C.FILLED, C.WIREFRAME, C.HIDDEN] = WIREFRAME,
        visibleEdges: Literal[C.FEATURE, C.EXTERIOR, C.ALL, C.FREE, C.NONE, C.SHADED] = FEATURE,
        edgeColorWireHide: str = "",
        edgeColorFillShade: str = "",
        edgeLineStyle: Literal[C.DASHED, C.SOLID, C.DOT_DASH, C.DOTTED] = SOLID,
        edgeLineThickness: Literal[C.THIN, C.THICK, C.VERY_THIN, C.MEDIUM] = VERY_THIN,
        colorCodeOverride: Boolean = ON,
        fillColor: str = "",
        translucency: Boolean = OFF,
        translucencyFactor: float = 0,
    ):
        """This method creates an OptionArg object.

        .. note::
            This function can be accessed by::

                visualization.OptionArg

        Parameters
        ----------
        renderStyle
            A SymbolicConstant specifying the render style of the plot. Possible values are
            WIREFRAME, FILLED, HIDDEN, and SHADED. The default value is WIREFRAME.
        visibleEdges
            A SymbolicConstant specifying which edges to plot. Possible values are ALL, EXTERIOR,
            FEATURE, FREE, and NONE. The default value is FEATURE.NONE can be used only when
            **renderStyle** = SHADED.
        edgeColorWireHide
            A String specifying the color to be used to plot the edges of the undeformed plot when
            **renderStyle** = WIREFRAME or HIDDEN. The default value is "Green".
        edgeColorFillShade
            A String specifying the color to be used to plot the edges of the undeformed plot when
            **renderStyle** = FILLED or SHADED. The default value is "Black".
        edgeLineStyle
            A SymbolicConstant specifying the edge line style. Possible values are SOLID, DASHED,
            DOTTED, and DOT_DASH. The default value is SOLID.
        edgeLineThickness
            A SymbolicConstant specifying the edge line thickness. Possible values are VERY_THIN,
            THIN, MEDIUM, and THICK. The default value is VERY_THIN.
        colorCodeOverride
            A Boolean specifying whether to allow color coded items in the output database to
            override the edge and fill color settings. The default value is ON.
        fillColor
            A String specifying the color to be used to fill elements when **renderStyle** = FILLED or
            SHADED. The default value is "Green".
        translucency
            A Boolean specifying whether to set translucency. The default value is OFF.
        translucencyFactor
            A Float specifying the translucency factor when **translucency** = ON. Possible values are
            0.0 ≤ **translucencyFactor** ≤ 1.0. The default value is 0.3.

        Returns
        -------
        OptionArg
            An :py:class:`~abaqus.PlotOptions.OptionArg.OptionArg` object.

        Raises
        ------
        RangeError
        """
        self.renderStyle = renderStyle
        self.visibleEdges = visibleEdges
        self.edgeColorWireHide = edgeColorWireHide
        self.edgeColorFillShade = edgeColorFillShade
        self.edgeLineStyle = edgeLineStyle
        self.edgeLineThickness = edgeLineThickness
        self.colorCodeOverride = colorCodeOverride
        self.fillColor = fillColor
        self.translucency = translucency
        self.translucencyFactor = translucencyFactor
