from __future__ import annotations

from .constants import DEFAULT_SPACING
from .FXComposite import FXComposite
from .FXPacker import FXPacker


class FXSwitcher(FXPacker):
    """The Switcher layout manager automatically arranges its child windows such that one of them is placed on
    top; all other child windows are hidden.

    Switcher provides a convenient method to conserve screen real-estate by arranging several GUI panels to
    appear in the same space, depending on context. Switcher ignores all layout hints from its children:-
    all children are stretched according to the switcher layout managers own size. When the
    SWITCHER\_HCOLLAPSE or SWITCHER\_VCOLLAPSE options are used, Switcher's default size is based on the
    width or height of the current child, instead of the maximum width or height of all of the children.
    """

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
        """Return default height.

        Reimplemented from FXPacker.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXPacker.
        """

    def setCurrent(self, index: int, notify: bool = False):
        """Bring the child window at index to the top.

        Parameters
        ----------
        index : int

        notify : bool
        """
