"""GUI plug-in commands register GUI plug-ins either in the **Plug-ins** menu or in a toolbox."""

from typing import Sequence

from ..UtilityAndView.abaqusConstants import ALL, SymbolicConstant
from .AFXMode import AFXMode
from .FXIcon import FXIcon
from .FXObject import FXObject
from .PluginToolsetBase import PluginToolsetBase


class GUIPluginToolset(PluginToolsetBase):
    def registerGuiMenuButton(
        self,
        object: FXObject,
        buttonText: str = "",
        messageId: int = AFXMode.ID_ACTIVATE,
        icon: FXIcon | None = None,
        kernelInitString: str = "",
        applicableModules: SymbolicConstant | Sequence[str] = ALL,
        version: str = "N/A",
        author: str = "N/A",
        description: str = "N/A",
        helpUrl: str = "N/A",
    ):
        """Registers a GUI plug-in in the **Plug-ins** menu.

        Parameters
        ----------
        object : FXObject
            The GUI object to which a (messageId, SEL_COMMAND) message will be sent. The object must have been inherited
            from FXObject.
        buttonText : str, optional
            A String specifying the text to be displayed in the **Plug-ins** menu. Use a pipe ( | ) between words to specify
            submenus. The default value is the empty string.
        messageId : int, optional
            An Int specifying the ID to be used when sending a command to the GUI object. The default value is
            _AFXMode.ID_ACTIVATE_.
        icon : FXIcon, optional
            A FXIcon object specifying an icon to be displayed to the left of the text in the menu. For more information,
            see [afxCreateIcon](pt01ch01gob125.htm?contextscope=all#gui-auxiliary-afxcreateicon) in the
            “Auxiliary functions” section of this guide. The default value is None.
        kernelInitString : str, optional
            A String specifying the string sent to the kernel the first time this plug-in is invoked. The string is intended
            to initialize the kernel (typically by importing modules) in preparation for commands that will be sent by this
            plug-in’s GUI. The default value is the empty string.
        applicableModules : SymbolicConstant | Sequence[str], optional
            The SymbolicConstant ALL or a sequence of one or more Strings specifying the list of modules to which this
            plug-in applies. If a plug-in is not applicable to a module, it will be hidden when the user switches into that
            module. Possible values of the Strings in the sequence are “Part”, “Property”, “Assembly”, “Step”,
            “Interaction”, “Load”, “Mesh”, “Job”, “Visualization”, and “Sketch”. The default value is ALL.
        version : str, optional
            A String specifying the version of the plug-in. The version is displayed in the **About Plug-ins** dialog box.
            The default value is “N/A”.
        author : str, optional
            A String specifying the author of the plug-in. The author is displayed in the **About Plug-ins** dialog box.
            The default value is “N/A”.
        description : str, optional
            A String specifying the description of the plug-in. The description is displayed in the **About Plug-ins**
            dialog box. The default value is “N/A”.
        helpUrl : str, optional
            A String specifying the universal resource locator (URL) that points to the help for this plug-in. This URL can
            be loaded in a web browser from the **View** button in the **About Plug-ins** dialog box. The default value is
            “N/A”.
        """

    def registerGuiToolButton(
        self,
        toolboxName: str,
        object: FXObject,
        messageId: int = AFXMode.ID_ACTIVATE,
        buttonText: str = "",
        icon: FXIcon | None = None,
        kernelInitString: str = "",
        applicableModules: SymbolicConstant | Sequence[str] = ALL,
        version: str = "N/A",
        author: str = "N/A",
        description: str = "N/A",
        helpUrl: str = "N/A",
    ):
        """Registers a GUI plug-in in a toolbox.

        Parameters
        ----------
        toolboxName : str
            A String specifying the name of the toolbox in which the button will be shown. The name appears in the toolbox
            title bar.
        object : FXObject
            The GUI object to which a (messageId, SEL_COMMAND) message will be sent. The object must have been inherited
            from FXObject.
        messageId : int, optional
            An Int specifying the ID to be used when sending a command to the GUI object. The default value is
            _AFXMode.ID_ACTIVATE_.
        buttonText : str, optional
            A String specifying the text to be displayed in the **Plug-ins** menu. The default value is the empty string.
        icon : FXIcon, optional
            A FXIcon object specifying an icon to be displayed to the left of the text in the menu. For more information,
            see [afxCreateIcon](pt01ch01gob125.htm?contextscope=all#gui-auxiliary-afxcreateicon) in the
            “Auxiliary functions” section of this guide. The default value is None.
        kernelInitString : str, optional
            A String specifying the string sent to the kernel the first time this plug-in is invoked. The string is intended
            to initialize the kernel (typically by importing modules) in preparation for commands that will be sent by this
            plug-in’s GUI. The default value is the empty string.
        applicableModules : SymbolicConstant | Sequence[str], optional
            The SymbolicConstant ALL or a sequence of one or more Strings specifying the list of modules to which this
            plug-in applies. If a plug-in is not applicable to a module, it will be hidden when the user switches into that
            module. Possible values of the Strings in the sequence are “Part”, “Property”, “Assembly”, “Step”,
            “Interaction”, “Load”, “Mesh”, “Job”, “Visualization”, and “Sketch”. The default value is ALL.
        version : str, optional
            A String specifying the version of the plug-in. The version is displayed in the **About Plug-ins** dialog box.
            The default value is “N/A”.
        author : str, optional
            A String specifying the author of the plug-in. The author is displayed in the **About Plug-ins** dialog box.
            The default value is “N/A”.
        description : str, optional
            A String specifying the description of the plug-in. The description is displayed in the **About Plug-ins**
            dialog box. The default value is “N/A”.
        helpUrl : str, optional
            A String specifying the universal resource locator (URL) that points to the help for this plug-in. This URL can
            be loaded in a web browser from the **View** button in the **About Plug-ins** dialog box. The default value is
            “N/A”.
        """
