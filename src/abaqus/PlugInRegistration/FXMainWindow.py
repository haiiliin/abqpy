from __future__ import annotations

from .constants import DECOR_ALL
from .FXApp import FXApp
from .FXIcon import FXIcon
from .FXTopWindow import FXTopWindow


class FXMainWindow(FXTopWindow):
    """Main application window."""

    def __init__(
        self,
        a: FXApp,
        name: str,
        ic: FXIcon | None = None,
        mi: FXIcon | None = None,
        opts: int = DECOR_ALL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = 0,
        pr: int = 0,
        pt: int = 0,
        pb: int = 0,
        hs: int = 0,
        vs: int = 0,
    ):
        """Construct a main window.

        Parameters
        ----------
        a : FXApp

        name : str

        ic : FXIcon | None

        mi : FXIcon | None

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
