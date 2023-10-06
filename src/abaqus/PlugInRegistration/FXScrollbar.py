from __future__ import annotations

from .FXColor import FXColor
from .FXComposite import FXComposite
from .FXObject import FXObject
from .FXWindow import FXWindow

#: Horizontally oriented.
SCROLLBAR_HORIZONTAL: int = hash("SCROLLBAR_HORIZONTAL")

#: Vertically oriented.
SCROLLBAR_VERTICAL: int = hash("SCROLLBAR_VERTICAL")


class FXScrollbar(FXWindow):
    """The scroll bar is used when a document has a larger content than may be made visible.

    The range is the total size of the document, the page is the part of the document which is visible. The
    size of the scrollbar thumb is adjusted to give feedback of the relative sizes of each. The scroll bar
    may be manipulated by the left mouse (normal scrolling), right mouse (vernier or fine-scrolling), or
    middle mouse (same as the left mouse only the scroll position can hop to the place where the click is
    made). Finally, if the mouse sports a wheel, the scroll bar can be manipulated by means of the mouse
    wheel as well. Holding down the Control-key during wheel motion will cause the scrolling to go faster
    than normal. While moving the scroll bar, a message of type SEL_CHANGED will be sent to the target, and
    the message data will reflect the current position of type FXint. At the end of the interaction, the
    scroll bar will send a message of type SEL_COMMAND to notify the target of the final position.
    """

    def __init__(
        self,
        p: FXComposite,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = SCROLLBAR_VERTICAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
    ):
        """Construct scroll bar.

        Parameters
        ----------
        p : FXComposite

        tgt : FXObject | None

        sel : int

        opts : int

        x : int

        y : int

        w : int

        h : int
        """

    def getBorderColor(self):
        """Change border color."""

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXWindow.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXWindow.
        """

    def getHiliteColor(self):
        """Return highlight color."""

    def getLine(self):
        """Return line increment."""

    def getPage(self):
        """Return page size."""

    def getPosition(self):
        """Return scroll position."""

    def getRange(self):
        """Return content size range."""

    def getScrollbarStyle(self):
        """Change the scrollbar style."""

    def getShadowColor(self):
        """Return shadow color."""

    def setBorderColor(self, clr: FXColor):
        """Return border color.

        Parameters
        ----------
        clr : FXColor
        """

    def setHiliteColor(self, clr: FXColor):
        """Change highlight color.

        Parameters
        ----------
        clr : FXColor
        """

    def setLine(self, l: int):
        """Set scoll increment for line.

        Parameters
        ----------
        l : int
        """

    def setPage(self, p: int):
        """Set viewport page size.

        Parameters
        ----------
        p : int
        """

    def setPosition(self, p: int, notifyTgt: bool = False):
        """Change current scroll position.

        Parameters
        ----------
        p : int

        notifyTgt : bool
        """

    def setRange(self, r: int):
        """Set content size range.

        Parameters
        ----------
        r : int
        """

    def setScrollbarStyle(self, style: int):
        """Get the current scrollbar style.

        Parameters
        ----------
        style : int
        """

    def setShadowColor(self, clr: FXColor):
        """Change shadow color.

        Parameters
        ----------
        clr : FXColor
        """
