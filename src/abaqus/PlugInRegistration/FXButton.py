from __future__ import annotations

from .constants import BUTTON_NORMAL, DEFAULT_PAD
from .FXComposite import FXComposite
from .FXIcon import FXIcon
from .FXObject import FXObject


class FXButton:
    """|"""

    def __init__(
        self,
        p: FXComposite,
        text: str,
        ic: FXIcon | None = None,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = BUTTON_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = DEFAULT_PAD,
        pr: int = DEFAULT_PAD,
        pt: int = DEFAULT_PAD,
        pb: int = DEFAULT_PAD,
    ):
        """Construct button with text and icon.

        Parameters
        ----------
        p : FXComposite

        text : str

        ic : FXIcon | None

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
        """Returns True because a button can receive focus. Reimplemented from FXWindow. Reimplemented in AFXFlyoutItem."""

    def getButtonStyle(self):
        """Get the button style flags."""

    def getState(self):
        """Get the button state."""

    def setButtonStyle(self, style: int):
        """Set the button style flags.

        Parameters
        ----------
        style : int

        """

    def setDefault(self, enable: bool = True):
        """Set as default button. Reimplemented from FXWindow.

        Parameters
        ----------
        enable : bool

        """

    def setState(self, s: int):
        """Set the button state.

        Parameters
        ----------
        s : int

        """
