from __future__ import annotations

from .FXComposite import FXComposite
from .FXWindow import FXWindow


class FXMenuSeparator(FXWindow):
    """The menu separator is a simple decorative groove used to delineate items in a popup menu."""

    def __init__(self, p: FXComposite, opts: int = 0):
        """Construct a menu separator.

        Parameters
        ----------
        p : FXComposite

        opts : int
        """

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXWindow.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXWindow.
        """
