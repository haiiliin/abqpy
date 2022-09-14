from abqpy.decorators import abaqus_class_doc
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class DGContourOptions:
    """The DGContourOptions object stores values and attributes associated with a contour plot.
    The DGContourOptions object has no constructor command. Abaqus creates an
    *odbDisplayOptions.contourOptions* member when a display group instance is created,
    using values from *odbDisplay.contourOptions*.

    .. note:: 
        This object can be accessed by::

            session.viewports[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions.contourOptions
            session.viewports[name].layers[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions.contourOptions
            session.viewports[name].layers[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions.contourOptions
            session.viewports[name].layers[name].partDisplay.displayGroupInstances[name].odbDisplayOptions.contourOptions
            session.viewports[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions.contourOptions
            session.viewports[name].partDisplay.displayGroupInstances[name].odbDisplayOptions.contourOptions
    """

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
    intervalLineAttributes: SymbolicConstant = None
