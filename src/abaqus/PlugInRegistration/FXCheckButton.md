| 

A check button is a tri-state button. Normally, it is either True or False, and toggles between True or False whenever it is pressed. A third state MAYBE may be set to indicate that no selection has been made yet by the user, or that the state is ambiguous. When pressed, the check button sends a SEL_COMMAND to its target, and the message data represents the state of the check button.

![](../SIMACAERefImages/gui-fxcheckbutton.png)

### FXCheckButton

###   

### FXCheckButton(p, text, tgt=None, sel=0, opts=CHECKBUTTON\_NORMAL, x=0, y=0, w=0, h=0, pl=DEFAULT\_PAD, pr=DEFAULT\_PAD, pt=DEFAULT\_PAD, pb=DEFAULT_PAD)  
![](../IconsReference/butix_top_wline.png)

Construct new check button.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   |   |
| text | String |   |   |
| tgt | FXObject | None |   |
| sel | Int | 0 |   |
| opts | Int | CHECKBUTTON_NORMAL |   |
| x | Int | 0 |   |
| y | Int | 0 |   |
| w | Int | 0 |   |
| h | Int | 0 |   |
| pl | Int | DEFAULT_PAD |   |
| pr | Int | DEFAULT_PAD |   |
| pt | Int | DEFAULT_PAD |   |
| pb | Int | DEFAULT_PAD |   |

### canFocus

###   

### canFocus()  
![](../IconsReference/butix_top_wline.png)

Returns True because a check button can receive focus.

Reimplemented from FXWindow.

### getCheck

###   

### getCheck()  
![](../IconsReference/butix_top_wline.png)

Get check button state (True, False or MAYBE).

Reimplemented in AFXCheckButton.

### getDefaultHeight

###   

### getDefaultHeight()  
![](../IconsReference/butix_top_wline.png)

Get default height.

Reimplemented from FXLabel.

### getDefaultWidth

###   

### getDefaultWidth()  
![](../IconsReference/butix_top_wline.png)

Get default width.

Reimplemented from FXLabel.

### setCheck

###   

### setCheck(state=True)  
![](../IconsReference/butix_top_wline.png)

Set check button state (True, False or MAYBE).

| **Argument** | **Type** | **Default** | **Description** |
| state | Bool | True |   |

###   
Global flags  
![](../IconsReference/butix_top_wline.png)

### 

**CheckButton styles**

| **CHECKBUTTON_AUTOGRAY** | 

Automatically gray out when not updated.

 |
| **CHECKBUTTON_AUTOHIDE** | 

Automatically hide when not updated.

 |



 |