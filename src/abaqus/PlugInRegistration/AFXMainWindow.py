from __future__ import annotations

from .AFXGuiObjectManager import AFXGuiObjectManager
from .AFXMenuPane import AFXMenuPane
from .AFXMenuTitle import AFXMenuTitle
from .AFXTarget import AFXTarget
from .AFXToolsetGui import AFXToolsetGui
from .constants import DECOR_ALL
from .FXApp import FXApp
from .FXIcon import FXIcon
from .FXMainWindow import FXMainWindow
from .FXMenubar import FXMenubar
from .FXSelector import FXSelector
from .FXTabItem import FXTabItem
from .PluginToolset import PluginToolset


class AFXMainWindow(FXMainWindow):
    """This class is responsible for constructing the components of the main window.

    It also provides accessors for the various components constructed.
    """

    #: Used to handle the quit message.
    ID_QUIT: int = hash("ID_QUIT")

    #: Used to handle tabbing.
    ID_TAB: int = hash("ID_TAB")

    #: Toggle the visibility of the model tree.
    ID_TOGGLE_MODEL_TREE: int = hash("ID_TOGGLE_MODEL_TREE")

    #: Toggle full screen.
    ID_TOGGLE_FULL_SCREEN: int = hash("ID_TOGGLE_FULL_SCREEN")

    #: Do not use, do not delete; for use by derived classes.
    ID_LAST: int = hash("ID_LAST")

    def __init__(
        self,
        app: FXApp,
        title: str,
        icon: FXIcon | None = None,
        miniIcon: FXIcon | None = None,
        opts: int = DECOR_ALL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
    ):
        """Constructor.

        Parameters
        ----------
        app : FXApp
            FXApp object.
        title : str
            Main window title.
        icon : FXIcon | None
            Main window icon.
        miniIcon : FXIcon | None
            Minimized icon.
        opts : int
            Main window options.
        x : int
            X location of the main window.
        y : int
            Y location of the main window.
        w : int
            Width of the main window.
        h : int
            Height of the main window.
        """

    def appendApplicableModuleForTreeTab(self, name: str, moduleName: str):
        """Appends a module name to the list of modules to which a tree tab is applicable.

        Parameters
        ----------
        name : str
            Name of the tab item.
        moduleName : str
            Module name to be appended to the list of the tab's applicable modules.
        """

    def appendTreeTab(self, text: str, name: str):
        """Appends a new tab item to the tree toolset tab book and returns a vertical frame managed by the new
        tab item; you must call create() on the vertical frame after you construct all its child widgets.

        Parameters
        ----------
        text : str
            Text to be shown in the new tab item.
        name : str
            Name of the new tab item.
        """

    def appendVisibleModuleForTreeTab(self, name: str, moduleName: str):
        """Appends a module to the list of modules in which a tree tab is visible.

        Parameters
        ----------
        name : str
            Name of the tab item.
        moduleName : str
            Module name to be appended to the list of the tab's modules in which it is visible.
        """

    def create(self):
        """Virtual base class method for creating windowing system resources.

        Reimplemented from FXTopWindow.
        """

    def getContextBar(self):
        """Returns a pointer to the context bar container."""

    def getCurrentTreeTab(self) -> FXTabItem:  # type: ignore
        """Returns the current tab item."""

    def getDefaultHeight(self) -> int:  # type: ignore
        """Returns the default main window height.

        Reimplemented from FXTopWindow.
        """

    def getDefaultWidth(self) -> int:  # type: ignore
        """Returns the default main window width.

        Reimplemented from FXTopWindow.
        """

    def getDisplayedNameAtIndex(self, index: int) -> str:  # type: ignore
        """Returns the displayed name at the given position in the list.

        Parameters
        ----------
        index : int
            Position in the module list.
        """

    def getDrawingAreaHeight(self) -> int:  # type: ignore
        """Returns the height of the drawing area in pixels."""

    def getDrawingAreaWidth(self) -> int:  # type: ignore
        """Returns the width of the drawing area in pixels."""

    def getHelpToolset(self):
        """Returns a pointer to the help toolset."""

    def getMenubar(self) -> FXMenubar:  # type: ignore
        """Returns a pointer to the menubar."""

    def getModule(self, name: str):
        """Returns the module specified by the given name argument.

        Parameters
        ----------
        name : str
            A String that specifies the module to get.
        """

    def getModuleName(self, displayedName: str) -> str:  # type: ignore
        """Returns the module name for the given displayed name.

        Parameters
        ----------
        displayedName : str
            Displayed module name (English).
        """

    def getNumModules(self) -> int:  # type: ignore
        """Returns the number of modules."""

    def getPluginToolset(self) -> PluginToolset:  # type: ignore
        """Returns the Plugin toolset."""

    def getSelectorFromFunction(self, function: str) -> FXSelector:  # type: ignore
        """Returns the selector of the given shortcut function. Throws exception if not found.

        Parameters
        ----------
        function : str
            A String specifying the function as shown in the Customize dialog box.
        """

    def getTargetFromFunction(self, function: str) -> AFXTarget:  # type: ignore
        """Returns the target of the given shortcut function. Throws exception if not found.

        Parameters
        ----------
        function : str
            A String specifying the function as shown in the Customize dialog box.
        """

    def getToolbox(self):
        """Returns a pointer to the module toolbox container."""

    def getToolMenuPane(self) -> AFXMenuPane:  # type: ignore
        """Returns a pointer to the tools menu pane."""

    def getToolMenuTitle(self) -> AFXMenuTitle:  # type: ignore
        """Returns a pointer to the Tools menu title."""

    def getToolset(self, name: str):
        """Returns the toolset specified by the given name argument.

        Parameters
        ----------
        name : str
            A String in the local language that specifies to toolset to get.
        """

    def getToolsetKernelInitializationCommands(self):
        """Returns the command string that should initialize the toolsets in the kernel that are corresponding
        to the toolsets registered with the main window."""

    def getWorkDirectory(self) -> str:  # type: ignore
        """Returns the current working directory."""

    def hideCli(self):
        """Hides the command line interface."""

    def hideMessageArea(self):
        """Hides the message area interface."""

    def makeCustomToolsets(self):
        """This method has no base class implementation; it may be used by customizers to construct Abaqus/CAE
        toolsets or toolsets derived from Abaqus/CAE toolsets; constructing those toolsets in this method is
        necessary to insure that the toolset will be available to standard Abaqus/CAE modules that register that
        toolset, and to avoid creating duplicate widgets when the toolset is used by a custom toolset."""

    def registerHelpToolset(self, tool: AFXToolsetGui, opts: int):
        """Registers the Help toolset.

        Parameters
        ----------
        tool : AFXToolsetGui
            Pointer to toolset being registered.
        opts : int
            Options for creating toolset GUI components.
        """

    def registerModule(self, displayedName: str, moduleImportName: str, kernelInitializationCommand: str):
        """Registers a module to make it available in the module combo; also registers the initialization string
        to be sent to the kernel the first time the module is loaded.

        Parameters
        ----------
        displayedName : str
            The name that will be displayed in the Module combo box in the context bar.
        moduleImportName : str
            The name that will be used to import this module.
        kernelInitializationCommand : str
            The Python command sent to kernel when the module is loaded.
        """

    def registerToolset(self, tool: AFXGuiObjectManager, opts: int):
        """Registers a toolset that is always available in the main window.

        Parameters
        ----------
        tool : AFXGuiObjectManager
            Pointer to the object being registered.
        opts : int
            Options for creating toolset GUI components.
        """

    def setApplicabilityForTreeTab(self, name: str, moduleNames: str):
        """Sets the modules that are applicable to the given tree tab. When switching modules, if the current
        tab is applicable to the new module, it will remain current. When a tree tab is created, it is
        applicable to all modules--use this method to set the applicability to only certain modules.

        Parameters
        ----------
        name : str
            Name of the tab item.
        moduleNames : str
            A String containing module names separated by commas.
        """

    def setCurrentTreeTab(self, name: str):
        """Sets the tree toolset tab book's current tab item to the tab item specified by the given name.

        Parameters
        ----------
        name : str
            Name of the tab item to be set current.
        """

    def setVisibilityForTreeTab(self, name: str, moduleNames: str):
        """Sets the modules in which a tree tab is visible. When switching modules, if the tab has not been
        specified to be visible in the new module, the tab will be hidden; otherwise it will be shown. When a
        tree tab is created it is visible in all modules--use this method to set the visibility to only certain
        modules.

        Parameters
        ----------
        name : str
            Name of the tab item.
        moduleNames : str
            A String containing module names separated by commas.
        """

    def setWorkDirectory(self, directory: str):
        """Sets the current working directory.

        Parameters
        ----------
        directory : str
            A String specifying the new work directory.
        """

    def showCli(self):
        """Shows the command line interface."""

    def showMessageArea(self):
        """Shows the message area interface."""

    def writeToMessageArea(self, message: str):
        """Writes a string to the message area.

        Parameters
        ----------
        message : str
        """
