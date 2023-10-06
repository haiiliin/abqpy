from __future__ import annotations

from .FXComposite import FXComposite

#: Show the scrollbars when needed.
SCROLLERS_NORMAL: int = hash("SCROLLERS_NORMAL")

#: Always show horizontal scrollers.
HSCROLLER_ALWAYS: int = hash("HSCROLLER_ALWAYS")

#: Never show horizontal scrollers.
HSCROLLER_NEVER: int = hash("HSCROLLER_NEVER")

#: Always show vertical scrollers.
VSCROLLER_ALWAYS: int = hash("VSCROLLER_ALWAYS")

#: Never show vertical scrollers.
VSCROLLER_NEVER: int = hash("VSCROLLER_NEVER")

#: Horizontal scrolling turned on (default).
HSCROLLING_ON: int = hash("HSCROLLING_ON")

#: Horizontal scrolling turned off.
HSCROLLING_OFF: int = hash("HSCROLLING_OFF")

#: Vertical scrolling turned on (default).
VSCROLLING_ON: int = hash("VSCROLLING_ON")

#: Vertical scrolling turned off.
VSCROLLING_OFF: int = hash("VSCROLLING_OFF")

#: Scrollers track continuously for smooth scrolling.
SCROLLERS_TRACK: int = hash("SCROLLERS_TRACK")

#: Scrollers don't track continuously.
SCROLLERS_DONT_TRACK: int = hash("SCROLLERS_DONT_TRACK")


class FXScrollArea(FXComposite):
    """The scroll area widget manages a content area and a viewport area through which the content is viewed.

    When the content area becomes larger than the viewport area, scrollbars are placed to permit viewing of
    the entire content by scrolling the content. Depending on the mode, scrollbars may be displayed on an
    as-needed basis, always, or never. Normally, the scroll area's size and the content's size are
    independent; however, it is possible to disable scrolling in the horizontal (vertical) direction. In
    this case, the content width (height) will influence the width (height) of the scroll area widget. For
    content which is time-consuming to repaint, continuous scrolling may be turned off.
    """

    def getContentWidth(self):
        """Return content size.

        Reimplemented in FXIconList, FXImageView, FXList, FXMDIClient, FXScrollWindow, FXTable, FXText,
        FXTreeList, AFXBaseTable, and AFXOptionTreeList.
        """

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXComposite. Reimplemented in FXList, FXTable, FXText, FXTreeList, AFXBaseTable,
        AFXList, AFXOptionTreeList, AFXTable, and AFXTreeTable.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXComposite. Reimplemented in FXList, FXTable, FXText, FXTreeList, AFXBaseTable,
        AFXOptionTreeList, AFXTable, and AFXTreeTable.
        """

    def getPosition(self, x: int, y: int):
        """Get the current position.

        Parameters
        ----------
        x : int

        y : int
        """

    def getScrollStyle(self):
        """Return scroll style."""

    def getViewportHeight(self):
        """Return viewport size.

        Reimplemented in FXIconList.
        """

    def getXPosition(self):
        """Return the current x-position."""

    def getYPosition(self):
        """Return the current y-position."""

    def horizontalScrollbar(self):
        """Return a pointer to the horizontal scrollbar."""

    def isHorizontalScrollable(self):
        """Return True if horizontally scrollable."""

    def isVerticalScrollable(self):
        """Return True if vertically scrollable."""

    def moveContents(self, x: int, y: int):
        """Move contents to the specified position. Reimplemented in FXIconList, FXMDIClient, FXScrollWindow,
        FXTable, FXText, AFXBaseTable, AFXOptionTreeList, and AFXTable.

        Parameters
        ----------
        x : int

        y : int
        """

    def setPosition(self, x: int, y: int):
        """Set the current position.

        Parameters
        ----------
        x : int

        y : int
        """

    def setScrollStyle(self, style: int):
        """Change scroll style.

        Parameters
        ----------
        style : int
        """

    def verticalScrollbar(self):
        """Return a pointer to the vertical scrollbar."""
