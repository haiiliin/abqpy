from __future__ import annotations

from .constants import DEFAULT_SPACING
from .FXComposite import FXComposite
from .FXObject import FXObject
from .FXTabBar import FXTabBar

#: Normal tab book style.
TABBOOK_NORMAL: int = hash("TABBOOK_NORMAL")


class FXTabBook(FXTabBar):
    """The tab book layout manager arranges pairs of children; the even numbered children (0,2,4,...) are
    usually tab items, and are placed on the top.

    The odd numbered children are usually layout managers, and are placed below; all the odd numbered
    children are placed on top of each other, similar to the switcher widget. When the user presses one of
    the tab items, the tab item is raised above the neighboring tabs, and the corresponding panel is raised
    to the top. Thus, a tab book can be used to present many GUI controls in a small space by placing
    several panels on top of each other and using tab items to select the desired panel.
    """

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
        """Construct tab book.

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

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXTabBar.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXTabBar.
        """
