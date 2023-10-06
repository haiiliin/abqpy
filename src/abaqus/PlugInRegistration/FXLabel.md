A label widget can be used to place a text and/or icon for explanation purposes. The text label may have an optional tooltip and/or help string.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fxlabel.png)

### FXLabel(p, text, ic=None, opts=LABEL\_NORMAL, x=0, y=0, w=0, h=0, pl=DEFAULT\_PAD, pr=DEFAULT\_PAD, pt=DEFAULT\_PAD, pb=DEFAULT_PAD)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Construct label with given text and icon.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   |   |
| text | String |   |   |
| ic | FXIcon | None |   |
| opts | Int | LABEL_NORMAL |   |
| x | Int | 0 |   |
| y | Int | 0 |   |
| w | Int | 0 |   |
| h | Int | 0 |   |
| pl | Int | DEFAULT_PAD |   |
| pr | Int | DEFAULT_PAD |   |
| pt | Int | DEFAULT_PAD |   |
| pb | Int | DEFAULT_PAD |   |

### create()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Create server-side resources.

Reimplemented from FXWindow.

Reimplemented in FXMenuButton, FXOptionMenu, FXToggleButton, and AFXFlyoutButton.

### detach()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Detach server-side resources.

Reimplemented from FXWindow.

Reimplemented in FXMenuButton, FXOptionMenu, FXToggleButton, and AFXFlyoutButton.

### disable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Disable the window.

Reimplemented from FXWindow.

Reimplemented in AFXFlyoutButton.

### enable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Enable the window.

Reimplemented from FXWindow.

Reimplemented in AFXFlyoutButton.

### getDefaultHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default height.

Reimplemented from FXFrame.

Reimplemented in FXCheckButton, FXMDIDeleteButton, FXMDIRestoreButton, FXMDIMaximizeButton, FXMDIMinimizeButton, FXMDIWindowButton, FXMenuButton, FXOption, FXOptionMenu, FXRadioButton, and FXToggleButton.

### getDefaultWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default width.

Reimplemented from FXFrame.

Reimplemented in FXCheckButton, FXMDIDeleteButton, FXMDIRestoreButton, FXMDIMaximizeButton, FXMDIMinimizeButton, FXMDIWindowButton, FXMenuButton, FXOption, FXOptionMenu, FXRadioButton, and FXToggleButton.

### getFont()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get the text font.

### getHelpText()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get the status line help text for this label.

### getIcon()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get the icon for this label.

### getIconPosition()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get the current icon position.

### getJustify()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get the current text-justification mode.

### getText()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get the text for this label.

### getTextColor()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get the current text color.

### getTipText()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get the tool tip message for this label.

### setFont(fnt)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the text font.

| **Argument** | **Type** | **Default** | **Description** |
| fnt | FXFont |   |   |

### setHelpText(text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the status line help text for this label.

Reimplemented in AFXFlyoutItem.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   |   |

### setIcon(ic)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the icon for this label.

Reimplemented in AFXFlyoutItem.

| **Argument** | **Type** | **Default** | **Description** |
| ic | FXIcon |   |   |

### setIconPosition(mode)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the current icon position.

| **Argument** | **Type** | **Default** | **Description** |
| mode | Int |   |   |

### setJustify(mode)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the current text-justification mode.

| **Argument** | **Type** | **Default** | **Description** |
| mode | Int |   |   |

### setText(text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the text for this label.

Reimplemented in AFXFlyoutItem.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   |   |

### setTextColor(clr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the current text color.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor |   |   |

### setTipText(text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the tool tip message for this label.

Reimplemented in AFXFlyoutItem.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   |   |

### Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Relationship options for icon-labels**

| **ICON\_UNDER\_TEXT** | 

Icon appears under text.

 |
| **ICON\_AFTER\_TEXT** | 

Icon appears after text (to its right).

 |
| **ICON\_BEFORE\_TEXT** | 

Icon appears before text (to its left).

 |
| **ICON\_ABOVE\_TEXT** | 

Icon appears above text.

 |
| **ICON\_BELOW\_TEXT** | 

Icon appears below text.

 |
| **TEXT\_OVER\_ICON** | 

Same as ICON\_UNDER\_TEXT.

 |
| **TEXT\_AFTER\_ICON** | 

Same as ICON\_BEFORE\_TEXT.

 |
| **TEXT\_BEFORE\_ICON** | 

Same as ICON\_AFTER\_TEXT.

 |
| **TEXT\_ABOVE\_ICON** | 

Same as ICON\_BELOW\_TEXT.

 |
| **TEXT\_BELOW\_ICON** | 

Same as ICON\_ABOVE\_TEXT.

 |


**Normal way to show label**

| **LABEL_NORMAL** | 

Combination of JUSTIFY\_NORMAL & ICON\_BEFORE_TEXT.

 |