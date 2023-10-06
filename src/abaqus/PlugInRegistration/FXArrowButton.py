from __future__ import annotations

from .constants import DEFAULT_PAD
from .FXColor import FXColor
from .FXComposite import FXComposite
from .FXFrame import FXFrame
from .FXObject import FXObject

#: No arrow.
ARROW_NONE: int = hash("ARROW_NONE")

#: Arrow points up.
ARROW_UP: int = hash("ARROW_UP")

#: Arrow points down.
ARROW_DOWN: int = hash("ARROW_DOWN")

#: Arrow points left.
ARROW_LEFT: int = hash("ARROW_LEFT")

#: Arrow points right.
ARROW_RIGHT: int = hash("ARROW_RIGHT")

#: Button repeats if held down.
ARROW_REPEAT: int = hash("ARROW_REPEAT")

#: Automatically gray out when not updated.
ARROW_AUTOGRAY: int = hash("ARROW_AUTOGRAY")

#: Automatically hide button when not updated.
ARROW_AUTOHIDE: int = hash("ARROW_AUTOHIDE")

#: Button is toolbar-style.
ARROW_TOOLBAR: int = hash("ARROW_TOOLBAR")

#: Button is spinner-style.
ARROW_SPINNER: int = hash("ARROW_SPINNER")

#: Normal arrow button.
ARROW_NORMAL: int = hash("ARROW_NORMAL")


class FXArrowButton(FXFrame):
    """Button with an arrow; the arrow can point in any direction.

    When clicked, the arrow button sends a SEL_COMMAND to its target. When ARROW_REPEAT is passed, the
    arrow button sends a SEL_COMMAND repeatedly while the button is pressed.
    """

    def __init__(
        self,
        p: FXComposite,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = ARROW_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = DEFAULT_PAD,
        pr: int = DEFAULT_PAD,
        pt: int = DEFAULT_PAD,
        pb: int = DEFAULT_PAD,
    ):
        """Construct arrow button.

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

        pl : int

        pr : int

        pt : int

        pb : int
        """

    def canFocus(self):
        """Returns True because a button can receive focus.

        Reimplemented from FXWindow.
        """

    def disable(self):
        """Disable the button.

        Reimplemented from FXWindow.
        """

    def enable(self):
        """Enable the button.

        Reimplemented from FXWindow.
        """

    def getArrowColor(self):
        """Get the fill color for the arrow."""

    def getArrowSize(self):
        """Get the default arrow size."""

    def getArrowStyle(self):
        """Get the arrow style flags."""

    def getDefaultHeight(self):
        """Get default height.

        Reimplemented from FXFrame.
        """

    def getDefaultWidth(self):
        """Get default width.

        Reimplemented from FXFrame.
        """

    def getJustify(self):
        """Get the current justification mode."""

    def getState(self):
        """Get the button state (where True means the button is down)."""

    def getTipText(self):
        """Get tool tip message for this arrow button."""

    def setArrowColor(self, clr: FXColor):
        """Set the fill color for the arrow.

        Parameters
        ----------
        clr : FXColor
        """

    def setArrowSize(self, size: int):
        """Set the default arrow size.

        Parameters
        ----------
        size : int
        """

    def setArrowStyle(self, style: int):
        """Set the arrow style flags.

        Parameters
        ----------
        style : int
        """

    def setJustify(self, mode: int):
        """Set the current justification mode.

        Parameters
        ----------
        mode : int
        """

    def setState(self, s: bool):
        """Set the button state (where True means the button is down).

        Parameters
        ----------
        s : bool
        """

    def setTipText(self, text: str):
        """Set tool tip message for this arrow button.

        Parameters
        ----------
        text : str
        """
