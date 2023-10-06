from __future__ import annotations

from typing import Any

from .FXApp import FXApp
from .FXColor import FXColor


class FXBMPIcon:
    """|"""

    def __init__(
        self,
        a: FXApp,
        pix: Any | None = None,
        clr: FXColor = FXRGB(192, 192, 192),
        opts: int = 0,
        w: int = 1,
        h: int = 1,
    ):
        """Construct icon from memory stream formatted in Microsoft BMP format.

        Parameters
        ----------
        a : FXApp

        pix : Any | None

        clr : FXColor

        opts : int

        w : int

        h : int

        """
