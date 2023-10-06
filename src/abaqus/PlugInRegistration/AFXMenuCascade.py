from __future__ import annotations

from .AFXGuiObjectManager import AFXGuiObjectManager
from .FXComposite import FXComposite
from .FXIcon import FXIcon
from .FXMenuCascade import FXMenuCascade
from .FXPopup import FXPopup


class AFXMenuCascade(FXMenuCascade):
    """This class provides the interface for creating an FXMenuCascade and performing various management
    activities on it.

    It will use utility methods so the menu cascade is correctly managed for modules and toolsets.
    """

    def __init__(
        self,
        owner: AFXGuiObjectManager,
        p: FXComposite,
        label: str,
        ic: FXIcon | None = None,
        popup: FXPopup | None = None,
    ):
        """Constructor.

        Parameters
        ----------
        owner : AFXGuiObjectManager
            Creator of the menu cascade.
        p : FXComposite
            Parent widget.
        label : str
            Label for the menu button.
        ic : FXIcon | None
            Menu button icon.
        popup : FXPopup | None
            Menu cascade's pullright pane.
        """

    def getOwner(self):
        """Returns the owner of the menu cascade.

        Reimplemented from FXWindow.
        """
