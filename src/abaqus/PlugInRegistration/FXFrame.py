from __future__ import annotations

from .constants import DEFAULT_PAD, FRAME_NORMAL
from .FXColor import FXColor
from .FXComposite import FXComposite
from .FXWindow import FXWindow


class FXFrame(FXWindow):
    """Base Frame."""

    def __init__(
        self,
        p: FXComposite,
        opts: int = FRAME_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = DEFAULT_PAD,
        pr: int = DEFAULT_PAD,
        pt: int = DEFAULT_PAD,
        pb: int = DEFAULT_PAD,
    ):
        """Construct frame window.

        Parameters
        ----------
        p : FXComposite

        opts : int

        x : int

        y : int

        w : int

        h : int

        pl : int

        pr : int

        pt : int

        pb : int
        """

    def getBaseColor(self):
        """Get base gui color."""

    def getBorderColor(self):
        """Get border color."""

    def getBorderWidth(self):
        """Get border width."""

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXWindow. Reimplemented in FXArrowButton, FXCheckButton, FXColorBar, FXColorWell,
        FXColorWheel, FXDial, FXDockTitle, FXHeader, FXLabel, FXMDIDeleteButton, FXMDIRestoreButton,
        FXMDIMaximizeButton, FXMDIMinimizeButton, FXMDIWindowButton, FXMenuButton, FXProgressBar, FXOption,
        FXOptionMenu, FXRadioButton, FXHorizontalSeparator, FXVerticalSeparator, FXSlider, FXStatusline,
        FXTextField, FXToggleButton, FXToolbarGrip, FXToolbarTab, and AFXProgressBar.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXWindow. Reimplemented in FXArrowButton, FXCheckButton, FXColorBar, FXColorWell,
        FXColorWheel, FXDial, FXDockTitle, FXHeader, FXLabel, FXMDIDeleteButton, FXMDIRestoreButton,
        FXMDIMaximizeButton, FXMDIMinimizeButton, FXMDIWindowButton, FXMenuButton, FXProgressBar, FXOption,
        FXOptionMenu, FXRadioButton, FXHorizontalSeparator, FXVerticalSeparator, FXSlider, FXStatusline,
        FXTextField, FXToggleButton, FXToolbarGrip, FXToolbarTab, and AFXProgressBar.
        """

    def getFrameStyle(self):
        """Get current frame style."""

    def getHiliteColor(self):
        """Get highlight color."""

    def getPadBottom(self):
        """Get bottom interior padding."""

    def getPadLeft(self):
        """Get left interior padding."""

    def getPadRight(self):
        """Get right interior padding."""

    def getPadTop(self):
        """Get top interior padding."""

    def getShadowColor(self):
        """Get shadow color."""

    def setBaseColor(self, clr: FXColor):
        """Change base gui color.

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

    def setPadBottom(self, pb: int):
        """Change bottom padding.

        Parameters
        ----------
        pb : int
        """

    def setPadLeft(self, pl: int):
        """Change left padding.

        Parameters
        ----------
        pl : int
        """

    def setPadRight(self, pr: int):
        """Change right padding.

        Parameters
        ----------
        pr : int
        """

    def setPadTop(self, pt: int):
        """Change top padding.

        Parameters
        ----------
        pt : int
        """

    def setShadowColor(self, clr: FXColor):
        """Change shadow color.

        Parameters
        ----------
        clr : FXColor
        """
