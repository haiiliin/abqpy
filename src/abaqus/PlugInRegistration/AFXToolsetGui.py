from __future__ import annotations

from .AFXGuiObjectManager import AFXGuiObjectManager


class AFXToolsetGui(AFXGuiObjectManager):
    """This is the base class for toolset GUIs and provides an interface for managing the toolset's GUI items.

    It provides a mechanism to add in menubar, toolbar, and toolbox GUI items.
    """

    def __init__(self, toolsetName: str):
        """Constructor.

        Parameters
        ----------
        toolsetName : str
            Toolset name passed in from derived toolsets.
        """

    def activate(self):
        """Activates the toolset (if there is no mode factory, then this method need not be redefined)."""

    def deactivate(self):
        """Deactivates the toolset (if there is no mode factory, then this method need not be redefined)."""

    def getToolsetName(self):
        """Returns the name of the toolset given on construction."""

    def hide(self, location: int):
        """Hides the GUI components in the menubar, toolbar, and toolbox.

        Parameters
        ----------
        location : int
            Flags indicating the location where GUI components are placed. Possible values are GUI_IN_NONE, GUI_IN_MENUBAR, GUI_IN_TOOL_PANE, GUI_IN_TOOLBAR, and GUI_IN_TOOLBOX.
        """

    def show(self, location: int):
        """Shows the GUI components in the menubar, toolbar, and toolbox.

        Parameters
        ----------
        location : int
            Flags indicating the location where GUI components are placed. Possible values are GUI_IN_NONE, GUI_IN_MENUBAR, GUI_IN_TOOL_PANE, GUI_IN_TOOLBAR, and GUI_IN_TOOLBOX.
        """
