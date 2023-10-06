from __future__ import annotations

from .constants import DEFAULT_PAD
from .FXColor import FXColor
from .FXComposite import FXComposite
from .FXFont import FXFont
from .FXFrame import FXFrame
from .FXIcon import FXIcon

#: Icon appears under text.
ICON_UNDER_TEXT: int = hash("ICON_UNDER_TEXT")

#: Icon appears after text (to its right).
ICON_AFTER_TEXT: int = hash("ICON_AFTER_TEXT")

#: Icon appears before text (to its left).
ICON_BEFORE_TEXT: int = hash("ICON_BEFORE_TEXT")

#: Icon appears above text.
ICON_ABOVE_TEXT: int = hash("ICON_ABOVE_TEXT")

#: Icon appears below text.
ICON_BELOW_TEXT: int = hash("ICON_BELOW_TEXT")

#: Same as ICON_UNDER_TEXT.
TEXT_OVER_ICON: int = hash("TEXT_OVER_ICON")

#: Same as ICON_BEFORE_TEXT.
TEXT_AFTER_ICON: int = hash("TEXT_AFTER_ICON")

#: Same as ICON_AFTER_TEXT.
TEXT_BEFORE_ICON: int = hash("TEXT_BEFORE_ICON")

#: Same as ICON_BELOW_TEXT.
TEXT_ABOVE_ICON: int = hash("TEXT_ABOVE_ICON")

#: Same as ICON_ABOVE_TEXT.
TEXT_BELOW_ICON: int = hash("TEXT_BELOW_ICON")

#: Combination of JUSTIFY_NORMAL & ICON_BEFORE_TEXT.
LABEL_NORMAL: int = hash("LABEL_NORMAL")


class FXLabel(FXFrame):
    """A label widget can be used to place a text and/or icon for explanation purposes.

    The text label may have an optional tooltip and/or help string.
    """

    def __init__(
        self,
        p: FXComposite,
        text: str,
        ic: FXIcon | None = None,
        opts: int = LABEL_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = DEFAULT_PAD,
        pr: int = DEFAULT_PAD,
        pt: int = DEFAULT_PAD,
        pb: int = DEFAULT_PAD,
    ):
        """Construct label with given text and icon.

        Parameters
        ----------
        p : FXComposite

        text : str

        ic : FXIcon | None

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

    def create(self):
        """Create server-side resources.

        Reimplemented from FXWindow. Reimplemented in FXMenuButton, FXOptionMenu, FXToggleButton, and
        AFXFlyoutButton.
        """

    def detach(self):
        """Detach server-side resources.

        Reimplemented from FXWindow. Reimplemented in FXMenuButton, FXOptionMenu, FXToggleButton, and
        AFXFlyoutButton.
        """

    def disable(self):
        """Disable the window.

        Reimplemented from FXWindow. Reimplemented in AFXFlyoutButton.
        """

    def enable(self):
        """Enable the window.

        Reimplemented from FXWindow. Reimplemented in AFXFlyoutButton.
        """

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXFrame. Reimplemented in FXCheckButton, FXMDIDeleteButton, FXMDIRestoreButton,
        FXMDIMaximizeButton, FXMDIMinimizeButton, FXMDIWindowButton, FXMenuButton, FXOption, FXOptionMenu,
        FXRadioButton, and FXToggleButton.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXFrame. Reimplemented in FXCheckButton, FXMDIDeleteButton, FXMDIRestoreButton,
        FXMDIMaximizeButton, FXMDIMinimizeButton, FXMDIWindowButton, FXMenuButton, FXOption, FXOptionMenu,
        FXRadioButton, and FXToggleButton.
        """

    def getFont(self):
        """Get the text font."""

    def getHelpText(self):
        """Get the status line help text for this label."""

    def getIcon(self):
        """Get the icon for this label."""

    def getIconPosition(self):
        """Get the current icon position."""

    def getJustify(self):
        """Get the current text-justification mode."""

    def getText(self):
        """Get the text for this label."""

    def getTextColor(self):
        """Get the current text color."""

    def getTipText(self):
        """Get the tool tip message for this label."""

    def setFont(self, fnt: FXFont):
        """Set the text font.

        Parameters
        ----------
        fnt : FXFont
        """

    def setHelpText(self, text: str):
        """Set the status line help text for this label. Reimplemented in AFXFlyoutItem.

        Parameters
        ----------
        text : str
        """

    def setIcon(self, ic: FXIcon):
        """Set the icon for this label. Reimplemented in AFXFlyoutItem.

        Parameters
        ----------
        ic : FXIcon
        """

    def setIconPosition(self, mode: int):
        """Set the current icon position.

        Parameters
        ----------
        mode : int
        """

    def setJustify(self, mode: int):
        """Set the current text-justification mode.

        Parameters
        ----------
        mode : int
        """

    def setText(self, text: str):
        """Set the text for this label. Reimplemented in AFXFlyoutItem.

        Parameters
        ----------
        text : str
        """

    def setTextColor(self, clr: FXColor):
        """Set the current text color.

        Parameters
        ----------
        clr : FXColor
        """

    def setTipText(self, text: str):
        """Set the tool tip message for this label. Reimplemented in AFXFlyoutItem.

        Parameters
        ----------
        text : str
        """
