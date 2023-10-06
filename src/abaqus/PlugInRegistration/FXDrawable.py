from __future__ import annotations

from .FXId import FXId


class FXDrawable(FXId):
    """Drawable is an abstract base class for any surface that can be drawn upon, such as a FXWindow, or
    FXImage."""

    def getHeight(self):
        """Height of drawable."""

    def getVisual(self):
        """Get the visual."""

    def getWidth(self):
        """Width of drawable."""

    def resize(self, w: int, h: int):
        """Resize drawable to the specified width and height. Reimplemented in FXBitmap, FXIcon, FXIconList,
        FXImage, FXMDIChild, FXRootWindow, FXText, FXTopWindow, and FXWindow.

        Parameters
        ----------
        w : int

        h : int
        """
