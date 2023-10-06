from __future__ import annotations

from typing_extensions import Self

from .AFXDialog import AFXDialog
from .FXIcon import FXIcon
from .FXObject import FXObject

#: GUI has no components in standard locations.
GUI_IN_NONE: int = hash("GUI_IN_NONE")

#: GUI has components in the menubar.
GUI_IN_MENUBAR: int = hash("GUI_IN_MENUBAR")

#: GUI has components in the Tools pull down pane.
GUI_IN_TOOL_PANE: int = hash("GUI_IN_TOOL_PANE")

#: GUI has components in the toolbar.
GUI_IN_TOOLBAR: int = hash("GUI_IN_TOOLBAR")

#: GUI has components in the toolbox.
GUI_IN_TOOLBOX: int = hash("GUI_IN_TOOLBOX")


class AFXGuiObjectManager(FXObject):
    """This is a base class for management of GUI components found in the menubar, toolbar, and toolbox."""

    #: Used to destroy dialogs.
    ID_DESTROY_DIALOGS: int = hash("ID_DESTROY_DIALOGS")

    def __init__(self, source: Self):
        """Undefined copy constructor (this class does not have copy semantics).

        Parameters
        ----------
        source : Self
            Object to be copied.
        """

    def getDialog(self, widgetAlias: str):
        """Returns the dialog box with the specified widget key.

        Parameters
        ----------
        widgetAlias : str
            Dialog box alias.
        """

    def getKernelInitializationCommand(self):
        """Returns the command that should initialize the corresponding module or toolset in the kernel.

        Called by the module manager the first time the GUI module is switched into.
        """

    def hide(self, location: int):
        """Hides the GUI components in the menubar, toolbar, and toolbox.

        Parameters
        ----------
        location : int
            Location where GUI components are placed.
        """

    def registerAndShowDialog(self, dialog: AFXDialog):
        """Registers the given dialog box and its widget key with the manager and posts the dialog box.

        Parameters
        ----------
        dialog : AFXDialog
            Dialog box.
        """

    def registerAndShowModalDialog(self, dialog: AFXDialog):
        """Registers the given dialog box and its widget key with the manager and posts the dialog box as a
        modal dialog box.

        Parameters
        ----------
        dialog : AFXDialog
            Dialog box.
        """

    def registerShortcutFunction(
        self,
        text: str,
        tgt: FXObject,
        sel: int,
        ic: FXIcon | None = None,
        tipText: str = "''",
        displayedName: str = "''",
        typesToDisplay: int = 0,
    ):
        """Registers a shortcut function; this function will be available in the GUI so that users can assign it
        shortcut keys.

        Parameters
        ----------
        text : str
            Label used to identify the function in the GUI; To specify a shortcut, separate it from the label using "t".
        tgt : FXObject
            Message target.
        sel : int
            Messaged ID.
        ic : FXIcon | None
            Icon for the shortcut
        tipText : str
            Text used for buttom tooltip
        displayedName : str
            Name of the module to which this function belongs.
        typesToDisplay : int
            Flags specifying the types of objects displayed in the module; see AFXModuleGui.
        """

    def sendCommandString(self, command: str, writeToReplay: bool = True, writeToJournal: bool = False):
        """Sends the given command string (which can contain multiple commands, separated by command
        delimiters).

        Parameters
        ----------
        command : str
            Command string.
        writeToReplay : bool
            True if commands should be written to the replay file; False if not.
        writeToJournal : bool
            True if commands should be written to the journal file; False if not.
        """

    def show(self, location: int):
        """Shows the GUI components in the menubar, toolbar, and toolbox.

        Parameters
        ----------
        location : int
            Location where GUI components are placed.
        """

    def unregisterDialog(self, widgetAlias: str):
        """Unregisters the dialog box of the given widget key from the manager.

        Parameters
        ----------
        widgetAlias : str
            Dialog box alias.
        """
