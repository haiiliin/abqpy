This class provides a scrolled list of groups of options that may be toggled on or off as a group or individually.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxoptiontreelist.png)

### AFXOptionTreeList(p, nvis, opts=0, x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING, pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite | | Parent widget. |
| nvis | Int | | Number of visible items of list. |
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

### addItemFirst(text, tgt=None, msg=0)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Adds a new item with the given text as the first item of the list.

| **Argument** | **Type** | **Default** | **Description** |
| text | String | | Item text. |
| tgt | FXObject | None | Item target. |
| msg | Int | 0 | Item selector. |

### addItemLast(text, tgt=None, msg=0)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Adds a new item with the given text as the last item of the list.

| **Argument** | **Type** | **Default** | **Description** |
| text | String | | Item text. |
| tgt | FXObject | None | Item target. |
| msg | Int | 0 | Item selector. |

### clearItems()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Removes all items from the list.

### computeItemHeight(p=None)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Computes the item size to be used as a base for default height computation.

| **Argument** | **Type** | **Default** | **Description** |
| p | AFXOptionTreeItem | None | Item. |

### createItem(text, tgt, msg)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Creates a new tree item object.

| **Argument** | **Type** | **Default** | **Description** |
| text | String | | Item text. |
| tgt | FXObject | | Item target. |
| msg | Int | | Item selector. |

### getContentHeight()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the content height.

Reimplemented from FXScrollWindow.

### getContents()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the content window.

### getContentWidth()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the content width.

Reimplemented from FXScrollWindow.

### getDefaultHeight()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default height.

Reimplemented from FXScrollArea.

### getDefaultWidth()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default width.

Reimplemented from FXScrollArea.

### getFirstItem()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the first root item.

### getHSpacing()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the horizontal inter-child spacing.

### getLastItem()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the last root item.

### getNumItems()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of top-level items.

### getNumVisible()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of visible items.

### getPadBottom()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the bottom padding.

### getPadLeft()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the left padding.

### getPadRight()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the right padding.

### getPadTop()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the top padding.

### getVSpacing()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the vertical inter-child spacing.

### layout()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Recalculates layout.

Reimplemented from FXScrollWindow.

### moveContents(x, y)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Moves contents to the specified position.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int | | X location. |
| y | Int | | Y location |

### removeItem(item)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Removes the given item from the list. This method does nothing if the given item does not exist.

| **Argument** | **Type** | **Default** | **Description** |
| item | AFXOptionTreeItem | | Item to be removed. |

### setHSpacing(hs)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the horizontal inter-child spacing.

| **Argument** | **Type** | **Default** | **Description** |
| hs | Int | | Horizontal spacing. |

### setNumVisible(nvis)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the number of visible items.

| **Argument** | **Type** | **Default** | **Description** |
| nvis | Int | | Number of visible items. |

### setPadBottom(pb)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the bottom padding.

| **Argument** | **Type** | **Default** | **Description** |
| pb | Int | | Bottom padding. |

### setPadLeft(pl)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the left padding.

| **Argument** | **Type** | **Default** | **Description** |
| pl | Int | | Left padding. |

### setPadRight(pr)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the right padding.

| **Argument** | **Type** | **Default** | **Description** |
| pr | Int | | Right padding. |

### setPadTop(pt)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the top padding.

| **Argument** | **Type** | **Default** | **Description** |
| pt | Int | | Top padding. |

### setVSpacing(vs)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the vertical inter-child spacing.

| **Argument** | **Type** | **Default** | **Description** |
| vs | Int | | Vertical spacing. |

### Class flags

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

**Message ID's.**

| **ID_CONTENTS** |

ID for the content window.

|
