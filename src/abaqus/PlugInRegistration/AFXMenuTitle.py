from __future__ import annotations

from .FXComposite import FXComposite
from .FXIcon import FXIcon
from .FXMenuTitle import FXMenuTitle
from .FXPopup import FXPopup


class AFXMenuTitle(FXMenuTitle):
    """This class provides the interface for creating an FXMenuTitle and performing various management
    activities on it.

    It will use utility methods so the menu title is correctly managed for modules and procedure toolsets.
    """

    def __init__(self, parent: FXComposite, label: str, ic: FXIcon | None = None, popup: FXPopup | None = None):
        """Constructor that takes a parent.

        Parameters
        ----------
        parent : FXComposite
            Parent widget.
        label : str
            Label string.
        ic : FXIcon | None
            Icon.
        popup : FXPopup | None
            Pulldown menu.
        """

    def getOwner(self):
        """Returns the owner of the menu title.

        Reimplemented from FXWindow.
        """

    def hide(self):
        """Hides the widget.

        Reimplemented from FXWindow.
        """

    def show(self):
        """Shows the widget.

        Reimplemented from FXWindow.
        """
