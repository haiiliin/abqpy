Convenience class for creating a labeled spinner. The label field can be a label or check button (AFXFLOATSPINNER_CHECKBUTTON option).

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxfloatspinner.png)

### AFXFloatSpinner(p, ncols, labelText, tgt=None, sel=0, opts=0, x=0, y=0, w=0, h=0, pl=DEFAULT\_PAD, pr=DEFAULT\_PAD, pt=DEFAULT\_PAD, pb=DEFAULT\_PAD)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   | Parent widget. |
| ncols | Int |   | Number of columns in the spinner. |
| labelText | String |   | Label preceeding spinner. |
| tgt | FXObject | None | Message target. |
| sel | Int | 0 | Message ID. |
| opts | Int | 0 | Options and hints. |
| x | Int | 0 | X coordinate of origin. |
| y | Int | 0 | Y coordinate of origin. |
| w | Int | 0 | Width of the widget. |
| h | Int | 0 | Height of the widget. |
| pl | Int | DEFAULT_PAD | Left padding. |
| pr | Int | DEFAULT_PAD | Right padding. |
| pt | Int | DEFAULT_PAD | Top padding. |
| pb | Int | DEFAULT_PAD | Bottom padding. |

### canFocus()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the spinner can recieve focus.

Reimplemented from FXWindow.

### create()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Creates the spinner.

Reimplemented from FXComposite.

### disable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Disables the spinner.

Reimplemented from FXWindow.

### enable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Enables the spinner.

Reimplemented from FXWindow.

### getCheck()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the state of the check button or the radio button.

### getHelpText()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the status line help text.

### getIncrement()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the spinner increment.

### getLabelFont()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the label font.

### getLabelText()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the label string.

### getRange()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns a sequence of floats (low, high) representing the widget's allowable minimum and maximum values.

### getTipText()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the tool tip message.

### getValue()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the spinner value.

### isCheckStateChanged()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the state of the check button or the radio button has changed by the user since it was programmatically set last time.

### isEditable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the input field of spinner may be edited.

### isReadOnlyState()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the spinner is set to the read-only state.

### setCheck(state)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the state of the check button or the radio button.

| **Argument** | **Type** | **Default** | **Description** |
| state | Bool |   | Button state. |

### setCheckButtonSelector(sel)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the message ID of the check button or the radio button.

| **Argument** | **Type** | **Default** | **Description** |
| sel | Int |   | Selector. |

### setCheckButtonTarget(tgt)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the message target of the check button or the radio button.

| **Argument** | **Type** | **Default** | **Description** |
| tgt | FXObject |   | Target. |

### setEditable(edit=True)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the editable state for the input field of spinner.

| **Argument** | **Type** | **Default** | **Description** |
| edit | Bool | True | Editable state. |

### setHelpText(text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the status line help text.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   | Help text. |

### setIncrement(incr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the spinner increment.

| **Argument** | **Type** | **Default** | **Description** |
| incr | Float |   | Increment. |

### setLabelFont(fnt)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the label font.

| **Argument** | **Type** | **Default** | **Description** |
| fnt | FXFont |   | Label font. |

### setLabelText(txt)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the label string.

| **Argument** | **Type** | **Default** | **Description** |
| txt | String |   | Label text. |

### setRange(low, high)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the spinner range.

| **Argument** | **Type** | **Default** | **Description** |
| low | Float |   | Minimum value. |
| high | Float |   | Maximum value. |

### setReadOnlyState(edit=True)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the read-only state of the spinner.

| **Argument** | **Type** | **Default** | **Description** |
| edit | Bool | True | Read-only state. |

### setTipText(text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the tool tip message.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   | Tooltip text. |

### setValue(val, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the spinner value.

| **Argument** | **Type** | **Default** | **Description** |
| val | Float |   | Value. |
| notify | Bool | False | Notification flag. |

###   
Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

### 

| **ID_BUTTON** | 

ID for the check or radio button.

 |
| **ID_SPINNER** | 

ID for the spinner.

 |

###   
Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

### 

**Flags for AFX float spinner options.**

| **AFXFLOATSPINNER_CHECKBUTTON** | 

Use a check button instead of a label.

 |
| **AFXFLOATSPINNER_RADIOBUTTON** | 

Use a radio button instead of a label.

 |
| **AFXFLOATSPINNER_VERTICAL** | 

Orient label or button above spinner.

 |
| **AFXFLOATSPINNER_READONLY** | 

Configure spinner to the read-only state.

 |