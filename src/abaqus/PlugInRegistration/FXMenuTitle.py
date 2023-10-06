from __future__ import annotations

from .FXComposite import FXComposite
from .FXIcon import FXIcon
from .FXMenuCaption import FXMenuCaption
from .FXPopup import FXPopup


class FXMenuTitle(FXMenuCaption):
    """A menu title is a child of a menu bar which is responsible for popping up a pulldown menu."""

    def __init__(self, p: FXComposite, text: str, ic: FXIcon | None = None, pup: FXPopup | None = None, opts: int = 0):
        """Constructor.

        Parameters
        ----------
        p : FXComposite

        text : str

        ic : FXIcon | None

        pup : FXPopup | None

        opts : int
        """

    def canFocus(self):
        """Yes it can receive the focus.

        Reimplemented from FXWindow.
        """

    def create(self):
        """Create server-side resources.

        Reimplemented from FXMenuCaption.
        """

    def detach(self):
        """Detach server-side resources.

        Reimplemented from FXMenuCaption.
        """

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXMenuCaption.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXMenuCaption.
        """

    def getMenu(self):
        """Return popup menu."""

    def setMenu(self, menu: FXPopup):
        """Set popup menu to pop up.

        Parameters
        ----------
        menu : FXPopup
        """
