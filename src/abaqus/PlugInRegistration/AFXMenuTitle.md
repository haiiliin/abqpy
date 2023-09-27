| 

This class provides the interface for creating an FXMenuTitle and performing various management activities on it. It will use utility methods so the menu title is correctly managed for modules and procedure toolsets.

![](../SIMACAERefImages/gui-afxmenutitle.png)

### AFXMenuTitle

###   

### AFXMenuTitle(owner, label, ic=None, popup=None)  
![](../IconsReference/butix_top_wline.png)

Constructor that takes an owner.

| **Argument** | **Type** | **Default** | **Description** |
| owner | AFXGuiObjectManager |   | Owner (module or toolset GUI). |
| label | String |   | Label string. |
| ic | FXIcon | None | Icon. |
| popup | FXPopup | None | Pulldown menu. |

### AFXMenuTitle

###   

### AFXMenuTitle(parent, label, ic=None, popup=None)  
![](../IconsReference/butix_top_wline.png)

Constructor that takes a parent.

| **Argument** | **Type** | **Default** | **Description** |
| parent | FXComposite |   | Parent widget. |
| label | String |   | Label string. |
| ic | FXIcon | None | Icon. |
| popup | FXPopup | None | Pulldown menu. |

### getOwner

###   

### getOwner()  
![](../IconsReference/butix_top_wline.png)

Returns the owner of the menu title.

Reimplemented from FXWindow.

### hide

###   

### hide()  
![](../IconsReference/butix_top_wline.png)

Hides the widget.

Reimplemented from FXWindow.

### show

###   

### show()  
![](../IconsReference/butix_top_wline.png)

Shows the widget.

Reimplemented from FXWindow.



 |