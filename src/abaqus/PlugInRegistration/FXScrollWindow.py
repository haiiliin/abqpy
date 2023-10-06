from __future__ import annotations

from .FXComposite import FXComposite
from .FXSrollArea import FXSrollArea


class FXScrollWindow(FXSrollArea):
    """The scroll window widget scrolls an arbitrary child window.

    Use the scroll window when parts of the user interface itself need to be scrolled, for example when
    applications need to run on small screens.
    """

    def __init__(self, p: FXComposite, opts: int = 0, x: int = 0, y: int = 0, w: int = 0, h: int = 0):
        """Construct a scroll window.

        Parameters
        ----------
        p : FXComposite

        opts : int

        x : int

        y : int

        w : int

        h : int
        """

    def contentWindow(self):
        """Return a pointer to the contents window."""

    def create(self):
        """Create server-side resources.

        Reimplemented from FXComposite.
        """

    def getContentHeight(self):
        """Return the height of the contents.

        Reimplemented from FXScrollArea. Reimplemented in AFXOptionTreeList.
        """

    def getContentWidth(self):
        """Return the width of the contents.

        Reimplemented from FXScrollArea. Reimplemented in AFXOptionTreeList.
        """

    def moveContents(self, x: int, y: int):
        """Move contents to the specified position. Reimplemented from FXScrollArea. Reimplemented in
        AFXOptionTreeList.

        Parameters
        ----------
        x : int

        y : int
        """
