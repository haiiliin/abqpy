FXTabBar

| 

The tab bar layout manager arranges tab items side by side, and raises the active tab item above the neighboring tab items. The tab bar can be have the tab items on the top or bottom for horizontal arrangement, or on the left or right for vertical arrangement.

![](../SIMACAERefImages/gui-fxtabbar.png)

### FXTabBar

###   

### FXTabBar(p, tgt=None, sel=0, opts=TABBOOK\_NORMAL, x=0, y=0, w=0, h=0, pl=DEFAULT\_SPACING, pr=DEFAULT\_SPACING, pt=DEFAULT\_SPACING, pb=DEFAULT_SPACING)  
![](../IconsReference/butix_top_wline.png)

Construct a tab bar.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   |   |
| tgt | FXObject | None |   |
| sel | Int | 0 |   |
| opts | Int | TABBOOK_NORMAL |   |
| x | Int | 0 |   |
| y | Int | 0 |   |
| w | Int | 0 |   |
| h | Int | 0 |   |
| pl | Int | DEFAULT_SPACING |   |
| pr | Int | DEFAULT_SPACING |   |
| pt | Int | DEFAULT_SPACING |   |
| pb | Int | DEFAULT_SPACING |   |

### create

###   

### create()  
![](../IconsReference/butix_top_wline.png)

Create all of the server-side resources for this window // CAE.

Reimplemented from FXComposite.

### getCurrent

###   

### getCurrent()  
![](../IconsReference/butix_top_wline.png)

Return the currently active tab item.

### getDefaultHeight

###   

### getDefaultHeight()  
![](../IconsReference/butix_top_wline.png)

Return default height.

Reimplemented from FXPacker.

Reimplemented in FXTabBook.

### getDefaultWidth

###   

### getDefaultWidth()  
![](../IconsReference/butix_top_wline.png)

Return default width.

Reimplemented from FXPacker.

Reimplemented in FXTabBook.

### getTabStyle

###   

### getTabStyle()  
![](../IconsReference/butix_top_wline.png)

Return tab bar style.

### setCurrent

###   

### setCurrent(panel, notify=False)  
![](../IconsReference/butix_top_wline.png)

Change currently active tab item; this raises the active tab item slightly above the neighboring tab items.

| **Argument** | **Type** | **Default** | **Description** |
| panel | Int |   |   |
| notify | Bool | False |   |

### setTabStyle

###   

### setTabStyle(style)  
![](../IconsReference/butix_top_wline.png)

Change tab tab style.

| **Argument** | **Type** | **Default** | **Description** |
| style | Int |   |   |

###   
Class flags  
![](../IconsReference/butix_top_wline.png)

### 

| **ID\_OPEN\_ITEM** | 

Sent from one of the FXTabItems.

 |
| **ID\_OPEN\_FIRST** | 

Switch to panel ID\_OPEN\_FIRST+i.

 |

###   
Global flags  
![](../IconsReference/butix_top_wline.png)

### 

**Tab Book options**

| **TABBOOK_TOPTABS** | 

Tabs on top (default).

 |
| **TABBOOK_BOTTOMTABS** | 

Tabs on bottom.

 |
| **TABBOOK_SIDEWAYS** | 

Tabs on left.

 |
| **TABBOOK_LEFTTABS** | 

Tabs on left.

 |
| **TABBOOK_RIGHTTABS** | 

Tabs on right.

 |


