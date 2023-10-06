Kernel plug-in commands register kernel plug-ins in either the **Plug-ins** menu or in a toolbox.

**Access**

from abaqusGui import getAFXApp
toolset=getAFXApp().getAFXMainWindow().getPluginToolset()

![](../IconsReference/butix_top_wline.png)

registerKernelMenuButton(...)
-----------------------------

This method registers a kernel plug-in in the **Plug-ins** menu.

**Path**

toolset.registerKernelMenuButton

**Required arguments**

_moduleName_

> A String specifying the name of the module to be imported. The module must contain the function to be executed.

_functionName_

> A String specifying the name of the function to be executed. The function must be located in _moduleName_.

_buttonText_

> A String specifying the text to be displayed in the **Plug-ins** menu. Use a pipe ( | ) between words to specify submenus. The default value is the empty string.

**Optional arguments**

_icon_

> A FXIcon object specifying an icon to be displayed to the left of the text in the menu. For more information, see [afxCreateIcon](pt01ch01gob125.htm?contextscope=all#gui-auxiliary-afxcreateicon) in the “Auxiliary functions” section of this guide. The default value is None.

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

registerKernelToolButton(...)
-----------------------------

Registers a kernel plug-in in a toolbox.

**Path**

toolset.registerKernelToolButton

**Required arguments**

_toolboxName_

> A String specifying the name of the toolbox in which the button will be shown. The name appears in the toolbox title bar.

_moduleName_

> A String specifying the name of the module to be imported. The module must contain the function to be executed.

_functionName_

> A String specifying the name of the function to be executed. The function must be located in _moduleName_.

**Optional arguments**

_buttonText_

> A String specifying the text to be displayed in the **Plug-ins** menu. The default value is the empty string.

_icon_

> A FXIcon object specifying an icon to be displayed to the left of the text in the menu. For more information, see [afxCreateIcon](pt01ch01gob125.htm?contextscope=all#gui-auxiliary-afxcreateicon) in the “Auxiliary functions” section of this guide. The default value is None.

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