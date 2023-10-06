from __future__ import annotations

from .constants import DEFAULT_PAD
from .FXIcon import FXIcon
from .FXLabel import FXLabel
from .FXTabBar import FXTabBar

#: Top side tabs.
TAB_TOP: int = hash("TAB_TOP")

#: Left side tabs.
TAB_LEFT: int = hash("TAB_LEFT")

#: Right side tabs.
TAB_RIGHT: int = hash("TAB_RIGHT")

#: Bottom side tabs.
TAB_BOTTOM: int = hash("TAB_BOTTOM")

#: Normal tab item style.
TAB_TOP_NORMAL: int = hash("TAB_TOP_NORMAL")


class FXTabItem(FXLabel):
    """A tab item is placed in a tab bar or tab book.

    When selected, the tab item sends a message to its parent, and causes itself to become the active tab,
    and raised slightly above the other tabs. In the tab book, activating a tab item also causes the
    corresponding panel to be raised to the top.
    """

    def __init__(
        self,
        p: FXTabBar,
        text: str,
        ic: FXIcon | None = None,
        opts: int = TAB_TOP_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = 6,
        pr: int = 6,
        pt: int = DEFAULT_PAD,
        pb: int = DEFAULT_PAD,
    ):
        """Construct a tab item.

        Parameters
        ----------
        p : FXTabBar

        text : str

        ic : FXIcon | None

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

    def canFocus(self):
        """Returns True because a tab item can receive focus.

        Reimplemented from FXWindow.
        """
