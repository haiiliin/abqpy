from __future__ import annotations

from .FXIcon import FXIcon
from .FXShell import FXShell

#: Borderless window.
DECOR_NONE: int = hash("DECOR_NONE")

#: Window title.
DECOR_TITLE: int = hash("DECOR_TITLE")

#: Minimize button.
DECOR_MINIMIZE: int = hash("DECOR_MINIMIZE")

#: Maximize button.
DECOR_MAXIMIZE: int = hash("DECOR_MAXIMIZE")

#: Close button.
DECOR_CLOSE: int = hash("DECOR_CLOSE")

#: Border.
DECOR_BORDER: int = hash("DECOR_BORDER")

#: Resize handles.
DECOR_RESIZE: int = hash("DECOR_RESIZE")

#: Window menu.
DECOR_MENU: int = hash("DECOR_MENU")

#: Place it at the default size and location.
PLACEMENT_DEFAULT: int = hash("PLACEMENT_DEFAULT")

#: Place window to be fully visible.
PLACEMENT_VISIBLE: int = hash("PLACEMENT_VISIBLE")

#: Place it under the cursor position.
PLACEMENT_CURSOR: int = hash("PLACEMENT_CURSOR")

#: Place it centered on its owner.
PLACEMENT_OWNER: int = hash("PLACEMENT_OWNER")

#: Place it centered on the screen.
PLACEMENT_SCREEN: int = hash("PLACEMENT_SCREEN")

#: Place it maximized to the screen size.
PLACEMENT_MAXIMIZED: int = hash("PLACEMENT_MAXIMIZED")


class FXTopWindow(FXShell):
    """Abstract base class for all top-level windows."""

    def create(self):
        """Create server-side resources.

        Reimplemented from FXShell. Reimplemented in FXPrintDialog, FXToolbarShell, AFXMainWindow, and
        AFXDialog.
        """

    def deiconify(self):
        """Deiconify window."""

    def detach(self):
        """Detach the server-side resources for this window.

        Reimplemented from FXComposite.
        """

    def getDecorations(self):
        """Return current title and border decorations."""

    def getDefaultHeight(self):
        """Return the default height of this window.

        Reimplemented from FXComposite. Reimplemented in FXToolbarShell, and AFXMainWindow.
        """

    def getDefaultWidth(self):
        """Return the default width of this window.

        Reimplemented from FXComposite. Reimplemented in FXToolbarShell, and AFXMainWindow.
        """

    def getHSpacing(self):
        """Return horizontal spacing between children."""

    def getIcon(self):
        """Return window icon."""

    def getMiniIcon(self):
        """Return window mini (title) icon."""

    def getPackingHints(self):
        """Return packing hints for children."""

    def getPadBottom(self):
        """Get bottom interior padding."""

    def getPadLeft(self):
        """Get left interior padding."""

    def getPadRight(self):
        """Get right interior padding."""

    def getPadTop(self):
        """Get top interior padding."""

    def getTitle(self):
        """Return window title."""

    def getVSpacing(self):
        """Return vertical spacing between children."""

    def hide(self):
        """Hide this window.

        Reimplemented from FXWindow. Reimplemented in AFXManagerMenuDB, AFXDialog, and AFXMessageDialog.
        """

    def iconify(self):
        """Iconify window."""

    def isIconified(self):
        """Return True if window has been iconified."""

    def killFocus(self):
        """Remove the focus from this window.

        Reimplemented from FXShell.
        """

    def move(self, x: int, y: int):
        """Move this window to the specified position in the parent's coordinates. Reimplemented from FXWindow.

        Parameters
        ----------
        x : int

        y : int
        """

    def place(self, placement: int):
        """Position the window based on placement.

        Parameters
        ----------
        placement : int
        """

    def position(self, x: int, y: int, w: int, h: int):
        """Move and resize this window in the parent's coordinates. Reimplemented from FXWindow.

        Parameters
        ----------
        x : int

        y : int

        w : int

        h : int
        """

    def resize(self, w: int, h: int):
        """Resize this window to the specified width and height. Reimplemented from FXWindow.

        Parameters
        ----------
        w : int

        h : int
        """

    def setDecorations(self, decorations: int):
        """Change title and border decorations.

        Parameters
        ----------
        decorations : int
        """

    def setFocus(self):
        """Move the focus to this window.

        Reimplemented from FXShell.
        """

    def setHSpacing(self, hs: int):
        """Change horizontal spacing between children.

        Parameters
        ----------
        hs : int
        """

    def setIcon(self, ic: FXIcon):
        """Change window icon.

        Parameters
        ----------
        ic : FXIcon
        """

    def setMiniIcon(self, ic: FXIcon):
        """Change window mini (title) icon.

        Parameters
        ----------
        ic : FXIcon
        """

    def setPackingHints(self, ph: int):
        """Change packing hints for children.

        Parameters
        ----------
        ph : int
        """

    def setPadBottom(self, pb: int):
        """Change bottom padding.

        Parameters
        ----------
        pb : int
        """

    def setPadLeft(self, pl: int):
        """Change left padding.

        Parameters
        ----------
        pl : int
        """

    def setPadRight(self, pr: int):
        """Change right padding.

        Parameters
        ----------
        pr : int
        """

    def setPadTop(self, pt: int):
        """Change top padding.

        Parameters
        ----------
        pt : int
        """

    def setTitle(self, name: str):
        """Change window title.

        Parameters
        ----------
        name : str
        """

    def setVSpacing(self, vs: int):
        """Change vertical spacing between children.

        Parameters
        ----------
        vs : int
        """

    def show(self):
        """Show this window.

        Reimplemented from FXWindow. Reimplemented in AFXDialog, AFXFileDialog, and AFXMessageDialog.
        """
