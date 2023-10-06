from __future__ import annotations

from typing import Any

from .FXApp import FXApp
from .FXColor import FXColor
from .FXDrawable import FXDrawable


class FXImage(FXDrawable):
    """Image class"""

    def __init__(self, a: FXApp, pix: Any | None = None, opts: int = 0, w: int = 1, h: int = 1):
        """Create an image.

        Parameters
        ----------
        a : FXApp

        pix : Any | None

        opts : int

        w : int

        h : int

        """

    def blend(self, color: FXColor, sharpen: bool = True):
        """Blends the icon with the specified color; should only be used on icons that support an alpha channel, for example, PNG.

        Parameters
        ----------
        color : FXColor

        sharpen : bool

        """

    def create(self):
        """Create image resource. Reimplemented from FXId. Reimplemented in FXIcon."""

    def destroy(self):
        """Destroy image resource. Reimplemented from FXId. Reimplemented in FXIcon."""

    def detach(self):
        """Detach image resource. Reimplemented from FXId. Reimplemented in FXIcon."""

    def getOptions(self):
        """To get to the option flags."""

    def getPixel(self, x: int, y: int):
        """Get pixel at x,y.

        Parameters
        ----------
        x : int

        y : int

        """

    def render(self):
        """Render the image from client-side pixel buffer. Reimplemented in FXIcon."""

    def resize(self, w: int, h: int):
        """Resize pixmap to the specified width and height. Reimplemented from FXDrawable. Reimplemented in FXIcon.

        Parameters
        ----------
        w : int

        h : int

        """

    def scale(self, w: int, h: int):
        """Rescale pixels image to the specified width and height.

        Parameters
        ----------
        w : int

        h : int

        """

    def setPixel(self, x: int, y: int, color: FXColor):
        """Change pixel at x,y.

        Parameters
        ----------
        x : int

        y : int

        color : FXColor

        """
