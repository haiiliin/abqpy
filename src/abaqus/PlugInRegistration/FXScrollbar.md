The scroll bar is used when a document has a larger content than may be made visible. The range is the total size of the document, the page is the part of the document which is visible. The size of the scrollbar thumb is adjusted to give feedback of the relative sizes of each. The scroll bar may be manipulated by the left mouse (normal scrolling), right mouse (vernier or fine-scrolling), or middle mouse (same as the left mouse only the scroll position can hop to the place where the click is made). Finally, if the mouse sports a wheel, the scroll bar can be manipulated by means of the mouse wheel as well. Holding down the Control-key during wheel motion will cause the scrolling to go faster than normal. While moving the scroll bar, a message of type SEL\_CHANGED will be sent to the target, and the message data will reflect the current position of type FXint. At the end of the interaction, the scroll bar will send a message of type SEL\_COMMAND to notify the target of the final position.

![](../SIMACAERefImages/gui-fxscrollbar.png)

### FXScrollbar

###   

### FXScrollbar(p, tgt=None, sel=0, opts=SCROLLBAR_VERTICAL, x=0, y=0, w=0, h=0)  
![](../IconsReference/butix_top_wline.png)

Construct scroll bar.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   |   |
| tgt | FXObject | None |   |
| sel | Int | 0 |   |
| opts | Int | SCROLLBAR_VERTICAL |   |
| x | Int | 0 |   |
| y | Int | 0 |   |
| w | Int | 0 |   |
| h | Int | 0 |   |

### getBorderColor

###   

### getBorderColor()  
![](../IconsReference/butix_top_wline.png)

Change border color.

### getDefaultHeight

###   

### getDefaultHeight()  
![](../IconsReference/butix_top_wline.png)

Return default height.

Reimplemented from FXWindow.

### getDefaultWidth

###   

### getDefaultWidth()  
![](../IconsReference/butix_top_wline.png)

Return default width.

Reimplemented from FXWindow.

### getHiliteColor

###   

### getHiliteColor()  
![](../IconsReference/butix_top_wline.png)

Return highlight color.

### getLine

###   

### getLine()  
![](../IconsReference/butix_top_wline.png)

Return line increment.

### getPage

###   

### getPage()  
![](../IconsReference/butix_top_wline.png)

Return page size.

### getPosition

###   

### getPosition()  
![](../IconsReference/butix_top_wline.png)

return scroll position

### getRange

###   

### getRange()  
![](../IconsReference/butix_top_wline.png)

Return content size range.

### getScrollbarStyle

###   

### getScrollbarStyle()  
![](../IconsReference/butix_top_wline.png)

Change the scrollbar style.

### getShadowColor

###   

### getShadowColor()  
![](../IconsReference/butix_top_wline.png)

Return shadow color.

### setBorderColor

###   

### setBorderColor(clr)  
![](../IconsReference/butix_top_wline.png)

Return border color.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor |   |   |

### setHiliteColor

###   

### setHiliteColor(clr)  
![](../IconsReference/butix_top_wline.png)

Change highlight color.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor |   |   |

### setLine

###   

### setLine(l)  
![](../IconsReference/butix_top_wline.png)

Set scoll increment for line.

| **Argument** | **Type** | **Default** | **Description** |
| l | Int |   |   |

### setPage

###   

### setPage(p)  
![](../IconsReference/butix_top_wline.png)

Set viewport page size.

| **Argument** | **Type** | **Default** | **Description** |
| p | Int |   |   |

### setPosition

###   

### setPosition(p, notifyTgt=False)  
![](../IconsReference/butix_top_wline.png)

Change current scroll position.

| **Argument** | **Type** | **Default** | **Description** |
| p | Int |   |   |
| notifyTgt | Bool | False |   |

### setRange

###   

### setRange(r)  
![](../IconsReference/butix_top_wline.png)

Set content size range.

| **Argument** | **Type** | **Default** | **Description** |
| r | Int |   |   |

### setScrollbarStyle

###   

### setScrollbarStyle(style)  
![](../IconsReference/butix_top_wline.png)

Get the current scrollbar style.

| **Argument** | **Type** | **Default** | **Description** |
| style | Int |   |   |

### setShadowColor

###   

### setShadowColor(clr)  
![](../IconsReference/butix_top_wline.png)

Change shadow color.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor |   |   |

### Global flags  
![](../IconsReference/butix_top_wline.png)


**Scrollbar styles**

| **SCROLLBAR_HORIZONTAL** | 

Horizontally oriented.

 |
| **SCROLLBAR_VERTICAL** | 

Vertically oriented.

 |



 |