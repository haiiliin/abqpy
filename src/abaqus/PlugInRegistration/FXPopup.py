from __future__ import annotations

from .FXColor import FXColor
from .FXShell import FXShell
from .FXWindow import FXWindow

#: Vertical orientation.
POPUP_VERTICAL: int = hash("POPUP_VERTICAL")

#: Horizontal orientation.
POPUP_HORIZONTAL: int = hash("POPUP_HORIZONTAL")

#: Shrinkwrap to content.
POPUP_SHRINKWRAP: int = hash("POPUP_SHRINKWRAP")


class FXPopup(FXShell):
    """Popup window."""

    def __init__(self, owner: FXWindow, x: int = 0, y: int = 0, w: int = 0, h: int = 0):
        """Construct popup pane.

        Parameters
        ----------
        owner : FXWindow

        x : int

        y : int

        w : int

        h : int
        """

    def getBaseColor(self):
        """Return base color."""

    def getBorderColor(self):
        """Return border color."""

    def getBorderWidth(self):
        """Return border width."""

    def getDefaultHeight(self):
        """Return the default height of this window.

        Reimplemented from FXComposite.
        """

    def getDefaultWidth(self):
        """Return the default width of this window.

        Reimplemented from FXComposite.
        """

    def getFrameStyle(self):
        """Return frame style."""

    def getGrabOwner(self):
        """Return current grab owner."""

    def getHiliteColor(self):
        """Return highlight color."""

    def getOrientation(self):
        """Return popup orientation."""

    def getShadowColor(self):
        """Return shadow color."""

    def getShrinkWrap(self):
        """Return shrinkwrap mode."""

    def popdown(self):
        """Pop down the menu."""

    def popup(self, grabto: FXWindow, x: int, y: int, w: int = 0, h: int = 0):
        """Popup the menu and grab to the given owner.

        Parameters
        ----------
        grabto : FXWindow

        x : int

        y : int

        w : int

        h : int
        """

    def setBaseColor(self, clr: FXColor):
        """Change base color.

        Parameters
        ----------
        clr : FXColor
        """

    def setBorderColor(self, clr: FXColor):
        """Change border color.

        Parameters
        ----------
        clr : FXColor
        """

    def setFrameStyle(self, style: int):
        """Change frame style.

        Parameters
        ----------
        style : int
        """

    def setHiliteColor(self, clr: FXColor):
        """Change highlight color.

        Parameters
        ----------
        clr : FXColor
        """

    def setOrientation(self, orient: int):
        """Change popup orientation.

        Parameters
        ----------
        orient : int
        """

    def setShadowColor(self, clr: FXColor):
        """Change shadow color.

        Parameters
        ----------
        clr : FXColor
        """

    def setShrinkWrap(self, sw: bool):
        """Change shrinkwrap mode.

        Parameters
        ----------
        sw : bool
        """
