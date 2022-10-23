from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from ..UtilityAndView.abaqusConstants import SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from .._OptionsBase import _CopyOptionsBase


@abaqus_class_doc
class DisplayOptions(_CopyOptionsBase):
    """The DisplayOptions object stores a plot state.

    .. note::
        This object can be accessed by::

            import visualization
            session.viewports[name].layers[name].odbDisplay.display
            session.viewports[name].odbDisplay.display
    """

    #: A tuple of SymbolicConstants specifying the plot state of the display. Possible values
    #: are UNDEFORMED, DEFORMED, CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, SYMBOLS_ON_UNDEF,
    #: SYMBOLS_ON_DEF, ORIENT_ON_UNDEF, and ORIENT_ON_DEF. The default value is (UNDEFORMED).
    plotState: Optional[SymbolicConstant] = None

    @abaqus_method_doc
    def setValues(
        self,
        options: Optional["DisplayOptions"] = None,
        plotState: Optional[
            Literal[
                C.SYMBOLS_ON_DEF,
                C.ORIENT_ON_UNDEF,
                C.DEFORMED,
                C.ORIENT_ON_DEF,
                C.CONTOURS_ON_DEF,
                C.CONTOURS_ON_UNDEF,
                C.SYMBOLS_ON_UNDEF,
                C.UNDEFORMED,
            ]
        ] = None,
    ):
        """This method modifies the DisplayOptions object.

        Parameters
        ----------
        options
            A :py:class:`~abaqus.PlotOptions.DisplayOptions.DisplayOptions` object from which values are to be copied.
            If other arguments are also supplied to setValues, they will override the values in **options**. The default
            value is None.
        plotState
            A sequence of SymbolicConstants specifying the plot state of the display. Possible
            values are UNDEFORMED, DEFORMED, CONTOURS_ON_UNDEF, CONTOURS_ON_DEF, SYMBOLS_ON_UNDEF,
            SYMBOLS_ON_DEF, ORIENT_ON_UNDEF, and ORIENT_ON_DEF. The default value is (UNDEFORMED).
        """
        super().setValues(options=options, plotState=plotState)
