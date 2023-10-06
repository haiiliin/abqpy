from __future__ import annotations

from .AFXOptionTreeItem import AFXOptionTreeItem
from .constants import DEFAULT_SPACING
from .FXComposite import FXComposite
from .FXObject import FXObject
from .FXScrollWindow import FXScrollWindow


class AFXOptionTreeList(FXScrollWindow):
    """This class provides a scrolled list of groups of options that may be toggled on or off as a group or
    individually."""

    #: ID for the content window.
    ID_CONTENTS: int = hash("ID_CONTENTS")

    def __init__(
        self,
        p: FXComposite,
        nvis: int,
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
        """Constructor.

        Parameters
        ----------
        p : FXComposite
            Parent widget.
        nvis : int
            Number of visible items of list.
        opts : int
            Options and hints.
        x : int
            X coordinate of origin.
        y : int
            Y coordinate of origin.
        w : int
            Width of the widget.
        h : int
            Height of the widget.
        pl : int
            Left padding.
        pr : int
            Right padding.
        pt : int
            Top padding.
        pb : int
            Bottom padding.
        hs : int
            Horizontal spacing.
        vs : int
            Vertical spacing.
        """

    def addItemFirst(self, text: str, tgt: FXObject | None = None, msg: int = 0):
        """Adds a new item with the given text as the first item of the list.

        Parameters
        ----------
        text : str
            Item text.
        tgt : FXObject | None
            Item target.
        msg : int
            Item selector.
        """

    def addItemLast(self, text: str, tgt: FXObject | None = None, msg: int = 0):
        """Adds a new item with the given text as the last item of the list.

        Parameters
        ----------
        text : str
            Item text.
        tgt : FXObject | None
            Item target.
        msg : int
            Item selector.
        """

    def clearItems(self):
        """Removes all items from the list."""

    def computeItemHeight(self, p: AFXOptionTreeItem | None = None):
        """Computes the item size to be used as a base for default height computation.

        Parameters
        ----------
        p : AFXOptionTreeItem | None
            Item.
        """

    def createItem(self, text: str, tgt: FXObject, msg: int):
        """Creates a new tree item object.

        Parameters
        ----------
        text : str
            Item text.
        tgt : FXObject
            Item target.
        msg : int
            Item selector.
        """

    def getContentHeight(self):
        """Returns the content height.

        Reimplemented from FXScrollWindow.
        """

    def getContents(self):
        """Returns the content window."""

    def getContentWidth(self):
        """Returns the content width.

        Reimplemented from FXScrollWindow.
        """

    def getDefaultHeight(self):
        """Returns the default height.

        Reimplemented from FXScrollArea.
        """

    def getDefaultWidth(self):
        """Returns the default width.

        Reimplemented from FXScrollArea.
        """

    def getFirstItem(self):
        """Returns the first root item."""

    def getHSpacing(self):
        """Returns the horizontal inter-child spacing."""

    def getLastItem(self):
        """Returns the last root item."""

    def getNumItems(self):
        """Returns the number of top-level items."""

    def getNumVisible(self):
        """Returns the number of visible items."""

    def getPadBottom(self):
        """Returns the bottom padding."""

    def getPadLeft(self):
        """Returns the left padding."""

    def getPadRight(self):
        """Returns the right padding."""

    def getPadTop(self):
        """Returns the top padding."""

    def getVSpacing(self):
        """Returns the vertical inter-child spacing."""

    def layout(self):
        """Recalculates layout.

        Reimplemented from FXScrollWindow.
        """

    def moveContents(self, x: int, y: int):
        """Moves contents to the specified position.

        Parameters
        ----------
        x : int
            X location.
        y : int
            Y location
        """

    def removeItem(self, item: AFXOptionTreeItem):
        """Removes the given item from the list. This method does nothing if the given item does not exist.

        Parameters
        ----------
        item : AFXOptionTreeItem
            Item to be removed.
        """

    def setHSpacing(self, hs: int):
        """Sets the horizontal inter-child spacing.

        Parameters
        ----------
        hs : int
            Horizontal spacing.
        """

    def setNumVisible(self, nvis: int):
        """Sets the number of visible items.

        Parameters
        ----------
        nvis : int
            Number of visible items.
        """

    def setPadBottom(self, pb: int):
        """Sets the bottom padding.

        Parameters
        ----------
        pb : int
            Bottom padding.
        """

    def setPadLeft(self, pl: int):
        """Sets the left padding.

        Parameters
        ----------
        pl : int
            Left padding.
        """

    def setPadRight(self, pr: int):
        """Sets the right padding.

        Parameters
        ----------
        pr : int
            Right padding.
        """

    def setPadTop(self, pt: int):
        """Sets the top padding.

        Parameters
        ----------
        pt : int
            Top padding.
        """

    def setVSpacing(self, vs: int):
        """Sets the vertical inter-child spacing.

        Parameters
        ----------
        vs : int
            Vertical spacing.
        """
