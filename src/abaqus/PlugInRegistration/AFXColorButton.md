This class contains a label that precedes a color well, which allows the user to bring up a color dialog box by double clicking. When connected to an AFXStringKeyword, this widget will assign the value of the button's current color to the keyword in hex format (for example, "FF0000").

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxcolorbutton.png)

### AFXColorButton(p, text, tgt=None, sel=0, opts=0, x=0, y=0, w=0, h=0, pl=DEFAULT\_SPACING, pr=DEFAULT\_SPACING, pt=DEFAULT\_SPACING, pb=DEFAULT\_SPACING)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   | Parent widget. |
| text | String |   | Label string. |
| tgt | FXObject | None | Message target. |
| sel | Int | 0 | Message ID. |
| opts | Int | 0 | Options and hints. |
| x | Int | 0 | X coordinate of origin. |
| y | Int | 0 | Y coordinate of origin. |
| w | Int | 0 | Width of the widget. |
| h | Int | 0 | Width of the widget. |
| pl | Int | DEFAULT_SPACING | Left padding (margin). |
| pr | Int | DEFAULT_SPACING | Right padding (margin). |
| pt | Int | DEFAULT_SPACING | Top padding (margin). |
| pb | Int | DEFAULT_SPACING | Bottom padding (margin). |

### create()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Creates the color button widget.

Reimplemented from FXComposite.

### disable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Disables the color button.

Reimplemented from FXWindow.

### enable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Enables the color button.

Reimplemented from FXWindow.

### getHelpText()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the status line help text.

### getLabelFont()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the label font.

### getLabelText()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the label string.

### getRGBA()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the color of the button.

### getTipText()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the tool tip message.

### setHelpText(text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the status line help text.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   |   |

### setLabelFont(fnt)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the label font.

| **Argument** | **Type** | **Default** | **Description** |
| fnt | FXFont |   |   |

### setLabelText(txt)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the label string.

| **Argument** | **Type** | **Default** | **Description** |
| txt | String |   |   |

### setRGBA(clr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the color of the button.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor |   |   |

### setTipText(text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the tool tip message.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   |   |

### Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Message ID's.**

| **ID_COLORWELL** | 

ID for color button.

 |

### Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Flags for AFX color button options.**

| **AFXCOLORBUTTON_VERTICAL** | 

Orient label above button.

 |