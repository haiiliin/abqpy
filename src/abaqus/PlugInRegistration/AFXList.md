This class is a list widget that allows displaying items in a scrollable window. Each item has associated data set as integers as items are added.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxlist.png)

### AFXList(p, nvis, tgt=None, sel=0, opts=0, x=0, y=0, w=0, h=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   | Parent widget. |
| nvis | Int |   | Number of visible items. |
| tgt | FXObject | None | Message target. |
| sel | Int | 0 | Message ID. |
| opts | Int | 0 | Options and hints. |
| x | Int | 0 | X coordinate of origin. |
| y | Int | 0 | Y coordinate of origin. |
| w | Int | 0 | Width of the widget. |
| h | Int | 0 | Height of the widget. |

### appendItem(text, icon=None, sel=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Adds a new item to the end of the list.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   | Text |
| icon | FXIcon | None | Icon |
| sel | Int | 0 | Integer associated with this item |

### disable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Disables the list.

Reimplemented from FXWindow.

### enable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Enables the list.

Reimplemented from FXWindow.

### getAutoCommit()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the auto-commit flag.

### getDefaultHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default height of the list.

Reimplemented from FXList.

### getItemIndexForData(data)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the index of the first item with the associated data or -1 if not found.

| **Argument** | **Type** | **Default** | **Description** |
| data |   |   |   |

### getItemProvider()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the provider of the list's items.

### getSingleSelection()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the index of the uniquely selected item. If more than one item or no items are selected, returns -1.

### insertItem(index, text, icon=None, sel=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Inserts a new item at the given index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Index |
| text | String |   | Text |
| icon | FXIcon | None | Icon |
| sel | Int | 0 | Integer associated with this item |

### replaceItem(index, text, icon=None, sel=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Replaces the item at the given index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Index |
| text | String |   | Text |
| icon | FXIcon | None | Icon |
| sel | Int | 0 | Integer associated with this item |

### setAutoCommit(commit)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the auto-commit option for handling double clicks. This option is turned on by default.

| **Argument** | **Type** | **Default** | **Description** |
| commit | Bool |   |   |

### setItemProvider(cp)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the provider of the list's items.

| **Argument** | **Type** | **Default** | **Description** |
| cp | FXObject |   |   |

### Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Flags for AFX list options.**

| **AFXLIST\_NO\_AUTOCOMMIT** | 

Don't automatically commit on double click.

 |