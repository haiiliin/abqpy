from __future__ import annotations

from typing import Any

from .AFXDataComponent import AFXDataComponent
from .constants import DEFAULT_PAD
from .FXComposite import FXComposite
from .FXFont import FXFont
from .FXIcon import FXIcon
from .FXObject import FXObject
from .FXPacker import FXPacker

#: Orient label above list box.
AFXLISTBOX_VERTICAL: int = hash("AFXLISTBOX_VERTICAL")

#: Configure list box to the read-only state.
AFXLISTBOX_READONLY: int = hash("AFXLISTBOX_READONLY")


class AFXListBox(FXPacker, AFXDataComponent):
    """This class implements a labeled list box.

    It allows the user to select entries from a drop-down list. Each item has associated data set as
    integers initially as items are added.
    """

    #: ID for the list box.
    ID_LIST: int = hash("ID_LIST")

    #: ID for the text field.
    ID_FIELD: int = hash("ID_FIELD")

    def __init__(
        self,
        p: FXComposite,
        nvis: int,
        labelText: str,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = 0,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = DEFAULT_PAD,
        pr: int = DEFAULT_PAD,
        pt: int = DEFAULT_PAD,
        pb: int = DEFAULT_PAD,
    ):
        """Constructor.

        Parameters
        ----------
        p : FXComposite
            Parent widget.
        nvis : int
            Number of visible items.
        labelText : str
            Label string.
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
        pl : int
            Left padding (margin).
        pr : int
            Right padding (margin).
        pt : int
            Top padding (margin).
        pb : int
            Bottom padding (margin).
        """

    def appendItem(self, text: str, icon: FXIcon | None = None, sel: int = 0):
        """Adds an item to the end of the list.

        Parameters
        ----------
        text : str
            Text
        icon : FXIcon | None

        sel : int
            Icon Integer associated with this item
        """

    def clearItems(self):
        """Removes all items from the list."""

    def create(self):
        """Creates the list box.

        Reimplemented from FXComposite.
        """

    def disable(self):
        """Disables the list box.

        Reimplemented from FXWindow.
        """

    def enable(self):
        """Enables the list box.

        Reimplemented from FXWindow.
        """

    def getCurrentItem(self):
        """Returns the index of the current item."""

    def getHelpText(self):
        """Returns the status line help text."""

    def getItemData(self, index: int):
        """Returns the data for the specified item.

        Parameters
        ----------
        index : int
        """

    def getItemIndexForData(self, data: Any):
        """Returns the index of the first item with the associated data or -1 if not found.

        Parameters
        ----------
        data : Any
        """

    def getLabelFont(self):
        """Returns the label font."""

    def getLabelText(self):
        """Returns the label string."""

    def getNumItems(self):
        """Returns the number of items in the list."""

    def getNumVisible(self):
        """Returns the number of visible items."""

    def getTipText(self):
        """Returns the tool tip message."""

    def insertItem(self, index: int, text: str, icon: FXIcon | None = None, sel: int = 0):
        """Inserts a new item at the specified index position.

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

    def isItemCurrent(self, index: int):
        """Returns True if the item at the specified index position is the current item.

        Parameters
        ----------
        index : int
        """

    def isReadOnlyState(self):
        """Returns True if the list box is set to the read-only state."""

    def removeItem(self, index: int):
        """Removes the item at the specified index position from the list.

        Parameters
        ----------
        index : int
        """

    def replaceItem(self, index: int, text: str, icon: FXIcon | None = None, sel: int = 0):
        """Replaces the item at the specified index position.

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

    def setCurrentItem(self, index: int, notify: bool = False):
        """Sets the current item. (The index is zero-based).

        Parameters
        ----------
        index : int

        notify : bool
        """

    def setHelpText(self, text: str):
        """Sets the status line help text.

        Parameters
        ----------
        text : str
        """

    def setItemData(self, index: int, ptr: str):
        """Sets the data for the specified item.

        Parameters
        ----------
        index : int

        ptr : str
        """

    def setLabelFont(self, fnt: FXFont):
        """Sets the label font.

        Parameters
        ----------
        fnt : FXFont
        """

    def setLabelText(self, txt: str):
        """Sets the label string.

        Parameters
        ----------
        txt : str
        """

    def setNumVisible(self, nvis: int):
        """Sets the number of visible items.

        Parameters
        ----------
        nvis : int
        """

    def setReadOnlyState(self, readonly: bool = True):
        """Sets the read-only state of the list box.

        Parameters
        ----------
        readonly : bool
        """

    def setTipText(self, text: str):
        """Sets the tool tip message.

        Parameters
        ----------
        text : str
        """
