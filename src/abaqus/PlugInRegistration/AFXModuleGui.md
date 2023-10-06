This is the base class for module GUIs and provides an interface for module GUI management.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxmodulegui.png)

### AFXModuleGui(moduleName, displayTypes)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| moduleName | String |   | Name used to identify this module. |
| displayTypes | Int |   | Types of primary objects that this module may display. |

### activate()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Activates the module during switch processing (allows for module specific activation requirements).

### deactivate()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deactivates the module when switching out (allows for module specific deactivation requirements).

### getModuleName()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the name of the module given on construction.

### getTypesToDisplay()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the type of the primary objects which may be displayed when this module is active (this currently assumes a single type).

### hide(location)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deactivates and hides the module's GUI components in the menubar, toolbar and toolbox.

| **Argument** | **Type** | **Default** | **Description** |
| location | Int |   | Location where gui components are placed. |

### show(location)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Activates and shows the module's GUI components in the menubar, toolbar and toolbox.

| **Argument** | **Type** | **Default** | **Description** |
| location | Int |   | Location where gui components are placed. |

### Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Message ID's.**

| **MISSING ENUMERATOR** | 

MISSING ENUMERATOR DESCRIPTION

 |


**Flags for the object to display.**

| **PART** | 

Displays a part primary object.

 |
| **ASSEMBLY** | 

Displays an assembly primary object.

 |
| **ODB** | 

Displays an ODB primary object.

 |
| **XY_PLOT** | 

Displays an XY plot primary object.

 |
| **SKETCH** | 

Displays a sketch primary object.

 |