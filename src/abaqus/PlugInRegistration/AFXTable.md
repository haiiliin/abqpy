This class implements an editable table.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxtable.png)

### AFXTable(p, numVisRows, numVisColumns, numRows, numColumns, tgt=None, sel=0, opts=AFXTABLE\_NORMAL, x=0, y=0, w=0, h=0, pl=4, pr=4, pt=DEFAULT\_MARGIN, pb=DEFAULT_MARGIN)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   | Parent widget. |
| numVisRows | Int |   | Number of rows to display. |
| numVisColumns | Int |   | Number of columns to display. |
| numRows | Int |   | Total number of rows including leading rows. |
| numColumns | Int |   | Total number of columns including leading columns. |
| tgt | FXObject | None | Message target. |
| sel | Int | 0 | Message ID. |
| opts | Int | AFXTABLE_NORMAL | Options and hints. |
| x | Int | 0 | X coordinate of the origin. |
| y | Int | 0 | Y coordinate of the origin. |
| w | Int | 0 | Width of the table widget. |
| h | Int | 0 | Height of the table widget. |
| pl | Int | 4 | Left padding (margin). |
| pr | Int | 4 | Right padding (margin). |
| pt | Int | DEFAULT_MARGIN | Top padding (margin). |
| pb | Int | DEFAULT_MARGIN | Bottom padding (margin). |

### addList(text, opts=AFXTABLE\_LIST\_NORMAL)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Adds a list that have only text items to the table and returns the list ID. The text strings of the list items are delimited by tab "\\t" characters in the given text. The list is used by items of type LIST.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   | Tab "\\t" delimited text string (e.g. "0\\t50\\t100\\t150"). |
| opts | Int | AFXTABLE\_LIST\_NORMAL | Options. |

### addList(opts=AFXTABLE\_LIST\_NORMAL)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Adds a list to the table and returns the list ID. The list is used by items of type LIST.

| **Argument** | **Type** | **Default** | **Description** |
| opts | Int | AFXTABLE\_LIST\_NORMAL | List flag. |

### appendListItem(listId, text, icon=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Appends an item to the specified table list; returns the index of the new item.

| **Argument** | **Type** | **Default** | **Description** |
| listId | Int |   | ID of the list to append to. |
| text | String |   | Item's text. |
| icon | FXIcon | None | Item's icon. |

### beginEdit(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the specified item in edit mode if the item is editable.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### cancelEdit()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Cancels the edit mode.

### clearContents(startRow, startColumn, endRow, endColumn, clearEditableOnly=True)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Clears the text in the items in the specified range.

| **Argument** | **Type** | **Default** | **Description** |
| startRow | Int |   | Row in which to start clearing. |
| startColumn | Int |   | Column in which to start clearing. |
| endRow | Int |   | Row in which to end clearing. |
| endColumn | Int |   | Column in which to end clearing. |
| clearEditableOnly | Bool | True | Specify True to clear the text of editable items only. |

### clearListItems(listId)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Removes all items from the specified table list.

| **Argument** | **Type** | **Default** | **Description** |
| listId | Int |   | ID of the list to clear. |

### create()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Creates server-side resources.

Reimplemented from AFXBaseTable.

### deleteColumns(startColumn, numColumns=1, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deletes columns starting at the specified column.

| **Argument** | **Type** | **Default** | **Description** |
| startColumn | Int |   | Starting column. |
| numColumns | Int | 1 | Number of columns to delete. |
| notify | Bool | False | Specify True to notify target of the deletion. |

### deleteRows(startRow, numRows=1, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deletes rows starting at the specified row.

| **Argument** | **Type** | **Default** | **Description** |
| startRow | Int |   | Starting row. |
| numRows | Int | 1 | Number of rows to delete. |
| notify | Bool | False | Specify True to notify target of the deletion. |

### deselectItem(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deselects the specified item.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### deselectRow(row)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deselects all items in the row.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index. |

### destroy()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Destroys server-side resources.

Reimplemented from FXComposite.

### detach()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Detaches server-side resources.

Reimplemented from AFXBaseTable.

### disable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Disables the table and the table items in the table.

Reimplemented from FXWindow.

### disableItem(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Disables the specified item.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### enable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Enables the table and the table items in the table.

Reimplemented from FXWindow.

### enableItem(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Enables the specified item.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### getColumnAtX(x)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the column at the specified x coordinate; returns -1 if x is outside of the table.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   | X coordinate. |

### getColumnSortOrder(column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the sort order of the given column.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |

### getColumnWidth(column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the width, in pixels, of the specified column.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |

### getCurrentColumn()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the column index of the current item.

Reimplemented from AFXBaseTable.

### getCurrentRow()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the row index of the current item.

Reimplemented from AFXBaseTable.

### getCurrentSortColumn()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the current sort column or -1 if none.

### getDefaultColumnWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default column width, in pixels, of the table.

### getDefaultHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default height of the table.

Reimplemented from AFXBaseTable.

### getDefaultRowHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default row height, in pixels, of the table.

### getDefaultWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default width of the table.

Reimplemented from AFXBaseTable.

### getFont()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Gets the font for all text items in the table.

Reimplemented from AFXBaseTable.

### getGridColor()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Gets the color of the gridlines in the table.

Reimplemented from AFXBaseTable.

### getItemBackColor(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Gets the background color of an item.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### getItemBoolValue(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the value of an item of type BOOL.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### getItemColor(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the color of an item of type COLOR. The color is "As is", "Default", or a color hex specification in the form of "RRGGBB" (e.g., "#0A1B2C").

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### getItemFloatValue(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the value of an item of type FLOAT.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### getItemIcon(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the icon of an item of type ICON.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### getItemIntValue(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the value of an item of type INT.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### getItemListId(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the list ID of an item of type LIST.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### getItemListIndex(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the list index (selection) of an item of type LIST.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### getItemProvider()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the item provider of this object.

### getItemSelector(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the message ID for an item.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### getItemTarget(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the target for an item.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### getItemText(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the text of an item of type TEXT.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### getItemTextColor(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the text color of an item.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### getItemType(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the type of an item.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### getItemValue(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the text-form value of an item of any type.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### getLeadingColumns()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of leading columns in the table.

Reimplemented from AFXBaseTable.

### getLeadingFont()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the font of the leading rows and columns.

### getLeadingRows()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of leading rows in the table.

Reimplemented from AFXBaseTable.

### getListItemIcon(listId, index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the icon of the item at the specified index of the specified table list.

| **Argument** | **Type** | **Default** | **Description** |
| listId | Int |   | ID of the list. |
| index | Int |   | Index into the list of the item to return. |

### getListItemText(listId, index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the text of the item at the specified index of the specified table list.

| **Argument** | **Type** | **Default** | **Description** |
| listId | Int |   | ID of the list. |
| index | Int |   | Index into the list of the item to return. |

### getNumColumns()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of columns in the table (including leading columns).

Reimplemented from AFXBaseTable.

### getNumEmptyRowsAtBottom()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of empty (non-trailing) rows at the bottom of the table.

### getNumListItems(listId)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of items in the specified table list.

| **Argument** | **Type** | **Default** | **Description** |
| listId | Int |   | ID of the list. |

### getNumRows()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of rows in the table (including leading rows).

Reimplemented from AFXBaseTable.

### getPreferredColumnWidth(column, excludeTitle=True)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the width required for a column.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| excludeTitle | Bool | True | Specify True to ignore the width of leading and trailing items of the column. |

### getPreferredRowHeight(row)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the height required for a row (useful for multi-line labels).

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index. |

### getRowAtY(y)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the row at the specified y coordinate; returns -1 if y is outside of the table.

| **Argument** | **Type** | **Default** | **Description** |
| y | Int |   | Y coordinate. |

### getRowHeight(row)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the height, in pixels, of the specified row.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index. |

### getSelBackColor()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Gets the selection background color of the table.

Reimplemented from AFXBaseTable.

### getSelTextColor()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Gets the selection text color of the table.

Reimplemented from AFXBaseTable.

### getStretchableColumn()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the index of the stretchable column.

### getTableStyle()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the options related only to the table.

### getVisibleColumns()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Gets the number of visible columns in the table.

Reimplemented from AFXBaseTable.

### getVisibleRows()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Gets the number of visible rows in the table.

Reimplemented from AFXBaseTable.

### insertColumns(startColumn, numColumns=1, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Inserts columns at the specified location.

| **Argument** | **Type** | **Default** | **Description** |
| startColumn | Int |   | Starting column. |
| numColumns | Int | 1 | Number of columns to insert. |
| notify | Bool | False | Specify True to notify target of the insertion. |

### insertRows(startRow, numRows=1, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Inserts rows at the specified location.

| **Argument** | **Type** | **Default** | **Description** |
| startRow | Int |   | Starting row. |
| numRows | Int | 1 | Number of rows to insert. |
| notify | Bool | False | Specify True to notify target of the insertion. |

### isAnyItemInColumnSelected(column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if any item in the column is selected.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |

### isAnyItemInRowSelected(row)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if any item in the row is selected.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index. |

### isColumnSelected(column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if all items in the column are selected.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |

### isColumnSortable(column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the items of the given column can be sorted.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |

### isItemBool(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the specified item is of type BOOL.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### isItemColor(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the specified item is of type COLOR.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### isItemEditable(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the item is editable.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### isItemEmpty(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the specified item does not have a value. This method checks the actual contents of the specified item and does not account for the empty-item policy for the item.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### isItemIcon(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the specified item is of type ICON.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### isItemList(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the specified item is of type LIST.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### isItemSelected(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the specified item is selected.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### isItemText(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the specified item is of type TEXT.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### isItemVisible(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the specified item is visible.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### isRowSelected(row)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if all items in the row are selected.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index. |

### killFocus()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Removes the focus from this window.

Reimplemented from AFXBaseTable.

### killSelection(notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deselects all items of the table; returns True if this method deselects any items that were selected.

| **Argument** | **Type** | **Default** | **Description** |
| notify | Bool | False | Specify True to notify target of the selection change (with a SEL_DESELECTED message). |

### layout()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Lays out the table contents.

Reimplemented from AFXBaseTable.

### makePositionVisible(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Scrolls to make the specified row, column fully visible.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### makeRowVisible(row)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Scrolls vertically (only) to make the specified row fully visible.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index. |

### moveContents(x, y)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Scrolls the contents.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   | Distance scrolled in X direction. |
| y | Int |   | Distance scrolled in Y direction. |

### recalc()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Propagates size changes.

Reimplemented from AFXBaseTable.

### removeListItem(listId, index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Removes the item at the specified index from the specified table list; returns the number of items remaining in list.

| **Argument** | **Type** | **Default** | **Description** |
| listId | Int |   | ID of the list to remove from. |
| index | Int |   | Index of the list item to remove. |

### selectItem(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Selects the specified item.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### selectRow(row)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Selects all items in the row.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index. |

### setColumnBoolIcons(column, trueIcon=None, falseIcon=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the True and False icons of all existing and future items in a column of type BOOL. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| trueIcon | FXIcon | None | Icon displayed when value is True; 0 = default icon. |
| falseIcon | FXIcon | None | Icon displayed when value is False; 0 = default icon. |

### setColumnBoolValue(column, value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the value of all existing and future items in a column of type BOOL. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| value | Bool |   | Specify True or False. |

### setColumnColor(column, color)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the color of all existing and future items in a column of type COLOR. The color can be "As is", "Default", a color hex specification in the form of "RRGGBB" (e.g., "#0A1B2C"), or a pre-defined color name (e.g., "Red"). Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| color | String |   | Color. |

### setColumnColorItemDefault(column, color)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the color of the color item in the flyout menu for all existing and future items that display "As is" or "Default" in a column of type COLOR. The color is either a color hex specification in the form of "RRGGBB" (e.g., "#0A1B2C") or a pre-defined color name (e.g., "Red"). Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| color | String |   | Color. |

### setColumnColorOptions(column, opts)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the color flyout options for all existing and future items in a column of type COLOR. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| opts | Int |   | Options (see ColorFlyoutOptions). |

### setColumnEditable(column, editable)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the editability of all existing and future items in a column. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| editable | Bool |   | Specify True for editable, False for read-only. |

### setColumnFloatValue(column, value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the value of all existing and future items in a column of type FLOAT. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| value | Float |   | Floating-point value. |

### setColumnIcon(column, icon=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the icon of all existing and future items in a column of type ICON. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| icon | FXIcon | None | Icon. |

### setColumnIntValue(column, value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the value of all existing and future items in a column of type INT. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| value | Int |   | Integer value. |

### setColumnJustify(column, justify)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the justification of all existing and future items in a column. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| justify | Int |   | Justification (see ItemJustify). |

### setColumnListId(column, listId)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the list ID of all existing and future items in a column of type LIST. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| listId | Int |   | List ID. |

### setColumnListIndex(column, index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the list index (selection) of all existing and future items in a column of type LIST. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| index | Int |   | Index of item to be selected. |

### setColumnSortable(column, sortable)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets a column to be sortable or not. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| sortable | Bool |   | Specify True for sortable, False for otherwise. |

### setColumnSortOrder(column, order)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the sort order of the given column. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| order | Int |   | Sort order (see SortOrder). |

### setColumnText(column, text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the text of all existing and future items in a column of type TEXT. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| text | String |   | Text. |

### setColumnType(column, type)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the type of a column. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| type | Int |   | Type (see Flags for item types). |

### setColumnWidth(column, width)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the width, in pixels, of the specified column. Specifying -1 for the column will change all non-leading and non-trailing columns in the table and set the default for the table. Specify -1 for the width will resize each specified column to best fit the width of the title(s) currently shown in its leading and trailing items.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| width | Int |   | Width in pixels. |

### setColumnWidthInChars(column, numChars)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the width, in number of characters, of the specified column. Specifying -1 for the column will change all non-leading and non-trailing columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| numChars | Int |   | Width in number of characters. |

### setCurrentItem(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the specified item to be the current item.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |

### setCurrentSortColumn(column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the current sort column. The given column must be sortable; otherwise the current sort column will not change.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |

### setDefaultBoolIcons(trueIcon=None, falseIcon=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default True and False icons for the table (0 = default icon).

| **Argument** | **Type** | **Default** | **Description** |
| trueIcon | FXIcon | None | Icon displayed when value is True; 0 = default icon. |
| falseIcon | FXIcon | None | Icon displayed when value is False; 0 = default icon. |

### setDefaultBoolValue(value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default bool value for the table.

| **Argument** | **Type** | **Default** | **Description** |
| value | Bool |   | Specify True or False. |

### setDefaultColor(color)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default color for all items of type COLOR in the table. The color can be "As is", "Default", a color hex specification in the form of "RRGGBB" (e.g., "#0A1B2C"), or a pre-defined color name (e.g., "Red").

| **Argument** | **Type** | **Default** | **Description** |
| color | String |   | Color. |

### setDefaultColumnWidth(width)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default width, in pixels, for all columns.

| **Argument** | **Type** | **Default** | **Description** |
| width | Int |   | Width in pixels. |

### setDefaultFloatValue(value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default floating-point value for the table.

| **Argument** | **Type** | **Default** | **Description** |
| value | Float |   | Floating-point value. |

### setDefaultIntValue(value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default integer value for the table.

| **Argument** | **Type** | **Default** | **Description** |
| value | Int |   | Integer value. |

### setDefaultJustify(justify)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default justification for the table.

| **Argument** | **Type** | **Default** | **Description** |
| justify | Int |   | Justification (see ItemJustify). |

### setDefaultRowHeight(height)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default height, in pixels, for all rows.

| **Argument** | **Type** | **Default** | **Description** |
| height | Int |   | Height in pixels. |

### setDefaultText(text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default text for the table.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   | Text. |

### setDefaultType(type)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default type for the table.

| **Argument** | **Type** | **Default** | **Description** |
| type | Int |   | Type (see Flags for item types). |

### setEmptyItemDefault(defaultVal)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default value (in text form) used for empty items of the table if its empty-item policy includes DEFAULT\_IF\_EMPTY.

| **Argument** | **Type** | **Default** | **Description** |
| defaultVal | String |   | Default value in text form. |

### setEmptyItemPolicy(policy)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the policy for handling empty items of the table (see EmptyItemPolicy).

| **Argument** | **Type** | **Default** | **Description** |
| policy | Int |   | Flags for handling empty items (see EmptyItemPolicy). |

### setFont(font)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the font for all text items in the table.

| **Argument** | **Type** | **Default** | **Description** |
| font | FXFont |   | Font. |

### setGridColor(color)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the color for the gridlines in the table.

| **Argument** | **Type** | **Default** | **Description** |
| color | FXColor |   | Color. |

### setItemBackColor(row, column, color)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the background color of an item using an FXColor.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |
| color | FXColor |   | Color index. |

### setItemBackColor(row, column, color)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the background color of an item using a string.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |
| color | String |   | Color name. |

### setItemBoolIcons(row, column, trueIcon=None, falseIcon=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the True and False icons of an item of type BOOL.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |
| trueIcon | FXIcon | None | Icon displayed when value is True; 0 = default icon. |
| falseIcon | FXIcon | None | Icon displayed when value is False; 0 = default icon. |

### setItemBoolValue(row, column, value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the value of an item of type BOOL.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |
| value | Bool |   | Specify True or False. |

### setItemColor(row, column, color)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the color of an item of type COLOR. The color can be "As is", "Default", a color hex specification in the form of "RRGGBB" (e.g., "#0A1B2C"), or a pre-defined color name (e.g., "Red").

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |
| color | String |   | Color. |

### setItemEditable(row, column, editable)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the editability of an item.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |
| editable | Bool |   | Specify True for editable, False for read-only. |

### setItemFloatValue(row, column, value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the value of an item of type FLOAT.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |
| value | Float |   | Floating-point value. |

### setItemIcon(row, column, icon=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the icon of an item of type ICON.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |
| icon | FXIcon | None | Icon. |

### setItemIntValue(row, column, value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the value of an item of type INT.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |
| value | Int |   | Integer value. |

### setItemJustify(row, column, justify)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the justification of an item.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |
| justify | Int |   | Justification (see ItemJustify). |

### setItemListId(row, column, listId)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the list ID of an item of type LIST.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |
| listId | Int |   | List ID. |

### setItemListIndex(row, column, index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the list index (selection) of an item of type LIST.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |
| index | Int |   | Index of item to be selected. |

### setItemProvider(ip)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the item provider of this object.

| **Argument** | **Type** | **Default** | **Description** |
| ip | FXObject |   | Item provideer. |

### setItemSpan(row, column, numRows, numColumns)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets a leading item to span more than one row or column.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |
| numRows | Int |   | Number of rows to span. |
| numColumns | Int |   | Number of columns to span. |

### setItemTarget(row, column, tgt, msg=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the target and message ID for an item.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |
| tgt | FXObject |   | Target. |
| msg | Int | 0 | Message ID. |

### setItemText(row, column, text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the text of an item of type TEXT.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |
| text | String |   | Text. |

### setItemTextColor(row, column, color)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the text color of an item using an FXColor.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |
| color | FXColor |   | Color index. |

### setItemTextColor(row, column, color)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the text color of an item using a string.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |
| color | String |   | Color name. |

### setItemType(row, column, type)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the type of an item.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |
| type | Int |   | Type (see Flags for item types). |

### setItemValue(row, column, valueText)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the value of an item of any type that can interpret a text string for its value. Returns True if the value of the specified item is set successfully.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index of item. |
| column | Int |   | Column index of item. |
| valueText | String |   | Text-form value of item. |

### setLeadingColumnLabels(str, column=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the labels of a leading column. Note: this API must be used to set the header column labels, otherwise labels will be overwritten by auto-numbering.

| **Argument** | **Type** | **Default** | **Description** |
| str | String |   | Tab "\\t" delimited list, can also contain newline characters indicating that label contains multiple lines of text (e.g. "Young's\\nModulus\\tPoisson's\\nRatio"). |
| column | Int | 0 | Column, this column must have previously been specified as a leading column (see setLeadingColumns). |

### setLeadingColumns(numColumns)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the number of leading columns.

| **Argument** | **Type** | **Default** | **Description** |
| numColumns | Int |   | Number of columns. |

### setLeadingFont(font)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the font of the leading rows and columns.

| **Argument** | **Type** | **Default** | **Description** |
| font | FXFont |   | Font. |

### setLeadingRowLabels(str, row=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the labels of a leading row. Note: this API must be used to set the header row labels, otherwise labels will be overwritten by auto-numbering.

| **Argument** | **Type** | **Default** | **Description** |
| str | String |   | Tab "\\t" delimited list, can also contain newline characters indicating that label contains multiple lines of text (e.g. "Young's\\nModulus\\tPoisson's\\nRatio"). |
| row | Int | 0 | Row, this row must have previously been specified as a leading row (see setLeadingRows). |

### setLeadingRows(numRows)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the number of leading rows.

| **Argument** | **Type** | **Default** | **Description** |
| numRows | Int |   | Number of rows. |

### setListMaxVisible(maxVisible)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the maximum number of visible items for all table lists.

| **Argument** | **Type** | **Default** | **Description** |
| maxVisible | Int |   | Maximum number of visible items. |

### setRowHeight(row, height)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the height, in pixels, of the specified row.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index. |
| height | Int |   | Height in pixels. |

### setSelBackColor(color)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the selection background color of the table.

| **Argument** | **Type** | **Default** | **Description** |
| color | FXColor |   | Color index. |

### setSelTextColor(color)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the selection text color of the table.

| **Argument** | **Type** | **Default** | **Description** |
| color | FXColor |   | Color index. |

### setStretchableColumn(column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the stretchable column. (This method only works for the last column.)

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |

### setTableSize(numRows, numColumns, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the size of the table.

| **Argument** | **Type** | **Default** | **Description** |
| numRows | Int |   | Number of rows. |
| numColumns | Int |   | Number of columns. |
| notify | Bool | False | Specify True to notify target of change. |

### setTableStyle(style)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the table options.

| **Argument** | **Type** | **Default** | **Description** |
| style | Int |   | Style flag (see Flags for AFX table options). |

### setVisibleColumns(visibleColumns)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the number of visible columns in the table.

| **Argument** | **Type** | **Default** | **Description** |
| visibleColumns | Int |   | Number of visible columns. |

### setVisibleRows(visibleRows)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the number of visible rows in the table.

| **Argument** | **Type** | **Default** | **Description** |
| visibleRows | Int |   | Number of visible rows. |

### shadeReadOnlyItems(shadeItems)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Makes the table to use a different, typically shaded, background color for read-only items if True is passed to the method. The table would use the same regular background color for both editable and read-only items if False is passed to the method.

| **Argument** | **Type** | **Default** | **Description** |
| shadeItems | Bool |   | Specify True to use a different background color for read-only items. |

### showHorizontalGrid(on=True)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Controls the display of horizontal gridlines in the table.

| **Argument** | **Type** | **Default** | **Description** |
| on | Bool | True | True if gridlines should be displayed. |

### showVerticalGrid(on=True)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Controls the display of vertical gridlines in the table.

| **Argument** | **Type** | **Default** | **Description** |
| on | Bool | True | True if gridlines should be displayed. |

### Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Flags for popup menu items.**

| **POPUP_NONE** | 

Popup not displayed.

 |
| **POPUP_CUT** | 

Display "Cut" menu item.

 |
| **POPUP_COPY** | 

Display "Copy" menu item.

 |
| **POPUP_PASTE** | 

Display "Paste" menu item.

 |
| **POPUP_EDIT** | 

Convenience flag for specifying multiple menu items.

 |
| **POPUP\_INSERT\_ROW** | 

Display "Insert Row Before/After" menu items.

 |
| **POPUP\_INSERT\_COLUMN** | 

Display "Insert Column Before/After" menu items.

 |
| **POPUP\_DELETE\_ROW** | 

Display "Delete Rows" menu item.

 |
| **POPUP\_DELETE\_COLUMN** | 

Display "Delete Columns" menu item.

 |
| **POPUP\_CLEAR\_CONTENTS** | 

Display "Clear Contents" and "Clear Table" menu items.

 |
| **POPUP\_MODIFY\_ROW** | 

Convenience flag for specifying multiple menu items.

 |
| **POPUP\_MODIFY\_COLUMN** | 

Convenience flag for specifying multiple menu items.

 |
| **POPUP_MODIFY** | 

Convenience flag for specifying multiple menu items.

 |
| **POPUP\_READ\_FROM_FILE** | 

Display "Read from File" menu item.

 |
| **POPUP\_WRITE\_TO_FILE** | 

Display "Write to File" menu item.

 |
| **POPUP_FILE** | 

Display "Read from file" and "Write to file" menu items.

 |
| **POPUP_ALL** | 

Display all menu items.

 |


**Message ID's.**

| **ID\_CUT\_SEL** | 

ID for the Cut button.

 |
| **ID\_COPY\_SEL** | 

ID for the Copy button.

 |
| **ID\_PASTE\_SEL** | 

ID for the Paste button.

 |
| **ID\_ADD\_COLUMN** | 

ID for the Insert Column buttons.

 |
| **ID\_ADD\_ROW** | 

ID for the Insert Row buttons.

 |
| **ID\_DELETE\_COLUMNS** | 

ID for the Delete Columns button.

 |
| **ID\_DELETE\_ROWS** | 

ID for the Delete Rows button.

 |
| **ID\_CLEAR\_SEL** | 

ID for the Clear Contents button.

 |
| **ID\_CLEAR\_TABLE** | 

ID for the Clear Table button.

 |
| **ID\_READ\_SEL** | 

ID for the Read from File button.

 |
| **ID_WRITE** | 

ID for the Write to File button.

 |
| **ID\_FILE\_DB** | 

ID for the Read Data from ASCII File dialog box used by the Read from File button.

 |
| **ID\_READ\_WARNING** | 

ID for the "Data were truncated" warning dialog box.

 |
| **ID\_WRITE\_FILE_DB** | 

ID for the file selection dialog box used by the Write to File button.

 |
| **ID\_CONFIRM\_WRITE** | 

ID for the "OK to overwrite?" warning dialog box.

 |


| **IGNORE\_BOTTOM\_EMPTY_ROWS** | 

not exposed in python

 |


**Flags for color flyouts (used for items of type COLOR).**

| **COLOR\_INCLUDE\_COLOR_ONLY** | 

Color item has no As Is and Default in its flyout.

 |
| **COLOR\_INCLUDE\_AS_IS** | 

Color item has As Is in its flyout.

 |
| **COLOR\_INCLUDE\_DEFAULT** | 

Color item has Default in its flyout.

 |
| **COLOR\_INCLUDE\_ALL** | 

Color item has both As Is and Default in its flyout. This is the default option.

 |


**Flags for how empty items should be handled by the AFXTable value-retrieving and error-checking API's**

| **DISALLOW_EMPTY** | 

Disallow an item to be empty (default).

 |
| **ALLOW_EMPTY** | 

Allow an item to be empty.

 |
| **DEFAULT\_IF\_EMPTY** | 

Allow an item to be empty and use its default value for the item.

 |
| **KEEP\_BOTTOM\_EMPTY_ROWS** | 

Include empty rows at the bottom of the table.

 |


**Flags for item alignment.**

| **LEFT** | 

Left justified.

 |
| **RIGHT** | 

Right justified.

 |
| **CENTER** | 

Center justified (horizontal).

 |
| **TOP** | 

Top justified.

 |
| **BOTTOM** | 

Bottom justified.

 |
| **MIDDLE** | 

Middle justified (vertical).

 |


**Flags for item types.**

| **TEXT** | 

Item accepts a text string via a text field.

 |
| **FLOAT** | 

Item accepts a floating-point number via a text field.

 |
| **INT** | 

Item accepts an integer via a text field.

 |
| **LIST** | 

Item accepts input from a list.

 |
| **BOOL** | 

Item is a boolean; displayed as an icon.

 |
| **ICON** | 

Item displays an icon and does not accept input.

 |
| **COLOR** | 

Item accepts color selection via a color flyout.

 |


**Flags for real formats.**

| **GENERAL** | 

General.

 |
| **SCIENTIFIC** | 

Scientific.

 |
| **AUTOMATIC** | 

Automatic.

 |


**Flags for sorting items in a column.**

| **SORT_INACTIVE** | 

Sort currently not active for the column.

 |
| **SORT_ASCENDING** | 

Sort items of the column in the ascending order.

 |
| **SORT_DESCENDING** | 

Sort items of the column in the descending order.

 |

### Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Flags for AFX table options.**

| **AFXTABLE\_COLUMN\_RESIZABLE** | 

Allow users to resize columns.

 |
| **AFXTABLE\_ROW\_RESIZABLE** | 

Allow users to resize rows.

 |
| **AFXTABLE_RESIZE** | 

Allow users to resize rows and columns.

 |
| **AFXTABLE\_NO\_COLUMN_SELECT** | 

Disallow column selections (selecting a header/footer item in a column selects the whole column).

 |
| **AFXTABLE\_NO\_ROW_SELECT** | 

Disallow row selections (selecting a header/footer item in a row selects the whole row).

 |
| **AFXTABLE\_ROW\_MODE** | 

Selecting any item in a row selects the whole row.

 |
| **AFXTABLE\_EXTENDED\_SELECT** | 

Use extended selection mode that allows multiple items to be selected and allows users to drag-select a range of items.

 |
| **AFXTABLE\_SINGLE\_SELECT** | 

Use single selection mode that allows up to one item to be selected.

 |
| **AFXTABLE\_BROWSE\_SELECT** | 

Use browse selection mode that enforces one single item to be selected at all times.

 |
| **AFXTABLE_EDITABLE** | 

Table is editable.

 |
| **AFXTABLE_NORMAL** | 

Default table options--use extended selection mode, columns are resizable, and layout fills both X and Y directions.

 |


**Flags for the table's list (for items of type LIST).**

| **AFXTABLE\_LIST\_PRESELECT_NONE** | 

Do not pre-select any list item.

 |