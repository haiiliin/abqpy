from __future__ import annotations

from .AFXGuiObjectManager import AFXGuiObjectManager
from .FXComposite import FXComposite


class AFXToolboxGroup:
    """|"""

    def __init__(self, owner: AFXGuiObjectManager, parent: FXComposite | None = None):
        """Constructor.

        Parameters
        ----------
        owner : AFXGuiObjectManager
            Creator of the toolbox group.
        parent : FXComposite | None
            Parent widget.
        """

    def getOwner(self):
        """Returns the owner of the toolbox group. Reimplemented from FXWindow."""
