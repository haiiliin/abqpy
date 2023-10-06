This class is responsible for constructing the components of the main window. It also provides accessors for the various components constructed.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxmainwindow.png)

### AFXMainWindow(app, title, icon=None, miniIcon=None, opts=DECOR_ALL, x=0, y=0, w=0, h=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| app | FXApp |   | FXApp object. |
| title | String |   | Main window title. |
| icon | FXIcon | None | Main window icon. |
| miniIcon | FXIcon | None | Minimized icon. |
| opts | Int | DECOR_ALL | Main window options. |
| x | Int | 0 | X location of the main window. |
| y | Int | 0 | Y location of the main window. |
| w | Int | 0 | Width of the main window. |
| h | Int | 0 | Height of the main window. |

### appendApplicableModuleForTreeTab(name, moduleName)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Appends a module name to the list of modules to which a tree tab is applicable.

| **Argument** | **Type** | **Default** | **Description** |
| name | String |   | Name of the tab item. |
| moduleName | String |   | Module name to be appended to the list of the tab's applicable modules. |

### appendTreeTab(text, name)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Appends a new tab item to the tree toolset tab book and returns a vertical frame managed by the new tab item; you must call create() on the vertical frame after you construct all its child widgets.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   | Text to be shown in the new tab item. |
| name | String |   | Name of the new tab item. |

### appendVisibleModuleForTreeTab(name, moduleName)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Appends a module to the list of modules in which a tree tab is visible.

| **Argument** | **Type** | **Default** | **Description** |
| name | String |   | Name of the tab item. |
| moduleName | String |   | Module name to be appended to the list of the tab's modules in which it is visible. |

### create()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Virtual base class method for creating windowing system resources.

Reimplemented from FXTopWindow.

### getContextBar()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns a pointer to the context bar container.

### getCurrentTreeTab()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the current tab item.

### getDefaultHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default main window height.

Reimplemented from FXTopWindow.

### getDefaultWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default main window width.

Reimplemented from FXTopWindow.

### getDisplayedNameAtIndex(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the displayed name at the given position in the list.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Position in the module list. |

### getDrawingAreaHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the height of the drawing area in pixels.

### getDrawingAreaWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the width of the drawing area in pixels.

### getHelpToolset()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns a pointer to the help toolset.

### getMenubar()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns a pointer to the menubar.

### getModule(name)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the module specified by the given name argument.

| **Argument** | **Type** | **Default** | **Description** |
| name | String |   | A String that specifies the module to get. |

### getModuleName(displayedName)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the module name for the given displayed name.

| **Argument** | **Type** | **Default** | **Description** |
| displayedName | String |   | Displayed module name (English). |

### getNumModules()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of modules.

### getPluginToolset()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the Plugin toolset.

### getSelectorFromFunction(function)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the selector of the given shortcut function. Throws exception if not found.

| **Argument** | **Type** | **Default** | **Description** |
| function | String |   | A String specifying the function as shown in the Customize dialog box. |

### getTargetFromFunction(function)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the target of the given shortcut function. Throws exception if not found.

| **Argument** | **Type** | **Default** | **Description** |
| function | String |   | A String specifying the function as shown in the Customize dialog box. |

### getToolbox()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns a pointer to the module toolbox container.

### getToolMenuPane()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns a pointer to the tools menu pane.

### getToolMenuTitle()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns a pointer to the Tools menu title.

### getToolset(name)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the toolset specified by the given name argument.

| **Argument** | **Type** | **Default** | **Description** |
| name | String |   | A String in the local language that specifies to toolset to get. |

### getToolsetKernelInitializationCommands()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the command string that should initialize the toolsets in the kernel that are corresponding to the toolsets registered with the main window.

### getWorkDirectory()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the current working directory.

### hideCli()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Hides the command line interface.

### hideMessageArea()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Hides the message area interface.

### makeCustomToolsets()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

This method has no base class implementation; it may be used by customizers to construct Abaqus/CAE toolsets or toolsets derived from Abaqus/CAE toolsets; constructing those toolsets in this method is necessary to insure that the toolset will be available to standard Abaqus/CAE modules that register that toolset, and to avoid creating duplicate widgets when the toolset is used by a custom toolset.

### registerHelpToolset(tool, opts)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Registers the Help toolset.

| **Argument** | **Type** | **Default** | **Description** |
| tool | AFXToolsetGui |   | Pointer to toolset being registered. |
| opts | Int |   | Options for creating toolset GUI components. |

### registerModule(displayedName, moduleImportName)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Registers a module to make it available in the module combo; Uses predefined initialization strings for Abaqus modules.

| **Argument** | **Type** | **Default** | **Description** |
| displayedName | String |   | The name that will be displayed in the Module combo box in the context bar. |
| moduleImportName | String |   | The name that will be used to import this module. |

### registerModule(displayedName, moduleImportName, kernelInitializationCommand)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Registers a module to make it available in the module combo; also registers the initialization string to be sent to the kernel the first time the module is loaded.

| **Argument** | **Type** | **Default** | **Description** |
| displayedName | String |   | The name that will be displayed in the Module combo box in the context bar. |
| moduleImportName | String |   | The name that will be used to import this module. |
| kernelInitializationCommand | String |   | The Python command sent to kernel when the module is loaded. |

### registerToolset(tool, opts)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Registers a toolset that is always available in the main window.

| **Argument** | **Type** | **Default** | **Description** |
| tool | AFXGuiObjectManager |   | Pointer to the object being registered. |
| opts | Int |   | Options for creating toolset GUI components. |

### setApplicabilityForTreeTab(name, moduleNames)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the modules that are applicable to the given tree tab. When switching modules, if the current tab is applicable to the new module, it will remain current. When a tree tab is created, it is applicable to all modules--use this method to set the applicability to only certain modules.

| **Argument** | **Type** | **Default** | **Description** |
| name | String |   | Name of the tab item. |
| moduleNames | String |   | A String containing module names separated by commas. |

### setCurrentTreeTab(name)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the tree toolset tab book's current tab item to the tab item specified by the given name.

| **Argument** | **Type** | **Default** | **Description** |
| name | String |   | Name of the tab item to be set current. |

### setVisibilityForTreeTab(name, moduleNames)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the modules in which a tree tab is visible. When switching modules, if the tab has not been specified to be visible in the new module, the tab will be hidden; otherwise it will be shown. When a tree tab is created it is visible in all modules--use this method to set the visibility to only certain modules.

| **Argument** | **Type** | **Default** | **Description** |
| name | String |   | Name of the tab item. |
| moduleNames | String |   | A String containing module names separated by commas. |

### setWorkDirectory(directory)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the current working directory.

| **Argument** | **Type** | **Default** | **Description** |
| directory | String |   | A String specifying the new work directory. |

### showCli()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Shows the command line interface.

### showMessageArea()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Shows the message area interface.

### writeToMessageArea(message)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Writes a string to the message area.

| **Argument** | **Type** | **Default** | **Description** |
| message | String |   |   |

### Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Message ID's.**

| **ID_QUIT** | 

Used to handle the quit message.

 |
| **ID_TAB** | 

Used to handle tabbing.

 |
| **ID\_TOGGLE\_MODEL_TREE** | 

Toggle the visibility of the model tree.

 |
| **ID\_TOGGLE\_FULL_SCREEN** | 

Toggle full screen.

 |
| **ID_LAST** | 

Do not use, do not delete; for use by derived classes.

 |