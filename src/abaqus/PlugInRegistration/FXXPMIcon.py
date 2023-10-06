from __future__ import annotations

from .FXApp import FXApp
from .FXColor import FXColor
from .FXIcon import FXIcon
from .FXRGB import FXRGB


class FXXPMIcon(FXIcon):
    """X Pixmap icon."""

    def __init__(
        self, a: FXApp, pix: str = "None", clr: FXColor = FXRGB(192, 192, 192), opts: int = 0, w: int = 1, h: int = 1
    ):
        """Construct icon from compiled-in X Pixmap format.

        Parameters
        ----------
        a : FXApp

        pix : str

        clr : FXColor

        opts : int

        w : int

        h : int
        """
