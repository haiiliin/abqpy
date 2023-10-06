from __future__ import annotations

from .AFXDataComponent import AFXDataComponent
from .FXComposite import FXComposite
from .FXIcon import FXIcon
from .FXObject import FXObject
from .FXScrollArea import FXScrollArea
from .FXTreeItem import FXTreeItem

#: Allow users to resize columns.
AFXTREETABLE_COLUMN_RESIZABLE: int = hash("AFXTREETABLE_COLUMN_RESIZABLE")

#: Disallow column selections (selecting a header/footer item in a column selects the whole column).
AFXTREETABLE_NO_COLUMN_SELECT: int = hash("AFXTREETABLE_NO_COLUMN_SELECT")

#: Selecting any item in a row selects the whole row.
AFXTREETABLE_ROW_MODE: int = hash("AFXTREETABLE_ROW_MODE")

#: Use extended selection mode that allows multiple items to be selected and allows users to drag-select a range of items.
AFXTREETABLE_EXTENDED_SELECT: int = hash("AFXTREETABLE_EXTENDED_SELECT")

#: Use single selection mode that allows up to one item to be selected.
AFXTREETABLE_SINGLE_SELECT: int = hash("AFXTREETABLE_SINGLE_SELECT")

#: Use browse selection mode that enforces one single item to be selected at all times.
AFXTREETABLE_BROWSE_SELECT: int = hash("AFXTREETABLE_BROWSE_SELECT")

#: Show item check boxes.
AFXTREETABLE_CHECK_BOXES: int = hash("AFXTREETABLE_CHECK_BOXES")

#: Propagate checked state to children and parents.
AFXTREETABLE_PROPAGATE_CHECKS: int = hash("AFXTREETABLE_PROPAGATE_CHECKS")

#: Default table options--use extended selection mode, columns are resizable, and layout fills both X and Y directions.
AFXTREETABLE_NORMAL: int = hash("AFXTREETABLE_NORMAL")

#: Do not pre-select any list item.
AFXTREETABLE_LIST_PRESELECT_NONE: int = hash("AFXTREETABLE_LIST_PRESELECT_NONE")

#: Normal list.
AFXTREETABLE_LIST_NORMAL: int = hash("AFXTREETABLE_LIST_NORMAL")


class AFXTreeTable(FXScrollArea, AFXDataComponent):
    """This class combines a tree widget with a table widget to allow associating a row of data with an item in
    a tree."""

    #: Color item has no As Is and Default in its flyout.
    COLOR_INCLUDE_COLOR_ONLY: int = hash("COLOR_INCLUDE_COLOR_ONLY")

    #: Color item has As Is in its flyout.
    COLOR_INCLUDE_AS_IS: int = hash("COLOR_INCLUDE_AS_IS")

    #: Color item has Default in its flyout.
    COLOR_INCLUDE_DEFAULT: int = hash("COLOR_INCLUDE_DEFAULT")

    #: Color item has both As Is and Default in its flyout. This is the default option.
    COLOR_INCLUDE_ALL: int = hash("COLOR_INCLUDE_ALL")

    #: Not yet implemented (Real).
    REAL: int = hash("REAL")

    #: Left justified.
    LEFT: int = hash("LEFT")

    #: Right justified.
    RIGHT: int = hash("RIGHT")

    #: Center justified (horizontal).
    CENTER: int = hash("CENTER")

    #: Top justified.
    TOP: int = hash("TOP")

    #: Bottom justified.
    BOTTOM: int = hash("BOTTOM")

    #: Middle justified (vertical).
    MIDDLE: int = hash("MIDDLE")

    #: Item accepts a text string via a text field.
    TEXT: int = hash("TEXT")

    #: Item accepts a floating-point number via a text field.
    FLOAT: int = hash("FLOAT")

    #: Item accepts an integer via a text field.
    INT: int = hash("INT")

    #: Item accepts input from a list.
    LIST: int = hash("LIST")

    #: Item is a boolean; displayed as an icon.
    BOOL: int = hash("BOOL")

    #: Item displays an icon and does not accept input.
    ICON: int = hash("ICON")

    #: Item accepts color selection via a color flyout.
    COLOR: int = hash("COLOR")

    #: General.
    GENERAL: int = hash("GENERAL")

    #: Scientific.
    SCIENTIFIC: int = hash("SCIENTIFIC")

    #: Automatic.
    AUTOMATIC: int = hash("AUTOMATIC")

    def __init__(
        self,
        p: FXComposite,
        numVisItems: int,
        numVisColumns: int,
        numColumns: int,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = AFXTREETABLE_NORMAL,
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
        numVisItems : int
            Number of items to display.
        numVisColumns : int
            Number of columns in the table to display.
        numColumns : int
            Number of columns in the table.
        tgt : FXObject | None
            Message target.
        sel : int
            Message ID.
        opts : int
            Options and hints.
        x : int
            X coordinate of the origin.
        y : int
            Y coordinate of the origin.
        w : int
            Width of the table widget.
        h : int
            Height of the table widget.
        """

    def addItemAfter(self, other: FXTreeItem, item: FXTreeItem, notify: bool = False):
        """Appends the new tree item after the other tree item.

        Parameters
        ----------
        other : FXTreeItem

        item : FXTreeItem

        notify : bool
        """

    def addItemBefore(self, other: FXTreeItem, item: FXTreeItem, notify: bool = False):
        """Prepends the new item prior to the other tree item.

        Parameters
        ----------
        other : FXTreeItem

        item : FXTreeItem

        notify : bool
        """

    def addItemFirst(self, p: FXTreeItem, item: FXTreeItem, notify: bool = False):
        """Prepends the new tree item as first child of parent.

        Parameters
        ----------
        p : FXTreeItem

        item : FXTreeItem

        notify : bool
        """

    def addItemLast(self, p: FXTreeItem, item: FXTreeItem, notify: bool = False):
        """Appends the new tree item as the last child of the parent.

        Parameters
        ----------
        p : FXTreeItem

        item : FXTreeItem

        notify : bool
        """

    def addList(self, opts: int = AFXTREETABLE_LIST_NORMAL):
        """Adds a list to the table and returns the list ID. The list is used by items of type LIST.

        Parameters
        ----------
        opts : int
            List flag.
        """

    def appendListItem(self, listId: int, text: str, icon: FXIcon | None = None):
        """Appends an item to the specified table list; returns the index of the new item.

        Parameters
        ----------
        listId : int
            ID of the list to append to.
        text : str
            Item's text.
        icon : FXIcon | None
            Item's icon.
        """

    def beginEdit(self, item: FXTreeItem, column: int):
        """Sets the specified item in edit mode if the item is editable.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of item.
        """

    def cancelEdit(self):
        """Cancels the edit mode."""

    def clearContents(
        self,
        startItem: FXTreeItem,
        startColumn: int,
        endItem: FXTreeItem,
        endColumn: int,
        clearEditableOnly: bool = True,
    ):
        """Clears the text in the items in the specified range.

        Parameters
        ----------
        startItem : FXTreeItem
            Tree item in which to start clearing.
        startColumn : int
            Column in which to start clearing.
        endItem : FXTreeItem
            Tree item in which to end clearing.
        endColumn : int
            Column in which to end clearing.
        clearEditableOnly : bool
            Specify True to clear the text of editable items only.
        """

    def clearItems(self, notify: bool = False):
        """Removes all tree items and table rows.

        Parameters
        ----------
        notify : bool
        """

    def clearListItems(self, listId: int):
        """Removes all items from the specified table list.

        Parameters
        ----------
        listId : int
            ID of the list to clear.
        """

    def closeItem(self, item: FXTreeItem, notify: bool = False):
        """Closes the specified item.

        Parameters
        ----------
        item : FXTreeItem

        notify : bool
        """

    def collapseTree(self, item: FXTreeItem, notify: bool = False):
        """Collapses the specified item to hide its children.

        Parameters
        ----------
        item : FXTreeItem

        notify : bool
        """

    def deleteColumns(self, startColumn: int, numColumns: int = 1, notify: bool = False):
        """Deletes columns starting at the specified column.

        Parameters
        ----------
        startColumn : int
            Starting column.
        numColumns : int
            Number of columns to delete.
        notify : bool
            Specify True to notify target of the deletion.
        """

    def deselectItem(self, item: FXTreeItem, column: int, notify: bool = False):
        """Deselects the specified item.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of item.
        notify : bool
        """

    def deselectRow(self, item: FXTreeItem, notify: bool = False):
        """Deselects all items in the row.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        notify : bool
        """

    def expandTree(self, item: FXTreeItem, notify: bool = False):
        """Expands the specified item to show its children.

        Parameters
        ----------
        item : FXTreeItem

        notify : bool
        """

    def getColumnWidth(self, column: int):
        """Returns the width, in pixels, of the specified column.

        Parameters
        ----------
        column : int
            Column index.
        """

    def getCurrentColumn(self):
        """Returns the column index of the current item."""

    def getCurrentItem(self):
        """Returns the current item, if any."""

    def getDefaultColumnWidth(self):
        """Returns the default column width, in pixels, of the table."""

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXScrollArea.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXScrollArea.
        """

    def getFirstItem(self):
        """Returns the first root tree item."""

    def getItemBoolValue(self, item: FXTreeItem, column: int):
        """Returns the value of a table item of type BOOL.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def getItemCheck(self, item: FXTreeItem):
        """Returns the item checked state.

        Parameters
        ----------
        item : FXTreeItem
        """

    def getItemClosedIcon(self, item: FXTreeItem):
        """Returns the tree item's closed icon.

        Parameters
        ----------
        item : FXTreeItem
        """

    def getItemColor(self, item: FXTreeItem, column: int):
        """Returns the color of a table item of type COLOR. The color is "As is", "Default", or a color hex
        specification in the form of "RRGGBB" (e.g., "#0A1B2C").

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def getItemFloatValue(self, item: FXTreeItem, column: int):
        """Returns the value of a table item of type FLOAT.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def getItemFormat(self, item: FXTreeItem, column: int):
        """Returns the format of a table item of type REAL (see RealFormat).

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def getItemIcon(self, item: FXTreeItem, column: int):
        """Returns the icon of a table item of type ICON.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def getItemIntValue(self, item: FXTreeItem, column: int):
        """Returns the value of a table item of type INT.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def getItemListId(self, item: FXTreeItem, column: int):
        """Returns the list ID of a table item of type LIST.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def getItemListIndex(self, item: FXTreeItem, column: int):
        """Returns the list index (selection) of a table item of type LIST.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def getItemNumDigits(self, item: FXTreeItem, column: int):
        """Returns the number of digits to the left of the decimal point for a table item of type REAL.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def getItemOpenIcon(self, item: FXTreeItem):
        """Returns the tree item's open icon.

        Parameters
        ----------
        item : FXTreeItem
        """

    def getItemPrecision(self, item: FXTreeItem, column: int):
        """Returns the precision for a table item of type REAL.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def getItemText(self, item: FXTreeItem, column: int):
        """Returns the text of an item of type TEXT.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of item.
        """

    def getItemType(self, item: FXTreeItem, column: int):
        """Returns the type of a table item.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def getItemValue(self, item: FXTreeItem, column: int):
        """Returns the text-form value of a table item of any type.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def getLastItem(self):
        """Returns the last root tree item."""

    def getListItemIcon(self, listId: int, index: int):
        """Returns the icon of the item at the specified index of the specified table list.

        Parameters
        ----------
        listId : int
            ID of the list.
        index : int
            Index into the list of the item to return.
        """

    def getListItemIndex(self, listId: int, text: str):
        """Returns the index of the item of the specified table list that has the specified text. Returns -1 if
        no such item exists.

        Parameters
        ----------
        listId : int
            ID of the list.
        text : str
            Text.
        """

    def getListItemText(self, listId: int, index: int):
        """Returns the text of the item at the specified index of the specified table list.

        Parameters
        ----------
        listId : int
            ID of the list.
        index : int
            Index into the list of the item to return.
        """

    def getNumColumns(self):
        """Returns the number of columns."""

    def getNumItems(self):
        """Returns the number of items."""

    def getNumListItems(self, listId: int):
        """Returns the number of items in the specified table list.

        Parameters
        ----------
        listId : int
            ID of the list.
        """

    def getTableStyle(self):
        """Returns the options related only to the table."""

    def getTreeColumn(self):
        """Returns the column index of the tree."""

    def getVisibleColumns(self):
        """Returns the number of visible columns."""

    def getVisibleItems(self):
        """Returns the number of visible items."""

    def insertColumns(self, startColumn: int, numColumns: int = 1, notify: bool = False):
        """Inserts columns at the specified location.

        Parameters
        ----------
        startColumn : int
            Starting column.
        numColumns : int
            Number of columns to insert.
        notify : bool
            Specify True to notify target of the insertion.
        """

    def isAnyItemInColumnSelected(self, column: int):
        """Returns True if any item in the column is selected.

        Parameters
        ----------
        column : int
            Column index.
        """

    def isAnyItemInRowSelected(self, item: FXTreeItem):
        """Returns True if any item in the row is selected.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        """

    def isColumnSelected(self, column: int):
        """Returns True if all items in the column are selected.

        Parameters
        ----------
        column : int
            Column index.
        """

    def isItemBool(self, item: FXTreeItem, column: int):
        """Returns True if the specified table item is of type BOOL.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def isItemColor(self, item: FXTreeItem, column: int):
        """Returns True if the specified table item is of type COLOR.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def isItemEditable(self, item: FXTreeItem, column: int):
        """Returns True if the table item is editable.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def isItemEmpty(self, item: FXTreeItem, column: int):
        """Returns True if the specified table item does not have a value.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def isItemExpanded(self, item: FXTreeItem):
        """Returns True if the tree item is expanded, False otherwise.

        Parameters
        ----------
        item : FXTreeItem
        """

    def isItemFloat(self, item: FXTreeItem, column: int):
        """Returns True if the specified table item is of type FLOAT.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def isItemIcon(self, item: FXTreeItem, column: int):
        """Returns True if the specified table item is of type ICON.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def isItemInt(self, item: FXTreeItem, column: int):
        """Returns True if the specified table item is of type INT.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def isItemLeaf(self, item: FXTreeItem):
        """Returns True if the tree item is a leaf-item (has no children), False otherwise.

        Parameters
        ----------
        item : FXTreeItem
        """

    def isItemList(self, item: FXTreeItem, column: int):
        """Returns True if the specified tabl eitem is of type LIST.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def isItemOpened(self, item: FXTreeItem):
        """Returns True if the tree item is opened, False otherwise.

        Parameters
        ----------
        item : FXTreeItem
        """

    def isItemSelected(self, item: FXTreeItem, column: int):
        """Returns True if the specified item is selected.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of item.
        """

    def isItemText(self, item: FXTreeItem, column: int):
        """Returns True if the specified table item is of type TEXT.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        """

    def isItemVisible(self, item: FXTreeItem, column: int):
        """Returns True if the specified item is visible.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of item.
        """

    def isRowSelected(self, item: FXTreeItem):
        """Returns True if all items in the row are selected.

        Parameters
        ----------
        item : FXTreeItem
        """

    def killSelection(self, notify: bool = False):
        """Deselects all items.

        Parameters
        ----------
        notify : bool
        """

    def makePositionVisible(self, item: FXTreeItem, column: int):
        """Scrolls to make the specified row, column fully visible.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of item.
        """

    def makeRowVisible(self, item: FXTreeItem):
        """Scrolls vertically (only) to make the specified row fully visible.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        """

    def openItem(self, item: FXTreeItem, notify: bool = False):
        """Opens the specified item.

        Parameters
        ----------
        item : FXTreeItem

        notify : bool
        """

    def removeItem(self, item: FXTreeItem, notify: bool = False):
        """Removes the specified tree item and corresponding table row.

        Parameters
        ----------
        item : FXTreeItem

        notify : bool
        """

    def removeItems(self, from_: FXTreeItem, to: FXTreeItem, notify: bool = False):
        """Removes the specified tree items and their corresponding table rows, inclusively.

        Parameters
        ----------
        from_ : FXTreeItem

        to : FXTreeItem

        notify : bool
        """

    def removeListItem(self, listId: int, index: int):
        """Removes the item at the specified index from the specified table list; returns the number of items
        remaining in list.

        Parameters
        ----------
        listId : int
            ID of the list to remove from.
        index : int
            Index of the list item to remove.
        """

    def selectItem(self, item: FXTreeItem, column: int, notify: bool = False):
        """Selects the specified item.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of item.
        notify : bool
        """

    def selectRow(self, item: FXTreeItem, notify: bool = False):
        """Selects all items in the row.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        notify : bool
        """

    def setColumnBoolIcons(self, column: int, trueIcon: FXIcon | None = None, falseIcon: FXIcon | None = None):
        """Sets the True and False icons of all existing and future table items in a column of type BOOL.
        Specifying -1 for the column will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Table column index.
        trueIcon : FXIcon | None
            Icon displayed when value is True; 0 = default icon.
        falseIcon : FXIcon | None
            Icon displayed when value is False; 0 = default icon.
        """

    def setColumnBoolValue(self, column: int, value: bool):
        """Sets the value of all existing and future table items in a column of type BOOL. Specifying -1 for the
        column will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Table column index.
        value : bool
            Specify True or False.
        """

    def setColumnColor(self, column: int, color: str):
        """Sets the color of all existing and future table items in a column of type COLOR. The color can be "As
        is", "Default", a color hex specification in the form of "RRGGBB" (e.g., "#0A1B2C"), or a pre-defined
        color name (e.g., "Red"). Specifying -1 for the column will change all columns in the table and set the
        default for the table.

        Parameters
        ----------
        column : int
            Table column index.
        color : str
            Color.
        """

    def setColumnColorItemDefault(self, column: int, color: str):
        """Sets the color of the color item in the flyout menu for all existing and future table items that
        display "As is" or "Default" in a column of type COLOR. The color is either a color hex specification in
        the form of "RRGGBB" (e.g., "#0A1B2C") or a pre-defined color name (e.g., "Red"). Specifying -1 for the
        column will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Table column index.
        color : str
            Color.
        """

    def setColumnColorOptions(self, column: int, opts: int):
        """Sets the color flyout options for all existing and future table items in a column of type COLOR.
        Specifying -1 for the column will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Table column index.
        opts : int
            Options (see ColorFlyoutOptions).
        """

    def setColumnEditable(self, column: int, editable: bool):
        """Sets the editability of all existing and future table items in a column. Specifying -1 for the column
        will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Table column index.
        editable : bool
            Specify True for editable, False for read-only.
        """

    def setColumnFloatValue(self, column: int, value: float):
        """Sets the value of all existing and future table items in a column of type FLOAT. Specifying -1 for
        the column will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Table column index.
        value : float
            Floating-point value.
        """

    def setColumnFormat(self, column: int, format: int):
        """Sets the real format for all existing and future table items in a column of type REAL.

        Parameters
        ----------
        column : int
            Table column index.
        format : int
            Default format of REAL values in column (see RealFormat).
        """

    def setColumnIcon(self, column: int, icon: FXIcon | None = None):
        """Sets the icon of all existing and future table items in a column of type ICON. Specifying -1 for the
        column will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Table column index.
        icon : FXIcon | None
            Icon.
        """

    def setColumnIntValue(self, column: int, value: int):
        """Sets the value of all existing and future table items in a column of type INT. Specifying -1 for the
        column will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Table column index.
        value : int
            Integer value.
        """

    def setColumnJustify(self, column: int, justify: int):
        """Sets the justification of all existing and future table items in a column. Specifying -1 for the
        column will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Table column index.
        justify : int
            Justification (see ItemJustify).
        """

    def setColumnListId(self, column: int, listId: int):
        """Sets the list ID of all existing and future table items in a column of type LIST. Specifying -1 for
        the column will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Table column index.
        listId : int
            List ID.
        """

    def setColumnListIndex(self, column: int, index: int):
        """Sets the list index (selection) of all existing and future table items in a column of type LIST.
        Specifying -1 for the column will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Table column index.
        index : int
            Index of item to be selected.
        """

    def setColumnNumDigits(self, column: int, numDigits: int):
        """Sets the number of digits to the left of the decimal point for all existing and future table items in
        a column of type REAL.

        Parameters
        ----------
        column : int
            Table column index.
        numDigits : int
            Default number of digits the left of the decimal point.
        """

    def setColumnPrecision(self, column: int, precision: int):
        """Sets the precision for all existing and future table items in a column of type REAL.

        Parameters
        ----------
        column : int
            Table column index.
        precision : int
            Number of digits to the right of the decimal point.
        """

    def setColumnText(self, column: int, text: str):
        """Sets the text of all existing and future table items in a column of type TEXT. Specifying -1 for the
        column will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Table column index.
        text : str
            Text.
        """

    def setColumnType(self, column: int, type: int):
        """Sets the type of a column. Specifying -1 for the table column will change all columns in the table
        and set the default for the table.

        Parameters
        ----------
        column : int
            Table column index.
        type : int
            Type (see Flags for item types).
        """

    def setColumnWidth(self, column: int, width: int):
        """Sets the width, in pixels, of the specified column. Specifying -1 for the column will change all non-
        leading and non-trailing columns in the table and set the default for the table. Specify -1 for the
        width will resize each specified column to best fit the width of the title(s) currently shown in its
        leading and trailing items.

        Parameters
        ----------
        column : int
            Column index.
        width : int
            Width in pixels.
        """

    def setColumnWidthInChars(self, column: int, numChars: int):
        """Sets the width, in number of characters, of the specified column. Specifying -1 for the column will
        change all non-leading and non-trailing columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Column index.
        numChars : int
            Width in number of characters.
        """

    def setCurrentItem(self, item: FXTreeItem, column: int, notify: bool = False):
        """Sets the current item.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of item.
        notify : bool
        """

    def setDefaultBoolIcons(self, trueIcon: FXIcon | None = None, falseIcon: FXIcon | None = None):
        """Sets the default True and False icons for the table (0 = default icon).

        Parameters
        ----------
        trueIcon : FXIcon | None
            Icon displayed when value is True; 0 = default icon.
        falseIcon : FXIcon | None
            Icon displayed when value is False; 0 = default icon.
        """

    def setDefaultBoolValue(self, value: bool):
        """Sets the default bool value for the table.

        Parameters
        ----------
        value : bool
            Specify True or False.
        """

    def setDefaultColor(self, color: str):
        """Sets the default color for all items of type COLOR in the table. The color can be "As is", "Default",
        a color hex specification in the form of "RRGGBB" (e.g., "#0A1B2C"), or a pre-defined color name (e.g.,
        "Red").

        Parameters
        ----------
        color : str
            Color.
        """

    def setDefaultColumnWidth(self, width: int):
        """Sets the default width, in pixels, for all columns.

        Parameters
        ----------
        width : int
            Width in pixels.
        """

    def setDefaultFloatValue(self, value: float):
        """Sets the default floating-point value for the table.

        Parameters
        ----------
        value : float
            Floating-point value.
        """

    def setDefaultFormat(self, format: int):
        """Sets the default real format for the table.

        Parameters
        ----------
        format : int
            Format flag.
        """

    def setDefaultIntValue(self, value: int):
        """Sets the default integer value for the table.

        Parameters
        ----------
        value : int
            Integer value.
        """

    def setDefaultJustify(self, justify: int):
        """Sets the default justification for the table.

        Parameters
        ----------
        justify : int
            Justification (see ItemJustify).
        """

    def setDefaultNumDigits(self, numDigits: int):
        """Sets the default number of digits to the left of the decimal point for the table.

        Parameters
        ----------
        numDigits : int
            Number of digits.
        """

    def setDefaultPrecision(self, precision: int):
        """Sets the precision for the table.

        Parameters
        ----------
        precision : int
            Precision.
        """

    def setDefaultText(self, text: str):
        """Sets the default text for the table.

        Parameters
        ----------
        text : str
            Text.
        """

    def setDefaultType(self, type: int):
        """Sets the default type for the table.

        Parameters
        ----------
        type : int
            Type (see Flags for item types).
        """

    def setItemBoolIcons(
        self, item: FXTreeItem, column: int, trueIcon: FXIcon | None = None, falseIcon: FXIcon | None = None
    ):
        """Sets the True and False icons of a table item of type BOOL.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        trueIcon : FXIcon | None
            Icon displayed when value is True; 0 = default icon.
        falseIcon : FXIcon | None
            Icon displayed when value is False; 0 = default icon.
        """

    def setItemBoolValue(self, item: FXTreeItem, column: int, value: bool):
        """Sets the value of a table item of type BOOL.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        value : bool
            Specify True or False.
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
        """Changes the tree item's closed icon.

        Parameters
        ----------
        item : FXTreeItem

        icon : FXIcon
        """

    def setItemColor(self, item: FXTreeItem, column: int, color: str):
        """Sets the color of a table item of type COLOR. The color can be "As is", "Default", a color hex
        specification in the form of "RRGGBB" (e.g., "#0A1B2C"), or a pre-defined color name (e.g., "Red").

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        color : str
            Color.
        """

    def setItemEditable(self, item: FXTreeItem, column: int, editable: bool):
        """Sets the editability of a table item.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        editable : bool
            Specify True for editable, False for read-only.
        """

    def setItemFloatValue(self, item: FXTreeItem, column: int, value: float):
        """Sets the value of a table item of type FLOAT.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        value : float
            Floating-point value.
        """

    def setItemFormat(self, item: FXTreeItem, column: int, format: int):
        """Sets the format for a table item of type REAL (see RealFormat).

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Table column index of item.
        format : int
            Format of table item (see RealFormat).
        """

    def setItemIcon(self, item: FXTreeItem, column: int, icon: FXIcon | None = None):
        """Sets the icon of a table item of type ICON.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        icon : FXIcon | None
            Icon.
        """

    def setItemIntValue(self, item: FXTreeItem, column: int, value: int):
        """Sets the value of a table item of type INT.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        value : int
            Integer value.
        """

    def setItemJustify(self, item: FXTreeItem, column: int, justify: int):
        """Sets the justification of an item.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        justify : int
            Justification (see ItemJustify).
        """

    def setItemListId(self, item: FXTreeItem, column: int, listId: int):
        """Sets the list ID of a table item of type LIST.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        listId : int
            List ID.
        """

    def setItemListIndex(self, item: FXTreeItem, column: int, index: int):
        """Sets the list index (selection) of a table item of type LIST.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        index : int
            Index of item to be selected.
        """

    def setItemNumDigits(self, item: FXTreeItem, column: int, numDigits: int):
        """Sets the number of digits to the left of the decimal point for a table item of type REAL.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        numDigits : int
            Number of digits.
        """

    def setItemOpenIcon(self, item: FXTreeItem, icon: FXIcon):
        """Sets the tree item's open icon.

        Parameters
        ----------
        item : FXTreeItem

        icon : FXIcon
        """

    def setItemPrecision(self, item: FXTreeItem, column: int, precision: int):
        """Sets the precision for a table item of type REAL.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        precision : int
            Number of digits to the right of the decimal point.
        """

    def setItemText(self, item: FXTreeItem, column: int, text: str):
        """Sets the text of an item of type TEXT.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of item.
        text : str
            Text.
        """

    def setItemType(self, item: FXTreeItem, column: int, type: int):
        """Sets the type of a table item.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        type : int
            Type (see Flags for item types).
        """

    def setItemValue(self, item: FXTreeItem, column: int, valueText: str):
        """Sets the value of a table item of any type that can interpret a text string for its value. Returns
        True if the value of the specified item is set successfully.

        Parameters
        ----------
        item : FXTreeItem
            Tree item.
        column : int
            Column index of table item.
        valueText : str
            Text-form value of table item.
        """

    def setLeadingRowLabels(self, str: str):
        """Set the labels of the leading row. Note: this API must be used to set the header row labels,
        otherwise labels will be overwritten by auto-numbering.

        Parameters
        ----------
        str : str
            Tab "t" delimited list, can also contain newline characters indicating that label contains multiple lines of text (e.g. "Young'snModulustPoisson'snRatio").
        """

    def setListMaxVisible(self, maxVisible: int):
        """Sets the maximum number of visible items for all table lists.

        Parameters
        ----------
        maxVisible : int
            Maximum number of visible items.
        """

    def setTableStyle(self, style: int):
        """Sets the table options.

        Parameters
        ----------
        style : int
            Style flag (see Flags for AFX table options).
        """

    def setVisibleColumns(self, visibleColumns: int):
        """Sets the number of visible columns.

        Parameters
        ----------
        visibleColumns : int
            Number of visible columns.
        """

    def setVisibleItems(self, visibleItems: int):
        """Sets the number of visible items.

        Parameters
        ----------
        visibleItems : int
            Number of visible items.
        """

    def shadeReadOnlyItems(self, shadeItems: bool):
        """Makes the table to use a different, typically shaded, background color for read-only items if True is
        passed to the method. The table would use the same regular background color for both editable and read-
        only items if False is passed to the method.

        Parameters
        ----------
        shadeItems : bool
            Specify True to use a different background color for read-only items.
        """
