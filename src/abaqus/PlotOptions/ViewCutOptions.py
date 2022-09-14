from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..UtilityAndView.abaqusConstants import *
from .._OptionsBase import _CopyOptionsBase


@abaqus_class_doc
class ViewCutOptions(_CopyOptionsBase):
    """The ViewCutOptions object stores values and attributes associated with a view cut plot.
    The ViewCutOptions object has no constructor command. Abaqus creates a
    *defaultOdbDisplay.viewCutOptions* member when you import the Visualization module.
    Abaqus creates an **viewCutOptions** member when it creates the OdbDisplay object, using
    the values from *defaultOdbDisplay.viewCutOptions*. Abaqus creates the **odbDisplay**
    member when a viewport is created, using the values from **defaultOdbDisplay**.
    ViewCutOptions objects are accessed in one of two ways:
    - The default view cut options. These settings are used as defaults when other
    **viewCutOptions** members are created. These settings can be set to customize user
    preferences.
    - The view cut options associated with a particular viewport.

    .. note:: 
        This object can be accessed by::

            import visualization
            session.defaultOdbDisplay.viewCutOptions
            session.viewports[name].layers[name].odbDisplay.viewCutOptions
            session.viewports[name].odbDisplay.viewCutOptions
    """

    #: A Boolean specifying whether to use the options defined for displaying the model below
    #: the cut. The default value is OFF.
    useBelowOptions: Boolean = OFF

    #: A Boolean specifying whether to use the options defined for displaying the model on the
    #: cut. The default value is OFF.
    useOnOptions: Boolean = OFF

    #: A Boolean specifying whether to use the options defined for displaying the model above
    #: the cut. The default value is OFF.
    useAboveOptions: Boolean = OFF

    #: An Int specifying number of free bodies per view cut. The default value is 1.
    numCutFreeBody: int = 1

    #: A Boolean specifying whether to display slicing. The default value is OFF.
    displaySlicing: Boolean = OFF

    #: A Boolean specifying whether to slice at path nodes. The default value is OFF.
    slicingAtPathNodes: Boolean = OFF

    #: A Boolean specifying whether to put the summation point at the path. The default value
    #: is ON.
    freeBodySumOnPath: Boolean = ON

    #: A Float specifying free body minimum value. The default value is 0.0.
    cutFreeBodyMin: float = 0

    #: A Float specifying free body maximum value. The default value is 0.0.
    cutFreeBodyMax: float = 0

    #: A SymbolicConstant specifying the domain through which the free body cuts. Possible
    #: values are CURRENT_DISPLAY_GROUP and WHOLE_MODEL. The default value is
    #: CURRENT_DISPLAY_GROUP.
    freeBodyCutThru: SymbolicConstant = CURRENT_DISPLAY_GROUP

    #: A SymbolicConstant specifying the domain through which the free body steps. Possible
    #: values are ACTIVE_CUT_RANGE and PREDEFINED_PATH. The default value is ACTIVE_CUT_RANGE.
    freeBodyStepThru: SymbolicConstant = ACTIVE_CUT_RANGE

    #: A SymbolicConstant specifying whether to show the heat flow rate when available.
    #: Possible values are ON and OFF. The default value is ON.
    showHeatFlowRate: SymbolicConstant = ON

    #: A SymbolicConstant specifying the summation location for the free body cut. Possible
    #: values are CENTROID and SPECIFY. The default value is CENTROID.
    summationLoc: SymbolicConstant = CENTROID

    #: A SymbolicConstant specifying the component resolution choice for the free body cut.
    #: Possible values are NORMAL_TANGENTIAL and CSYS. The default value is NORMAL_TANGENTIAL.
    componentResolution: SymbolicConstant = NORMAL_TANGENTIAL

    #: None or an OptionArg object specifying values to be used for defining the options
    #: applicable on the model below the cut. The default value is None.
    belowOptions: str = None

    #: None or an OptionArg object specifying values to be used for defining the options
    #: applicable on the model on the cut. The default value is None.
    onOptions: str = None

    #: None or an OptionArg object specifying values to be used for defining the options
    #: applicable on the model above the cut. The default value is None.
    aboveOptions: str = None

    #: The SymbolicConstant GLOBAL or a String specifying the coordinate system name for the
    #: free body cut's component resolution. The default value is GLOBAL.
    csysName: SymbolicConstant = GLOBAL

    #: A String specifying the name of the path along which slicing occurs. The default value
    #: is an empty string.
    pathName: str = ""

    #: A tuple of three Floats specifying the summation point for the free body cut. The
    #: default value is (0, 0, 0).
    summationPoint: float = None

    #: A tuple of three Floats specifying the Y axis for free body component resolution. The
    #: default value is (0, 1, 0).
    yAxis: float = None

    @abaqus_method_doc
    def setValues(
        self,
        options: "ViewCutOptions" = None,
        *,
        belowOptions: str = None,
        useBelowOptions: Boolean = OFF,
        onOptions: str = None,
        useOnOptions: Boolean = OFF,
        aboveOptions: str = None,
        useAboveOptions: Boolean = OFF,
        freeBodyCutThru: SymbolicConstant = CURRENT_DISPLAY_GROUP,
        freeBodyStepThru: SymbolicConstant = ACTIVE_CUT_RANGE,
        numCutFreeBody: int = 1,
        displaySlicing: Boolean = OFF,
        slicingAtPathNodes: Boolean = OFF,
        freeBodySumOnPath: Boolean = ON,
        cutFreeBodyMin: float = 0,
        cutFreeBodyMax: float = 0,
        showHeatFlowRate: SymbolicConstant = ON,
        summationLoc: SymbolicConstant = CENTROID,
        componentResolution: SymbolicConstant = NORMAL_TANGENTIAL,
        csysName: SymbolicConstant = GLOBAL,
        pathName: str = "",
        summationPoint: tuple = (),
        yAxis: tuple = (),
    ):
        """This method modifies the ViewCutOptions object.

        Parameters
        ----------
        options
            A :py:class:`~abaqus.PlotOptions.ViewCutOptions.ViewCutOptions` object from which values are to be copied.
            If other arguments are also supplied to setValues, they will override the values in **options**. The default
            value is None.
        belowOptions
            None or an OptionArg object specifying values to be used for defining the options
            applicable on the model below the cut. The default value is None.
        useBelowOptions
            A Boolean specifying whether to use the options defined for displaying the model below
            the cut. The default value is OFF.
        onOptions
            None or an OptionArg object specifying values to be used for defining the options
            applicable on the model on the cut. The default value is None.
        useOnOptions
            A Boolean specifying whether to use the options defined for displaying the model on the
            cut. The default value is OFF.
        aboveOptions
            None or an OptionArg object specifying values to be used for defining the options
            applicable on the model above the cut. The default value is None.
        useAboveOptions
            A Boolean specifying whether to use the options defined for displaying the model above
            the cut. The default value is OFF.
        freeBodyCutThru
            A SymbolicConstant specifying the domain through which the free body cuts. Possible
            values are CURRENT_DISPLAY_GROUP and WHOLE_MODEL. The default value is
            CURRENT_DISPLAY_GROUP.
        freeBodyStepThru
            A SymbolicConstant specifying the domain through which the free body steps. Possible
            values are ACTIVE_CUT_RANGE and PREDEFINED_PATH. The default value is ACTIVE_CUT_RANGE.
        numCutFreeBody
            An Int specifying number of free bodies per view cut. The default value is 1.
        displaySlicing
            A Boolean specifying whether to display slicing. The default value is OFF.
        slicingAtPathNodes
            A Boolean specifying whether to slice at path nodes. The default value is OFF.
        freeBodySumOnPath
            A Boolean specifying whether to put the summation point at the path. The default value
            is ON.
        cutFreeBodyMin
            A Float specifying free body minimum value. The default value is 0.0.
        cutFreeBodyMax
            A Float specifying free body maximum value. The default value is 0.0.
        showHeatFlowRate
            A SymbolicConstant specifying whether to show the heat flow rate when available.
            Possible values are ON and OFF. The default value is ON.
        summationLoc
            A SymbolicConstant specifying the summation location for the free body cut. Possible
            values are CENTROID and SPECIFY. The default value is CENTROID.
        componentResolution
            A SymbolicConstant specifying the component resolution choice for the free body cut.
            Possible values are NORMAL_TANGENTIAL and CSYS. The default value is NORMAL_TANGENTIAL.
        csysName
            The SymbolicConstant GLOBAL or a String specifying the coordinate system name for the
            free body cut's component resolution. The default value is GLOBAL.
        pathName
            A String specifying the name of the path along which slicing occurs. The default value
            is an empty string.
        summationPoint
            A sequence of three Floats specifying the summation point for the free body cut. The
            default value is (0, 0, 0).
        yAxis
            A sequence of three Floats specifying the Y axis for free body component resolution. The
            default value is (0, 1, 0).

        Raises
        ------
        RangeError
        """
        super().setValues(
            options=options,
            aboveOptions=aboveOptions,
            belowOptions=belowOptions,
            componentResolution=componentResolution,
            csysName=csysName,
            cutFreeBodyMax=cutFreeBodyMax,
            cutFreeBodyMin=cutFreeBodyMin,
            displaySlicing=displaySlicing,
            freeBodyCutThru=freeBodyCutThru,
            freeBodyStepThru=freeBodyStepThru,
            freeBodySumOnPath=freeBodySumOnPath,
            numCutFreeBody=numCutFreeBody,
            onOptions=onOptions,
            pathName=pathName,
            showHeatFlowRate=showHeatFlowRate,
            slicingAtPathNodes=slicingAtPathNodes,
            summationLoc=summationLoc,
            summationPoint=summationPoint,
            useAboveOptions=useAboveOptions,
            useBelowOptions=useBelowOptions,
            useOnOptions=useOnOptions,
            yAxis=yAxis,
        )
