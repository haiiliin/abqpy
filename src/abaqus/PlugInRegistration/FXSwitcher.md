| 

The Switcher layout manager automatically arranges its child windows such that one of them is placed on top; all other child windows are hidden. Switcher provides a convenient method to conserve screen real-estate by arranging several GUI panels to appear in the same space, depending on context. Switcher ignores all layout hints from its children:- all children are stretched according to the switcher layout managers own size. When the SWITCHER\_HCOLLAPSE or SWITCHER\_VCOLLAPSE options are used, Switcher's default size is based on the width or height of the current child, instead of the maximum width or height of all of the children.

![](../SIMACAERefImages/gui-fxswitcher.png)

### FXSwitcher

###   

### FXSwitcher(p, opts=0, x=0, y=0, w=0, h=0, pl=DEFAULT\_SPACING, pr=DEFAULT\_SPACING, pt=DEFAULT\_SPACING, pb=DEFAULT\_SPACING)  
![](../IconsReference/butix_top_wline.png)

Construct a switcher layout manager.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   |   |
| opts | Int | 0 |   |
| x | Int | 0 |   |
| y | Int | 0 |   |
| w | Int | 0 |   |
| h | Int | 0 |   |
| pl | Int | DEFAULT_SPACING |   |
| pr | Int | DEFAULT_SPACING |   |
| pt | Int | DEFAULT_SPACING |   |
| pb | Int | DEFAULT_SPACING |   |

### getCurrent

###   

### getCurrent()  
![](../IconsReference/butix_top_wline.png)

Return the index of the child window currently on top.

### getDefaultHeight

###   

### getDefaultHeight()  
![](../IconsReference/butix_top_wline.png)

Return default height.

Reimplemented from FXPacker.

### getDefaultWidth

###   

### getDefaultWidth()  
![](../IconsReference/butix_top_wline.png)

Return default width.

Reimplemented from FXPacker.

### setCurrent

###   

### setCurrent(index, notify=False)  
![](../IconsReference/butix_top_wline.png)

Bring the child window at index to the top.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |
| notify | Bool | False |   |

### Class flags  
![](../IconsReference/butix_top_wline.png)


**ID's that identify children of the switcher; these ID's can be used to set the current child by sending the switcher a message using MKUINT(id, SEL_COMMAND).**

| **ID\_OPEN\_FIRST** | 

ID for the 1st child.

 |
| **ID\_OPEN\_SECOND** | 

ID for the 2nd child.

 |
| **ID\_OPEN\_THIRD** | 

ID for the 3rd child.

 |
| **ID\_OPEN\_FOURTH** | 

ID for the 4th child.

 |
| **ID\_OPEN\_FIFTH** | 

ID for the 5th child.

 |
| **ID\_OPEN\_SIXTH** | 

ID for the 6th child.

 |
| **ID\_OPEN\_SEVENTH** | 

ID for the 7th child.

 |
| **ID\_OPEN\_EIGHTH** | 

ID for the 8th child.

 |
| **ID\_OPEN\_NINETH** | 

ID for the 9th child.

 |
| **ID\_OPEN\_TENTH** | 

ID for the 10th child.

 |

### Global flags  
![](../IconsReference/butix_top_wline.png)


**Switcher options**

| **SWITCHER_HCOLLAPSE** | 

Collapse horizontally to width of current child.

 |
| **SWITCHER_VCOLLAPSE** | 

Collapse vertically to height of current child.

 |



 |