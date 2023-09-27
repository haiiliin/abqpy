A radio button is a tri-state button. Normally, it is either True or False; a third state MAYBE may be set to indicate that no selection has been made yet by the user, or that the state is ambiguous. When pressed, the radio button sets its state to True and sends a SEL_COMMAND to its target, and the message data set to the state of the radio button, of the type FXbool. If the radio button is contained inside a group box, the other radio buttons in the group box will be set to False and will send a message as well.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fxradiobutton.png)

### FXRadioButton(p, text, tgt=None, sel=0, opts=RADIOBUTTON\_NORMAL, x=0, y=0, w=0, h=0, pl=DEFAULT\_PAD, pr=DEFAULT\_PAD, pt=DEFAULT\_PAD, pb=DEFAULT_PAD)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Construct new radio button.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   |   |
| text | String |   |   |
| tgt | FXObject | None |   |
| sel | Int | 0 |   |
| opts | Int | RADIOBUTTON_NORMAL |   |
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

Returns True because a radio button can receive focus.

Reimplemented from FXWindow.

### getCheck()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get radio button state (True, False or MAYBE).

### getDefaultHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get default height.

Reimplemented from FXLabel.

### getDefaultWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get default width.

Reimplemented from FXLabel.

### setCheck(s=True)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set radio button state (True, False or MAYBE).

| **Argument** | **Type** | **Default** | **Description** |
| s | Bool | True |   |

###   
Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

### 

**RadioButton flags**

| **RADIOBUTTON_AUTOGRAY** | 

Automatically gray out when not updated.

 |
| **RADIOBUTTON_AUTOHIDE** | 

Automatically hide when not updated.

 |