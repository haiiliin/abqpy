This section lists various auxiliary GUI toolkit functions.

### addExitCallback(callback)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Registers a callback function to be called when the application is about to exit.

| **Argument** | **Type** | **Default** | **Description** |
| callback | Function | | The function to be called when the application is about to exit. |

### afxCreateIcon(fileName)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns an icon created by reading the specified file, which can be in one of these formats: BMP, GIF, PNG, XPM. The file format is assumed from the file extension (which is not case sensitive). Returns 0 if the file cannot be opened.

| **Argument** | **Type** | **Default** | **Description** |
| fileName | String | | File name. |

### afxCreateBMPIcon(fileName)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns an icon created by reading the specified file in BMP format. Returns 0 if the file cannot be opened.

| **Argument** | **Type** | **Default** | **Description** |
| fileName | String | | File name. |

### afxCreateGIFIcon(fileName)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns an icon created by reading the specified file in GIF format. Returns 0 if the file cannot be opened.

| **Argument** | **Type** | **Default** | **Description** |
| fileName | String | | File name. |

### afxCreatePNGIcon(fileName)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns an icon created by reading the specified file in PNG format. Returns 0 if the file cannot be opened.

| **Argument** | **Type** | **Default** | **Description** |
| fileName | String | | File name. |

### afxCreateXPMIcon(fileName)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns an icon created by reading the specified file in XPM format. Returns 0 if the file cannot be opened.

| **Argument** | **Type** | **Default** | **Description** |
| fileName | String | | File name. |

### afxGetIcon(fileName, size)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Enables you to use Abaqus/CAE icons in your customization. Set the _size_ argument to 1 for normal-sized icons or to 0 for small icons.

| **Argument** | **Type** | **Default** | **Description** |
| fileName | String | | File name. |
| size | String | | Icon size. |

### displayURL(url)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Displays the specified URL in a web browser. Returns the status of the call. This call will use an open web browser if there is one. This method can be accessed via webBrowser.displayURL from module uti. See also [openWithURL](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAEGUIRefHtml/pt01ch01gob125.htm?contextscope=all#gui-auxiliary-openwithurl).

| **Argument** | **Type** | **Default** | **Description** |
| url | String | | The URL of the page to be displayed. |

### getAFXApp()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the application object.

### getAFXAliasMap().setPrefix(widget, prefix)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the prefix key —usually the dialog box class name—of a widget.

| **Argument** | **Type** | **Default** | **Description** |
| widget | FXWindow | | The widget to which the prefix is being set. |
| prefix | String | | The prefix key for the widget. |

### getAFXAliasMap().setName(widget, name)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the name key of a widget.

| **Argument** | **Type** | **Default** | **Description** |
| widget | FXWindow | | The widget for which the name is being set. The name key is used, along with a prefix, to identify the widget. |
| name | String | | The name of the widget. |

### getAFXFont(opts=FONT_PROPORTIONAL)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the specified font.

| **Argument** | **Type** | **Default** | **Description** |
| opts | Int | FONT_PROPORTIONAL | Type of font to get. Possible choices are FONT_PROPORTIONAL, FONT_MONOSPACE, FONT_REGULAR, FONT_BOLD, FONT_ITALIC, FONT_BASE, or FONT_SMALL. |

### afxGetColorHexSpecFromID(colorId)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the equivalent hex string for the specified color index.

| **Argument** | **Type** | **Default** | **Description** |
| colorId | Integer | | The index of the color to be converted to a hex string. For example, green would be FXRGB(0, 255,0). See the Colors appendix of the Abaqus GUI Toolkit User's Guide for details. |

### afxGetColorHexSpecFromName(colorName)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the equivalent hex string for the specified color name.

| **Argument** | **Type** | **Default** | **Description** |
| colorName | String | | The name of the color to be converted to a hex string. For example, 'Red'. See the Colors appendix of the Abaqus GUI Toolkit User's Guide for details. |

### getCurrentContext()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the current GUI context dictionary, which contains the following keys: _mdbName_, _viewportName_, _objectPath_, _objectType_, _modelName_, and _moduleName_. You can be notified of context changes by using the [registerCurrentContext](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAEGUIRefHtml/pt01ch01gob125.htm?contextscope=all#gui-auxiliary-registercurrentcontext) function.

### getCurrentModuleGui()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the current moduleGui object. You can call that object's getModuleName method to check its name.

### getCursorPosition()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns a tuple of status,x,y,buttonState. The status (TRUE or FALSE) indicates the success of the call. The x and y values represent the position of the cursor in the window's coordinate system (origin is in the upper left, positive Y points downward). This method is defined in FXWindow, so it may be called on any object derived from FXWindow.

### getDisplayedObjectType()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the type of the object displayed in the current viewport. Possible return values are: PART, ASSEMBLY, ODB, XY_PLOT, SKETCH, or None.

### getSeparator(parent, count)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the nth (specified by the count argument) separator widget of the parent.

| **Argument** | **Type** | **Default** | **Description** |
| parent | Widget | | The widget to be searched (children are not traversed). |
| count | Int | | The number of the separator (e.g. specify 2 to get the second separator). |

### getWidgetFromText(parent, text)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns a widget whose label or tip text matches the specified text and is also a child of the specified widget.

| **Argument** | **Type** | **Default** | **Description** |
| parent | Widget | | The widget at which the search begins (children are traversed too). |
| text | String | | The text to be matched (must be an exact match). |

### openWithURL(url)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Displays the specified URL in a web browser. Returns the status of the call. This call will always open a new web browser. This method can be accessed via webBrowser.openWithURL from module uti. See also [displayURL](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAEGUIRefHtml/pt01ch01gob125.htm?contextscope=all#gui-auxiliary-displayurl).

| **Argument** | **Type** | **Default** | **Description** |
| url | String | | The URL of the page to be displayed. |

### registerCurrentContext(callbackFunction)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Registers a query on the current context. The specified callback function will be invoked when the current viewport or displayed object changes. Use the getCurrentContext method to get the values of the current objects. Note that [unregisterCurrentContext](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAEGUIRefHtml/pt01ch01gob125.htm?contextscope=all#gui-auxiliary-unregistercurrentcontext) should be called with the same argument to unregister the query when it is no longer needed.

| **Argument** | **Type** | **Default** | **Description** |
| callbackFunction | Function | | Function to be called when the current context changes. |

### objectPath.registerQuery(callbackFunction, callOnRegister=TRUE)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Registers a query on the object. The specified callback function will be invoked when the object changes. For more information, see “Receiving notification of kernel data changes,” in the Abaqus GUI Toolkit User's Guide. Note that [unregisterQuery](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAEGUIRefHtml/pt01ch01gob125.htm?contextscope=all#gui-auxiliary-unregisterquery) should be called with the same argument to unregister the query when it is no longer needed.

| **Argument** | **Type** | **Default** | **Description** |
| callbackFunction | Function | | Function to be called when the object changes. |
| callOnRegister | Bool | TRUE | If TRUE, the callback function will be called when the query is registered. |

### objectPath.registerInclusive(callbackFunction, callOnRegister=TRUE)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Registers a query on the object and its children. The specified callback function will be invoked when the object or its children change. Note that [unregisterQuery](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAEGUIRefHtml/pt01ch01gob125.htm?contextscope=all#gui-auxiliary-unregisterquery) should be called with the same argument to unregister the query when it is no longer needed.

| **Argument** | **Type** | **Default** | **Description** |
| callbackFunction | Function | | Function to be called when the object or its children change. |
| callOnRegister | Bool | TRUE | If TRUE, the callback function will be called when the query is registered. |

### removeExitCallback(callback)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Unregisters a callback function to be called when the application is about to exit. The function must have been previously registered using addExitCallback.

| **Argument** | **Type** | **Default** | **Description** |
| callback | Function | | The function to be removed from the callback list. |

### sendCommand(writeToJournal, command, writeToReplay=True, writeToJournal=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sends a command string to the kernel.

**Note:** The _writeToJournal_ argument should not usually be necessary. If the command is a built-in Abaqus Scripting Interface command, it will be written to the journal file automatically. If the command is not a built-in Abaqus Scripting Interface command but it changes the mdb using built-in Abaqus Scripting Interface commands, the changes to the mdb will be written to the journal file automatically. However, if the command is not a built-in Abaqus Scripting Interface command and it makes changes to the mdb that would not otherwise be written to the journal file, the command itself should use the journalMethodCall function to write itself to the journal file.

| **Argument** | **Type** | **Default** | **Description** |
| writeToJournal | | | |
| command | String | | Command string. |
| writeToReplay | Bool | True | If True, the command will be written to the replay file. |
| writeToJournal | Bool | False | If True, the command will be written to the journal file. |

### setCurrentModel(modelName)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the current model to the specified model name.

| **Argument** | **Type** | **Default** | **Description** |
| modelName | String | | The name of the model to be made current. |

### setSwitchModuleHook(callbackFunction)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets a function that will be called whenever the user switches into a GUI module. When the user switches into a GUI module, the specified function will be called, passing it the name (shown in the Module combo box) of the new module. Note that the setSwitchModuleHook function does not take keyword arguments and, if necessary, it may be called multiple times.

| **Argument** | **Type** | **Default** | **Description** |
| callbackFunction | Function | | The function to be called when a GUI module is switched into. Note that you cannot issue a kernel command from within this function or it will cause the application to lock up. |

### shutdown()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Exits Abaqus/CAE. This is equivalent to selecting File->Exit.

### switchModule(moduleName)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Switches into a GUI module.

| **Argument** | **Type** | **Default** | **Description** |
| moduleName | String | | Module to switch into. |

### unregisterCurrentContext(callbackFunction)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Unregisters a query on the current context. The specified callback function should be the same argument that was used to register the query.

| **Argument** | **Type** | **Default** | **Description** |
| callbackFunction | Function | | Function to be called when the current context changes. |

### objectPath.unregisterQuery(callbackFunction)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Unregisters a query on the object. The specified callback function should be the same argument that was specified to register the query.

| **Argument** | **Type** | **Default** | **Description** |
| callbackFunction | Function | | Function to be called when the object changes. |
