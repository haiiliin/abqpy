from __future__ import annotations

from .FXColor import FXColor
from .FXComposite import FXComposite
from .FXFont import FXFont
from .FXIcon import FXIcon
from .FXIconItem import FXIconItem
from .FXIconListSortFunc import FXIconListSortFunc
from .FXObject import FXObject
from .FXScrollArea import FXScrollArea

#: Extended selection mode.
ICONLIST_EXTENDEDSELECT: int = hash("ICONLIST_EXTENDEDSELECT")

#: At most one selected item.
ICONLIST_SINGLESELECT: int = hash("ICONLIST_SINGLESELECT")

#: Always exactly one selected item.
ICONLIST_BROWSESELECT: int = hash("ICONLIST_BROWSESELECT")

#: Multiple selection mode.
ICONLIST_MULTIPLESELECT: int = hash("ICONLIST_MULTIPLESELECT")

#: Automatically size item spacing.
ICONLIST_AUTOSIZE: int = hash("ICONLIST_AUTOSIZE")

#: List mode.
ICONLIST_DETAILED: int = hash("ICONLIST_DETAILED")

#: Mini Icon mode.
ICONLIST_MINI_ICONS: int = hash("ICONLIST_MINI_ICONS")

#: Big Icon mode.
ICONLIST_BIG_ICONS: int = hash("ICONLIST_BIG_ICONS")

#: Row-wise mode.
ICONLIST_ROWS: int = hash("ICONLIST_ROWS")

#: Column-wise mode.
ICONLIST_COLUMNS: int = hash("ICONLIST_COLUMNS")

#: Normal icon list style.
ICONLIST_NORMAL: int = hash("ICONLIST_NORMAL")


class FXIconList(FXScrollArea):
    """Icon List Widget."""

    def __init__(
        self,
        p: FXComposite,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = ICONLIST_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
    ):
        """Construct icon list.

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
        """

    def appendItem(self, item: FXIconItem, notify: bool = False):
        """Append a [possibly subclassed] item to the end of the list.

        Parameters
        ----------
        item : FXIconItem

        notify : bool
        """

    def canFocus(self):
        """Icon list can receive focus.

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

        Reimplemented from FXComposite. Reimplemented in FXFileList.
        """

    def deselectItem(self, index: int, notify: bool = False):
        """Deselect item at index.

        Parameters
        ----------
        index : int

        notify : bool
        """

    def detach(self):
        """Detach server-side resources.

        Reimplemented from FXComposite. Reimplemented in FXFileList.
        """

    def disableItem(self, index: int):
        """Disable item at index.

        Parameters
        ----------
        index : int
        """

    def enableItem(self, index: int):
        """Enable item at index.

        Parameters
        ----------
        index : int
        """

    def extendSelection(self, index: int, notify: bool = False):
        """Extend selection from anchor index to index.

        Parameters
        ----------
        index : int

        notify : bool
        """

    def findItem(self, text: str, start: int = -1):
        """Search items for item by name, starting from start item; the flags argument controls the search
        direction, and case sensitivity.

        Parameters
        ----------
        text : str

        start : int
        """

    def getAnchorItem(self):
        """Return anchor item index, or -1 if none."""

    def getContentHeight(self):
        """Return content height.

        Reimplemented from FXScrollArea.
        """

    def getContentWidth(self):
        """Compute and return content width.

        Reimplemented from FXScrollArea.
        """

    def getCurrentItem(self):
        """Return current item index, or -1 if none."""

    def getCursorItem(self):
        """Return index of item under cursor, or -1 if none."""

    def getFont(self):
        """Return text font."""

    def getHelpText(self):
        """Get the status line help text for this widget."""

    def getItemAt(self, x: int, y: int):
        """Return index of item at x,y, or -1 if none.

        Parameters
        ----------
        x : int

        y : int
        """

    def getItemBigIcon(self, index: int):
        """Return big icon of item at index.

        Parameters
        ----------
        index : int
        """

    def getItemData(self, index: int):
        """Return item user-data pointer.

        Parameters
        ----------
        index : int
        """

    def getItemHeight(self):
        """Return item height."""

    def getItemMiniIcon(self, index: int):
        """Return mini icon of item at index.

        Parameters
        ----------
        index : int
        """

    def getItemSpace(self):
        """Return maximum item space."""

    def getItemText(self, index: int):
        """Return item text.

        Parameters
        ----------
        index : int
        """

    def getItemWidth(self):
        """Return item width."""

    def getListStyle(self):
        """Get the current icon list style."""

    def getNumCols(self):
        """Return number of columns."""

    def getNumItems(self):
        """Return number of items."""

    def getNumRows(self):
        """Return number of rows."""

    def getSelBackColor(self):
        """Return selected text background."""

    def getSelTextColor(self):
        """Return selected text color."""

    def getSortFunc(self):
        """Return sort function."""

    def getTextColor(self):
        """Return normal text color."""

    def getViewportHeight(self):
        """Return viewport size.

        Reimplemented from FXScrollArea.
        """

    def hitItem(self, index: int, x: int, y: int, ww: int = 1, hh: int = 1):
        """Return item hit code: 0 outside, 1 icon, 2 text.

        Parameters
        ----------
        index : int

        x : int

        y : int

        ww : int

        hh : int

        """

    def insertItem(self, index: int, item: FXIconItem, notify: bool = False):
        """Insert a new [possibly subclassed] item at the give index.

        Parameters
        ----------
        index : int

        item : FXIconItem

        notify : bool
        """

    def isItemCurrent(self, index: int):
        """Return True if item at index is current.

        Parameters
        ----------
        index : int
        """

    def isItemEnabled(self, index: int):
        """Return True if item at index is enabled.

        Parameters
        ----------
        index : int
        """

    def isItemSelected(self, index: int):
        """Return True if item at index is selected.

        Parameters
        ----------
        index : int
        """

    def isItemVisible(self, index: int):
        """Return True if item at index is visible.

        Parameters
        ----------
        index : int
        """

    def killFocus(self):
        """Remove the focus from this window.

        Reimplemented from FXWindow.
        """

    def killSelection(self, notify: bool = False):
        """Deselect all items.

        Parameters
        ----------
        notify : bool
        """

    def makeItemVisible(self, index: int):
        """Scroll to make item at index visible.

        Parameters
        ----------
        index : int
        """

    def moveContents(self, x: int, y: int):
        """Move contents to the specified position. Reimplemented from FXScrollArea.

        Parameters
        ----------
        x : int

        y : int
        """

    def position(self, x: int, y: int, w: int, h: int):
        """Move and resize this window in the parent's coordinates. Reimplemented from FXWindow.

        Parameters
        ----------
        x : int

        y : int

        w : int

        h : int
        """

    def prependItem(self, item: FXIconItem, notify: bool = False):
        """Append a [possibly subclassed] item to the end of the list.

        Parameters
        ----------
        item : FXIconItem

        notify : bool
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

    def replaceItem(self, index: int, item: FXIconItem, notify: bool = False):
        """Replace the item with a [possibly subclassed] item.

        Parameters
        ----------
        index : int

        item : FXIconItem

        notify : bool
        """

    def resize(self, w: int, h: int):
        """Resize this window to the specified width and height. Reimplemented from FXWindow.

        Parameters
        ----------
        w : int

        h : int
        """

    def retrieveItem(self, index: int):
        """Return the item at the given index.

        Parameters
        ----------
        index : int
        """

    def selectInRectangle(self, x: int, y: int, w: int, h: int, notify: bool = False):
        """Select items in rectangle.

        Parameters
        ----------
        x : int

        y : int

        w : int

        h : int

        notify : bool
        """

    def selectItem(self, index: int, notify: bool = False):
        """Select item at index.

        Parameters
        ----------
        index : int

        notify : bool
        """

    def setAnchorItem(self, index: int):
        """Change anchor item index.

        Parameters
        ----------
        index : int
        """

    def setCurrentItem(self, index: int, notify: bool = False):
        """Change current item index.

        Parameters
        ----------
        index : int

        notify : bool
        """

    def setFocus(self):
        """Move the focus to this window.

        Reimplemented from FXWindow.
        """

    def setFont(self, fnt: FXFont):
        """Change text font.

        Parameters
        ----------
        fnt : FXFont
        """

    def setHelpText(self, text: str):
        """Set the status line help text for this widget.

        Parameters
        ----------
        text : str
        """

    def setItemBigIcon(self, index: int, icon: FXIcon):
        """Change item big icon.

        Parameters
        ----------
        index : int

        icon : FXIcon
        """

    def setItemData(self, index: int, ptr: str):
        """Change item user-data pointer.

        Parameters
        ----------
        index : int

        ptr : str
        """

    def setItemMiniIcon(self, index: int, icon: FXIcon):
        """Change item mini icon.

        Parameters
        ----------
        index : int

        icon : FXIcon
        """

    def setItemSpace(self, s: int):
        """Change maximum item space for each item.

        Parameters
        ----------
        s : int
        """

    def setItemText(self, index: int, text: str):
        """Change item text.

        Parameters
        ----------
        index : int

        text : str
        """

    def setListStyle(self, style: int):
        """Set the current icon list style.

        Parameters
        ----------
        style : int
        """

    def setSelBackColor(self, clr: FXColor):
        """Change selected text background.

        Parameters
        ----------
        clr : FXColor
        """

    def setSelTextColor(self, clr: FXColor):
        """Change selected text color.

        Parameters
        ----------
        clr : FXColor
        """

    def setSortFunc(self, func: FXIconListSortFunc):
        """Change sort function.

        Parameters
        ----------
        func : FXIconListSortFunc
        """

    def setTextColor(self, clr: FXColor):
        """Change normal text color.

        Parameters
        ----------
        clr : FXColor
        """

    def sortItems(self):
        """Sort items."""

    def toggleItem(self, index: int, notify: bool = False):
        """Toggle item at index.

        Parameters
        ----------
        index : int

        notify : bool
        """

    def updateItem(self, index: int):
        """Repaint item at index.

        Parameters
        ----------
        index : int
        """
