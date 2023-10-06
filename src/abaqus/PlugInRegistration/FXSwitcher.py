from __future__ import annotations

from .constants import DEFAULT_SPACING
from .FXComposite import FXComposite


class FXSwitcher:
    """|"""

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
    ):
        """Construct a switcher layout manager.

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

        """

    def getCurrent(self):
        """Return the index of the child window currently on top."""

    def getDefaultHeight(self):
        """Return default height. Reimplemented from FXPacker."""

    def getDefaultWidth(self):
        """Return default width. Reimplemented from FXPacker."""

    def setCurrent(self, index: int, notify: bool = False):
        """Bring the child window at index to the top.

        Parameters
        ----------
        index : int

        notify : bool

        """
