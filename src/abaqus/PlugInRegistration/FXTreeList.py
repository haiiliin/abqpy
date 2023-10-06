from __future__ import annotations

from .FXColor import FXColor
from .FXComposite import FXComposite
from .FXFont import FXFont
from .FXIcon import FXIcon
from .FXObject import FXObject
from .FXScrollArea import FXScrollArea
from .FXTreeItem import FXTreeItem

#: Extended selection mode allows for drag-selection of ranges of items.
TREELIST_EXTENDEDSELECT: int = hash("TREELIST_EXTENDEDSELECT")

#: Single selection mode allows up to one item to be selected.
TREELIST_SINGLESELECT: int = hash("TREELIST_SINGLESELECT")

#: Browse selection mode enforces one single item to be selected at all times.
TREELIST_BROWSESELECT: int = hash("TREELIST_BROWSESELECT")

#: Multiple selection mode is used for selection of individual items.
TREELIST_MULTIPLESELECT: int = hash("TREELIST_MULTIPLESELECT")

#: Automatically select under cursor.
TREELIST_AUTOSELECT: int = hash("TREELIST_AUTOSELECT")

#: Lines shown.
TREELIST_SHOWS_LINES: int = hash("TREELIST_SHOWS_LINES")

#: Boxes to expand shown.
TREELIST_SHOWS_BOXES: int = hash("TREELIST_SHOWS_BOXES")

#: Display root boxes also.
TREELIST_ROOT_BOXES: int = hash("TREELIST_ROOT_BOXES")

#: Display check boxes.
TREELIST_CHECK_BOXES: int = hash("TREELIST_CHECK_BOXES")

#: Propagate checked state to children and parents.
TREELIST_PROPAGATE_CHECKS: int = hash("TREELIST_PROPAGATE_CHECKS")

#: Normal tree list style.
TREELIST_NORMAL: int = hash("TREELIST_NORMAL")


class FXTreeList(FXScrollArea):
    """Tree list Widget."""

    def __init__(
        self,
        p: FXComposite,
        nvis: int,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = TREELIST_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
    ):
        """Construct a tree list with nvis visible items; the tree list is initially empty.

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

    def addItemAfter(self, other: FXTreeItem, item: FXTreeItem, notify: bool = False):
        """Append new [possibly subclassed] item after to other item.

        Parameters
        ----------
        other : FXTreeItem

        item : FXTreeItem

        notify : bool
        """

    def addItemBefore(self, other: FXTreeItem, item: FXTreeItem, notify: bool = False):
        """Prepend new [possibly subclassed] item prior to other item.

        Parameters
        ----------
        other : FXTreeItem

        item : FXTreeItem

        notify : bool
        """

    def addItemFirst(self, p: FXTreeItem, item: FXTreeItem, notify: bool = False):
        """Prepend new [possibly subclassed] item as first child of p.

        Parameters
        ----------
        p : FXTreeItem

        item : FXTreeItem

        notify : bool
        """

    def addItemLast(self, p: FXTreeItem, item: FXTreeItem, notify: bool = False):
        """Append new [possibly subclassed] item as last child of p.

        Parameters
        ----------
        p : FXTreeItem

        item : FXTreeItem

        notify : bool
        """

    def canFocus(self):
        """Tree list can receive focus.

        Reimplemented from FXWindow.
        """

    def clearItems(self, notify: bool = False):
        """Remove all items from list.

        Parameters
        ----------
        notify : bool
        """

    def closeItem(self, item: FXTreeItem, notify: bool = False):
        """Close item.

        Parameters
        ----------
        item : FXTreeItem

        notify : bool
        """

    def collapseTree(self, tree: FXTreeItem, notify: bool = False):
        """Collapse tree.

        Parameters
        ----------
        tree : FXTreeItem

        notify : bool
        """

    def create(self):
        """Create server-side resources.

        Reimplemented from FXComposite. Reimplemented in FXDirList.
        """

    def deselectItem(self, item: FXTreeItem, notify: bool = False):
        """Deselect item.

        Parameters
        ----------
        item : FXTreeItem

        notify : bool
        """

    def destroy(self):
        """Destroy server-side resources.

        Reimplemented from FXComposite. Reimplemented in FXDirList.
        """

    def detach(self):
        """Detach server-side resources.

        Reimplemented from FXComposite. Reimplemented in FXDirList.
        """

    def disableItem(self, item: FXTreeItem):
        """Disable item.

        Parameters
        ----------
        item : FXTreeItem
        """

    def enableItem(self, item: FXTreeItem):
        """Enable item.

        Parameters
        ----------
        item : FXTreeItem
        """

    def expandTree(self, tree: FXTreeItem, notify: bool = False):
        """Expand tree.

        Parameters
        ----------
        tree : FXTreeItem

        notify : bool
        """

    def extendSelection(self, item: FXTreeItem, notify: bool = False):
        """Extend selection from anchor item to item.

        Parameters
        ----------
        item : FXTreeItem

        notify : bool
        """

    def findItem(self, text: str, start: FXTreeItem | None = None):
        """Search items for item by name, starting from start item; the flags argument controls the search
        direction, and case sensitivity.

        Parameters
        ----------
        text : str

        start : FXTreeItem | None
        """

    def getAnchorItem(self):
        """Return anchor item, if any."""

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

    def getCursorItem(self):
        """Return item under cursor, if any."""

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXScrollArea.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXScrollArea.
        """

    def getFirstItem(self):
        """REturn first root item."""

    def getFont(self):
        """Return text font."""

    def getHelpText(self):
        """Get the status line help text for this list."""

    def getIndent(self):
        """Return parent-child indent amount."""

    def getItemAt(self, x: int, y: int):
        """Get item at x,y, if any.

        Parameters
        ----------
        x : int

        y : int
        """

    def getItemCheck(self, item: FXTreeItem):
        """Returns the item checked state.

        Parameters
        ----------
        item : FXTreeItem
        """

    def getItemClosedIcon(self, item: FXTreeItem):
        """Return item's closed icon.

        Parameters
        ----------
        item : FXTreeItem
        """

    def getItemData(self, item: FXTreeItem):
        """Return item user-data pointer.

        Parameters
        ----------
        item : FXTreeItem
        """

    def getItemHeight(self, item: FXTreeItem):
        """Return item height.

        Parameters
        ----------
        item : FXTreeItem
        """

    def getItemOpenIcon(self, item: FXTreeItem):
        """Return item's open icon.

        Parameters
        ----------
        item : FXTreeItem
        """

    def getItemText(self, item: FXTreeItem):
        """Return item's text.

        Parameters
        ----------
        item : FXTreeItem
        """

    def getItemWidth(self, item: FXTreeItem):
        """Return item width.

        Parameters
        ----------
        item : FXTreeItem
        """

    def getLastItem(self):
        """Return last root item."""

    def getLineColor(self):
        """Return line color."""

    def getListStyle(self):
        """Return list style."""

    def getNumItems(self):
        """Return number of items."""

    def getNumVisible(self):
        """Return number of visible items."""

    def getSelBackColor(self):
        """Return selected text background."""

    def getSelTextColor(self):
        """Return selected text color."""

    def getTextColor(self):
        """Return normal text color."""

    def hitItem(self, item: FXTreeItem, x: int, y: int):
        """Return item hit code: 0 outside, 1 icon, 2 text, 3 box.

        Parameters
        ----------
        item : FXTreeItem

        x : int

        y : int

        """

    def isItemCurrent(self, item: FXTreeItem):
        """Return True if item is current.

        Parameters
        ----------
        item : FXTreeItem
        """

    def isItemEnabled(self, item: FXTreeItem):
        """Return True if item is enabled.

        Parameters
        ----------
        item : FXTreeItem
        """

    def isItemExpanded(self, item: FXTreeItem):
        """Return True if item expanded.

        Parameters
        ----------
        item : FXTreeItem
        """

    def isItemLeaf(self, item: FXTreeItem):
        """Return True if item is a leaf-item, i.e. has no children.

        Parameters
        ----------
        item : FXTreeItem
        """

    def isItemOpened(self, item: FXTreeItem):
        """Return True if item opened.

        Parameters
        ----------
        item : FXTreeItem
        """

    def isItemSelected(self, item: FXTreeItem):
        """Return True if item is selected.

        Parameters
        ----------
        item : FXTreeItem
        """

    def isItemVisible(self, item: FXTreeItem):
        """Return True if item is visible.

        Parameters
        ----------
        item : FXTreeItem
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

    def makeItemVisible(self, item: FXTreeItem):
        """Scroll to make item visible.

        Parameters
        ----------
        item : FXTreeItem
        """

    def moveItemAfter(self, other: FXTreeItem, item: FXTreeItem):
        """Move item after other.

        Parameters
        ----------
        other : FXTreeItem

        item : FXTreeItem
        """

    def moveItemBefore(self, other: FXTreeItem, item: FXTreeItem):
        """Move item before other.

        Parameters
        ----------
        other : FXTreeItem

        item : FXTreeItem
        """

    def openItem(self, item: FXTreeItem, notify: bool = False):
        """Open item.

        Parameters
        ----------
        item : FXTreeItem

        notify : bool
        """

    def recalc(self):
        """Recalculate layout.

        Reimplemented from FXWindow.
        """

    def removeItem(self, item: FXTreeItem, notify: bool = False):
        """Remove item.

        Parameters
        ----------
        item : FXTreeItem

        notify : bool
        """

    def removeItems(self, fm: FXTreeItem, to: FXTreeItem, notify: bool = False):
        """Remove items in range [fm, to] inclusively.

        Parameters
        ----------
        fm : FXTreeItem

        to : FXTreeItem

        notify : bool
        """

    def reparentItem(self, item: FXTreeItem, p: FXTreeItem):
        """Reparent item under parent p.

        Parameters
        ----------
        item : FXTreeItem

        p : FXTreeItem
        """

    def selectItem(self, item: FXTreeItem, notify: bool = False):
        """Select item.

        Parameters
        ----------
        item : FXTreeItem

        notify : bool
        """

    def setAnchorItem(self, item: FXTreeItem):
        """Change anchor item.

        Parameters
        ----------
        item : FXTreeItem
        """

    def setCurrentItem(self, item: FXTreeItem, notify: bool = False):
        """Change current item.

        Parameters
        ----------
        item : FXTreeItem

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
        """Set the status line help text for this list.

        Parameters
        ----------
        text : str
        """

    def setIndent(self, in_: int):
        """Change parent-child indent amount.

        Parameters
        ----------
        in_ : int
        """

    def setItemCheck(self, item: FXTreeItem, check: int, notify: bool = False):
        """Sets the item checked state. Valid states are True, False and MAYBE. Returns True if the check value
        has changed, False otherwise.

        Parameters
        ----------
        item : FXTreeItem

        check : int

        notify : bool
        """

    def setItemClosedIcon(self, item: FXTreeItem, icon: FXIcon):
        """Chance item's closed icon.

        Parameters
        ----------
        item : FXTreeItem

        icon : FXIcon
        """

    def setItemData(self, item: FXTreeItem, ptr: str):
        """Change item user-data pointer.

        Parameters
        ----------
        item : FXTreeItem

        ptr : str
        """

    def setItemOpenIcon(self, item: FXTreeItem, icon: FXIcon):
        """Change item's open icon.

        Parameters
        ----------
        item : FXTreeItem

        icon : FXIcon
        """

    def setItemText(self, item: FXTreeItem, text: str):
        """Change item's text.

        Parameters
        ----------
        item : FXTreeItem

        text : str
        """

    def setLineColor(self, clr: FXColor):
        """Change line color.

        Parameters
        ----------
        clr : FXColor
        """

    def setListStyle(self, style: int):
        """Change list style.

        Parameters
        ----------
        style : int
        """

    def setNumVisible(self, nvis: int):
        """Change number of visible items.

        Parameters
        ----------
        nvis : int
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

    def setTextColor(self, clr: FXColor):
        """Change normal text color.

        Parameters
        ----------
        clr : FXColor
        """

    def toggleItem(self, item: FXTreeItem, notify: bool = False):
        """Toggle item selection.

        Parameters
        ----------
        item : FXTreeItem

        notify : bool
        """

    def updateItem(self, item: FXTreeItem):
        """Repaint item.

        Parameters
        ----------
        item : FXTreeItem
        """
