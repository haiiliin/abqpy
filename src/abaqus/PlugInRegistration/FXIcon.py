from __future__ import annotations

from typing import Any

from .FXApp import FXApp
from .FXColor import FXColor
from .FXImage import FXImage


class FXIcon(FXImage):
    """Icon class."""

    def __init__(self, a: FXApp, pix: Any | None = None, clr: FXColor | int = 0, opts: int = 0, w: int = 1, h: int = 1):
        """Create an icon with an initial pixel buffer pix, a transparent color clr, and options as in FXImage.

        Parameters
        ----------
        a : FXApp

        pix : Any | None

        clr : FXColor

        opts : int

        w : int

        h : int
        """

    def create(self):
        """Create the icon resource.

        Reimplemented from FXImage.
        """

    def destroy(self):
        """Destroy the icon resource.

        Reimplemented from FXImage.
        """

    def detach(self):
        """Detach the icon resource.

        Reimplemented from FXImage.
        """

    def render(self):
        """Render the image from client-side pixel buffer.

        Reimplemented from FXImage.
        """

    def resize(self, w: int, h: int):
        """Resize pixmap to the specified width and height. Reimplemented from FXImage.

        Parameters
        ----------
        w : int

        h : int
        """
