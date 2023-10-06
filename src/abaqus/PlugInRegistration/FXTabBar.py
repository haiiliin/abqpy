from __future__ import annotations

from .constants import DEFAULT_SPACING
from .FXComposite import FXComposite
from .FXObject import FXObject
from .FXPacker import FXPacker

#: Tabs on top (default).
TABBOOK_TOPTABS: int = hash("TABBOOK_TOPTABS")

#: Tabs on bottom.
TABBOOK_BOTTOMTABS: int = hash("TABBOOK_BOTTOMTABS")

#: Tabs on left.
TABBOOK_SIDEWAYS: int = hash("TABBOOK_SIDEWAYS")

#: Tabs on left.
TABBOOK_LEFTTABS: int = hash("TABBOOK_LEFTTABS")

#: Tabs on right.
TABBOOK_RIGHTTABS: int = hash("TABBOOK_RIGHTTABS")

#: Normal tab book style.
TABBOOK_NORMAL: int = hash("TABBOOK_NORMAL")


class FXTabBar(FXPacker):
    """The tab bar layout manager arranges tab items side by side, and raises the active tab item above the
    neighboring tab items.

    The tab bar can be have the tab items on the top or bottom for horizontal arrangement, or on the left or
    right for vertical arrangement.
    """

    #: Sent from one of the FXTabItems.
    ID_OPEN_ITEM: int = hash("ID_OPEN_ITEM")

    #: Switch to panel ID_OPEN_FIRST+i.
    ID_OPEN_FIRST: int = hash("ID_OPEN_FIRST")

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
        """Create all of the server-side resources for this window // CAE.

        Reimplemented from FXComposite.
        """

    def getCurrent(self):
        """Return the currently active tab item."""

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXPacker. Reimplemented in FXTabBook.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXPacker. Reimplemented in FXTabBook.
        """

    def getTabStyle(self):
        """Return tab bar style."""

    def setCurrent(self, panel: int, notify: bool = False):
        """Change currently active tab item; this raises the active tab item slightly above the neighboring tab
        items.

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
