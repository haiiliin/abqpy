This class implements a labeled list box. It allows the user to select entries from a drop-down list. Each item has associated data set as integers initially as items are added.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxlistbox.png)

### AFXListBox(p, nvis, labelText, tgt=None, sel=0, opts=0, x=0, y=0, w=0, h=0, pl=DEFAULT\_PAD, pr=DEFAULT\_PAD, pt=DEFAULT\_PAD, pb=DEFAULT\_PAD)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   | Parent widget. |
| nvis | Int |   | Number of visible items. |
| labelText | String |   | Label string. |
| tgt | FXObject | None | Message target. |
| sel | Int | 0 | Message ID. |
| opts | Int | 0 | Options and hints. |
| x | Int | 0 | X coordinate of origin. |
| y | Int | 0 | Y coordinate of origin. |
| w | Int | 0 | Width of the widget. |
| h | Int | 0 | Height of the widget. |
| pl | Int | DEFAULT_PAD | Left padding (margin). |
| pr | Int | DEFAULT_PAD | Right padding (margin). |
| pt | Int | DEFAULT_PAD | Top padding (margin). |
| pb | Int | DEFAULT_PAD | Bottom padding (margin). |

### appendItem(text, icon=None, sel=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Adds an item to the end of the list.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   | Text |
| icon | FXIcon | None |   |
| sel | Int | 0 | Icon Integer associated with this item |

### clearItems()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Removes all items from the list.

### create()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Creates the list box.

Reimplemented from FXComposite.

### disable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Disables the list box.

Reimplemented from FXWindow.

### enable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Enables the list box.

Reimplemented from FXWindow.

### getCurrentItem()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the index of the current item.

### getHelpText()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the status line help text.

### getItemData(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the data for the specified item.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |

### getItemIndexForData(data)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the index of the first item with the associated data or -1 if not found.

| **Argument** | **Type** | **Default** | **Description** |
| data | Any  |   |   |

### getLabelFont()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the label font.

### getLabelText()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the label string.

### getNumItems()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of items in the list.

### getNumVisible()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of visible items.

### getTipText()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the tool tip message.

### insertItem(index, text, icon=None, sel=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Inserts a new item at the specified index position.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Index |
| text | String |   | Text |
| icon | FXIcon | None | Icon |
| sel | Int | 0 | Integer associated with this item |

### isItemCurrent(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the item at the specified index position is the current item.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |

### isReadOnlyState()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the list box is set to the read-only state.

### removeItem(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Removes the item at the specified index position from the list.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |

### replaceItem(index, text, icon=None, sel=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Replaces the item at the specified index position.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Index |
| text | String |   | Text |
| icon | FXIcon | None | Icon |
| sel | Int | 0 | Integer associated with this item |

### setCurrentItem(index, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the current item. (The index is zero-based).

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |
| notify | Bool | False |   |

### setHelpText(text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the status line help text.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   |   |

### setItemData(index, ptr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the data for the specified item.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |
| ptr | String |   |   |

### setLabelFont(fnt)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the label font.

| **Argument** | **Type** | **Default** | **Description** |
| fnt | FXFont |   |   |

### setLabelText(txt)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the label string.

| **Argument** | **Type** | **Default** | **Description** |
| txt | String |   |   |

### setNumVisible(nvis)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the number of visible items.

| **Argument** | **Type** | **Default** | **Description** |
| nvis | Int |   |   |

### setReadOnlyState(readonly=True)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the read-only state of the list box.

| **Argument** | **Type** | **Default** | **Description** |
| readonly | Bool | True |   |

### setTipText(text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the tool tip message.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   |   |

### Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Message ID's.**

| **ID_LIST** | 

ID for the list box.

 |
| **ID_FIELD** | 

ID for the text field.

 |

### Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Flags for AFX list box options.**

| **AFXLISTBOX_VERTICAL** | 

Orient label above list box.

 |
| **AFXLISTBOX_READONLY** | 

Configure list box to the read-only state.

 |