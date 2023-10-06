from __future__ import annotations

from .constants import DEFAULT_SPACING
from .FXComposite import FXComposite
from .FXPacker import FXPacker


class FXVerticalFrame(FXPacker):
    """Vertical frame layout manager widget is used to automatically place child-windows vertically from top-to-
    bottom, or bottom-to-top, depending on the child window's layout hints."""

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
        """Construct a vertical frame layout manager.

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

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXPacker. Reimplemented in AFXVerticalAligner.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXPacker. Reimplemented in AFXVerticalAligner.
        """
