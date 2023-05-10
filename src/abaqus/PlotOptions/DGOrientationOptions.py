from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import (
    MODEL_SIZE,
    NONE,
    ON,
    PLY,
    VERY_THIN,
    Boolean,
    SymbolicConstant,
)


@abaqus_class_doc
class DGOrientationOptions:
    """The DGOrientationOptions object stores values and attributes associated with a material orientation plot.
    The DGOrientationOptions object has no constructor command. Abaqus creates an
    *odbDisplayOptions.materialOrientationOptions* member when a display group instance is created, using values
    from *odbDisplay.materialOrientationOptions*.

    .. note::
        This object can be accessed by::

            session.viewports[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions.materialOrientationOptions
            session.viewports[name].layers[name].assemblyDisplay.displayGroupInstances[name].odbDisplayOptions.materialOrientationOptions
            session.viewports[name].layers[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions.materialOrientationOptions
            session.viewports[name].layers[name].partDisplay.displayGroupInstances[name].odbDisplayOptions.materialOrientationOptions
            session.viewports[name].odbDisplay.displayGroupInstances[name].odbDisplayOptions.materialOrientationOptions
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

    #: A Float specifying the size of the material orientation triad. The default value is 6.0.
    symbolSize: float = 6

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
