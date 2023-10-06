Packer is a layout manager which automatically places child windows inside its area against the left, right, top, or bottom side. Each time a child is placed, the remaining space is decreased by the amount of space taken by the child window. The side against which a child is placed is determined by the LAYOUT_SIDE_TOP, LAYOUT_SIDE_BOTTOM, LAYOUT_SIDE_LEFT, and LAYOUT_SIDE_RIGHT hints given by the child window. Other layout hints from the child are observed as far as sensible. So for example, a child placed against the right edge can still have LAYOUT_FILL_Y or LAYOUT_TOP, and so on. The last child may have both LAYOUT_FILL_X and LAYOUT_FILL_Y, in which case it will be placed to take all remaining space.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fxpacker.png)

### FXPacker(p, opts=0, x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING, pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Construct packer layout manager.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite | | |
| opts | Int | 0 | |
| x | Int | 0 | |
| y | Int | 0 | |
| w | Int | 0 | |
| h | Int | 0 | |
| pl | Int | DEFAULT_SPACING | |
| pr | Int | DEFAULT_SPACING | |
| pt | Int | DEFAULT_SPACING | |
| pb | Int | DEFAULT_SPACING | |
| hs | Int | DEFAULT_SPACING | |
| vs | Int | DEFAULT_SPACING | |

### getBaseColor()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get base gui color.

### getBorderColor()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get border color.

### getBorderWidth()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get border width.

### getDefaultHeight()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default height.

Reimplemented from FXComposite.

Reimplemented in FXComboBox, FXDockSite, FXGroupBox, FXHorizontalFrame, FXListBox, FXMatrix, FXSpinner, FXStatusbar, FXSwitcher, FXTabBar, FXTabBook, FXToolbar, FXTreeListBox, FXVerticalFrame, AFXToolbarGroup, AFXPrimFloatSpinner, AFXSlider, and AFXVerticalAligner.

### getDefaultWidth()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default width.

Reimplemented from FXComposite.

Reimplemented in FXComboBox, FXDockSite, FXGroupBox, FXHorizontalFrame, FXListBox, FXMatrix, FXSpinner, FXStatusbar, FXSwitcher, FXTabBar, FXTabBook, FXToolbar, FXTreeListBox, FXVerticalFrame, AFXToolbarGroup, AFXOptionTreeItem, AFXPrimFloatSpinner, AFXSlider, AFXTextField, and AFXVerticalAligner.

### getFrameStyle()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get current frame style.

### getHiliteColor()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get highlight color.

### getHSpacing()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return current horizontal inter-child spacing.

### getPackingHints()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return packing hints.

### getPadBottom()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get bottom interior padding.

### getPadLeft()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get left interior padding.

### getPadRight()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get right interior padding.

### getPadTop()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get top interior padding.

### getShadowColor()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get shadow color.

### getVSpacing()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return current vertical inter-child spacing.

### setBaseColor(clr)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change base gui color.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor | | |

### setBorderColor(clr)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change border color.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor | | |

### setFrameStyle(style)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change frame style.

| **Argument** | **Type** | **Default** | **Description** |
| style | Int | | |

### setHiliteColor(clr)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change highlight color.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor | | |

### setHSpacing(hs)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change horizontal inter-child spacing.

| **Argument** | **Type** | **Default** | **Description** |
| hs | Int | | |

### setPackingHints(ph)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change packing hints.

| **Argument** | **Type** | **Default** | **Description** |
| ph | Int | | |

### setPadBottom(pb)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change bottom padding.

| **Argument** | **Type** | **Default** | **Description** |
| pb | Int | | |

### setPadLeft(pl)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change left padding.

| **Argument** | **Type** | **Default** | **Description** |
| pl | Int | | |

### setPadRight(pr)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change right padding.

| **Argument** | **Type** | **Default** | **Description** |
| pr | Int | | |

### setPadTop(pt)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change top padding.

| **Argument** | **Type** | **Default** | **Description** |
| pt | Int | | |

### setShadowColor(clr)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change shadow color.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor | | |

### setVSpacing(vs)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change vertical inter-child spacing.

| **Argument** | **Type** | **Default** | **Description** |
| vs | Int | | |

By clicking on Send, you accept that Dassault Systèmes will process your personal data and may contact you for further information.

[Privacy Policy](https://www.3ds.com/privacy-policy).

Total Results:

Results per page

This page cannot be found.

The page might not exist or is temporarily unavailable. Try again or try searching for the topic.
