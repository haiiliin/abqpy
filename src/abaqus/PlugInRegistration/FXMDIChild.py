from __future__ import annotations

from .FXColor import FXColor
from .FXComposite import FXComposite
from .FXFont import FXFont
from .FXIcon import FXIcon
from .FXMDIClient import FXMDIClient
from .FXMenuPane import FXMenuPane
from .FXPopup import FXPopup

#: Normal display mode.
MDI_NORMAL: int = hash("MDI_NORMAL")

#: Window appears maximized.
MDI_MAXIMIZED: int = hash("MDI_MAXIMIZED")

#: Window is iconified or minimized.
MDI_MINIMIZED: int = hash("MDI_MINIMIZED")


class FXMDIChild(FXComposite):
    """The MDI child window contains the application work area in a Multiple Document Interface application."""

    def __init__(
        self,
        p: FXMDIClient,
        name: str,
        ic: FXIcon | None = None,
        mn: FXMenuPane | None = None,
        opts: int = 0,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
    ):
        """Construct MDI Child window with given name and icon.

        Parameters
        ----------
        p : FXMDIClient

        name : str

        ic : FXIcon | None

        mn : FXMenuPane | None

        opts : int

        x : int

        y : int

        w : int

        h : int
        """

    def canFocus(self):
        """MDI Child can receive focus.

        Reimplemented from FXWindow.
        """

    def contentWindow(self):
        """Return content window."""

    def create(self):
        """Create window.

        Reimplemented from FXComposite.
        """

    def detach(self):
        """Detach window.

        Reimplemented from FXComposite.
        """

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXComposite.
        """

    def getDefaultWidth(self):
        """Compute default size.

        Reimplemented from FXComposite.
        """

    def getFont(self):
        """Get title font."""

    def getHiliteColor(self):
        """Get colors."""

    def getIconX(self):
        """Return iconified position."""

    def getMDINext(self):
        """Get next MDI Child."""

    def getMDIPrev(self):
        """Get previous MDI Child."""

    def getNormalX(self):
        """Return normal (restored) position."""

    def getTitle(self):
        """Get current title."""

    def getWindowIcon(self):
        """Get window icon."""

    def getWindowMenu(self):
        """Get window menu."""

    def isMaximized(self):
        """Return True if maximized."""

    def isMinimized(self):
        """Return True if minimized."""

    def maximize(self, notify: bool = False):
        """Maximize MDI Child.

        Parameters
        ----------
        notify : bool
        """

    def minimize(self, notify: bool = False):
        """Minimize/iconify MDI Child.

        Parameters
        ----------
        notify : bool
        """

    def move(self, x: int, y: int):
        """Move this window to the specified position in the parent's coordinates. Reimplemented from FXWindow.

        Parameters
        ----------
        x : int

        y : int
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

    def restore(self, notify: bool = False):
        """Restore MDI Child to normal.

        Parameters
        ----------
        notify : bool
        """

    def setFont(self, fnt: FXFont):
        """Set title font.

        Parameters
        ----------
        fnt : FXFont
        """

    def setHiliteColor(self, clr: FXColor):
        """Change colors.

        Parameters
        ----------
        clr : FXColor
        """

    def setIconX(self, x: int):
        """Change iconified position.

        Parameters
        ----------
        x : int
        """

    def setNormalX(self, x: int):
        """Change normal (restored) position.

        Parameters
        ----------
        x : int
        """

    def setTitle(self, name: str):
        """Change MDI Child's title.

        Parameters
        ----------
        name : str
        """

    def setWindowIcon(self, icon: FXIcon):
        """Set window icon.

        Parameters
        ----------
        icon : FXIcon
        """

    def setWindowMenu(self, menu: FXPopup):
        """Set window menu.

        Parameters
        ----------
        menu : FXPopup
        """
