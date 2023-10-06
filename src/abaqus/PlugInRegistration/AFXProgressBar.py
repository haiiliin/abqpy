from __future__ import annotations

from .constants import DEFAULT_PAD
from .FXComposite import FXComposite
from .FXObject import FXObject
from .FXProgressBar import FXProgressBar

#: Percentage complete mode.
AFXPROGRESSBAR_PERCENTAGE: int = hash("AFXPROGRESSBAR_PERCENTAGE")

#: Horizontal display.
AFXPROGRESSBAR_HORIZONTAL: int = hash("AFXPROGRESSBAR_HORIZONTAL")

#: Vertical display.
AFXPROGRESSBAR_VERTICAL: int = hash("AFXPROGRESSBAR_VERTICAL")

#: Scanner mode.
AFXPROGRESSBAR_SCANNER: int = hash("AFXPROGRESSBAR_SCANNER")

#: Iterator mode.
AFXPROGRESSBAR_ITERATOR: int = hash("AFXPROGRESSBAR_ITERATOR")


class AFXProgressBar(FXProgressBar):
    """This class contains a progress bar, which can present work-in-progress in a number of different
    styles."""

    def __init__(
        self,
        p: FXComposite,
        tgt: FXObject | None = None,
        sel: int = 0,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = DEFAULT_PAD,
        pr: int = DEFAULT_PAD,
        pt: int = DEFAULT_PAD,
        pb: int = DEFAULT_PAD,
    ):
        """Constructor.

        Parameters
        ----------
        p : FXComposite
            Parent widget.
        tgt : FXObject | None
            Message target.
        sel : int
            Message ID.
        x : int
            X coordinate of origin.
        y : int
            Y coordinate of origin.
        w : int
            Width of the widget.
        h : int
            Height of the widget.
        pl : int
            Left padding (margin).
        pr : int
            Right padding (margin).
        pt : int
            Top padding (margin).
        pb : int
            Bottom padding (margin).
        """

    def create(self):
        """Creates the progress bar.

        Reimplemented from FXProgressBar.
        """

    def getBarStyle(self):
        """Returns the progress bar style.

        Reimplemented from FXProgressBar.
        """

    def getDefaultHeight(self):
        """Returns the default height.

        Reimplemented from FXProgressBar.
        """

    def getDefaultWidth(self):
        """Returns the default width.

        Reimplemented from FXProgressBar.
        """

    def getNumCursorBoxes(self):
        """Returns the number of cursor boxes displayed."""

    def getProgress(self):
        """Returns the current progress amount.

        Reimplemented from FXProgressBar.
        """

    def getTotal(self):
        """Returns the total progress amount.

        Reimplemented from FXProgressBar.
        """

    def hide(self):
        """Hides the progress bar.

        Reimplemented from FXWindow.
        """

    def hideNumber(self):
        """Hides the progress bar iteration or percentage text.

        Reimplemented from FXProgressBar.
        """

    def setBarStyle(self, style: int):
        """Sets the progress bar style.

        Parameters
        ----------
        style : int
            Style flag.
        """

    def setNumCursorBoxes(self, nb: int):
        """Sets the number of cursor boxes to display.

        Parameters
        ----------
        nb : int
            Number of boxes.
        """

    def setProgress(self, value: int):
        """Sets the current progress amount that is used by a progress bar in either iteration or percentage
        mode; the progress amount is ingored by a progress bar in scanner mode. Reimplemented from
        FXProgressBar.

        Parameters
        ----------
        value : int
        """

    def setTotal(self, value: int):
        """Sets the total progress amount that is used by a progress bar in either iteration or percentage mode;
        the progress amount is ingored by a progress bar in scanner mode. Reimplemented from FXProgressBar.

        Parameters
        ----------
        value : int
        """

    def show(self):
        """Shows the progress bar.

        Reimplemented from FXWindow.
        """

    def showNumber(self, style: int = AFXPROGRESSBAR_PERCENTAGE):
        """Shows the progress iteration or percentage text.

        Parameters
        ----------
        style : int
            Style flag.
        """
