from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ..PlotOptions.DGDisplayBodyOptions import DGDisplayBodyOptions
from ..UtilityAndView.abaqusConstants import (Boolean, EXTERIOR, OFF, ON, SOLID, SymbolicConstant,
                                              VERY_THIN)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class DisplayBodyOptions(DGDisplayBodyOptions):
    """The DisplayBodyOptions object stores values and attributes that are common to all plot
    states. The DisplayBodyOptions object has no constructor command. Abaqus creates a
    *defaultOdbDisplay.displayBodyOptions* member when you import the Visualization module.
    Abaqus creates a **displayBodyOptions** member when it creates the OdbDisplay object,
    using the values from *defaultOdbDisplay.displayBodyOptions*. Abaqus creates the
    **odbDisplay** member when a viewport is created, using the values from
    **defaultOdbDisplay**.
    DisplayBodyOptions objects are accessed in one of two ways:
    - The default display body options. These settings are used as defaults when other
    **displayBodyOptions** members are created. These settings can be set to customize user
    preferences.
    - The display body options associated with a particular viewport.
    The DisplayBodyOptions object is derived from the DGDisplayBodyOptions object.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.defaultOdbDisplay.displayBodyOptions
            session.viewports[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions.displayBodyOptions
            session.viewports[name].layers[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions.displayBodyOptions
            session.viewports[name].layers[name].odbDisplay.displayBodyOptions
            session.viewports[name].layers[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions.displayBodyOptions
            session.viewports[name].layers[name].partDisplay.displayGroupInstances[name].odbDisplayOptions.displayBodyOptions
            session.viewports[name].odbDisplay.displayBodyOptions
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
    coordinateScaleFactors: Optional[float] = None

    @abaqus_method_doc
    def setValues(
        self,
        options: Optional["DisplayBodyOptions"] = None,
        visibleEdges: Literal[C.FEATURE, C.EXTERIOR, C.ALL, C.FREE, C.NONE, C.SHADED] = EXTERIOR,
        edgeColorWireHide: str = "",
        edgeColorFillShade: str = "",
        edgeLineStyle: Literal[C.DASHED, C.SOLID, C.DOT_DASH, C.DOTTED] = SOLID,
        edgeLineThickness: Literal[C.THIN, C.THICK, C.VERY_THIN, C.MEDIUM] = VERY_THIN,
        fillColor: str = "",
        colorCodeOverride: Boolean = ON,
        elementShrink: Boolean = OFF,
        elementShrinkFactor: int = 5,
        coordinateScale: Boolean = OFF,
        coordinateScaleFactors: tuple = (),
        translucency: Boolean = OFF,
        translucencyFactor: float = 0,
    ):
        """This method modifies the DisplayBodyOptions object.

        Parameters
        ----------
        options
            A :py:class:`~abaqus.OdbDisplay.DisplayBodyOptions.DisplayBodyOptions` object from which values are to be copied. If other arguments are
            also supplied to setValues, they will override the values in **options**. The default
            value is None.
        visibleEdges
            A SymbolicConstant specifying which edges to plot. Possible values are ALL, EXTERIOR,
            FEATURE, FREE, and NONE. The default value is EXTERIOR.NONE can be used only when
            **renderStyle** = SHADED.
        edgeColorWireHide
            A String specifying the color to be used to plot the edges of the model when
            **renderStyle** = WIREFRAME or HIDDEN. The default value is "White".
        edgeColorFillShade
            A String specifying the color to be used to plot the edges of the model when
            **renderStyle** = FILLED or SHADED. The default value is "Black".
        edgeLineStyle
            A SymbolicConstant specifying the edge line style. Possible values are SOLID, DASHED,
            DOTTED, and DOT_DASH. The default value is SOLID.
        edgeLineThickness
            A SymbolicConstant specifying the edge line thickness. Possible values are VERY_THIN,
            THIN, MEDIUM, and THICK. The default value is VERY_THIN.
        fillColor
            A String specifying the color to be used to fill elements when **renderStyle** = FILLED or
            SHADED. The default value is "White".
        colorCodeOverride
            A Boolean specifying whether to allow color coded items in the output database to
            override the edge and fill color settings. The default value is ON.
        elementShrink
            A Boolean specifying whether elements are displayed in a shrunk format. The default
            value is OFF.
        elementShrinkFactor
            An Int specifying the percentage to shrink the elements when **elementShrink** = ON.
            Possible values are 0≤elementShrinkPercentage* ≤ 90. The default value is 5.
        coordinateScale
            A Boolean specifying whether to scale coordinates. The default value is OFF.
        coordinateScaleFactors
            A sequence of three Floats specifying the coordinate scaling in each of the three
            coordinate directions when **coordinateScale** = ON. The default value is (1, 1, 1).
        translucency
            A Boolean specifying whether to set translucency. The default value is OFF.
        translucencyFactor
            A Float specifying the translucency factor when **translucency** = ON. Possible values are
            0.0≤ **translucencyFactor** ≤ 1.0. The default value is 0.3.

        Raises
        ------
        RangeError
        """
        ...
