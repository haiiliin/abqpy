from __future__ import annotations

from .constants import DEFAULT_SPACING, GROUPBOX_NORMAL
from .FXComposite import FXComposite


class FXGroupBox:
    """Abaqus"""

    def __init__(
        self,
        p: FXComposite,
        text: str,
        opts: int = GROUPBOX_NORMAL,
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
        """Construct group box layout manager.

        Parameters
        ----------
        p : FXComposite

        text : str

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

    def create(self):
        """Create server-side resources. Reimplemented from FXComposite."""

    def detach(self):
        """Detach server-side resources. Reimplemented from FXComposite."""

    def disable(self):
        """Disable the window. Reimplemented from FXWindow."""

    def enable(self):
        """Enable the window. Reimplemented from FXWindow."""

    def getDefaultHeight(self):
        """Return default height. Reimplemented from FXPacker."""

    def getDefaultWidth(self):
        """Return default width. Reimplemented from FXPacker."""

    def getText(self):
        """Return current groupbox title text."""

    def setText(self, text: str):
        """Change group box title text.

        Parameters
        ----------
        text : str

        """
