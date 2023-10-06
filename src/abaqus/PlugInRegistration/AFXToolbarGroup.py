from __future__ import annotations

from .AFXGuiObjectManager import AFXGuiObjectManager
from .FXToolbar import FXToolbar


class AFXToolbarGroup(FXToolbar):
    """This class creates a container to be used for groups in the toolbar.

    It creates a vertical separator after the group. It will use utility methods so the group is correctly
    managed.
    """

    def __init__(self, owner: AFXGuiObjectManager, name: str = "''", title: str = "''"):
        """Constructor.

        Parameters
        ----------
        owner : AFXGuiObjectManager
            Creator of the group.
        name : str
            English toolset name.
        title : str
            Name appearing in the title bar when the group is floating.
        """

    def getDefaultHeight(self):
        """Returns the default height.

        Reimplemented from FXToolbar.
        """

    def getDefaultWidth(self):
        """Returns the default width.

        Reimplemented from FXToolbar.
        """

    def getName(self):
        """Returns the English identifier for the group."""

    def getOwner(self):
        """Returns the creator of the group.

        Reimplemented from FXWindow.
        """

    def getTitle(self):
        """Returns the name appearing in the title bar when the group is floating."""

    def hide(self):
        """Hide this window.

        Reimplemented from FXWindow. Reimplemented in AFXToolbarGroupRender, and AFXToolbarGroupVisibility.
        """

    def isActive(self):
        """Return True if the window is active.

        Reimplemented from FXWindow.
        """

    def layout(self):
        """Calculates layout.

        Reimplemented from FXToolbar.
        """

    def setName(self, name: str):
        """Sets the English identifier for the group.

        Parameters
        ----------
        name : str
        """

    def setTitle(self, title: str):
        """Sets the name appearing in the title bar when the group is floating.

        Parameters
        ----------
        title : str
        """

    def show(self):
        """Show this window.

        Reimplemented from FXWindow. Reimplemented in AFXToolbarGroupRender, and AFXToolbarGroupVisibility.
        """
