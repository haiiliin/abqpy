| 

GUI plug-in commands register GUI plug-ins either in the **Plug-ins** menu or in a toolbox.

![](../IconsReference/butix_top_wline.png)

registerGuiMenuButton(...)
--------------------------

Registers a GUI plug-in in the **Plug-ins** menu.

**Path**

toolset.registerGuiMenuButton

**Required arguments**

_object_

> The GUI object to which a (messageId, SEL_COMMAND) message will be sent. The object must have been inherited from FXObject.

_buttonText_

> A String specifying the text to be displayed in the **Plug-ins** menu. Use a pipe ( | ) between words to specify submenus. The default value is the empty string.

**Optional arguments**

_messageId_

> An Int specifying the ID to be used when sending a command to the GUI object. The default value is _AFXMode.ID_ACTIVATE_.

_icon_

> A FXIcon object specifying an icon to be displayed to the left of the text in the menu. For more information, see [afxCreateIcon](pt01ch01gob125.htm?contextscope=all#gui-auxiliary-afxcreateicon) in the “Auxiliary functions” section of this guide. The default value is None.

_kernelInitString_

> A String specifying the string sent to the kernel the first time this plug-in is invoked. The string is intended to initialize the kernel (typically by importing modules) in preparation for commands that will be sent by this plug-in’s GUI. The default value is the empty string.

_applicableModules_

> The SymbolicConstant ALL or a sequence of one or more Strings specifying the list of modules to which this plug-in applies. If a plug-in is not applicable to a module, it will be hidden when the user switches into that module. Possible values of the Strings in the sequence are “Part”, “Property”, “Assembly”, “Step”, “Interaction”, “Load”, “Mesh”, “Job”, “Visualization”, and “Sketch”. The default value is ALL.

_version_

> A String specifying the version of the plug-in. The version is displayed in the **About Plug-ins** dialog box. The default value is “N/A”.

_author_

> A String specifying the author of the plug-in. The author is displayed in the **About Plug-ins** dialog box. The default value is “N/A”.

_description_

> A String specifying the description of the plug-in. The description is displayed in the **About Plug-ins** dialog box. The default value is “N/A”.

_helpUrl_

> A String specifying the universal resource locator (URL) that points to the help for this plug-in. This URL can be loaded in a web browser from the **View** button in the **About Plug-ins** dialog box. The default value is “N/A”.

**Return value**

None

**Exceptions**

None.

![](../IconsReference/butix_top_wline.png)

registerGuiToolButton(...)
--------------------------

Registers a GUI plug-in in a toolbox.

**Path**

toolset.registerGuiToolButton

**Required arguments**

_toolboxName_

> A String specifying the name of the toolbox in which the button will be shown. The name appears in the toolbox title bar.

_object_

> The GUI object to which a (messageId, SEL_COMMAND) message will be sent. The object must have been inherited from FXObject.

**Optional arguments**

_messageId_

> An Int specifying the ID to be used when sending a command to the GUI object. The default value is _AFXMode.ID_ACTIVATE_.

_buttonText_

> A String specifying the text to be displayed in the **Plug-ins** menu. The default value is the empty string.

_icon_

> A FXIcon object specifying an icon to be displayed to the left of the text in the menu. For more information, see [afxCreateIcon](pt01ch01gob125.htm?contextscope=all#gui-auxiliary-afxcreateicon) in the “Auxiliary functions” section of this guide. The default value is None.

_kernelInitString_

> A String specifying the string sent to the kernel the first time this plug-in is invoked. The string is intended to initialize the kernel (typically by importing modules) in preparation for commands that will be sent by this plug-in’s GUI. The default value is the empty string.

_applicableModules_

> The SymbolicConstant ALL or a sequence of one or more Strings specifying the list of modules to which this plug-in applies. If a plug-in is not applicable to a module, it will be hidden when the user switches into that module. Possible values of the Strings in the sequence are “Part”, “Property”, “Assembly”, “Step”, “Interaction”, “Load”, “Mesh”, “Job”, “Visualization”, and “Sketch”. The default value is ALL.

_version_

> A String specifying the version of the plug-in. The version is displayed in the **About Plug-ins** dialog box. The default value is “N/A”.

_author_

> A String specifying the author of the plug-in. The author is displayed in the **About Plug-ins** dialog box. The default value is “N/A”.

_description_

> A String specifying the description of the plug-in. The description is displayed in the **About Plug-ins** dialog box. The default value is “N/A”.

_helpUrl_

> A String specifying the universal resource locator (URL) that points to the help for this plug-in. This URL can be loaded in a web browser from the **View** button in the **About Plug-ins** dialog box. The default value is “N/A”.

**Return value**

None

**Exceptions**

None.



 |