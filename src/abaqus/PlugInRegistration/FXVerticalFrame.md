Abaqus

GUI Toolkit Reference

All Classes

FXVerticalFrame

Vertical frame layout manager widget is used to automatically place child-windows vertically from top-to-bottom, or bottom-to-top, depending on the child window's layout hints.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fxverticalframe.png)

### FXVerticalFrame(p, opts=0, x=0, y=0, w=0, h=0, pl=DEFAULT\_SPACING, pr=DEFAULT\_SPACING, pt=DEFAULT\_SPACING, pb=DEFAULT\_SPACING, hs=DEFAULT\_SPACING, vs=DEFAULT\_SPACING)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Construct a vertical frame layout manager.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   |   |
| opts | Int | 0 |   |
| x | Int | 0 |   |
| y | Int | 0 |   |
| w | Int | 0 |   |
| h | Int | 0 |   |
| pl | Int | DEFAULT_SPACING |   |
| pr | Int | DEFAULT_SPACING |   |
| pt | Int | DEFAULT_SPACING |   |
| pb | Int | DEFAULT_SPACING |   |
| hs | Int | DEFAULT_SPACING |   |
| vs | Int | DEFAULT_SPACING |   |

### getDefaultHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default height.

Reimplemented from FXPacker.

Reimplemented in AFXVerticalAligner.

### getDefaultWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default width.

Reimplemented from FXPacker.

Reimplemented in AFXVerticalAligner.