from __future__ import annotations

from .FXComposite import FXComposite
from .FXFrame import FXFrame


class FXVerticalSeparator(FXFrame):
    """Vertical separator"""

    def __init__(
        self,
        p: FXComposite,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = 0,
        pr: int = 0,
        pt: int = 1,
        pb: int = 1,
    ):
        """Constructor.

        Parameters
        ----------
        p : FXComposite

        x : int

        y : int

        w : int

        h : int

        pl : int

        pr : int

        pt : int

        pb : int

        """

    def getDefaultHeight(self):
        """Return default height. Reimplemented from FXFrame."""

    def getDefaultWidth(self):
        """Return default width. Reimplemented from FXFrame."""
