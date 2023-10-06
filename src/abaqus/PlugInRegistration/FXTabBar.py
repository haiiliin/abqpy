from __future__ import annotations

from .constants import DEFAULT_SPACING, TABBOOK_NORMAL
from .FXComposite import FXComposite
from .FXObject import FXObject


class FXTabBar:
    """FXTabBar"""

    def __init__(
        self,
        p: FXComposite,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = TABBOOK_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = DEFAULT_SPACING,
        pr: int = DEFAULT_SPACING,
        pt: int = DEFAULT_SPACING,
        pb: int = DEFAULT_SPACING,
    ):
        """Construct a tab bar.

        Parameters
        ----------
        p : FXComposite

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

    def create(self):
        """Create all of the server-side resources for this window // CAE. Reimplemented from FXComposite."""

    def getCurrent(self):
        """Return the currently active tab item."""

    def getDefaultHeight(self):
        """Return default height. Reimplemented from FXPacker. Reimplemented in FXTabBook."""

    def getDefaultWidth(self):
        """Return default width. Reimplemented from FXPacker. Reimplemented in FXTabBook."""

    def getTabStyle(self):
        """Return tab bar style."""

    def setCurrent(self, panel: int, notify: bool = False):
        """Change currently active tab item; this raises the active tab item slightly above the neighboring tab items.

        Parameters
        ----------
        panel : int

        notify : bool

        """

    def setTabStyle(self, style: int):
        """Change tab tab style.

        Parameters
        ----------
        style : int

        """
