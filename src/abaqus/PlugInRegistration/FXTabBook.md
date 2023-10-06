The tab book layout manager arranges pairs of children; the even numbered children (0,2,4,...) are usually tab items, and are placed on the top. The odd numbered children are usually layout managers, and are placed below; all the odd numbered children are placed on top of each other, similar to the switcher widget. When the user presses one of the tab items, the tab item is raised above the neighboring tabs, and the corresponding panel is raised to the top. Thus, a tab book can be used to present many GUI controls in a small space by placing several panels on top of each other and using tab items to select the desired panel.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fxtabbook.png)

### FXTabBook(p, tgt=None, sel=0, opts=TABBOOK_NORMAL, x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING, pt=DEFAULT_SPACING, pb=DEFAULT_SPACING)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Construct tab book.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite | | |
| tgt | FXObject | None | |
| sel | Int | 0 | |
| opts | Int | TABBOOK_NORMAL | |
| x | Int | 0 | |
| y | Int | 0 | |
| w | Int | 0 | |
| h | Int | 0 | |
| pl | Int | DEFAULT_SPACING | |
| pr | Int | DEFAULT_SPACING | |
| pt | Int | DEFAULT_SPACING | |
| pb | Int | DEFAULT_SPACING | |

### getDefaultHeight()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default height.

Reimplemented from FXTabBar.

### getDefaultWidth()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default width.

Reimplemented from FXTabBar.
