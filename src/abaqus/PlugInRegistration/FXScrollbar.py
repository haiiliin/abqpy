from __future__ import annotations

from .constants import SCROLLBAR_VERTICAL
from .FXColor import FXColor
from .FXComposite import FXComposite
from .FXObject import FXObject


class FXScrollbar:
    """|"""

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
        """Return default height. Reimplemented from FXWindow."""

    def getDefaultWidth(self):
        """Return default width. Reimplemented from FXWindow."""

    def getHiliteColor(self):
        """Return highlight color."""

    def getLine(self):
        """Return line increment."""

    def getPage(self):
        """Return page size."""

    def getPosition(self):
        """return scroll position"""

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
