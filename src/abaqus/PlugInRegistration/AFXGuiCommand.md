This class is designed for the GUI commands processed by modes.

![](../SIMACAERefImages/gui-afxguicommand.png)

### AFXGuiCommand

###

### AFXGuiCommand(mode, method, objectName='', registerQuery=False)

![](../IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| mode | AFXGuiMode | | Host mode. |
| method | String | | Method. |
| objectName | String | '' | Object name. |
| registerQuery | Bool | False | True if a query should be registered so that the command's keyword values can be updated based on the kernel state. |

### getMode

###

### getMode()

![](../IconsReference/butix_top_wline.png)

Retrieves the command's mode.

|
