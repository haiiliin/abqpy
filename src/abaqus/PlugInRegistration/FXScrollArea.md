The scroll area widget manages a content area and a viewport area through which the content is viewed. When the content area becomes larger than the viewport area, scrollbars are placed to permit viewing of the entire content by scrolling the content. Depending on the mode, scrollbars may be displayed on an as-needed basis, always, or never. Normally, the scroll area's size and the content's size are independent; however, it is possible to disable scrolling in the horizontal (vertical) direction. In this case, the content width (height) will influence the width (height) of the scroll area widget. For content which is time-consuming to repaint, continuous scrolling may be turned off.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fxscrollarea.png)

### getContentWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return content size.

Reimplemented in FXIconList, FXImageView, FXList, FXMDIClient, FXScrollWindow, FXTable, FXText, FXTreeList, AFXBaseTable, and AFXOptionTreeList.

### getDefaultHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default height.

Reimplemented from FXComposite.

Reimplemented in FXList, FXTable, FXText, FXTreeList, AFXBaseTable, AFXList, AFXOptionTreeList, AFXTable, and AFXTreeTable.

### getDefaultWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default width.

Reimplemented from FXComposite.

Reimplemented in FXList, FXTable, FXText, FXTreeList, AFXBaseTable, AFXOptionTreeList, AFXTable, and AFXTreeTable.

### getPosition(x, y)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get the current position.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   |   |
| y | Int |   |   |

### getScrollStyle()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return scroll style.

### getViewportHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return viewport size.

Reimplemented in FXIconList.

### getXPosition()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return the current x-position.

### getYPosition()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return the current y-position.

### horizontalScrollbar()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return a pointer to the horizontal scrollbar.

### isHorizontalScrollable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if horizontally scrollable.

### isVerticalScrollable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if vertically scrollable.

### moveContents(x, y)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Move contents to the specified position.

Reimplemented in FXIconList, FXMDIClient, FXScrollWindow, FXTable, FXText, AFXBaseTable, AFXOptionTreeList, and AFXTable.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   |   |
| y | Int |   |   |

### setPosition(x, y)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the current position.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   |   |
| y | Int |   |   |

### setScrollStyle(style)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change scroll style.

| **Argument** | **Type** | **Default** | **Description** |
| style | Int |   |   |

### verticalScrollbar()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return a pointer to the vertical scrollbar.

### Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Scrollbar options**

| **SCROLLERS_NORMAL** | 

Show the scrollbars when needed.

 |
| **HSCROLLER_ALWAYS** | 

Always show horizontal scrollers.

 |
| **HSCROLLER_NEVER** | 

Never show horizontal scrollers.

 |
| **VSCROLLER_ALWAYS** | 

Always show vertical scrollers.

 |
| **VSCROLLER_NEVER** | 

Never show vertical scrollers.

 |
| **HSCROLLING_ON** | 

Horizontal scrolling turned on (default).

 |
| **HSCROLLING_OFF** | 

Horizontal scrolling turned off.

 |
| **VSCROLLING_ON** | 

Vertical scrolling turned on (default).

 |
| **VSCROLLING_OFF** | 

Vertical scrolling turned off.

 |
| **SCROLLERS_TRACK** | 

Scrollers track continuously for smooth scrolling.

 |
| **SCROLLERS\_DONT\_TRACK** | 

Scrollers don't track continuously.

 |