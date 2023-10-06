from __future__ import annotations

from .AFXGuiObjectManager import AFXGuiObjectManager
from .FXMenuPane import FXMenuPane


class AFXMenuPane(FXMenuPane):
    """This class provides the interface for creating an FXMenuPane and performing various management activities
    on it."""

    def __init__(self, owner: AFXGuiObjectManager):
        """Constructor.

        Parameters
        ----------
        owner : AFXGuiObjectManager
            Manager of the pane.
        """

    def getOwner(self):
        """Returns the owner of the menu pane.

        Reimplemented from FXWindow.
        """
