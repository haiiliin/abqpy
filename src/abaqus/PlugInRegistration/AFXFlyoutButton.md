This class contains a button that acts like a regular FXButton when pressed and released quickly but displays a popup menu when pressed and held for a short time duration.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxflyoutbutton.png)

### AFXFlyoutButton(p, pup=None, act=0, opts=AFXFLYOUT_NORMAL, x=0, y=0, w=0, h=0, pl=0, pr=0, pt=0, pb=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   | Parent widget. |
| pup | FXPopup | None | Popup containing flyout items. |
| act | Int | 0 | Current button index (0-based). |
| opts | Int | AFXFLYOUT_NORMAL | Options and hints. |
| x | Int | 0 | X coordinate of origin. |
| y | Int | 0 | Y coordinate of origin. |
| w | Int | 0 | Width of the widget. |
| h | Int | 0 | Height of the widget. |
| pl | Int | 0 | Left padding (margin). |
| pr | Int | 0 | Right padding (margin). |
| pt | Int | 0 | Top padding (margin). |
| pb | Int | 0 | Bottom padding (margin). |

### canFocus()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True (because a flyout button can receive focus).

Reimplemented from FXWindow.

### create()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Creates the flyout button.

Reimplemented from FXLabel.

### detach()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Detaches server-side resources for the flyout button.

Reimplemented from FXLabel.

### disable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Disables the flyout button.

Reimplemented from FXLabel.

### enable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Enables the flyout button.

Reimplemented from FXLabel.

### getButtonStyle()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the flyout button style.

### getCurrentItem()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the current item.

### getPane()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the popup menu.

### getState()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the flyout button state.

### setButtonStyle(style)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the flyout button style.

| **Argument** | **Type** | **Default** | **Description** |
| style | Int |   | Button style (see Flags for flyout button options.) |

### setCurrentItem(item)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the current item.

| **Argument** | **Type** | **Default** | **Description** |
| item | AFXFlyoutItem |   | Item. |

### setCurrentItem(index, setCheck=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the current item and depresses the button if setCheck is True. The specified item index is 0-based, and only valid items are counted (items such as separators are not counted).

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Index. |
| setCheck | Bool | False | Value of check button. |

### setPane(pup)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the popup menu.

| **Argument** | **Type** | **Default** | **Description** |
| pup | FXPopup |   | Popup menu. |

### setState(state)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the flyout button state.

| **Argument** | **Type** | **Default** | **Description** |
| state | Int |   | State (see FXButton's Button state bits). |

### Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Message ID's.**

| **ID\_AFXFLYOUT\_TIMER** | 

ID for the popup timer.

 |
| **ID\_HIDE\_ITEM** | 

ID used when hiding flyout item.

 |

### Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Flags for flyout button options.**

| **AFXFLYOUT_AUTOGRAY** | 

Automatically gray out when no target.

 |
| **AFXFLYOUT_AUTOHIDE** | 

Automatically hide when no target.

 |
| **AFXFLYOUT_TOOLBAR** | 

Toolbar style button.

 |
| **AFXFLYOUT_HORIZONTAL** | 

Popup horizontal.

 |
| **AFXFLYOUT_VERTICAL** | 

Popup vertical.

 |
| **AFXFLYOUT_RADIO** | 

Current item is always active.

 |