from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ..PlotOptions.DGContourOptions import DGContourOptions
from ..UtilityAndView.abaqusConstants import (
    ALL_FRAMES,
    BANDED,
    Boolean,
    MEDIUM,
    N2,
    OFF,
    ON,
    SOLID,
    SymbolicConstant,
    TEXTURE_MAPPED,
    UNIFORM,
    VERY_THIN,
)
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class ContourOptions(DGContourOptions):
    """The ContourOptions object stores values and attributes associated with a contour plot.
    The ContourOptions object has no constructor command. Abaqus creates a
    *defaultOdbDisplay.contourOptions* member when you import the Visualization module.
    Abaqus creates a **contourOptions** member when it creates the OdbDisplay object, using
    the values from *defaultOdbDisplay.contourOptions*. Abaqus creates the **odbDisplay**
    member when a viewport is created, using the values from **defaultOdbDisplay**.
    ContourOptions objects are accessed in one of two ways:
    - The default contour options. These settings are used as defaults when other
    **contourOptions** members are created. These settings can be set to customize user
    preferences.
    - The contour options associated with a particular viewport.
    The ContourOptions object is derived from the DGContourOptions object.

    .. note::
        This object can be accessed by::

            import visualization
            session.defaultOdbDisplay.contourOptions
            session.viewports[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions.contourOptions
            session.viewports[name].layers[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions.contourOptions
            session.viewports[name].layers[name].odbDisplay.contourOptions
            session.viewports[name].layers[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions.contourOptions
            session.viewports[name].layers[name].partDisplay.displayGroupInstances[name].odbDisplayOptions.contourOptions
            session.viewports[name].odbDisplay.contourOptions
            session.viewports[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions.contourOptions
            session.viewports[name].partDisplay.displayGroupInstances[name].odbDisplayOptions.contourOptions
    """

    #: A SymbolicConstant specifying the contour type. Possible values are LINE, BANDED, QUILT,
    #: and ISOSURFACE. The default value is BANDED.
    contourType: SymbolicConstant = BANDED

    #: An Int specifying the number of intervals when **contourStyle** = UNIFORM. Possible values
    #: are 2 ≤ **numIntervals** ≤ 24. The default value is 12.
    numIntervals: int = 12

    #: A SymbolicConstant specifying the interval type of the contour plot. Possible values are
    #: UNIFORM, LOG, and USER_DEFINED. The default value is UNIFORM.
    intervalType: SymbolicConstant = UNIFORM

    #: A Boolean specifying whether the contour range maximum value should be computed from the
    #: output data to be contoured. The default value is ON.
    maxAutoCompute: Boolean = ON

    #: A Float specifying the contour range maximum value to be used in the plot when
    #: **maxAutoCompute** = ON. The default value is **autoMaxValue**.
    maxValue: Optional[float] = None

    #: A Boolean specifying whether the contour range minimum value should be computed from the
    #: output data to be contoured. The default value is ON.
    minAutoCompute: Boolean = ON

    #: A Float specifying the contour range minimum value to be used in the plot when
    #: **minAutoCompute** = ON. The default value is **autoMinValue**.
    minValue: Optional[float] = None

    #: A SymbolicConstant specifying the method to be used when contour limits are
    #: automatically computed for animation. **animationAutoLimits** will only effect the minimum
    #: limit and/or maximum limit when **minAutoCompute** and/or **maxAutoCompute** = True. Possible
    #: values are FIRST_AND_LAST, CURRENT_FRAME, RECOMPUTE_EACH_FRAME, and ALL_FRAMES. The
    #: default value is ALL_FRAMES.
    animationAutoLimits: SymbolicConstant = ALL_FRAMES

    #: A SymbolicConstant specifying the color of contour values that exceed the limits of the
    #: plot. Possible values are SPECTRUM and SPECIFY.When **outsideLimitsMode** = SPECTRUM, the
    #: maximum and minimum contour spectrum colors are used for values that exceed the limits
    #: of the plot. When **outsideLimitsMode** = SPECIFY, the values of **outsideLimitsAboveColor**
    #: and **outsideLimitsBelowColor** are used for values that exceed the limits of the plot.
    outsideLimitsMode: Optional[SymbolicConstant] = None

    #: A Boolean specifying whether to auto-compute contour limits using extrapolated values
    #: alone or extrapolated values that are averaged. The default value is OFF.
    extrapolatedAveraging: Boolean = OFF

    #: A Boolean specifying whether to display location of maximum value. The default value is
    #: OFF.
    showMaxLocation: Boolean = OFF

    #: A Boolean specifying whether to display location of minimum value. The default value is
    #: OFF.
    showMinLocation: Boolean = OFF

    #: A Float specifying the maximum value to be used in the plot. The value is computed from
    #: the output data to be contoured. This value is read-only.
    autoMaxValue: Optional[float] = None

    #: A Float specifying the minimum value to be used in the plot. The value is computed from
    #: the output data to be contoured. This value is read-only.
    autoMinValue: Optional[float] = None

    #: A String specifying the color to be used for values that exceed the limits of the plot
    #: when **outsideLimitsMode** = SPECIFY. The default value is "Grey80".
    outsideLimitsAboveColor: str = ""

    #: A String specifying the color to be used for values that exceed the limits of the plot
    #: when **outsideLimitsMode** = SPECIFY. The default value is "Grey20".
    outsideLimitsBelowColor: str = ""

    #: A String specifying the name of the color spectrum to be used in the contour plot. The
    #: default value is "Rainbow".
    spectrum: str = ""

    #: A Boolean specifying whether the contour legend should show the lowest value at the top
    #: and the highest value at the bottom (**reversedContourLegendRange=ON**) or vice versa. The
    #: default value is OFF.
    #:
    #: ..versionadded:: 2018
    #:     The `reversedContourLegendRange` attribute was added.
    reversedContourLegendRange: Boolean = OFF

    #: A tuple of Floats specifying the interval values when **intervalType** = USER_DEFINED.
    intervalValues: Optional[float] = None

    #: A SymbolicConstant specifying the contour rendering method. Possible values are
    #: TEXTURE_MAPPED and TESSELLATED. The default value is TEXTURE_MAPPED.
    contourMethod: SymbolicConstant = TEXTURE_MAPPED

    #: A Boolean specifying whether tick mark plots should be displayed on line-type elements.
    #: If **tickmarkPlots** = ON, Abaqus displays a tick mark plot. If **tickmarkPlots** = OFF, Abaqus
    #: displays contours on the element faces. The default value is OFF.
    tickmarkPlots: Boolean = OFF

    #: A SymbolicConstant specifying the interval style of the contour plot. Possible values
    #: are CONTINUOUS and UNIFORM. The default value is UNIFORM.
    contourStyle: SymbolicConstant = UNIFORM

    #: A Boolean specifying whether to plot the edges of each contour interval when
    #: **contourType** = BANDED or ISOSURFACE. The default value is OFF.
    contourEdges: Boolean = OFF

    #: A SymbolicConstant specifying the edge line style to be used to plot the contour edges
    #: when **contourType** = BANDED or ISOSURFACE. Possible values are SOLID, DASHED, DOTTED, and
    #: DOT_DASH. The default value is SOLID.
    contourEdgeStyle: SymbolicConstant = SOLID

    #: A SymbolicConstant specifying the edge line thickness to be used to plot the edge of the
    #: contour intervals when **contourType** = BANDED or ISOSURFACE. Possible values are
    #: VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.
    contourEdgeThickness: SymbolicConstant = VERY_THIN

    #: A Boolean specifying the display of the nodal averaged coordinate systems used when
    #: averaging element vector or tensor data. The default value is OFF.
    averagedOrientationDisplay: Boolean = OFF

    #: A Boolean specifying whether the label for the matching ply shows up in the viewport.
    #: The default value is OFF.
    matchingPlyLabels: Boolean = OFF

    #: A Boolean specifying whether the contour color is driven by the matching ply. The
    #: default value is OFF.
    colorByMatchingPlies: Boolean = OFF

    #: A SymbolicConstant specifying the length of the tick mark plot axes. Possible values are
    #: SHORT, MEDIUM, and LONG. The default value is MEDIUM.
    tickmarkAxisLength: SymbolicConstant = MEDIUM

    #: A Float specifying the base contour value defining the tick mark axis contour value that
    #: intersects the elements. Possible values are **autoMinValue** ≤ **tickmarkBaseValue** ≤
    #: **autoMaxValue**. The default value is 0.0.
    tickmarkBaseValue: float = 0

    #: A SymbolicConstant specifying the orientation of the tick mark plots. Possible values
    #: are N1 and N2. The default value is N2.
    tickmarkOrientation: SymbolicConstant = N2

    #: A String specifying the edge color to be used when **contourType** = LINE. The default value
    #: is "White".
    edgeColorLine: str = ""

    #: A String specifying the edge color to be used when **contourType** = BANDED or QUILT. The
    #: default value is "Black".
    edgeColorBandedQuilt: str = ""

    #: A String specifying the color to be used to plot the contour edges when
    #: **contourType** = BANDED or ISOSURFACE. The default value is "Grey60".
    contourEdgeColor: str = ""

    #: A String specifying the color to be used to plot the tick mark curve. The default value
    #: is "Cyan".
    tickmarkCurveColor: str = ""

    #: A tuple of tuples of SymbolicConstants specifying the line style and line thickness for
    #: each interval in the plot when **contourType** = LINE. The size of the outer sequence must
    #: be equal to **numIntervals**-1. The inner sequence consists of two SymbolicConstants
    #: specifying the line style and line thickness. For possible values, refer to the
    #: **edgeLineStyle** and **edgeLineThickness** members of the DGCommonOptions object. The
    #: default is ((SOLID, VERY_THIN), ).
    intervalLineAttributes: Optional[SymbolicConstant] = None

    #: A Boolean specifying whether to hide the values outside the specified min/max in the
    #: contour legend. This setting hides the **autoMinValue** and **autoMaxValue** from the
    #: spectrum when **legendHideOutsideLimits** = ON.The default value is OFF.
    #:
    #: ..versionadded:: 2019
    #:     The `legendHideOutsideLimits` attribute was added.
    legendHideOutsideLimits: Boolean = OFF

    @abaqus_method_doc
    def setValues(
        self,
        options: Optional["ContourOptions"] = None,
        contourType: Literal[C.ISOSURFACE, C.BANDED, C.LINE, C.QUILT] = BANDED,
        contourMethod: Literal[C.TESSELLATED, C.TEXTURE_MAPPED] = TEXTURE_MAPPED,
        tickmarkPlots: Boolean = OFF,
        contourStyle: Literal[C.CONTINUOUS, C.UNIFORM] = UNIFORM,
        numIntervals: int = 12,
        intervalType: Literal[C.USER_DEFINED, C.LOG, C.UNIFORM] = UNIFORM,
        intervalValues: tuple = (),
        maxAutoCompute: Boolean = ON,
        maxValue: Optional[float] = None,
        minAutoCompute: Boolean = ON,
        minValue: Optional[float] = None,
        animationAutoLimits: Literal[
            C.CURRENT_FRAME, C.RECOMPUTE_EACH_FRAME, C.ALL_FRAMES, C.FIRST_AND_LAST
        ] = ALL_FRAMES,
        edgeColorLine: str = "",
        edgeColorBandedQuilt: str = "",
        spectrum: str = "",
        reversedContourLegendRange: Boolean = OFF,
        outsideLimitsMode: Optional[Literal[C.SPECIFY, C.SPECTRUM]] = None,
        outsideLimitsAboveColor: str = "",
        outsideLimitsBelowColor: str = "",
        intervalLineAttributes: Optional[Literal[C.LINE]] = None,
        contourEdges: Boolean = OFF,
        contourEdgeColor: str = "",
        contourEdgeStyle: Literal[C.SOLID, C.DOT_DASH, C.DASHED, C.DOTTED, C.ISOSURFACE, C.BANDED] = SOLID,
        contourEdgeThickness: Literal[C.THICK, C.VERY_THIN, C.THIN, C.ISOSURFACE, C.BANDED, C.MEDIUM] = VERY_THIN,
        tickmarkAxisLength: Literal[C.SHORT, C.MEDIUM, C.LONG] = MEDIUM,
        tickmarkBaseValue: float = 0,
        tickmarkOrientation: Literal[C.N1, C.N2] = N2,
        tickmarkCurveColor: str = "",
        averagedOrientationDisplay: Boolean = OFF,
        extrapolatedAveraging: Boolean = OFF,
        showMaxLocation: Boolean = OFF,
        showMinLocation: Boolean = OFF,
        legendHideOutsideLimits: Boolean = OFF,
    ):
        """This method modifies the ContourOptions object.

        Parameters
        ----------
        options
            A ContourOptions object from which values are to be copied. If other arguments are also
            supplied to setValues, they will override the values in **options**. The default value is
            None.
        contourType
            A SymbolicConstant specifying the contour type. Possible values are LINE, BANDED, QUILT,
            and ISOSURFACE. The default value is BANDED.
        contourMethod
            A SymbolicConstant specifying the contour rendering method. Possible values are
            TEXTURE_MAPPED and TESSELLATED. The default value is TEXTURE_MAPPED.
        tickmarkPlots
            A Boolean specifying whether tick mark plots should be displayed on line-type elements.
            If **tickmarkPlots** = ON, Abaqus displays a tick mark plot. If **tickmarkPlots** = OFF, Abaqus
            displays contours on the element faces. The default value is OFF.
        contourStyle
            A SymbolicConstant specifying the interval style of the contour plot. Possible values
            are CONTINUOUS and UNIFORM. The default value is UNIFORM.
        numIntervals
            An Int specifying the number of intervals when **contourStyle** = UNIFORM. Possible values
            are 2 ≤ **numIntervals** ≤ 24. The default value is 12.
        intervalType
            A SymbolicConstant specifying the interval type of the contour plot. Possible values are
            UNIFORM, LOG, and USER_DEFINED. The default value is UNIFORM.
        intervalValues
            A sequence of Floats specifying the interval values when **intervalType** = USER_DEFINED.
        maxAutoCompute
            A Boolean specifying whether the contour range maximum value should be computed from the
            output data to be contoured. The default value is ON.
        maxValue
            A Float specifying the contour range maximum value to be used in the plot when
            **maxAutoCompute** = ON. The default value is **autoMaxValue**.
        minAutoCompute
            A Boolean specifying whether the contour range minimum value should be computed from the
            output data to be contoured. The default value is ON.
        minValue
            A Float specifying the contour range minimum value to be used in the plot when
            **minAutoCompute** = ON. The default value is **autoMinValue**.
        animationAutoLimits
            A SymbolicConstant specifying the method to be used when contour limits are
            automatically computed for animation. **animationAutoLimits** will only effect the minimum
            limit and/or maximum limit when **minAutoCompute** and/or **maxAutoCompute** = True. Possible
            values are FIRST_AND_LAST, CURRENT_FRAME, RECOMPUTE_EACH_FRAME, and ALL_FRAMES. The
            default value is ALL_FRAMES.
        edgeColorLine
            A String specifying the edge color to be used when **contourType** = LINE. The default value
            is "White".
        edgeColorBandedQuilt
            A String specifying the edge color to be used when **contourType** = BANDED or QUILT. The
            default value is "Black".
        spectrum
            A String specifying the name of the color spectrum to be used in the contour plot. The
            default value is "Rainbow".
        reversedContourLegendRange
            A Boolean specifying whether the contour legend should show the lowest value at the top
            and the highest value at the bottom (*reversedContourLegendRange* = ON) or vice versa. The
            default value is OFF.

            .. versionadded:: 2018
                The `reversedContourLegendRange` argument was added.
        outsideLimitsMode
            A SymbolicConstant specifying the color of contour values that exceed the limits of the
            plot. Possible values are SPECTRUM and SPECIFY.When **outsideLimitsMode** = SPECTRUM, the
            maximum and minimum contour spectrum colors are used for values that exceed the limits
            of the plot. When **outsideLimitsMode** = SPECIFY, the values of **outsideLimitsAboveColor**
            and **outsideLimitsBelowColor** are used for values that exceed the limits of the plot.
        outsideLimitsAboveColor
            A String specifying the color to be used for values that exceed the limits of the plot
            when **outsideLimitsMode** = SPECIFY. The default value is "Grey80".
        outsideLimitsBelowColor
            A String specifying the color to be used for values that exceed the limits of the plot
            when **outsideLimitsMode** = SPECIFY. The default value is "Grey20".
        intervalLineAttributes
            A sequence of sequences of SymbolicConstants specifying the line style and line
            thickness for each interval in the plot when **contourType** = LINE. The size of the outer
            sequence must be equal to **numIntervals**-1. The inner sequence consists of two
            SymbolicConstants specifying the line style and line thickness. For possible values,
            refer to the **edgeLineStyle** and **edgeLineThickness** members of the DGCommonOptions
            object. The default is ((SOLID, VERY_THIN), ).
        contourEdges
            A Boolean specifying whether to plot the edges of each contour interval when
            **contourType** = BANDED or ISOSURFACE. The default value is OFF.
        contourEdgeColor
            A String specifying the color to be used to plot the contour edges when
            **contourType** = BANDED or ISOSURFACE. The default value is "Grey60".
        contourEdgeStyle
            A SymbolicConstant specifying the edge line style to be used to plot the contour edges
            when **contourType** = BANDED or ISOSURFACE. Possible values are SOLID, DASHED, DOTTED, and
            DOT_DASH. The default value is SOLID.
        contourEdgeThickness
            A SymbolicConstant specifying the edge line thickness to be used to plot the edge of the
            contour intervals when **contourType** = BANDED or ISOSURFACE. Possible values are
            VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.
        tickmarkAxisLength
            A SymbolicConstant specifying the length of the tick mark plot axes. Possible values are
            SHORT, MEDIUM, and LONG. The default value is MEDIUM.
        tickmarkBaseValue
            A Float specifying the base contour value defining the tick mark axis contour value that
            intersects the elements. Possible values are **autoMinValue** ≤ **tickmarkBaseValue** ≤
            **autoMaxValue**. The default value is 0.0.
        tickmarkOrientation
            A SymbolicConstant specifying the orientation of the tick mark plots. Possible values
            are N1 and N2. The default value is N2.
        tickmarkCurveColor
            A String specifying the color to be used to plot the tick mark curve. The default value
            is "Cyan".
        averagedOrientationDisplay
            A Boolean specifying the display of the nodal averaged coordinate systems used when
            averaging element vector or tensor data. The default value is OFF.
        extrapolatedAveraging
            A Boolean specifying whether to auto-compute contour limits using extrapolated values
            alone or extrapolated values that are averaged. The default value is OFF.
        showMaxLocation
            A Boolean specifying whether to display location of maximum value. The default value is
            OFF.
        showMinLocation
            A Boolean specifying whether to display location of minimum value. The default value is
            OFF.
        legendHideOutsideLimits
            A Boolean specifying whether to hide the values outside the specified minimum/maximum
            for the contour interval when **legendHideOutsideLimits** = ON. The default value is OFF.

            .. versionadded:: 2019
                The `legendHideOutsideLimits` argument was added.

        Raises
        ------
        RangeError
        """
        ...
