from __future__ import annotations

from .constants import DEFAULT_SPACING
from .FXComposite import FXComposite
from .FXPacker import FXPacker

#: Title is left-justified.
GROUPBOX_TITLE_LEFT: int = hash("GROUPBOX_TITLE_LEFT")

#: Title is centered.
GROUPBOX_TITLE_CENTER: int = hash("GROUPBOX_TITLE_CENTER")

#: Title is right-justified.
GROUPBOX_TITLE_RIGHT: int = hash("GROUPBOX_TITLE_RIGHT")

#: Normal group box style.
GROUPBOX_NORMAL: int = hash("GROUPBOX_NORMAL")


class FXGroupBox(FXPacker):
    """A group box widget provides a nice raised or sunken border around a group of widgets, providing a visual
    delineation.

    Typically, a title is placed over the border to provide some clarification. Radio buttons placed inside
    a group box automatically assume mutually exclusive behaviour, i.e. at most one radio button will be
    checked at any one time.
    """

    def __init__(
        self,
        p: FXComposite,
        text: str,
        opts: int = GROUPBOX_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = DEFAULT_SPACING,
        pr: int = DEFAULT_SPACING,
        pt: int = DEFAULT_SPACING,
        pb: int = DEFAULT_SPACING,
        hs: int = DEFAULT_SPACING,
        vs: int = DEFAULT_SPACING,
    ):
        """Construct group box layout manager.

        Parameters
        ----------
        p : FXComposite

        text : str

        opts : int

        x : int

        y : int

        w : int

        h : int

        pl : int

        pr : int

        pt : int

        pb : int

        hs : int

        vs : int
        """

    def create(self):
        """Create server-side resources.

        Reimplemented from FXComposite.
        """

    def detach(self):
        """Detach server-side resources.

        Reimplemented from FXComposite.
        """

    def disable(self):
        """Disable the window.

        Reimplemented from FXWindow.
        """

    def enable(self):
        """Enable the window.

        Reimplemented from FXWindow.
        """

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXPacker.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXPacker.
        """

    def getText(self):
        """Return current groupbox title text."""

    def setText(self, text: str):
        """Change group box title text.

        Parameters
        ----------
        text : str
        """
