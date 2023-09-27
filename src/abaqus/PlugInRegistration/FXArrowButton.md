Button with an arrow; the arrow can point in any direction. When clicked, the arrow button sends a SEL\_COMMAND to its target. When ARROW\_REPEAT is passed, the arrow button sends a SEL_COMMAND repeatedly while the button is pressed.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fxarrowbutton.png)

### FXArrowButton(p, tgt=None, sel=0, opts=ARROW\_NORMAL, x=0, y=0, w=0, h=0, pl=DEFAULT\_PAD, pr=DEFAULT\_PAD, pt=DEFAULT\_PAD, pb=DEFAULT_PAD)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Construct arrow button.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   |   |
| tgt | FXObject | None |   |
| sel | Int | 0 |   |
| opts | Int | ARROW_NORMAL |   |
| x | Int | 0 |   |
| y | Int | 0 |   |
| w | Int | 0 |   |
| h | Int | 0 |   |
| pl | Int | DEFAULT_PAD |   |
| pr | Int | DEFAULT_PAD |   |
| pt | Int | DEFAULT_PAD |   |
| pb | Int | DEFAULT_PAD |   |

### canFocus()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True because a button can receive focus.

Reimplemented from FXWindow.

### disable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Disable the button.

Reimplemented from FXWindow.

### enable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Enable the button.

Reimplemented from FXWindow.

### getArrowColor()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get the fill color for the arrow.

### getArrowSize()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get the default arrow size.

### getArrowStyle()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get the arrow style flags.

### getDefaultHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get default height.

Reimplemented from FXFrame.

### getDefaultWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get default width.

Reimplemented from FXFrame.

### getJustify()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get the current justification mode.

### getState()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get the button state (where True means the button is down).

### getTipText()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get tool tip message for this arrow button.

### setArrowColor(clr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the fill color for the arrow.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor |   |   |

### setArrowSize(size)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the default arrow size.

| **Argument** | **Type** | **Default** | **Description** |
| size | Int |   |   |

### setArrowStyle(style)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the arrow style flags.

| **Argument** | **Type** | **Default** | **Description** |
| style | Int |   |   |

### setJustify(mode)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the current justification mode.

| **Argument** | **Type** | **Default** | **Description** |
| mode | Int |   |   |

### setState(s)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the button state (where True means the button is down).

| **Argument** | **Type** | **Default** | **Description** |
| s | Bool |   |   |

### setTipText(text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set tool tip message for this arrow button.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   |   |

###   
Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

### 

**Arrow style options**

| **ARROW_NONE** | 

No arrow.

 |
| **ARROW_UP** | 

Arrow points up.

 |
| **ARROW_DOWN** | 

Arrow points down.

 |
| **ARROW_LEFT** | 

Arrow points left.

 |
| **ARROW_RIGHT** | 

Arrow points right.

 |
| **ARROW_REPEAT** | 

Button repeats if held down.

 |
| **ARROW_AUTOGRAY** | 

Automatically gray out when not updated.

 |
| **ARROW_AUTOHIDE** | 

Automatically hide button when not updated.

 |
| **ARROW_TOOLBAR** | 

Button is toolbar-style.

 |
| **ARROW_SPINNER** | 

Button is spinner-style.

 |