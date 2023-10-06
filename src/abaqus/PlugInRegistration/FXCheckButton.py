from __future__ import annotations

from .constants import CHECKBUTTON_NORMAL, DEFAULT_PAD
from .FXComposite import FXComposite
from .FXObject import FXObject


class FXCheckButton:
    """|"""

    def __init__(
        self,
        p: FXComposite,
        text: str,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = CHECKBUTTON_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = DEFAULT_PAD,
        pr: int = DEFAULT_PAD,
        pt: int = DEFAULT_PAD,
        pb: int = DEFAULT_PAD,
    ):
        """Construct new check button.

        Parameters
        ----------
        p : FXComposite

        text : str

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
        """Returns True because a check button can receive focus. Reimplemented from FXWindow."""

    def getCheck(self):
        """Get check button state (True, False or MAYBE). Reimplemented in AFXCheckButton."""

    def getDefaultHeight(self):
        """Get default height. Reimplemented from FXLabel."""

    def getDefaultWidth(self):
        """Get default width. Reimplemented from FXLabel."""

    def setCheck(self, state: bool = True):
        """Set check button state (True, False or MAYBE).

        Parameters
        ----------
        state : bool

        """
