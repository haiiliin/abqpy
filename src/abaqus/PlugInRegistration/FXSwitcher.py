from __future__ import annotations

from .constants import DEFAULT_SPACING
from .FXComposite import FXComposite
from .FXPacker import FXPacker

#: Collapse horizontally to width of current child.
SWITCHER_HCOLLAPSE: int = hash("SWITCHER_HCOLLAPSE")

#: Collapse vertically to height of current child.
SWITCHER_VCOLLAPSE: int = hash("SWITCHER_VCOLLAPSE")


class FXSwitcher(FXPacker):
    """The Switcher layout manager automatically arranges its child windows such that one of them is placed on
    top; all other child windows are hidden.

    Switcher provides a convenient method to conserve screen real-estate by arranging several GUI panels to
    appear in the same space, depending on context. Switcher ignores all layout hints from its children:-
    all children are stretched according to the switcher layout managers own size. When the
    SWITCHER_HCOLLAPSE or SWITCHER_VCOLLAPSE options are used, Switcher's default size is based on the
    width or height of the current child, instead of the maximum width or height of all of the children.
    """

    #: ID for the 1st child.
    ID_OPEN_FIRST: int = hash("ID_OPEN_FIRST")

    #: ID for the 2nd child.
    ID_OPEN_SECOND: int = hash("ID_OPEN_SECOND")

    #: ID for the 3rd child.
    ID_OPEN_THIRD: int = hash("ID_OPEN_THIRD")

    #: ID for the 4th child.
    ID_OPEN_FOURTH: int = hash("ID_OPEN_FOURTH")

    #: ID for the 5th child.
    ID_OPEN_FIFTH: int = hash("ID_OPEN_FIFTH")

    #: ID for the 6th child.
    ID_OPEN_SIXTH: int = hash("ID_OPEN_SIXTH")

    #: ID for the 7th child.
    ID_OPEN_SEVENTH: int = hash("ID_OPEN_SEVENTH")

    #: ID for the 8th child.
    ID_OPEN_EIGHTH: int = hash("ID_OPEN_EIGHTH")

    #: ID for the 9th child.
    ID_OPEN_NINETH: int = hash("ID_OPEN_NINETH")

    #: ID for the 10th child.
    ID_OPEN_TENTH: int = hash("ID_OPEN_TENTH")

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
