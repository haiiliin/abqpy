from __future__ import annotations

from .FXComposite import FXComposite
from .FXIcon import FXIcon
from .FXListItem import FXListItem
from .FXObject import FXObject
from .FXScrollArea import FXScrollArea

#: Extended selection mode allows for drag-selection of ranges of items.
LIST_EXTENDEDSELECT: int = hash("LIST_EXTENDEDSELECT")

#: Single selection mode allows up to one item to be selected.
LIST_SINGLESELECT: int = hash("LIST_SINGLESELECT")

#: Browse selection mode enforces one single item to be selected at all times.
LIST_BROWSESELECT: int = hash("LIST_BROWSESELECT")

#: Multiple selection mode is used for selection of individual items.
LIST_MULTIPLESELECT: int = hash("LIST_MULTIPLESELECT")

#: Automatically select under cursor.
LIST_AUTOSELECT: int = hash("LIST_AUTOSELECT")

#: Normal list style.
LIST_NORMAL: int = hash("LIST_NORMAL")


class FXList(FXScrollArea):
    """List Widget."""

    def __init__(
        self,
        p: FXComposite,
        nvis: int,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = LIST_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
    ):
        """Construct a list with nvis visible items; the list is initially empty.

        Parameters
        ----------
        p : FXComposite

        nvis : int

        tgt : FXObject | None

        sel : int

        opts : int

        x : int

        y : int

        w : int

        h : int
        """

    def appendItem(self, item: FXListItem, notify: bool = False):
        """Append a [possibly subclassed] item to the list.

        Parameters
        ----------
        item : FXListItem

        notify : bool
        """

    def canFocus(self):
        """List widget can receive focus.

        Reimplemented from FXWindow.
        """

    def clearItems(self, notify: bool = False):
        """Remove all items from list.

        Parameters
        ----------
        notify : bool
        """

    def create(self):
        """Create server-side resources.

        Reimplemented from FXComposite.
        """

    def deselectItem(self, index: int, notify: bool = False):
        """Deselect item.

        Parameters
        ----------
        index : int

        notify : bool
        """

    def detach(self):
        """Detach server-side resources.

        Reimplemented from FXComposite.
        """

    def findItem(self, text: str, start: int = -1):
        """Search items for item by name, starting from start item; the flags argument controls the search
        direction, and case sensitivity.

        Parameters
        ----------
        text : str

        start : int
        """

    def getContentHeight(self):
        """Return content height.

        Reimplemented from FXScrollArea.
        """

    def getContentWidth(self):
        """Compute and return content width.

        Reimplemented from FXScrollArea.
        """

    def getCurrentItem(self):
        """Return current item, if any."""

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXScrollArea. Reimplemented in AFXList.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXScrollArea.
        """

    def getItemData(self, index: int):
        """Return item user-data pointer.

        Parameters
        ----------
        index : int
        """

    def getItemHeight(self, index: int):
        """Return item height.

        Parameters
        ----------
        index : int
        """

    def getItemIcon(self, index: int):
        """Return item icon, if any.

        Parameters
        ----------
        index : int
        """

    def getItemText(self, index: int):
        """Return item text.

        Parameters
        ----------
        index : int
        """

    def getItemWidth(self, index: int):
        """Return item width.

        Parameters
        ----------
        index : int
        """

    def getListStyle(self):
        """Return list style."""

    def getNumItems(self):
        """Return the number of items in the list."""

    def getNumVisible(self):
        """Return number of visible items."""

    def insertItem(self, index: int, item: FXListItem, notify: bool = False):
        """Insert a new [possibly subclassed] item at the give index.

        Parameters
        ----------
        index : int

        item : FXListItem

        notify : bool
        """

    def isItemSelected(self, index: int):
        """Return True if item is selected.

        Parameters
        ----------
        index : int
        """

    def isItemVisible(self, index: int):
        """Return True if item is visible.

        Parameters
        ----------
        index : int
        """

    def killSelection(self, notify: bool = False):
        """Deselect all items.

        Parameters
        ----------
        notify : bool
        """

    def makeItemVisible(self, index: int):
        """Scroll to bring item into view.

        Parameters
        ----------
        index : int
        """

    def recalc(self):
        """Recalculate layout.

        Reimplemented from FXWindow.
        """

    def removeItem(self, index: int, notify: bool = False):
        """Remove item from list.

        Parameters
        ----------
        index : int

        notify : bool
        """

    def replaceItem(self, index: int, item: FXListItem, notify: bool = False):
        """Replace the item with a [possibly subclassed] item.

        Parameters
        ----------
        index : int

        item : FXListItem

        notify : bool
        """

    def retrieveItem(self, index: int):
        """Return the item at the given index.

        Parameters
        ----------
        index : int
        """

    def selectItem(self, index: int, notify: bool = False):
        """Select item.

        Parameters
        ----------
        index : int

        notify : bool
        """

    def setCurrentItem(self, index: int, notify: bool = False):
        """Change current item.

        Parameters
        ----------
        index : int

        notify : bool
        """

    def setItemData(self, index: int, ptr: str):
        """Change item user-data pointer.

        Parameters
        ----------
        index : int

        ptr : str
        """

    def setItemIcon(self, index: int, icon: FXIcon):
        """Change item icon.

        Parameters
        ----------
        index : int

        icon : FXIcon
        """

    def setItemText(self, index: int, text: str):
        """Change item text.

        Parameters
        ----------
        index : int

        text : str
        """

    def setListStyle(self, style: int):
        """Change list style.

        Parameters
        ----------
        style : int
        """

    def setNumVisible(self, nvis: int):
        """Change the number of visible items.

        Parameters
        ----------
        nvis : int
        """
