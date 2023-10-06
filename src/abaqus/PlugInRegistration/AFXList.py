from __future__ import annotations

from .FXComposite import FXComposite
from .FXIcon import FXIcon
from .FXList import FXList
from .FXObject import FXObject

#: Don't automatically commit on double click.
AFXLIST_NO_AUTOCOMMIT: int = hash("AFXLIST_NO_AUTOCOMMIT")


class AFXList(FXList):
    """This class is a list widget that allows displaying items in a scrollable window.

    Each item has associated data set as integers as items are added.
    """

    def __init__(
        self,
        p: FXComposite,
        nvis: int,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = 0,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
    ):
        """Constructor.

        Parameters
        ----------
        p : FXComposite
            Parent widget.
        nvis : int
            Number of visible items.
        tgt : FXObject | None
            Message target.
        sel : int
            Message ID.
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
        """

    def appendItem(self, text: str, icon: FXIcon | None = None, sel: int = 0):  # type: ignore
        """Adds a new item to the end of the list.

        Parameters
        ----------
        text : str
            Text
        icon : FXIcon | None
            Icon
        sel : int
            Integer associated with this item
        """

    def disable(self):
        """Disables the list.

        Reimplemented from FXWindow.
        """

    def enable(self):
        """Enables the list.

        Reimplemented from FXWindow.
        """

    def getAutoCommit(self):
        """Returns the auto-commit flag."""

    def getDefaultHeight(self):
        """Returns the default height of the list.

        Reimplemented from FXList.
        """

    def getItemIndexForData(self, data: str):
        """Returns the index of the first item with the associated data or -1 if not found.

        Parameters
        ----------
        data : str
        """

    def getItemProvider(self):
        """Returns the provider of the list's items."""

    def getSingleSelection(self):
        """Returns the index of the uniquely selected item.

        If more than one item or no items are selected, returns -1.
        """

    def insertItem(self, index: int, text: str, icon: FXIcon | None = None, sel: int = 0):  # type: ignore
        """Inserts a new item at the given index.

        Parameters
        ----------
        index : int
            Index
        text : str
            Text
        icon : FXIcon | None
            Icon
        sel : int
            Integer associated with this item
        """

    def replaceItem(self, index: int, text: str, icon: FXIcon | None = None, sel: int = 0):  # type: ignore
        """Replaces the item at the given index.

        Parameters
        ----------
        index : int
            Index
        text : str
            Text
        icon : FXIcon | None
            Icon
        sel : int
            Integer associated with this item
        """

    def setAutoCommit(self, commit: bool):
        """Sets the auto-commit option for handling double clicks. This option is turned on by default.

        Parameters
        ----------
        commit : bool
        """

    def setItemProvider(self, cp: FXObject):
        """Sets the provider of the list's items.

        Parameters
        ----------
        cp : FXObject
        """
