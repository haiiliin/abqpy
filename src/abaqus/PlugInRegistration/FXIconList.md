Icon List Widget

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fxiconlist.png)

### FXIconList(p, tgt=None, sel=0, opts=ICONLIST_NORMAL, x=0, y=0, w=0, h=0)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Construct icon list.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite | | |
| tgt | FXObject | None | |
| sel | Int | 0 | |
| opts | Int | ICONLIST_NORMAL | |
| x | Int | 0 | |
| y | Int | 0 | |
| w | Int | 0 | |
| h | Int | 0 | |

### appendItem(text, big=None, mini=None, ptr=None, notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Append new item with given text and optional icons, and user-data pointer.

| **Argument** | **Type** | **Default** | **Description** |
| text | String | | |
| big | FXIcon | None | |
| mini | FXIcon | None | |
| ptr | String | None | |
| notify | Bool | False | |

### appendItem(item, notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Append a \[possibly subclassed\] item to the end of the list.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXIconItem | | |
| notify | Bool | False | |

### canFocus()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Icon list can receive focus.

Reimplemented from FXWindow.

### clearItems(notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Remove all items from list.

| **Argument** | **Type** | **Default** | **Description** |
| notify | Bool | False | |

### create()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Create server-side resources.

Reimplemented from FXComposite.

Reimplemented in FXFileList.

### deselectItem(index, notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deselect item at index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |
| notify | Bool | False | |

### detach()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Detach server-side resources.

Reimplemented from FXComposite.

Reimplemented in FXFileList.

### disableItem(index)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Disable item at index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |

### enableItem(index)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Enable item at index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |

### extendSelection(index, notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Extend selection from anchor index to index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |
| notify | Bool | False | |

### findItem(text, start=-1, flags=SEARCH_FORWARD| SEARCH_WRAP)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Search items for item by name, starting from start item; the flags argument controls the search direction, and case sensitivity.

| **Argument** | **Type** | **Default** | **Description** |
| text | String | | |
| start | Int | -1 | |
| flags | Int | SEARCH_FORWARD| SEARCH_WRAP | |

### getAnchorItem()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return anchor item index, or -1 if none.

### getContentHeight()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return content height.

Reimplemented from FXScrollArea.

### getContentWidth()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Compute and return content width.

Reimplemented from FXScrollArea.

### getCurrentItem()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return current item index, or -1 if none.

### getCursorItem()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return index of item under cursor, or -1 if none.

### getFont()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return text font.

### getHelpText()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get the status line help text for this widget.

### getItemAt(x, y)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return index of item at x,y, or -1 if none.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int | | |
| y | Int | | |

### getItemBigIcon(index)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return big icon of item at index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |

### getItemData(index)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return item user-data pointer.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |

### getItemHeight()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return item height.

### getItemMiniIcon(index)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return mini icon of item at index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |

### getItemSpace()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return maximum item space.

### getItemText(index)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return item text.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |

### getItemWidth()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return item width.

### getListStyle()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get the current icon list style.

### getNumCols()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return number of columns.

### getNumItems()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return number of items.

### getNumRows()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return number of rows.

### getSelBackColor()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return selected text background.

### getSelTextColor()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return selected text color.

### getSortFunc()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return sort function.

### getTextColor()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return normal text color.

### getViewportHeight()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return viewport size.

Reimplemented from FXScrollArea.

### hitItem(index, x, y, ww=1, hh=1)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return item hit code: 0 outside, 1 icon, 2 text.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |
| x | Int | | |
| y | Int | | |
| ww | Int | 1 | |
| hh | Int | 1 | |

### insertItem(index, text, big=None, mini=None, ptr=None, notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Insert item at index with given text, icons, and user-data pointer.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |
| text | String | | |
| big | FXIcon | None | |
| mini | FXIcon | None | |
| ptr | String | None | |
| notify | Bool | False | |

### insertItem(index, item, notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Insert a new \[possibly subclassed\] item at the give index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |
| item | FXIconItem | | |
| notify | Bool | False | |

### isItemCurrent(index)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if item at index is current.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |

### isItemEnabled(index)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if item at index is enabled.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |

### isItemSelected(index)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if item at index is selected.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |

### isItemVisible(index)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if item at index is visible.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |

### killFocus()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Remove the focus from this window.

Reimplemented from FXWindow.

### killSelection(notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deselect all items.

| **Argument** | **Type** | **Default** | **Description** |
| notify | Bool | False | |

### makeItemVisible(index)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Scroll to make item at index visible.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |

### moveContents(x, y)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Move contents to the specified position.

Reimplemented from FXScrollArea.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int | | |
| y | Int | | |

### position(x, y, w, h)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Move and resize this window in the parent's coordinates.

Reimplemented from FXWindow.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int | | |
| y | Int | | |
| w | Int | | |
| h | Int | | |

### prependItem(text, big=None, mini=None, ptr=None, notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Append new item with given text and optional icons, and user-data pointer.

| **Argument** | **Type** | **Default** | **Description** |
| text | String | | |
| big | FXIcon | None | |
| mini | FXIcon | None | |
| ptr | String | None | |
| notify | Bool | False | |

### prependItem(item, notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Append a \[possibly subclassed\] item to the end of the list.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXIconItem | | |
| notify | Bool | False | |

### recalc()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Recalculate layout.

Reimplemented from FXWindow.

### removeItem(index, notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Remove item from list.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |
| notify | Bool | False | |

### replaceItem(index, text, big=None, mini=None, ptr=None, notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Replace items text, icons, and user-data pointer.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |
| text | String | | |
| big | FXIcon | None | |
| mini | FXIcon | None | |
| ptr | String | None | |
| notify | Bool | False | |

### replaceItem(index, item, notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Replace the item with a \[possibly subclassed\] item.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |
| item | FXIconItem | | |
| notify | Bool | False | |

### resize(w, h)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Resize this window to the specified width and height.

Reimplemented from FXWindow.

| **Argument** | **Type** | **Default** | **Description** |
| w | Int | | |
| h | Int | | |

### retrieveItem(index)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return the item at the given index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |

### selectInRectangle(x, y, w, h, notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Select items in rectangle.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int | | |
| y | Int | | |
| w | Int | | |
| h | Int | | |
| notify | Bool | False | |

### selectItem(index, notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Select item at index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |
| notify | Bool | False | |

### setAnchorItem(index)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change anchor item index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |

### setCurrentItem(index, notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change current item index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |
| notify | Bool | False | |

### setFocus()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Move the focus to this window.

Reimplemented from FXWindow.

### setFont(fnt)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change text font.

| **Argument** | **Type** | **Default** | **Description** |
| fnt | FXFont | | |

### setHelpText(text)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the status line help text for this widget.

| **Argument** | **Type** | **Default** | **Description** |
| text | String | | |

### setItemBigIcon(index, icon)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change item big icon.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |
| icon | FXIcon | | |

### setItemData(index, ptr)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change item user-data pointer.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |
| ptr | String | | |

### setItemMiniIcon(index, icon)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change item mini icon.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |
| icon | FXIcon | | |

### setItemSpace(s)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change maximum item space for each item.

| **Argument** | **Type** | **Default** | **Description** |
| s | Int | | |

### setItemText(index, text)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change item text.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |
| text | String | | |

### setListStyle(style)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the current icon list style.

| **Argument** | **Type** | **Default** | **Description** |
| style | Int | | |

### setSelBackColor(clr)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change selected text background.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor | | |

### setSelTextColor(clr)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change selected text color.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor | | |

### setSortFunc(func)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change sort function.

| **Argument** | **Type** | **Default** | **Description** |
| func | FXIconListSortFunc | | |

### setTextColor(clr)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change normal text color.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor | | |

### sortItems()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sort items.

### toggleItem(index, notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Toggle item at index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |
| notify | Bool | False | |

### updateItem(index)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Repaint item at index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | |

### Global flags

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

**Icon list styles**

| **ICONLIST_EXTENDEDSELECT** |

Extended selection mode.

|
| **ICONLIST_SINGLESELECT** |

At most one selected item.

|
| **ICONLIST_BROWSESELECT** |

Always exactly one selected item.

|
| **ICONLIST_MULTIPLESELECT** |

Multiple selection mode.

|
| **ICONLIST_AUTOSIZE** |

Automatically size item spacing.

|
| **ICONLIST_DETAILED** |

List mode.

|
| **ICONLIST_MINI_ICONS** |

Mini Icon mode.

|
| **ICONLIST_BIG_ICONS** |

Big Icon mode.

|
| **ICONLIST_ROWS** |

Row-wise mode.

|
| **ICONLIST_COLUMNS** |

Column-wise mode.

|

By clicking on Send, you accept that Dassault Systèmes will process your personal data and may contact you for further information.

[Privacy Policy](https://www.3ds.com/privacy-policy).

Total Results:

Results per page

This page cannot be found.

The page might not exist or is temporarily unavailable. Try again or try searching for the topic.
