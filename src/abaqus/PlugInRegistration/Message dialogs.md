The following methods provide access to the standard message dialogs.

### showAFXDismissableWarningDialog(owner, message, tgt=None, sel=0)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Posts a modal dismissable warning dialog box that has a "Show this dialog next time" check button, via which the user can request not to see a specific type of messages in the future. The dialog box has a getCheckButtonState method that can be called to get the state of the check button in the dialog box.

| **Argument** | **Type** | **Default** | **Description** |
| owner | FXWindow | | Window over which the dialog box is to be centered. |
| message | String | | Text to be displayed in the dialog box. |
| tgt | FXObject | None | Message target. |
| sel | Int | 0 | Message ID. |

### showAFXErrorDialog(owner, message, tgt=None, sel=0)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Shows an error dialog box.

| **Argument** | **Type** | **Default** | **Description** |
| owner | FXWindow | | Window over which the dialog box is to be centered. |
| message | String | | Text to be displayed in the dialog box. |
| tgt | FXObject | None | Message target. |
| sel | Int | 0 | Message ID. |

### showAFXItemsWarningDialog(owner, topMessage, items, bottomMessage, buttonIds=YES|NO|CANCEL, tgt=None, sel=0)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Shows a modal warning dialog box that has a scrollable list of items and two messages: one placed above and one below the list. .

| **Argument** | **Type** | **Default** | **Description** |
| owner | FXWindow | | Window over which the dialog box is to be centered. |
| topMessage | String | | Text to be displayed on top of the list of items. |
| items | String | | A String containing a comma-separated list of items to be displayed between the topMessage and bottomMessage. |
| bottomMessage | String | | Text to be displayed below the list of items. |
| buttonIds | Int | YES|NO|CANCEL | ID's of the action area buttons to be created. |
| tgt | FXObject | None | Message target. |
| sel | Int | 0 | Message ID. |

### showAFXWarningDialog(owner, message, buttonIds=YES|NO|CANCEL, tgt=None, sel=0)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Shows a warning dialog box.

| **Argument** | **Type** | **Default** | **Description** |
| owner | FXWindow | | Window over which the dialog box is to be centered. |
| message | String | | Text to be displayed in the dialog box. |
| buttonIds | Int | YES|NO|CANCEL | ID's of the action area buttons to be created. |
| tgt | FXObject | None | Message target. |
| sel | Int | 0 | Message ID. |

### showAFXInformationDialog(owner, message, tgt=None, sel=0)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Shows an information dialog box.

| **Argument** | **Type** | **Default** | **Description** |
| owner | FXWindow | | Window over which the dialog box is to be centered. |
| message | String | | Text to be displayed in the dialog box. |
| tgt | FXObject | None | Message target. |
| sel | Int | 0 | Message ID. |
