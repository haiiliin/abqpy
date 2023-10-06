| 

This is the base class for toolset GUIs and provides an interface for managing the toolset's GUI items. It provides a mechanism to add in menubar, toolbar, and toolbox GUI items.

![](../SIMACAERefImages/gui-afxtoolsetgui.png)

### AFXToolsetGui

###   

### AFXToolsetGui(toolsetName)  
![](../IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| toolsetName | String |   | Toolset name passed in from derived toolsets. |

### activate

###   

### activate()  
![](../IconsReference/butix_top_wline.png)

Activates the toolset (if there is no mode factory, then this method need not be redefined).

### deactivate

###   

### deactivate()  
![](../IconsReference/butix_top_wline.png)

Deactivates the toolset (if there is no mode factory, then this method need not be redefined).

### getToolsetName

###   

### getToolsetName()  
![](../IconsReference/butix_top_wline.png)

Returns the name of the toolset given on construction.

### hide

###   

### hide(location)  
![](../IconsReference/butix_top_wline.png)

Hides the GUI components in the menubar, toolbar, and toolbox.

| **Argument** | **Type** | **Default** | **Description** |
| location | Int |   | Flags indicating the location where GUI components are placed. Possible values are GUI\_IN\_NONE, GUI\_IN\_MENUBAR, GUI\_IN\_TOOL\_PANE, GUI\_IN\_TOOLBAR, and GUI\_IN_TOOLBOX. |

### show

###   

### show(location)  
![](../IconsReference/butix_top_wline.png)

Shows the GUI components in the menubar, toolbar, and toolbox.

| **Argument** | **Type** | **Default** | **Description** |
| location | Int |   | Flags indicating the location where GUI components are placed. Possible values are GUI\_IN\_NONE, GUI\_IN\_MENUBAR, GUI\_IN\_TOOL\_PANE, GUI\_IN\_TOOLBAR, and GUI\_IN_TOOLBOX. |



 |