This is a base class for management of GUI components found in the menubar, toolbar, and toolbox.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxguiobjectmanager.png)

### AFXGuiObjectManager()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

### AFXGuiObjectManager(source)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Undefined copy constructor (this class does not have copy semantics).

| **Argument** | **Type** | **Default** | **Description** |
| source | AFXGuiObjectManager | | Object to be copied. |

### getDialog(widgetAlias)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the dialog box with the specified widget key.

| **Argument** | **Type** | **Default** | **Description** |
| widgetAlias | String | | Dialog box alias. |

### getKernelInitializationCommand()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the command that should initialize the corresponding module or toolset in the kernel. Called by the module manager the first time the GUI module is switched into.

### hide(location)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Hides the GUI components in the menubar, toolbar, and toolbox.

| **Argument** | **Type** | **Default** | **Description** |
| location | Int | | Location where GUI components are placed. |

### registerAndShowDialog(dialog)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Registers the given dialog box and its widget key with the manager and posts the dialog box.

| **Argument** | **Type** | **Default** | **Description** |
| dialog | AFXDialog | | Dialog box. |

### registerAndShowModalDialog(dialog)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Registers the given dialog box and its widget key with the manager and posts the dialog box as a modal dialog box.

| **Argument** | **Type** | **Default** | **Description** |
| dialog | AFXDialog | | Dialog box. |

### registerShortcutFunction(text, tgt, sel, ic=None, tipText='', displayedName='', typesToDisplay=0)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Registers a shortcut function; this function will be available in the GUI so that users can assign it shortcut keys.

| **Argument** | **Type** | **Default** | **Description** |
| text | String | | Label used to identify the function in the GUI; To specify a shortcut, separate it from the label using "\\t". |
| tgt | FXObject | | Message target. |
| sel | Int | | Messaged ID. |
| ic | FXIcon | None | Icon for the shortcut |
| tipText | String | '' | Text used for buttom tooltip |
| displayedName | String | '' | Name of the module to which this function belongs. |
| typesToDisplay | Int | 0 | Flags specifying the types of objects displayed in the module; see AFXModuleGui. |

### sendCommandString(command, writeToReplay=True, writeToJournal=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sends the given command string (which can contain multiple commands, separated by command delimiters).

| **Argument** | **Type** | **Default** | **Description** |
| command | String | | Command string. |
| writeToReplay | Bool | True | True if commands should be written to the replay file; False if not. |
| writeToJournal | Bool | False | True if commands should be written to the journal file; False if not. |

### show(location)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Shows the GUI components in the menubar, toolbar, and toolbox.

| **Argument** | **Type** | **Default** | **Description** |
| location | Int | | Location where GUI components are placed. |

### unregisterDialog(widgetAlias)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Unregisters the dialog box of the given widget key from the manager.

| **Argument** | **Type** | **Default** | **Description** |
| widgetAlias | String | | Dialog box alias. |

### Class flags

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

**Message ID's.**

| **ID_DESTROY_DIALOGS** |

Used to destroy dialogs.

|

### Global flags

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

**Flags for GUI locations.**

| **GUI_IN_NONE** |

GUI has no components in standard locations.

|
| **GUI_IN_MENUBAR** |

GUI has components in the menubar.

|
| **GUI_IN_TOOL_PANE** |

GUI has components in the Tools pull down pane.

|
| **GUI_IN_TOOLBAR** |

GUI has components in the toolbar.

|
| **GUI_IN_TOOLBOX** |

GUI has components in the toolbox.

|
