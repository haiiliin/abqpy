"""Kernel plug-in commands register kernel plug-ins in either the **Plug-ins** menu or in a toolbox.

These functions can be accessed by::

    from abaqusGui import getAFXApp
    toolset=getAFXApp().getAFXMainWindow().getPluginToolset()
"""

from typing import Sequence

from ..UtilityAndView.abaqusConstants import ALL, SymbolicConstant
from .FXIcon import FXIcon
from .PluginToolsetBase import PluginToolsetBase


class KernelPluginToolset(PluginToolsetBase):
    def registerKernelMenuButton(
        self,
        moduleName: str,
        functionName: str,
        buttonText: str = "",
        icon: FXIcon | None = None,
        applicableModules: SymbolicConstant | Sequence[str] = ALL,
        version: str = "N/A",
        author: str = "N/A",
        description: str = "N/A",
        helpUrl: str = "N/A",
    ):
        """Registers a kernel plug-in in the Plug-ins menu.

        Parameters
        ----------
        moduleName : str
            A String specifying the name of the module to be imported. The module must contain the function to be executed.
        functionName : str
            A String specifying the name of the function to be executed. The function must be located in moduleName.
        buttonText : str, optional
            A String specifying the text to be displayed in the Plug-ins menu. Use a pipe ( | ) between words to specify
            submenus. The default value is the empty string.
        icon : str, optional
            A FXIcon object specifying an icon to be displayed to the left of the text in the menu. For more information,
            see afxCreateIcon in the “Auxiliary functions” section of this guide. The default value is None.
        applicableModules : str, optional
            The SymbolicConstant ALL or a sequence of one or more Strings specifying the list of modules to which this
            plug-in applies. If a plug-in is not applicable to a module, it will be hidden when the user switches into that
            module. Possible values of the Strings in the sequence are “Part”, “Property”, “Assembly”, “Step”,
            “Interaction”, “Load”, “Mesh”, “Job”, “Visualization”, and “Sketch”. The default value is ALL.
        version : str, optional
            A String specifying the version of the plug-in. The version is displayed in the About Plug-ins dialog box.
            The default value is “N/A”.
        author : str, optional
            A String specifying the author of the plug-in. The author is displayed in the About Plug-ins dialog box.
            The default value is “N/A”.
        description : str, optional
            A String specifying the description of the plug-in. The description is displayed in the About Plug-ins dialog
            box. The default value is “N/A”.
        helpUrl : str, optional
            A String specifying the universal resource locator (URL) that points to the help for this plug-in. This URL can
            be loaded in a web browser from the View button in the About Plug-ins dialog box. The default value is “N/A”.
        """

    def registerKernelToolButton(
        self,
        toolboxName: str,
        moduleName: str,
        functionName: str,
        buttonText: str = "",
        icon: FXIcon | None = None,
        applicableModules: SymbolicConstant | Sequence[str] = ALL,
        version: str = "N/A",
        author: str = "N/A",
        description: str = "N/A",
        helpUrl: str = "N/A",
    ):
        """Registers a kernel plug-in in a toolbox.

        Parameters
        ----------
        toolboxName : str
            A String specifying the name of the toolbox in which the button will be shown. The name appears in the toolbox
            title bar.
        moduleName : str
            A String specifying the name of the module to be imported. The module must contain the function to be executed.
        functionName : str
            A String specifying the name of the function to be executed. The function must be located in _moduleName_.
        buttonText : str, optional
            A String specifying the text to be displayed in the Plug-ins menu. The default value is the empty string.
        icon : str, optional
            A FXIcon object specifying an icon to be displayed to the left of the text in the menu. For more information,
            see afxCreateIcon in the “Auxiliary functions” section of this guide. The default value is None.
        applicableModules : str, optional
            The SymbolicConstant ALL or a sequence of one or more Strings specifying the list of modules to which this
            plug-in applies. If a plug-in is not applicable to a module, it will be hidden when the user switches into that
            module. Possible values of the Strings in the sequence are “Part”, “Property”, “Assembly”, “Step”,
            “Interaction”, “Load”, “Mesh”, “Job”, “Visualization”, and “Sketch”. The default value is ALL.
        version : str, optional
            A String specifying the version of the plug-in. The version is displayed in the About Plug-ins dialog box.
            The default value is “N/A”.
        author : str, optional
            A String specifying the author of the plug-in. The author is displayed in the About Plug-ins dialog box. The
            default value is “N/A”.
        description : str, optional
            A String specifying the description of the plug-in. The description is displayed in the About Plug-ins dialog
            box. The default value is “N/A”.
        helpUrl : str, optional
            A String specifying the universal resource locator (URL) that points to the help for this plug-in. This URL can
            be loaded in a web browser from the View button in the About Plug-ins dialog box. The default value is “N/A”.
        """
