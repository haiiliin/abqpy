Abaqus

GUI Toolkit Reference

All Classes

AFXTreeTable

This class combines a tree widget with a table widget to allow associating a row of data with an item in a tree.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxtreetable.png)

### AFXTreeTable(p, numVisItems, numVisColumns, numColumns, tgt=None, sel=0, opts=AFXTREETABLE_NORMAL, x=0, y=0, w=0, h=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   | Parent widget. |
| numVisItems | Int |   | Number of items to display. |
| numVisColumns | Int |   | Number of columns in the table to display. |
| numColumns | Int |   | Number of columns in the table. |
| tgt | FXObject | None | Message target. |
| sel | Int | 0 | Message ID. |
| opts | Int | AFXTREETABLE_NORMAL | Options and hints. |
| x | Int | 0 | X coordinate of the origin. |
| y | Int | 0 | Y coordinate of the origin. |
| w | Int | 0 | Width of the table widget. |
| h | Int | 0 | Height of the table widget. |

### addItemAfter(other, text, oi=None, ci=None, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Appends a new tree item with the given text and optional icon after the other tree item.

| **Argument** | **Type** | **Default** | **Description** |
| other | FXTreeItem |   |   |
| text | String |   |   |
| oi | FXIcon | None |   |
| ci | FXIcon | None |   |
| notify | Bool | False |   |

### addItemAfter(other, item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Appends the new tree item after the other tree item.

| **Argument** | **Type** | **Default** | **Description** |
| other | FXTreeItem |   |   |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### addItemBefore(other, text, oi=None, ci=None, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Prepends a new tree item with the given text and optional icon prior to the other item.

| **Argument** | **Type** | **Default** | **Description** |
| other | FXTreeItem |   |   |
| text | String |   |   |
| oi | FXIcon | None |   |
| ci | FXIcon | None |   |
| notify | Bool | False |   |

### addItemBefore(other, item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Prepends the new item prior to the other tree item.

| **Argument** | **Type** | **Default** | **Description** |
| other | FXTreeItem |   |   |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### addItemFirst(p, text, oi=None, ci=None, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Prepends a new tree item with the given text and optional icon as the first child of the parent.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXTreeItem |   |   |
| text | String |   |   |
| oi | FXIcon | None |   |
| ci | FXIcon | None |   |
| notify | Bool | False |   |

### addItemFirst(p, item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Prepends the new tree item as first child of parent.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXTreeItem |   |   |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### addItemLast(p, text, oi=None, ci=None, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Appends a new tree item with the given text and optional icon as the last child of the parent.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXTreeItem |   |   |
| text | String |   |   |
| oi | FXIcon | None |   |
| ci | FXIcon | None |   |
| notify | Bool | False |   |

### addItemLast(p, item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Appends the new tree item as the last child of the parent.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXTreeItem |   |   |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### addList(text, opts=AFXTREETABLE\_LIST\_NORMAL)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Adds a list that have only text items to the table and returns the list ID. The text strings of the list items are delimited by tab "\\t" characters in the given text. The list is used by items of type LIST.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   | Tab "\\t" delimited text string (e.g. "0\\t50\\t100\\t150"). |
| opts | Int | AFXTREETABLE\_LIST\_NORMAL | Options. |

### addList(opts=AFXTREETABLE\_LIST\_NORMAL)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Adds a list to the table and returns the list ID. The list is used by items of type LIST.

| **Argument** | **Type** | **Default** | **Description** |
| opts | Int | AFXTREETABLE\_LIST\_NORMAL | List flag. |

### appendListItem(listId, text, icon=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Appends an item to the specified table list; returns the index of the new item.

| **Argument** | **Type** | **Default** | **Description** |
| listId | Int |   | ID of the list to append to. |
| text | String |   | Item's text. |
| icon | FXIcon | None | Item's icon. |

### beginEdit(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the specified item in edit mode if the item is editable.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of item. |

### cancelEdit()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Cancels the edit mode.

### clearContents(startItem, startColumn, endItem, endColumn, clearEditableOnly=True)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Clears the text in the items in the specified range.

| **Argument** | **Type** | **Default** | **Description** |
| startItem | FXTreeItem |   | Tree item in which to start clearing. |
| startColumn | Int |   | Column in which to start clearing. |
| endItem | FXTreeItem |   | Tree item in which to end clearing. |
| endColumn | Int |   | Column in which to end clearing. |
| clearEditableOnly | Bool | True | Specify True to clear the text of editable items only. |

### clearItems(notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Removes all tree items and table rows.

| **Argument** | **Type** | **Default** | **Description** |
| notify | Bool | False |   |

### clearListItems(listId)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Removes all items from the specified table list.

| **Argument** | **Type** | **Default** | **Description** |
| listId | Int |   | ID of the list to clear. |

### closeItem(item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Closes the specified item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### collapseTree(item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Collapses the specified item to hide its children.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### deleteColumns(startColumn, numColumns=1, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deletes columns starting at the specified column.

| **Argument** | **Type** | **Default** | **Description** |
| startColumn | Int |   | Starting column. |
| numColumns | Int | 1 | Number of columns to delete. |
| notify | Bool | False | Specify True to notify target of the deletion. |

### deselectItem(item, column, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deselects the specified item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of item. |
| notify | Bool | False |   |

### deselectRow(item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deselects all items in the row.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| notify | Bool | False |   |

### expandTree(item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Expands the specified item to show its children.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### getColumnWidth(column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the width, in pixels, of the specified column.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |

### getCurrentColumn()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the column index of the current item.

### getCurrentItem()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the current item, if any.

### getDefaultColumnWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default column width, in pixels, of the table.

### getDefaultHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default height.

Reimplemented from FXScrollArea.

### getDefaultWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default width.

Reimplemented from FXScrollArea.

### getFirstItem()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the first root tree item.

### getItemBoolValue(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the value of a table item of type BOOL.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### getItemCheck(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the item checked state.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### getItemClosedIcon(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the tree item's closed icon.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### getItemColor(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the color of a table item of type COLOR. The color is "As is", "Default", or a color hex specification in the form of "RRGGBB" (e.g., "#0A1B2C").

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### getItemFloatValue(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the value of a table item of type FLOAT.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### getItemFormat(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the format of a table item of type REAL (see RealFormat).

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### getItemIcon(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the icon of a table item of type ICON.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### getItemIntValue(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the value of a table item of type INT.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### getItemListId(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the list ID of a table item of type LIST.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### getItemListIndex(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the list index (selection) of a table item of type LIST.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### getItemNumDigits(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of digits to the left of the decimal point for a table item of type REAL.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### getItemOpenIcon(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the tree item's open icon.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### getItemPrecision(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the precision for a table item of type REAL.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### getItemText(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the text of an item of type TEXT.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of item. |

### getItemType(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the type of a table item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### getItemValue(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the text-form value of a table item of any type.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### getLastItem()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the last root tree item.

### getListItemIcon(listId, index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the icon of the item at the specified index of the specified table list.

| **Argument** | **Type** | **Default** | **Description** |
| listId | Int |   | ID of the list. |
| index | Int |   | Index into the list of the item to return. |

### getListItemIndex(listId, icon)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the index of the item of the specified table list that has the specified icon. Returns -1 if no such item exists.

| **Argument** | **Type** | **Default** | **Description** |
| listId | Int |   | ID of the list. |
| icon | FXIcon |   | Icon. |

### getListItemIndex(listId, text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the index of the item of the specified table list that has the specified text. Returns -1 if no such item exists.

| **Argument** | **Type** | **Default** | **Description** |
| listId | Int |   | ID of the list. |
| text | String |   | Text. |

### getListItemText(listId, index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the text of the item at the specified index of the specified table list.

| **Argument** | **Type** | **Default** | **Description** |
| listId | Int |   | ID of the list. |
| index | Int |   | Index into the list of the item to return. |

### getNumColumns()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of columns.

### getNumItems()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of items.

### getNumListItems(listId)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of items in the specified table list.

| **Argument** | **Type** | **Default** | **Description** |
| listId | Int |   | ID of the list. |

### getTableStyle()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the options related only to the table.

### getTreeColumn()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the column index of the tree.

### getVisibleColumns()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of visible columns.

### getVisibleItems()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of visible items.

### insertColumns(startColumn, numColumns=1, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Inserts columns at the specified location.

| **Argument** | **Type** | **Default** | **Description** |
| startColumn | Int |   | Starting column. |
| numColumns | Int | 1 | Number of columns to insert. |
| notify | Bool | False | Specify True to notify target of the insertion. |

### isAnyItemInColumnSelected(column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if any item in the column is selected.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |

### isAnyItemInRowSelected(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if any item in the row is selected.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |

### isColumnSelected(column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if all items in the column are selected.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |

### isItemBool(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the specified table item is of type BOOL.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### isItemColor(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the specified table item is of type COLOR.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### isItemEditable(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the table item is editable.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### isItemEmpty(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the specified table item does not have a value.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### isItemExpanded(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the tree item is expanded, False otherwise.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### isItemFloat(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the specified table item is of type FLOAT.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### isItemIcon(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the specified table item is of type ICON.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### isItemInt(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the specified table item is of type INT.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### isItemLeaf(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the tree item is a leaf-item (has no children), False otherwise.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### isItemList(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the specified tabl eitem is of type LIST.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### isItemOpened(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the tree item is opened, False otherwise.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### isItemSelected(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the specified item is selected.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of item. |

### isItemText(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the specified table item is of type TEXT.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |

### isItemVisible(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the specified item is visible.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of item. |

### isRowSelected(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if all items in the row are selected.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### killSelection(notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deselects all items.

| **Argument** | **Type** | **Default** | **Description** |
| notify | Bool | False |   |

### makePositionVisible(item, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Scrolls to make the specified row, column fully visible.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of item. |

### makeRowVisible(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Scrolls vertically (only) to make the specified row fully visible.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |

### openItem(item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Opens the specified item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### removeItem(item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Removes the specified tree item and corresponding table row.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### removeItems(from, to, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Removes the specified tree items and their corresponding table rows, inclusively.

| **Argument** | **Type** | **Default** | **Description** |
| from | FXTreeItem |   |   |
| to | FXTreeItem |   |   |
| notify | Bool | False |   |

### removeListItem(listId, index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Removes the item at the specified index from the specified table list; returns the number of items remaining in list.

| **Argument** | **Type** | **Default** | **Description** |
| listId | Int |   | ID of the list to remove from. |
| index | Int |   | Index of the list item to remove. |

### selectItem(item, column, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Selects the specified item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of item. |
| notify | Bool | False |   |

### selectRow(item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Selects all items in the row.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| notify | Bool | False |   |

### setColumnBoolIcons(column, trueIcon=None, falseIcon=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the True and False icons of all existing and future table items in a column of type BOOL. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Table column index. |
| trueIcon | FXIcon | None | Icon displayed when value is True; 0 = default icon. |
| falseIcon | FXIcon | None | Icon displayed when value is False; 0 = default icon. |

### setColumnBoolValue(column, value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the value of all existing and future table items in a column of type BOOL. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Table column index. |
| value | Bool |   | Specify True or False. |

### setColumnColor(column, color)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the color of all existing and future table items in a column of type COLOR. The color can be "As is", "Default", a color hex specification in the form of "RRGGBB" (e.g., "#0A1B2C"), or a pre-defined color name (e.g., "Red"). Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Table column index. |
| color | String |   | Color. |

### setColumnColorItemDefault(column, color)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the color of the color item in the flyout menu for all existing and future table items that display "As is" or "Default" in a column of type COLOR. The color is either a color hex specification in the form of "RRGGBB" (e.g., "#0A1B2C") or a pre-defined color name (e.g., "Red"). Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Table column index. |
| color | String |   | Color. |

### setColumnColorOptions(column, opts)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the color flyout options for all existing and future table items in a column of type COLOR. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Table column index. |
| opts | Int |   | Options (see ColorFlyoutOptions). |

### setColumnEditable(column, editable)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the editability of all existing and future table items in a column. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Table column index. |
| editable | Bool |   | Specify True for editable, False for read-only. |

### setColumnFloatValue(column, value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the value of all existing and future table items in a column of type FLOAT. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Table column index. |
| value | Float |   | Floating-point value. |

### setColumnFormat(column, format)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the real format for all existing and future table items in a column of type REAL.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Table column index. |
| format | Int |   | Default format of REAL values in column (see RealFormat). |

### setColumnIcon(column, icon=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the icon of all existing and future table items in a column of type ICON. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Table column index. |
| icon | FXIcon | None | Icon. |

### setColumnIntValue(column, value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the value of all existing and future table items in a column of type INT. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Table column index. |
| value | Int |   | Integer value. |

### setColumnJustify(column, justify)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the justification of all existing and future table items in a column. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Table column index. |
| justify | Int |   | Justification (see ItemJustify). |

### setColumnListId(column, listId)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the list ID of all existing and future table items in a column of type LIST. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Table column index. |
| listId | Int |   | List ID. |

### setColumnListIndex(column, index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the list index (selection) of all existing and future table items in a column of type LIST. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Table column index. |
| index | Int |   | Index of item to be selected. |

### setColumnNumDigits(column, numDigits)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the number of digits to the left of the decimal point for all existing and future table items in a column of type REAL.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Table column index. |
| numDigits | Int |   | Default number of digits the left of the decimal point. |

### setColumnPrecision(column, precision)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the precision for all existing and future table items in a column of type REAL.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Table column index. |
| precision | Int |   | Number of digits to the right of the decimal point. |

### setColumnText(column, text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the text of all existing and future table items in a column of type TEXT. Specifying -1 for the column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Table column index. |
| text | String |   | Text. |

### setColumnType(column, type)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the type of a column. Specifying -1 for the table column will change all columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Table column index. |
| type | Int |   | Type (see Flags for item types). |

### setColumnWidth(column, width)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the width, in pixels, of the specified column. Specifying -1 for the column will change all non-leading and non-trailing columns in the table and set the default for the table. Specify -1 for the width will resize each specified column to best fit the width of the title(s) currently shown in its leading and trailing items.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| width | Int |   | Width in pixels. |

### setColumnWidthInChars(column, numChars)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the width, in number of characters, of the specified column. Specifying -1 for the column will change all non-leading and non-trailing columns in the table and set the default for the table.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| numChars | Int |   | Width in number of characters. |

### setCurrentItem(item, column, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the current item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of item. |
| notify | Bool | False |   |

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
| value | Bool |   | Specify True or False. |

### setDefaultColor(color)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default color for all items of type COLOR in the table. The color can be "As is", "Default", a color hex specification in the form of "RRGGBB" (e.g., "#0A1B2C"), or a pre-defined color name (e.g., "Red").

| **Argument** | **Type** | **Default** | **Description** |
| color | String |   | Color. |

### setDefaultColumnWidth(width)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default width, in pixels, for all columns.

| **Argument** | **Type** | **Default** | **Description** |
| width | Int |   | Width in pixels. |

### setDefaultFloatValue(value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default floating-point value for the table.

| **Argument** | **Type** | **Default** | **Description** |
| value | Float |   | Floating-point value. |

### setDefaultFormat(format)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default real format for the table.

| **Argument** | **Type** | **Default** | **Description** |
| format | Int |   | Format flag. |

### setDefaultIntValue(value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default integer value for the table.

| **Argument** | **Type** | **Default** | **Description** |
| value | Int |   | Integer value. |

### setDefaultJustify(justify)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default justification for the table.

| **Argument** | **Type** | **Default** | **Description** |
| justify | Int |   | Justification (see ItemJustify). |

### setDefaultNumDigits(numDigits)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default number of digits to the left of the decimal point for the table.

| **Argument** | **Type** | **Default** | **Description** |
| numDigits | Int |   | Number of digits. |

### setDefaultPrecision(precision)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the precision for the table.

| **Argument** | **Type** | **Default** | **Description** |
| precision | Int |   | Precision. |

### setDefaultText(text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default text for the table.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   | Text. |

### setDefaultType(type)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default type for the table.

| **Argument** | **Type** | **Default** | **Description** |
| type | Int |   | Type (see Flags for item types). |

### setItemBoolIcons(item, column, trueIcon=None, falseIcon=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the True and False icons of a table item of type BOOL.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |
| trueIcon | FXIcon | None | Icon displayed when value is True; 0 = default icon. |
| falseIcon | FXIcon | None | Icon displayed when value is False; 0 = default icon. |

### setItemBoolValue(item, column, value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the value of a table item of type BOOL.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |
| value | Bool |   | Specify True or False. |

### setItemCheck(item, check, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the item checked state. Valid states are True, False and MAYBE. Returns True if the check value has changed, False otherwise.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| check | Int |   |   |
| notify | Bool | False |   |

### setItemClosedIcon(item, icon)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Changes the tree item's closed icon.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| icon | FXIcon |   |   |

### setItemColor(item, column, color)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the color of a table item of type COLOR. The color can be "As is", "Default", a color hex specification in the form of "RRGGBB" (e.g., "#0A1B2C"), or a pre-defined color name (e.g., "Red").

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |
| color | String |   | Color. |

### setItemEditable(item, column, editable)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the editability of a table item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |
| editable | Bool |   | Specify True for editable, False for read-only. |

### setItemFloatValue(item, column, value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the value of a table item of type FLOAT.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |
| value | Float |   | Floating-point value. |

### setItemFormat(item, column, format)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the format for a table item of type REAL (see RealFormat).

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Table column index of item. |
| format | Int |   | Format of table item (see RealFormat). |

### setItemIcon(item, column, icon=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the icon of a table item of type ICON.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |
| icon | FXIcon | None | Icon. |

### setItemIntValue(item, column, value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the value of a table item of type INT.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |
| value | Int |   | Integer value. |

### setItemJustify(item, column, justify)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the justification of an item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |
| justify | Int |   | Justification (see ItemJustify). |

### setItemListId(item, column, listId)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the list ID of a table item of type LIST.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |
| listId | Int |   | List ID. |

### setItemListIndex(item, column, index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the list index (selection) of a table item of type LIST.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |
| index | Int |   | Index of item to be selected. |

### setItemNumDigits(item, column, numDigits)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the number of digits to the left of the decimal point for a table item of type REAL.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |
| numDigits | Int |   | Number of digits. |

### setItemOpenIcon(item, icon)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the tree item's open icon.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| icon | FXIcon |   |   |

### setItemPrecision(item, column, precision)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the precision for a table item of type REAL.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |
| precision | Int |   | Number of digits to the right of the decimal point. |

### setItemText(item, column, text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the text of an item of type TEXT.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of item. |
| text | String |   | Text. |

### setItemType(item, column, type)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the type of a table item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |
| type | Int |   | Type (see Flags for item types). |

### setItemValue(item, column, valueText)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the value of a table item of any type that can interpret a text string for its value. Returns True if the value of the specified item is set successfully.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   | Tree item. |
| column | Int |   | Column index of table item. |
| valueText | String |   | Text-form value of table item. |

### setLeadingRowLabels(str)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the labels of the leading row. Note: this API must be used to set the header row labels, otherwise labels will be overwritten by auto-numbering.

| **Argument** | **Type** | **Default** | **Description** |
| str | String |   | Tab "\\t" delimited list, can also contain newline characters indicating that label contains multiple lines of text (e.g. "Young's\\nModulus\\tPoisson's\\nRatio"). |

### setListMaxVisible(maxVisible)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the maximum number of visible items for all table lists.

| **Argument** | **Type** | **Default** | **Description** |
| maxVisible | Int |   | Maximum number of visible items. |

### setTableStyle(style)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the table options.

| **Argument** | **Type** | **Default** | **Description** |
| style | Int |   | Style flag (see Flags for AFX table options). |

### setVisibleColumns(visibleColumns)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the number of visible columns.

| **Argument** | **Type** | **Default** | **Description** |
| visibleColumns | Int |   | Number of visible columns. |

### setVisibleItems(visibleItems)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the number of visible items.

| **Argument** | **Type** | **Default** | **Description** |
| visibleItems | Int |   | Number of visible items. |

### shadeReadOnlyItems(shadeItems)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Makes the table to use a different, typically shaded, background color for read-only items if True is passed to the method. The table would use the same regular background color for both editable and read-only items if False is passed to the method.

| **Argument** | **Type** | **Default** | **Description** |
| shadeItems | Bool |   | Specify True to use a different background color for read-only items. |

### Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


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


**Flags for item alignment.**

| **REAL** | 

Not yet implemented (Real).

 |
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

### Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Flags for AFX tree table options.**

| **AFXTREETABLE\_COLUMN\_RESIZABLE** | 

Allow users to resize columns.

 |
| **AFXTREETABLE\_NO\_COLUMN_SELECT** | 

Disallow column selections (selecting a header/footer item in a column selects the whole column).

 |
| **AFXTREETABLE\_ROW\_MODE** | 

Selecting any item in a row selects the whole row.

 |
| **AFXTREETABLE\_EXTENDED\_SELECT** | 

Use extended selection mode that allows multiple items to be selected and allows users to drag-select a range of items.

 |
| **AFXTREETABLE\_SINGLE\_SELECT** | 

Use single selection mode that allows up to one item to be selected.

 |
| **AFXTREETABLE\_BROWSE\_SELECT** | 

Use browse selection mode that enforces one single item to be selected at all times.

 |
| **AFXTREETABLE\_CHECK\_BOXES** | 

Show item check boxes.

 |
| **AFXTREETABLE\_PROPAGATE\_CHECKS** | 

Propagate checked state to children and parents.

 |
| **AFXTREETABLE_NORMAL** | 

Default table options--use extended selection mode, columns are resizable, and layout fills both X and Y directions.

 |


**Flags for the table's list (for items of type LIST).**

| **AFXTREETABLE\_LIST\_PRESELECT_NONE** | 

Do not pre-select any list item.

 |

By clicking on Send, you accept that Dassault Systèmes will process your personal data and may contact you for further information.

[Privacy Policy](https://www.3ds.com/privacy-policy).

Total Results:

Results per page

This page cannot be found.

The page might not exist or is temporarily unavailable. Try again or try searching for the topic.