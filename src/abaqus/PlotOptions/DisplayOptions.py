from abaqusConstants import *


class DisplayOptions:
    """The DisplayOptions object stores a plot state.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import visualization
            session.viewports[name].layers[name].odbDisplay.display
            session.viewports[name].odbDisplay.display
    """

    #: A tuple of SymbolicConstants specifying the plot state of the display. Possible values
    #: are UNDEFORMED, DEFORMED, CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, SYMBOLS_ON_UNDEF,
    #: SYMBOLS_ON_DEF, ORIENT_ON_UNDEF, and ORIENT_ON_DEF. The default value is (UNDEFORMED).
    plotState: SymbolicConstant = None

    def setValues(
        self, options: "DisplayOptions" = None, plotState: SymbolicConstant = None
    ):
        """This method modifies the DisplayOptions object.

        Parameters
        ----------
        options
            A :py:class:`~abaqus.PlotOptions.DisplayOptions.DisplayOptions` object from which values are to be copied. If other arguments are also
            supplied to setValues, they will override the values in **options**. The default value is
            None.
        plotState
            A sequence of SymbolicConstants specifying the plot state of the display. Possible
            values are UNDEFORMED, DEFORMED, CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, SYMBOLS_ON_UNDEF,
            SYMBOLS_ON_DEF, ORIENT_ON_UNDEF, and ORIENT_ON_DEF. The default value is (UNDEFORMED).
        """
        pass
