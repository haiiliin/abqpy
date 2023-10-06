Tree list Widget

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fxtreelist.png)

### FXTreeList(p, nvis, tgt=None, sel=0, opts=TREELIST_NORMAL, x=0, y=0, w=0, h=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Construct a tree list with nvis visible items; the tree list is initially empty.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   |   |
| nvis | Int |   |   |
| tgt | FXObject | None |   |
| sel | Int | 0 |   |
| opts | Int | TREELIST_NORMAL |   |
| x | Int | 0 |   |
| y | Int | 0 |   |
| w | Int | 0 |   |
| h | Int | 0 |   |

### addItemAfter(other, text, oi=None, ci=None, ptr=None, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Append new item with given text and optional icon, and user-data pointer after to other item.

| **Argument** | **Type** | **Default** | **Description** |
| other | FXTreeItem |   |   |
| text | String |   |   |
| oi | FXIcon | None |   |
| ci | FXIcon | None |   |
| ptr | String | None |   |
| notify | Bool | False |   |

### addItemAfter(other, text, oi=None, ci=None, ptr=None, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Append new item with given text and optional icon, and user-data pointer after to other item.

| **Argument** | **Type** | **Default** | **Description** |
| other | FXTreeItem |   |   |
| text | String |   |   |
| oi | FXIcon | None |   |
| ci | FXIcon | None |   |
| ptr | String | None |   |
| notify | Bool | False |   |

### addItemAfter(other, item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Append new \[possibly subclassed\] item after to other item.

| **Argument** | **Type** | **Default** | **Description** |
| other | FXTreeItem |   |   |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### addItemBefore(other, text, oi=None, ci=None, ptr=None, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Prepend new item with given text and optional icon, and user-data pointer prior to other item.

| **Argument** | **Type** | **Default** | **Description** |
| other | FXTreeItem |   |   |
| text | String |   |   |
| oi | FXIcon | None |   |
| ci | FXIcon | None |   |
| ptr | String | None |   |
| notify | Bool | False |   |

### addItemBefore(other, text, oi=None, ci=None, ptr=None, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Prepend new item with given text and optional icon, and user-data pointer prior to other item.

| **Argument** | **Type** | **Default** | **Description** |
| other | FXTreeItem |   |   |
| text | String |   |   |
| oi | FXIcon | None |   |
| ci | FXIcon | None |   |
| ptr | String | None |   |
| notify | Bool | False |   |

### addItemBefore(other, item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Prepend new \[possibly subclassed\] item prior to other item.

| **Argument** | **Type** | **Default** | **Description** |
| other | FXTreeItem |   |   |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### addItemFirst(p, text, oi=None, ci=None, ptr=None, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Prepend new item with given text and optional icon, and user-data pointer as first child of p.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXTreeItem |   |   |
| text | String |   |   |
| oi | FXIcon | None |   |
| ci | FXIcon | None |   |
| ptr | String | None |   |
| notify | Bool | False |   |

### addItemFirst(p, text, oi=None, ci=None, ptr=None, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Prepend new item with given text and optional icon, and user-data pointer as first child of p.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXTreeItem |   |   |
| text | String |   |   |
| oi | FXIcon | None |   |
| ci | FXIcon | None |   |
| ptr | String | None |   |
| notify | Bool | False |   |

### addItemFirst(p, item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Prepend new \[possibly subclassed\] item as first child of p.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXTreeItem |   |   |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### addItemLast(p, text, oi=None, ci=None, ptr=None, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Append new item with given text and optional icon, and user-data pointer as last child of p.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXTreeItem |   |   |
| text | String |   |   |
| oi | FXIcon | None |   |
| ci | FXIcon | None |   |
| ptr | String | None |   |
| notify | Bool | False |   |

### addItemLast(p, text, oi=None, ci=None, ptr=None, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Append new item with given text and optional icon, and user-data pointer as last child of p.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXTreeItem |   |   |
| text | String |   |   |
| oi | FXIcon | None |   |
| ci | FXIcon | None |   |
| ptr | String | None |   |
| notify | Bool | False |   |

### addItemLast(p, item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Append new \[possibly subclassed\] item as last child of p.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXTreeItem |   |   |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### canFocus()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Tree list can receive focus.

Reimplemented from FXWindow.

### clearItems(notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Remove all items from list.

| **Argument** | **Type** | **Default** | **Description** |
| notify | Bool | False |   |

### closeItem(item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Close item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### collapseTree(tree, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Collapse tree.

| **Argument** | **Type** | **Default** | **Description** |
| tree | FXTreeItem |   |   |
| notify | Bool | False |   |

### create()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Create server-side resources.

Reimplemented from FXComposite.

Reimplemented in FXDirList.

### deselectItem(item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deselect item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### destroy()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Destroy server-side resources.

Reimplemented from FXComposite.

Reimplemented in FXDirList.

### detach()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Detach server-side resources.

Reimplemented from FXComposite.

Reimplemented in FXDirList.

### disableItem(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Disable item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### enableItem(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Enable item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### expandTree(tree, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Expand tree.

| **Argument** | **Type** | **Default** | **Description** |
| tree | FXTreeItem |   |   |
| notify | Bool | False |   |

### extendSelection(item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Extend selection from anchor item to item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### findItem(text, start=None, flags=SEARCH\_FORWARD| SEARCH\_WRAP)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Search items for item by name, starting from start item; the flags argument controls the search direction, and case sensitivity.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   |   |
| start | FXTreeItem | None |   |
| flags | Int | SEARCH\_FORWARD| SEARCH\_WRAP |   |

### getAnchorItem()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return anchor item, if any.

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

Return current item, if any.

### getCursorItem()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return item under cursor, if any.

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

REturn first root item.

### getFont()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return text font.

### getHelpText()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get the status line help text for this list.

### getIndent()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return parent-child indent amount.

### getItemAt(x, y)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get item at x,y, if any.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   |   |
| y | Int |   |   |

### getItemCheck(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the item checked state.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### getItemClosedIcon(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return item's closed icon.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### getItemData(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return item user-data pointer.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### getItemHeight(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return item height.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### getItemOpenIcon(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return item's open icon.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### getItemText(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return item's text.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### getItemWidth(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return item width.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### getLastItem()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return last root item.

### getLineColor()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return line color.

### getListStyle()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return list style.

### getNumItems()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return number of items.

### getNumVisible()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return number of visible items.

### getSelBackColor()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return selected text background.

### getSelTextColor()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return selected text color.

### getTextColor()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return normal text color.

### hitItem(item, x, y)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return item hit code: 0 outside, 1 icon, 2 text, 3 box.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| x | Int |   |   |
| y | Int |   |   |

### isItemCurrent(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if item is current.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### isItemEnabled(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if item is enabled.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### isItemExpanded(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if item expanded.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### isItemLeaf(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if item is a leaf-item, i.e. has no children.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### isItemOpened(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if item opened.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### isItemSelected(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if item is selected.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### isItemVisible(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if item is visible.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### killFocus()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Remove the focus from this window.

Reimplemented from FXWindow.

### killSelection(notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deselect all items.

| **Argument** | **Type** | **Default** | **Description** |
| notify | Bool | False |   |

### makeItemVisible(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Scroll to make item visible.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### moveItemAfter(other, item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Move item after other.

| **Argument** | **Type** | **Default** | **Description** |
| other | FXTreeItem |   |   |
| item | FXTreeItem |   |   |

### moveItemBefore(other, item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Move item before other.

| **Argument** | **Type** | **Default** | **Description** |
| other | FXTreeItem |   |   |
| item | FXTreeItem |   |   |

### openItem(item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Open item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### recalc()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Recalculate layout.

Reimplemented from FXWindow.

### removeItem(item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Remove item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### removeItems(fm, to, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Remove items in range \[fm, to\] inclusively.

| **Argument** | **Type** | **Default** | **Description** |
| fm | FXTreeItem |   |   |
| to | FXTreeItem |   |   |
| notify | Bool | False |   |

### reparentItem(item, p)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Reparent item under parent p.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| p | FXTreeItem |   |   |

### selectItem(item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Select item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### setAnchorItem(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change anchor item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### setCurrentItem(item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change current item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### setFocus()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Move the focus to this window.

Reimplemented from FXWindow.

### setFont(fnt)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change text font.

| **Argument** | **Type** | **Default** | **Description** |
| fnt | FXFont |   |   |

### setHelpText(text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the status line help text for this list.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   |   |

### setIndent(in_)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change parent-child indent amount.

| **Argument** | **Type** | **Default** | **Description** |
| in_ | Int |   |   |

### setItemCheck(item, check, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the item checked state. Valid states are True, False and MAYBE. Returns True if the check value has changed, False otherwise.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| check | Int |   |   |
| notify | Bool | False |   |

### setItemClosedIcon(item, icon)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Chance item's closed icon.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| icon | FXIcon |   |   |

### setItemData(item, ptr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change item user-data pointer.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| ptr | String |   |   |

### setItemOpenIcon(item, icon)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change item's open icon.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| icon | FXIcon |   |   |

### setItemText(item, text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change item's text.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| text | String |   |   |

### setLineColor(clr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change line color.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor |   |   |

### setListStyle(style)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change list style.

| **Argument** | **Type** | **Default** | **Description** |
| style | Int |   |   |

### setNumVisible(nvis)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change number of visible items.

| **Argument** | **Type** | **Default** | **Description** |
| nvis | Int |   |   |

### setSelBackColor(clr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change selected text background.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor |   |   |

### setSelTextColor(clr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change selected text color.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor |   |   |

### setTextColor(clr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change normal text color.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor |   |   |

### toggleItem(item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Toggle item selection.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |
| notify | Bool | False |   |

### updateItem(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Repaint item.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXTreeItem |   |   |

### Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Tree list styles**

| **TREELIST_EXTENDEDSELECT** | 

Extended selection mode allows for drag-selection of ranges of items.

 |
| **TREELIST_SINGLESELECT** | 

Single selection mode allows up to one item to be selected.

 |
| **TREELIST_BROWSESELECT** | 

Browse selection mode enforces one single item to be selected at all times.

 |
| **TREELIST_MULTIPLESELECT** | 

Multiple selection mode is used for selection of individual items.

 |
| **TREELIST_AUTOSELECT** | 

Automatically select under cursor.

 |
| **TREELIST\_SHOWS\_LINES** | 

Lines shown.

 |
| **TREELIST\_SHOWS\_BOXES** | 

Boxes to expand shown.

 |
| **TREELIST\_ROOT\_BOXES** | 

Display root boxes also.

 |
| **TREELIST\_CHECK\_BOXES** | 

Display check boxes.

 |
| **TREELIST\_PROPAGATE\_CHECKS** | 

Propagate checked state to children and parents.

 |

By clicking on Send, you accept that Dassault Systèmes will process your personal data and may contact you for further information.

[Privacy Policy](https://www.3ds.com/privacy-policy).

Total Results:

Results per page

This page cannot be found.

The page might not exist or is temporarily unavailable. Try again or try searching for the topic.