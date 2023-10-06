from __future__ import annotations

from .AFXGuiObjectManager import AFXGuiObjectManager
from .FXComposite import FXComposite
from .FXMatrix import FXMatrix


class AFXToolboxGroup(FXMatrix):
    """This class creates a container to be used for groups in the toolbox.

    It will use utility methods so the group is correctly managed for modules and toolsets.
    """

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
        """Returns the owner of the toolbox group.

        Reimplemented from FXWindow.
        """
