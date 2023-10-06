This class is a tree widget with check buttons.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxoptiontreeitem.png)

### AFXOptionTreeItem(p, label, tgt=None, sel=0, opts=0, x=0, y=0, w=0, h=0, pl=DEFAULT\_SPACING, pr=DEFAULT\_SPACING, pt=DEFAULT\_SPACING, pb=DEFAULT\_SPACING, hs=DEFAULT\_SPACING, vs=DEFAULT\_SPACING)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor creating a top-level (root) tree item.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   | Parent widget. |
| label | String |   | Label text. |
| tgt | FXObject | None | Message target. |
| sel | Int | 0 | Message ID. |
| opts | Int | 0 | Options and hints. |
| x | Int | 0 | X coordinate of origin. |
| y | Int | 0 | Y coordinate of origin. |
| w | Int | 0 | Width of the widget. |
| h | Int | 0 | Height of the widget. |
| pl | Int | DEFAULT_SPACING | Left padding. |
| pr | Int | DEFAULT_SPACING | Right padding. |
| pt | Int | DEFAULT_SPACING | Top padding. |
| pb | Int | DEFAULT_SPACING | Bottom padding. |
| hs | Int | DEFAULT_SPACING | Horizontal spacing. |
| vs | Int | DEFAULT_SPACING | Vertical spacing. |

### addItemAfter(label, tgt=None, sel=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Creates a new tree item as a sibling after (below) the tree item.

| **Argument** | **Type** | **Default** | **Description** |
| label | String |   | Item label. |
| tgt | FXObject | None | Item target. |
| sel | Int | 0 | Item selector. |

### addItemBefore(label, tgt=None, sel=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Creates a new tree item as a sibling before (above) the tree item.

| **Argument** | **Type** | **Default** | **Description** |
| label | String |   | Item label. |
| tgt | FXObject | None | Item target. |
| sel | Int | 0 | Item selector. |

### addItemFirst(label, tgt=None, sel=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Creates a new tree item as the first child of the tree item.

| **Argument** | **Type** | **Default** | **Description** |
| label | String |   | Item label. |
| tgt | FXObject | None | Item target. |
| sel | Int | 0 | Item selector. |

### addItemLast(label, tgt=None, sel=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Creates a new tree item as the last child of the tree item.

| **Argument** | **Type** | **Default** | **Description** |
| label | String |   | Item label. |
| tgt | FXObject | None | Item target. |
| sel | Int | 0 | Item selector. |

### childAtIndex(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the child tree at the given index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Index. |

### collapse()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Collapses (hides) the children.

### computeDefaultArrowSize()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Computes default size of the arrow button.

### containsChild(tree)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Checks whether the given tree is a child of this object.

| **Argument** | **Type** | **Default** | **Description** |
| tree | AFXOptionTreeItem |   | Item. |

### create()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Creates the tree item.

Reimplemented from FXComposite.

### disable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Disables the tree item.

Reimplemented from FXWindow.

### enable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Enables the tree item.

Reimplemented from FXWindow.

### expand()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Expands (shows) the children.

### getArrowSize()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the size of the arrow button.

### getCheck()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the check state of the tree item.

### getDefaultWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default width of the tree item.

Reimplemented from FXPacker.

### getFirst()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the first child tree.

Reimplemented from FXWindow.

### getLast()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the last child tree.

Reimplemented from FXWindow.

### getNext()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the next sibling tree.

Reimplemented from FXWindow.

### getParent()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the parent tree widget, or NULL if the tree item is the root.

Reimplemented from FXWindow.

### getPrev()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the previous sibling tree.

Reimplemented from FXWindow.

### getText()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the label text shown in the tree item's check button.

### hasVisibleChildren()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Checks whether the tree item has any visible children.

### hide()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Hides the tree item.

Reimplemented from FXWindow.

### indexOfChild(tree)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the index of an immediate child tree, or -1 if not found.

| **Argument** | **Type** | **Default** | **Description** |
| tree | AFXOptionTreeItem |   | Item. |

### isChildOf(tree)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Checks whether this object is contained in the given tree.

| **Argument** | **Type** | **Default** | **Description** |
| tree | AFXOptionTreeItem |   | Item. |

### isExpanded()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Checks whether the tree item shows its children.

### numChildren()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of child trees.

Reimplemented from FXWindow.

### setArrowSize(size)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the size of the arrow button for this object and all its children.

| **Argument** | **Type** | **Default** | **Description** |
| size | Int |   | Size. |

### setCheck(check, notify, propagating=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the check state of the tree item and its children, optionally notifying targets.

| **Argument** | **Type** | **Default** | **Description** |
| check | Int |   | Check state. |
| notify | Bool |   | Notification flag. |
| propagating | Bool | False | Propagation flag. |

### setCheck(check=True)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the check state of the tree item and its children.

| **Argument** | **Type** | **Default** | **Description** |
| check | Int | True | Check state. |

### setText(txt)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the label text shown in the tree item's check button.

| **Argument** | **Type** | **Default** | **Description** |
| txt | String |   | Label text. |

### show()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Shows the tree item.

Reimplemented from FXWindow.

### updateCheck(notify)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Updates the check state of the tree item and its ancestors.

| **Argument** | **Type** | **Default** | **Description** |
| notify | Bool |   | Notification flag. |

### Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Message ID's.**

| **ID_TOGGLEEXPAND** | 

Toggles display of frame with children.

 |
| **ID_CHECKSTATE** | 

Represents checked state of this object.

 |
| **ID_SUBTREE** | 

Container for the subtree.

 |
| **ID_EXPAND** | 

Expands frame with children.

 |
| **ID_COLLAPSE** | 

Collapses frame with children.

 |