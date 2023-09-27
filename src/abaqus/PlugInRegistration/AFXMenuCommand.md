This class provides the interface for creating an FXMenuCommand and performing various management activities on it. It will use utility methods so the menu command is correctly managed for modules and toolsets.

![](../SIMACAERefImages/gui-afxmenucommand.png)

### AFXMenuCommand

###   

### AFXMenuCommand(owner, p, label, ic=None, tgt=None, sel=0)  
![](../IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| owner | AFXGuiObjectManager |   | Creator of the menu command. |
| p | FXComposite |   | Parent widget. |
| label | String |   | Label for the menu button. |
| ic | FXIcon | None | Menu button icon. |
| tgt | FXObject | None | Message target. |
| sel | Int | 0 | Message ID. |

### getOwner

###   

### getOwner()  
![](../IconsReference/butix_top_wline.png)

Returns the owner of the menu command.

Reimplemented from FXWindow.