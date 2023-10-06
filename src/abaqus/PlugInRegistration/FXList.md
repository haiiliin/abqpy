List Widget

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fxlist.png)

### FXList(p, nvis, tgt=None, sel=0, opts=LIST_NORMAL, x=0, y=0, w=0, h=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Construct a list with nvis visible items; the list is initially empty.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   |   |
| nvis | Int |   |   |
| tgt | FXObject | None |   |
| sel | Int | 0 |   |
| opts | Int | LIST_NORMAL |   |
| x | Int | 0 |   |
| y | Int | 0 |   |
| w | Int | 0 |   |
| h | Int | 0 |   |

### appendItem(text, icon=None, ptr=None, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Append new item with given text and optional icon, and user-data pointer.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   |   |
| icon | FXIcon | None |   |
| ptr | String | None |   |
| notify | Bool | False |   |

### appendItem(item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Append a \[possibly subclassed\] item to the list.

| **Argument** | **Type** | **Default** | **Description** |
| item | FXListItem |   |   |
| notify | Bool | False |   |

### canFocus()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

List widget can receive focus.

Reimplemented from FXWindow.

### clearItems(notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Remove all items from list.

| **Argument** | **Type** | **Default** | **Description** |
| notify | Bool | False |   |

### create()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Create server-side resources.

Reimplemented from FXComposite.

### deselectItem(index, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deselect item.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |
| notify | Bool | False |   |

### detach()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Detach server-side resources.

Reimplemented from FXComposite.

### findItem(text, start=-1, flags=SEARCH\_FORWARD| SEARCH\_WRAP)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Search items for item by name, starting from start item; the flags argument controls the search direction, and case sensitivity.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   |   |
| start | Int | -1 |   |
| flags | Int | SEARCH\_FORWARD| SEARCH\_WRAP |   |

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

### getDefaultHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default height.

Reimplemented from FXScrollArea.

Reimplemented in AFXList.

### getDefaultWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default width.

Reimplemented from FXScrollArea.

### getItemData(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return item user-data pointer.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |

### getItemHeight(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return item height.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |

### getItemIcon(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return item icon, if any.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |

### getItemText(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return item text.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |

### getItemWidth(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return item width.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |

### getListStyle()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return list style.

### getNumItems()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return the number of items in the list.

### getNumVisible()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return number of visible items.

### insertItem(index, text, icon=None, ptr=None, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Insert item at index with given text, icon, and user-data pointer.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |
| text | String |   |   |
| icon | FXIcon | None |   |
| ptr | String | None |   |
| notify | Bool | False |   |

### insertItem(index, item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Insert a new \[possibly subclassed\] item at the give index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |
| item | FXListItem |   |   |
| notify | Bool | False |   |

### isItemSelected(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if item is selected.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |

### isItemVisible(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if item is visible.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |

### killSelection(notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deselect all items.

| **Argument** | **Type** | **Default** | **Description** |
| notify | Bool | False |   |

### makeItemVisible(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Scroll to bring item into view.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |

### recalc()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Recalculate layout.

Reimplemented from FXWindow.

### removeItem(index, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Remove item from list.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |
| notify | Bool | False |   |

### replaceItem(index, text, icon=None, ptr=None, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Replace items text, icon, and user-data pointer.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |
| text | String |   |   |
| icon | FXIcon | None |   |
| ptr | String | None |   |
| notify | Bool | False |   |

### replaceItem(index, item, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Replace the item with a \[possibly subclassed\] item.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |
| item | FXListItem |   |   |
| notify | Bool | False |   |

### retrieveItem(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return the item at the given index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |

### selectItem(index, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Select item.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |
| notify | Bool | False |   |

### setCurrentItem(index, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change current item.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |
| notify | Bool | False |   |

### setItemData(index, ptr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change item user-data pointer.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |
| ptr | String |   |   |

### setItemIcon(index, icon)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change item icon.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |
| icon | FXIcon |   |   |

### setItemText(index, text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change item text.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |
| text | String |   |   |

### setListStyle(style)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change list style.

| **Argument** | **Type** | **Default** | **Description** |
| style | Int |   |   |

### setNumVisible(nvis)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change the number of visible items.

| **Argument** | **Type** | **Default** | **Description** |
| nvis | Int |   |   |

### Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**List styles**

| **LIST_EXTENDEDSELECT** | 

Extended selection mode allows for drag-selection of ranges of items.

 |
| **LIST_SINGLESELECT** | 

Single selection mode allows up to one item to be selected.

 |
| **LIST_BROWSESELECT** | 

Browse selection mode enforces one single item to be selected at all times.

 |
| **LIST_MULTIPLESELECT** | 

Multiple selection mode is used for selection of individual items.

 |
| **LIST_AUTOSELECT** | 

Automatically select under cursor.

 |

By clicking on Send, you accept that Dassault Systèmes will process your personal data and may contact you for further information.

[Privacy Policy](https://www.3ds.com/privacy-policy).

Total Results:

Results per page

This page cannot be found.

The page might not exist or is temporarily unavailable. Try again or try searching for the topic.