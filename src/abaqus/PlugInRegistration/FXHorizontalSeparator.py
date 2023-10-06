from __future__ import annotations

from .FXComposite import FXComposite
from .FXFrame import FXFrame


class FXHorizontalSeparator(FXFrame):
    """Horizontal separator."""

    def __init__(
        self,
        p: FXComposite,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = 1,
        pr: int = 1,
        pt: int = 0,
        pb: int = 0,
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
        """Return default height.

        Reimplemented from FXFrame.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXFrame.
        """
