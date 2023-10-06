from __future__ import annotations

from .AFXGuiObjectManager import AFXGuiObjectManager
from .FXComposite import FXComposite
from .FXIcon import FXIcon
from .FXMenuCommand import FXMenuCommand
from .FXObject import FXObject


class AFXMenuCommand(FXMenuCommand):
    """This class provides the interface for creating an FXMenuCommand and performing various management
    activities on it.

    It will use utility methods so the menu command is correctly managed for modules and toolsets.
    """

    def __init__(
        self,
        owner: AFXGuiObjectManager,
        p: FXComposite,
        label: str,
        ic: FXIcon | None = None,
        tgt: FXObject | None = None,
        sel: int = 0,
    ):
        """Constructor.

        Parameters
        ----------
        owner : AFXGuiObjectManager
            Creator of the menu command.
        p : FXComposite
            Parent widget.
        label : str
            Label for the menu button.
        ic : FXIcon | None
            Menu button icon.
        tgt : FXObject | None
            Message target.
        sel : int
            Message ID.
        """

    def getOwner(self):
        """Returns the owner of the menu command.

        Reimplemented from FXWindow.
        """
