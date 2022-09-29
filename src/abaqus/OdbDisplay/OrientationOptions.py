from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..PlotOptions.DGOrientationOptions import DGOrientationOptions
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class OrientationOptions(DGOrientationOptions):
    """The OrientationOptions object stores values and attributes associated with a material
    orientation plot. The OrientationOptions object has no constructor command. Abaqus
    creates a *defaultOdbDisplay.materialOrientationOptions* member when you import the
    Visualization module. Abaqus creates a **materialOrientationOptions** member when it
    creates the OdbDisplay object, using the values from
    *defaultOdbDisplay.materialOrientationOptions*. Abaqus creates the **odbDisplay** member
    when a viewport is created, using the values from **defaultOdbDisplay**.
    OrientationOptions objects are accessed in one of two ways:
    - The default material orientation options. These settings are used as defaults when
    other **materialOrientationOptions** members are created. These settings can be set to
    customize user preferences.
    - The material orientation options associated with a particular viewport.
    The OrientationOptions object is derived from the DGOrientationOptions object.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.defaultOdbDisplay.materialOrientationOptions
            session.viewports[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions.materialOrientationOptions
            session.viewports[name].layers[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions.materialOrientationOptions
            session.viewports[name].layers[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions.materialOrientationOptions
            session.viewports[name].layers[name].odbDisplay.materialOrientationOptions
            session.viewports[name].layers[name].partDisplay.displayGroupInstances[name].odbDisplayOptions.materialOrientationOptions
            session.viewports[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions.materialOrientationOptions
            session.viewports[name].odbDisplay.materialOrientationOptions
            session.viewports[name].partDisplay.displayGroupInstances[name].odbDisplayOptions.materialOrientationOptions
    """

    #: A Boolean specifying whether axis 1 of the material orientation triad should be
    #: displayed. The default value is ON.
    showAxis1: Boolean = ON

    #: A Boolean specifying whether axis 2 of the material orientation triad should be
    #: displayed. The default value is ON.
    showAxis2: Boolean = ON

    #: A Boolean specifying whether axis 3 of the material orientation triad should be
    #: displayed. The default value is ON.
    showAxis3: Boolean = ON

    #: A Float specifying the size of the material orientation triad. The default value is
    #: 12.0.
    symbolSize: float = 12

    #: A SymbolicConstant specifying the thickness of the material orientation triad. Possible
    #: values are VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.
    lineThickness: SymbolicConstant = VERY_THIN

    #: A SymbolicConstant specifying the orientation used for composites. Possible values are
    #: PLY and LAYUP. The default value is PLY.
    orientation: SymbolicConstant = PLY

    #: A SymbolicConstant specifying the arrowhead style for the material orientation triad.
    #: Possible values are NONE, FILLED, and WIRE. The default value is NONE.
    arrowheadStyle: SymbolicConstant = NONE

    #: A SymbolicConstant specifying the scaling basis for the material orientation triad.
    #: Possible values are MODEL_SIZE and SCREEN_SIZE. The default value is MODEL_SIZE.
    scaleMode: SymbolicConstant = MODEL_SIZE

    #: A String specifying the color of axis 1 of the material orientation triad. The default
    #: value is "Cyan".
    axis1Color: str = ""

    #: A String specifying the color of axis 2 of the material orientation triad. The default
    #: value is "Yellow".
    axis2Color: str = ""

    #: A String specifying the color of axis 3 of the material orientation triad. The default
    #: value is "Red".
    axis3Color: str = ""

    @abaqus_method_doc
    def setValues(
        self,
        options: Optional["OrientationOptions"] = None,
        axis1Color: str = "",
        showAxis1: Boolean = ON,
        axis2Color: str = "",
        showAxis2: Boolean = ON,
        axis3Color: str = "",
        showAxis3: Boolean = ON,
        symbolSize: float = 12,
        lineThickness: SymbolicConstant = VERY_THIN,
        orientation: SymbolicConstant = PLY,
        arrowheadStyle: SymbolicConstant = NONE,
        scaleMode: SymbolicConstant = MODEL_SIZE,
    ):
        """This method modifies the OrientationOptions object.

        Parameters
        ----------
        options
            An :py:class:`~abaqus.OdbDisplay.OrientationOptions.OrientationOptions` object from which values are to be copied. If other arguments are
            also supplied to setValues, they will override the values in **options**. The default
            value is None.
        axis1Color
            A String specifying the color of axis 1 of the material orientation triad. The default
            value is "Cyan".
        showAxis1
            A Boolean specifying whether axis 1 of the material orientation triad should be
            displayed. The default value is ON.
        axis2Color
            A String specifying the color of axis 2 of the material orientation triad. The default
            value is "Yellow".
        showAxis2
            A Boolean specifying whether axis 2 of the material orientation triad should be
            displayed. The default value is ON.
        axis3Color
            A String specifying the color of axis 3 of the material orientation triad. The default
            value is "Red".
        showAxis3
            A Boolean specifying whether axis 3 of the material orientation triad should be
            displayed. The default value is ON.
        symbolSize
            A Float specifying the size of the material orientation triad. The default value is
            12.0.
        lineThickness
            A SymbolicConstant specifying the thickness of the material orientation triad. Possible
            values are VERY_THIN, THIN, MEDIUM, and THICK. The default value is VERY_THIN.
        orientation
            A SymbolicConstant specifying the orientation used for composites. Possible values are
            PLY and LAYUP. The default value is PLY.
        arrowheadStyle
            A SymbolicConstant specifying the arrowhead style for the material orientation triad.
            Possible values are NONE, FILLED, and WIRE. The default value is NONE.
        scaleMode
            A SymbolicConstant specifying the scaling basis for the material orientation triad.
            Possible values are MODEL_SIZE and SCREEN_SIZE. The default value is MODEL_SIZE.

        Raises
        ------
        RangeError
        """
        ...
