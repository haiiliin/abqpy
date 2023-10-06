from __future__ import annotations

from .AFXBaseTable import AFXBaseTable
from .AFXDataComponent import AFXDataComponent
from .constants import AFXTABLE_LIST_NORMAL, AFXTABLE_NORMAL, DEFAULT_MARGIN
from .FXColor import FXColor
from .FXComposite import FXComposite
from .FXFont import FXFont
from .FXIcon import FXIcon
from .FXObject import FXObject


class AFXTable(AFXBaseTable, AFXDataComponent):
    """This class implements an editable table."""

    def __init__(
        self,
        p: FXComposite,
        numVisRows: int,
        numVisColumns: int,
        numRows: int,
        numColumns: int,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = AFXTABLE_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = 4,
        pr: int = 4,
        pt: int = DEFAULT_MARGIN,
        pb: int = DEFAULT_MARGIN,
    ):
        """Constructor.

        Parameters
        ----------
        p : FXComposite
            Parent widget.
        numVisRows : int
            Number of rows to display.
        numVisColumns : int
            Number of columns to display.
        numRows : int
            Total number of rows including leading rows.
        numColumns : int
            Total number of columns including leading columns.
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
        pl : int
            Left padding (margin).
        pr : int
            Right padding (margin).
        pt : int
            Top padding (margin).
        pb : int
            Bottom padding (margin).
        """

    def addList(self, opts: int = AFXTABLE_LIST_NORMAL):
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

    def beginEdit(self, row: int, column: int):
        """Sets the specified item in edit mode if the item is editable.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def cancelEdit(self):
        """Cancels the edit mode."""

    def clearContents(
        self, startRow: int, startColumn: int, endRow: int, endColumn: int, clearEditableOnly: bool = True
    ):
        """Clears the text in the items in the specified range.

        Parameters
        ----------
        startRow : int
            Row in which to start clearing.
        startColumn : int
            Column in which to start clearing.
        endRow : int
            Row in which to end clearing.
        endColumn : int
            Column in which to end clearing.
        clearEditableOnly : bool
            Specify True to clear the text of editable items only.
        """

    def clearListItems(self, listId: int):
        """Removes all items from the specified table list.

        Parameters
        ----------
        listId : int
            ID of the list to clear.
        """

    def create(self):
        """Creates server-side resources.

        Reimplemented from AFXBaseTable.
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

    def deleteRows(self, startRow: int, numRows: int = 1, notify: bool = False):
        """Deletes rows starting at the specified row.

        Parameters
        ----------
        startRow : int
            Starting row.
        numRows : int
            Number of rows to delete.
        notify : bool
            Specify True to notify target of the deletion.
        """

    def deselectItem(self, row: int, column: int):
        """Deselects the specified item.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def deselectRow(self, row: int):
        """Deselects all items in the row.

        Parameters
        ----------
        row : int
            Row index.
        """

    def destroy(self):
        """Destroys server-side resources.

        Reimplemented from FXComposite.
        """

    def detach(self):
        """Detaches server-side resources.

        Reimplemented from AFXBaseTable.
        """

    def disable(self):
        """Disables the table and the table items in the table.

        Reimplemented from FXWindow.
        """

    def disableItem(self, row: int, column: int):
        """Disables the specified item.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def enable(self):
        """Enables the table and the table items in the table.

        Reimplemented from FXWindow.
        """

    def enableItem(self, row: int, column: int):
        """Enables the specified item.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def getColumnAtX(self, x: int):
        """Returns the column at the specified x coordinate; returns -1 if x is outside of the table.

        Parameters
        ----------
        x : int
            X coordinate.
        """

    def getColumnSortOrder(self, column: int):
        """Returns the sort order of the given column.

        Parameters
        ----------
        column : int
            Column index.
        """

    def getColumnWidth(self, column: int):
        """Returns the width, in pixels, of the specified column.

        Parameters
        ----------
        column : int
            Column index.
        """

    def getCurrentColumn(self):
        """Returns the column index of the current item.

        Reimplemented from AFXBaseTable.
        """

    def getCurrentRow(self):
        """Returns the row index of the current item.

        Reimplemented from AFXBaseTable.
        """

    def getCurrentSortColumn(self):
        """Returns the current sort column or -1 if none."""

    def getDefaultColumnWidth(self):
        """Returns the default column width, in pixels, of the table."""

    def getDefaultHeight(self):
        """Returns the default height of the table.

        Reimplemented from AFXBaseTable.
        """

    def getDefaultRowHeight(self):
        """Returns the default row height, in pixels, of the table."""

    def getDefaultWidth(self):
        """Returns the default width of the table.

        Reimplemented from AFXBaseTable.
        """

    def getFont(self):
        """Gets the font for all text items in the table.

        Reimplemented from AFXBaseTable.
        """

    def getGridColor(self):
        """Gets the color of the gridlines in the table.

        Reimplemented from AFXBaseTable.
        """

    def getItemBackColor(self, row: int, column: int):
        """Gets the background color of an item.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def getItemBoolValue(self, row: int, column: int):
        """Returns the value of an item of type BOOL.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def getItemColor(self, row: int, column: int):
        """Returns the color of an item of type COLOR. The color is "As is", "Default", or a color hex
        specification in the form of "RRGGBB" (e.g., "#0A1B2C").

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def getItemFloatValue(self, row: int, column: int):
        """Returns the value of an item of type FLOAT.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def getItemIcon(self, row: int, column: int):
        """Returns the icon of an item of type ICON.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def getItemIntValue(self, row: int, column: int):
        """Returns the value of an item of type INT.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def getItemListId(self, row: int, column: int):
        """Returns the list ID of an item of type LIST.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def getItemListIndex(self, row: int, column: int):
        """Returns the list index (selection) of an item of type LIST.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def getItemProvider(self):
        """Returns the item provider of this object."""

    def getItemSelector(self, row: int, column: int):
        """Returns the message ID for an item.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def getItemTarget(self, row: int, column: int):
        """Returns the target for an item.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def getItemText(self, row: int, column: int):
        """Returns the text of an item of type TEXT.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def getItemTextColor(self, row: int, column: int):
        """Returns the text color of an item.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def getItemType(self, row: int, column: int):
        """Returns the type of an item.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def getItemValue(self, row: int, column: int):
        """Returns the text-form value of an item of any type.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def getLeadingColumns(self):
        """Returns the number of leading columns in the table.

        Reimplemented from AFXBaseTable.
        """

    def getLeadingFont(self):
        """Returns the font of the leading rows and columns."""

    def getLeadingRows(self):
        """Returns the number of leading rows in the table.

        Reimplemented from AFXBaseTable.
        """

    def getListItemIcon(self, listId: int, index: int):
        """Returns the icon of the item at the specified index of the specified table list.

        Parameters
        ----------
        listId : int
            ID of the list.
        index : int
            Index into the list of the item to return.
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
        """Returns the number of columns in the table (including leading columns).

        Reimplemented from AFXBaseTable.
        """

    def getNumEmptyRowsAtBottom(self):
        """Returns the number of empty (non-trailing) rows at the bottom of the table."""

    def getNumListItems(self, listId: int):
        """Returns the number of items in the specified table list.

        Parameters
        ----------
        listId : int
            ID of the list.
        """

    def getNumRows(self):
        """Returns the number of rows in the table (including leading rows).

        Reimplemented from AFXBaseTable.
        """

    def getPreferredColumnWidth(self, column: int, excludeTitle: bool = True):
        """Returns the width required for a column.

        Parameters
        ----------
        column : int
            Column index.
        excludeTitle : bool
            Specify True to ignore the width of leading and trailing items of the column.
        """

    def getPreferredRowHeight(self, row: int):
        """Returns the height required for a row (useful for multi-line labels).

        Parameters
        ----------
        row : int
            Row index.
        """

    def getRowAtY(self, y: int):
        """Returns the row at the specified y coordinate; returns -1 if y is outside of the table.

        Parameters
        ----------
        y : int
            Y coordinate.
        """

    def getRowHeight(self, row: int):
        """Returns the height, in pixels, of the specified row.

        Parameters
        ----------
        row : int
            Row index.
        """

    def getSelBackColor(self):
        """Gets the selection background color of the table.

        Reimplemented from AFXBaseTable.
        """

    def getSelTextColor(self):
        """Gets the selection text color of the table.

        Reimplemented from AFXBaseTable.
        """

    def getStretchableColumn(self):
        """Returns the index of the stretchable column."""

    def getTableStyle(self):
        """Returns the options related only to the table."""

    def getVisibleColumns(self):
        """Gets the number of visible columns in the table.

        Reimplemented from AFXBaseTable.
        """

    def getVisibleRows(self):
        """Gets the number of visible rows in the table.

        Reimplemented from AFXBaseTable.
        """

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

    def insertRows(self, startRow: int, numRows: int = 1, notify: bool = False):
        """Inserts rows at the specified location.

        Parameters
        ----------
        startRow : int
            Starting row.
        numRows : int
            Number of rows to insert.
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

    def isAnyItemInRowSelected(self, row: int):
        """Returns True if any item in the row is selected.

        Parameters
        ----------
        row : int
            Row index.
        """

    def isColumnSelected(self, column: int):
        """Returns True if all items in the column are selected.

        Parameters
        ----------
        column : int
            Column index.
        """

    def isColumnSortable(self, column: int):
        """Returns True if the items of the given column can be sorted.

        Parameters
        ----------
        column : int
            Column index.
        """

    def isItemBool(self, row: int, column: int):
        """Returns True if the specified item is of type BOOL.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def isItemColor(self, row: int, column: int):
        """Returns True if the specified item is of type COLOR.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def isItemEditable(self, row: int, column: int):
        """Returns True if the item is editable.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def isItemEmpty(self, row: int, column: int):
        """Returns True if the specified item does not have a value. This method checks the actual contents of
        the specified item and does not account for the empty-item policy for the item.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def isItemIcon(self, row: int, column: int):
        """Returns True if the specified item is of type ICON.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def isItemList(self, row: int, column: int):
        """Returns True if the specified item is of type LIST.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def isItemSelected(self, row: int, column: int):
        """Returns True if the specified item is selected.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def isItemText(self, row: int, column: int):
        """Returns True if the specified item is of type TEXT.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def isItemVisible(self, row: int, column: int):
        """Returns True if the specified item is visible.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def isRowSelected(self, row: int):
        """Returns True if all items in the row are selected.

        Parameters
        ----------
        row : int
            Row index.
        """

    def killFocus(self):
        """Removes the focus from this window.

        Reimplemented from AFXBaseTable.
        """

    def killSelection(self, notify: bool = False):
        """Deselects all items of the table; returns True if this method deselects any items that were selected.

        Parameters
        ----------
        notify : bool
            Specify True to notify target of the selection change (with a SEL_DESELECTED message).
        """

    def layout(self):
        """Lays out the table contents.

        Reimplemented from AFXBaseTable.
        """

    def makePositionVisible(self, row: int, column: int):
        """Scrolls to make the specified row, column fully visible.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def makeRowVisible(self, row: int):
        """Scrolls vertically (only) to make the specified row fully visible.

        Parameters
        ----------
        row : int
            Row index.
        """

    def moveContents(self, x: int, y: int):
        """Scrolls the contents.

        Parameters
        ----------
        x : int
            Distance scrolled in X direction.
        y : int
            Distance scrolled in Y direction.
        """

    def recalc(self):
        """Propagates size changes.

        Reimplemented from AFXBaseTable.
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

    def selectItem(self, row: int, column: int):
        """Selects the specified item.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def selectRow(self, row: int):
        """Selects all items in the row.

        Parameters
        ----------
        row : int
            Row index.
        """

    def setColumnBoolIcons(self, column: int, trueIcon: FXIcon | None = None, falseIcon: FXIcon | None = None):
        """Sets the True and False icons of all existing and future items in a column of type BOOL. Specifying
        -1 for the column will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Column index.
        trueIcon : FXIcon | None
            Icon displayed when value is True; 0 = default icon.
        falseIcon : FXIcon | None
            Icon displayed when value is False; 0 = default icon.
        """

    def setColumnBoolValue(self, column: int, value: bool):
        """Sets the value of all existing and future items in a column of type BOOL. Specifying -1 for the
        column will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Column index.
        value : bool
            Specify True or False.
        """

    def setColumnColor(self, column: int, color: str):
        """Sets the color of all existing and future items in a column of type COLOR. The color can be "As is",
        "Default", a color hex specification in the form of "RRGGBB" (e.g., "#0A1B2C"), or a pre-defined color
        name (e.g., "Red"). Specifying -1 for the column will change all columns in the table and set the
        default for the table.

        Parameters
        ----------
        column : int
            Column index.
        color : str
            Color.
        """

    def setColumnColorItemDefault(self, column: int, color: str):
        """Sets the color of the color item in the flyout menu for all existing and future items that display
        "As is" or "Default" in a column of type COLOR. The color is either a color hex specification in the
        form of "RRGGBB" (e.g., "#0A1B2C") or a pre-defined color name (e.g., "Red"). Specifying -1 for the
        column will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Column index.
        color : str
            Color.
        """

    def setColumnColorOptions(self, column: int, opts: int):
        """Sets the color flyout options for all existing and future items in a column of type COLOR. Specifying
        -1 for the column will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Column index.
        opts : int
            Options (see ColorFlyoutOptions).
        """

    def setColumnEditable(self, column: int, editable: bool):
        """Sets the editability of all existing and future items in a column. Specifying -1 for the column will
        change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Column index.
        editable : bool
            Specify True for editable, False for read-only.
        """

    def setColumnFloatValue(self, column: int, value: float):
        """Sets the value of all existing and future items in a column of type FLOAT. Specifying -1 for the
        column will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Column index.
        value : float
            Floating-point value.
        """

    def setColumnIcon(self, column: int, icon: FXIcon | None = None):
        """Sets the icon of all existing and future items in a column of type ICON. Specifying -1 for the column
        will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Column index.
        icon : FXIcon | None
            Icon.
        """

    def setColumnIntValue(self, column: int, value: int):
        """Sets the value of all existing and future items in a column of type INT. Specifying -1 for the column
        will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Column index.
        value : int
            Integer value.
        """

    def setColumnJustify(self, column: int, justify: int):
        """Sets the justification of all existing and future items in a column. Specifying -1 for the column
        will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Column index.
        justify : int
            Justification (see ItemJustify).
        """

    def setColumnListId(self, column: int, listId: int):
        """Sets the list ID of all existing and future items in a column of type LIST. Specifying -1 for the
        column will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Column index.
        listId : int
            List ID.
        """

    def setColumnListIndex(self, column: int, index: int):
        """Sets the list index (selection) of all existing and future items in a column of type LIST. Specifying
        -1 for the column will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Column index.
        index : int
            Index of item to be selected.
        """

    def setColumnSortable(self, column: int, sortable: bool):
        """Sets a column to be sortable or not. Specifying -1 for the column will change all columns in the
        table and set the default for the table.

        Parameters
        ----------
        column : int
            Column index.
        sortable : bool
            Specify True for sortable, False for otherwise.
        """

    def setColumnSortOrder(self, column: int, order: int):
        """Sets the sort order of the given column. Specifying -1 for the column will change all columns in the
        table and set the default for the table.

        Parameters
        ----------
        column : int
            Column index.
        order : int
            Sort order (see SortOrder).
        """

    def setColumnText(self, column: int, text: str):
        """Sets the text of all existing and future items in a column of type TEXT. Specifying -1 for the column
        will change all columns in the table and set the default for the table.

        Parameters
        ----------
        column : int
            Column index.
        text : str
            Text.
        """

    def setColumnType(self, column: int, type: int):
        """Sets the type of a column. Specifying -1 for the column will change all columns in the table and set
        the default for the table.

        Parameters
        ----------
        column : int
            Column index.
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

    def setCurrentItem(self, row: int, column: int):
        """Sets the specified item to be the current item.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        """

    def setCurrentSortColumn(self, column: int):
        """Sets the current sort column. The given column must be sortable; otherwise the current sort column
        will not change.

        Parameters
        ----------
        column : int
            Column index.
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

    def setDefaultRowHeight(self, height: int):
        """Sets the default height, in pixels, for all rows.

        Parameters
        ----------
        height : int
            Height in pixels.
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

    def setEmptyItemDefault(self, defaultVal: str):
        """Sets the default value (in text form) used for empty items of the table if its empty-item policy
        includes DEFAULT_IF_EMPTY.

        Parameters
        ----------
        defaultVal : str
            Default value in text form.
        """

    def setEmptyItemPolicy(self, policy: int):
        """Sets the policy for handling empty items of the table (see EmptyItemPolicy).

        Parameters
        ----------
        policy : int
            Flags for handling empty items (see EmptyItemPolicy).
        """

    def setFont(self, font: FXFont):
        """Sets the font for all text items in the table.

        Parameters
        ----------
        font : FXFont
            Font.
        """

    def setGridColor(self, color: FXColor):
        """Sets the color for the gridlines in the table.

        Parameters
        ----------
        color : FXColor
            Color.
        """

    def setItemBackColor(self, row: int, column: int, color: str):
        """Sets the background color of an item using a string.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        color : str
            Color name.
        """

    def setItemBoolIcons(self, row: int, column: int, trueIcon: FXIcon | None = None, falseIcon: FXIcon | None = None):
        """Sets the True and False icons of an item of type BOOL.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        trueIcon : FXIcon | None
            Icon displayed when value is True; 0 = default icon.
        falseIcon : FXIcon | None
            Icon displayed when value is False; 0 = default icon.
        """

    def setItemBoolValue(self, row: int, column: int, value: bool):
        """Sets the value of an item of type BOOL.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        value : bool
            Specify True or False.
        """

    def setItemColor(self, row: int, column: int, color: str):
        """Sets the color of an item of type COLOR. The color can be "As is", "Default", a color hex
        specification in the form of "RRGGBB" (e.g., "#0A1B2C"), or a pre-defined color name (e.g., "Red").

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        color : str
            Color.
        """

    def setItemEditable(self, row: int, column: int, editable: bool):
        """Sets the editability of an item.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        editable : bool
            Specify True for editable, False for read-only.
        """

    def setItemFloatValue(self, row: int, column: int, value: float):
        """Sets the value of an item of type FLOAT.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        value : float
            Floating-point value.
        """

    def setItemIcon(self, row: int, column: int, icon: FXIcon | None = None):
        """Sets the icon of an item of type ICON.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        icon : FXIcon | None
            Icon.
        """

    def setItemIntValue(self, row: int, column: int, value: int):
        """Sets the value of an item of type INT.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        value : int
            Integer value.
        """

    def setItemJustify(self, row: int, column: int, justify: int):
        """Sets the justification of an item.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        justify : int
            Justification (see ItemJustify).
        """

    def setItemListId(self, row: int, column: int, listId: int):
        """Sets the list ID of an item of type LIST.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        listId : int
            List ID.
        """

    def setItemListIndex(self, row: int, column: int, index: int):
        """Sets the list index (selection) of an item of type LIST.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        index : int
            Index of item to be selected.
        """

    def setItemProvider(self, ip: FXObject):
        """Sets the item provider of this object.

        Parameters
        ----------
        ip : FXObject
            Item provideer.
        """

    def setItemSpan(self, row: int, column: int, numRows: int, numColumns: int):
        """Sets a leading item to span more than one row or column.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        numRows : int
            Number of rows to span.
        numColumns : int
            Number of columns to span.
        """

    def setItemTarget(self, row: int, column: int, tgt: FXObject, msg: int = 0):
        """Sets the target and message ID for an item.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        tgt : FXObject
            Target.
        msg : int
            Message ID.
        """

    def setItemText(self, row: int, column: int, text: str):
        """Sets the text of an item of type TEXT.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        text : str
            Text.
        """

    def setItemTextColor(self, row: int, column: int, color: str):
        """Sets the text color of an item using a string.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        color : str
            Color name.
        """

    def setItemType(self, row: int, column: int, type: int):
        """Sets the type of an item.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        type : int
            Type (see Flags for item types).
        """

    def setItemValue(self, row: int, column: int, valueText: str):
        """Sets the value of an item of any type that can interpret a text string for its value. Returns True if
        the value of the specified item is set successfully.

        Parameters
        ----------
        row : int
            Row index of item.
        column : int
            Column index of item.
        valueText : str
            Text-form value of item.
        """

    def setLeadingColumnLabels(self, str: str, column: int = 0):
        """Sets the labels of a leading column. Note: this API must be used to set the header column labels,
        otherwise labels will be overwritten by auto-numbering.

        Parameters
        ----------
        str : str
            Tab "t" delimited list, can also contain newline characters indicating that label contains multiple lines of text (e.g. "Young'snModulustPoisson'snRatio").
        column : int
            Column, this column must have previously been specified as a leading column (see setLeadingColumns).
        """

    def setLeadingColumns(self, numColumns: int):
        """Sets the number of leading columns.

        Parameters
        ----------
        numColumns : int
            Number of columns.
        """

    def setLeadingFont(self, font: FXFont):
        """Sets the font of the leading rows and columns.

        Parameters
        ----------
        font : FXFont
            Font.
        """

    def setLeadingRowLabels(self, str: str, row: int = 0):
        """Set the labels of a leading row. Note: this API must be used to set the header row labels, otherwise
        labels will be overwritten by auto-numbering.

        Parameters
        ----------
        str : str
            Tab "t" delimited list, can also contain newline characters indicating that label contains multiple lines of text (e.g. "Young'snModulustPoisson'snRatio").
        row : int
            Row, this row must have previously been specified as a leading row (see setLeadingRows).
        """

    def setLeadingRows(self, numRows: int):
        """Sets the number of leading rows.

        Parameters
        ----------
        numRows : int
            Number of rows.
        """

    def setListMaxVisible(self, maxVisible: int):
        """Sets the maximum number of visible items for all table lists.

        Parameters
        ----------
        maxVisible : int
            Maximum number of visible items.
        """

    def setRowHeight(self, row: int, height: int):
        """Sets the height, in pixels, of the specified row.

        Parameters
        ----------
        row : int
            Row index.
        height : int
            Height in pixels.
        """

    def setSelBackColor(self, color: FXColor):
        """Sets the selection background color of the table.

        Parameters
        ----------
        color : FXColor
            Color index.
        """

    def setSelTextColor(self, color: FXColor):
        """Sets the selection text color of the table.

        Parameters
        ----------
        color : FXColor
            Color index.
        """

    def setStretchableColumn(self, column: int):
        """Sets the stretchable column. (This method only works for the last column.)

        Parameters
        ----------
        column : int
            Column index.
        """

    def setTableSize(self, numRows: int, numColumns: int, notify: bool = False):
        """Sets the size of the table.

        Parameters
        ----------
        numRows : int
            Number of rows.
        numColumns : int
            Number of columns.
        notify : bool
            Specify True to notify target of change.
        """

    def setTableStyle(self, style: int):
        """Sets the table options.

        Parameters
        ----------
        style : int
            Style flag (see Flags for AFX table options).
        """

    def setVisibleColumns(self, visibleColumns: int):
        """Sets the number of visible columns in the table.

        Parameters
        ----------
        visibleColumns : int
            Number of visible columns.
        """

    def setVisibleRows(self, visibleRows: int):
        """Sets the number of visible rows in the table.

        Parameters
        ----------
        visibleRows : int
            Number of visible rows.
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

    def showHorizontalGrid(self, on: bool = True):
        """Controls the display of horizontal gridlines in the table.

        Parameters
        ----------
        on : bool
            True if gridlines should be displayed.
        """

    def showVerticalGrid(self, on: bool = True):
        """Controls the display of vertical gridlines in the table.

        Parameters
        ----------
        on : bool
            True if gridlines should be displayed.
        """
