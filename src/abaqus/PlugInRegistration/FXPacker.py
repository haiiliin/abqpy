from __future__ import annotations

from .constants import DEFAULT_SPACING
from .FXColor import FXColor
from .FXComposite import FXComposite


class FXPacker(FXComposite):
    """Packer is a layout manager which automatically places child windows inside its area against the left,
    right, top, or bottom side.

    Each time a child is placed, the remaining space is decreased by the amount of space taken by the child
    window. The side against which a child is placed is determined by the LAYOUT_SIDE_TOP,
    LAYOUT_SIDE_BOTTOM, LAYOUT_SIDE_LEFT, and LAYOUT_SIDE_RIGHT hints given by the child window. Other
    layout hints from the child are observed as far as sensible. So for example, a child placed against the
    right edge can still have LAYOUT_FILL_Y or LAYOUT_TOP, and so on. The last child may have both
    LAYOUT_FILL_X and LAYOUT_FILL_Y, in which case it will be placed to take all remaining space.
    """

    def __init__(
        self,
        p: FXComposite,
        opts: int = 0,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = DEFAULT_SPACING,
        pr: int = DEFAULT_SPACING,
        pt: int = DEFAULT_SPACING,
        pb: int = DEFAULT_SPACING,
        hs: int = DEFAULT_SPACING,
        vs: int = DEFAULT_SPACING,
    ):
        """Construct packer layout manager.

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

        hs : int

        vs : int
        """

    def getBaseColor(self):
        """Get base gui color."""

    def getBorderColor(self):
        """Get border color."""

    def getBorderWidth(self):
        """Get border width."""

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXComposite. Reimplemented in FXComboBox, FXDockSite, FXGroupBox,
        FXHorizontalFrame, FXListBox, FXMatrix, FXSpinner, FXStatusbar, FXSwitcher, FXTabBar, FXTabBook,
        FXToolbar, FXTreeListBox, FXVerticalFrame, AFXToolbarGroup, AFXPrimFloatSpinner, AFXSlider, and
        AFXVerticalAligner.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXComposite. Reimplemented in FXComboBox, FXDockSite, FXGroupBox,
        FXHorizontalFrame, FXListBox, FXMatrix, FXSpinner, FXStatusbar, FXSwitcher, FXTabBar, FXTabBook,
        FXToolbar, FXTreeListBox, FXVerticalFrame, AFXToolbarGroup, AFXOptionTreeItem, AFXPrimFloatSpinner,
        AFXSlider, AFXTextField, and AFXVerticalAligner.
        """

    def getFrameStyle(self):
        """Get current frame style."""

    def getHiliteColor(self):
        """Get highlight color."""

    def getHSpacing(self):
        """Return current horizontal inter-child spacing."""

    def getPackingHints(self):
        """Return packing hints."""

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

    def getVSpacing(self):
        """Return current vertical inter-child spacing."""

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

    def setHSpacing(self, hs: int):
        """Change horizontal inter-child spacing.

        Parameters
        ----------
        hs : int
        """

    def setPackingHints(self, ph: int):
        """Change packing hints.

        Parameters
        ----------
        ph : int
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

    def setVSpacing(self, vs: int):
        """Change vertical inter-child spacing.

        Parameters
        ----------
        vs : int
        """
