from __future__ import annotations

from .AFXGuiObjectManager import AFXGuiObjectManager


class AFXMenuPane:
    """|"""

    def __init__(self, owner: AFXGuiObjectManager):
        """Constructor.

        Parameters
        ----------
        owner : AFXGuiObjectManager
            Manager of the pane.
        """

    def getOwner(self):
        """Returns the owner of the menu pane. Reimplemented from FXWindow."""
