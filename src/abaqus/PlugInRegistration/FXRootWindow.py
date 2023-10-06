from __future__ import annotations

from .FXApp import FXApp
from .FXComposite import FXComposite
from .FXVisual import FXVisual


class FXRootWindow(FXComposite):
    """Root window."""

    def __init__(self, a: FXApp, vis: FXVisual):
        """Construct root window.

        Parameters
        ----------
        a : FXApp

        vis : FXVisual
        """

    def create(self):
        """Root window need not be created.

        Reimplemented from FXComposite.
        """

    def destroy(self):
        """Root window can not be destroyed.

        Reimplemented from FXComposite.
        """

    def detach(self):
        """Root window may not be detached.

        Reimplemented from FXComposite.
        """

    def getDefaultHeight(self):
        """Return height of the root window.

        Reimplemented from FXComposite.
        """

    def getDefaultWidth(self):
        """Return width of the root window.

        Reimplemented from FXComposite.
        """

    def move(self, x: int, y: int):
        """Root window can not be moved. Reimplemented from FXWindow.

        Parameters
        ----------
        x : int

        y : int
        """

    def position(self, x: int, y: int, w: int, h: int):
        """Root window can not be positioned. Reimplemented from FXWindow.

        Parameters
        ----------
        x : int

        y : int

        w : int

        h : int
        """

    def recalc(self):
        """No op.

        Reimplemented from FXWindow.
        """

    def resize(self, w: int, h: int):
        """Root window can not be resized. Reimplemented from FXWindow.

        Parameters
        ----------
        w : int

        h : int
        """
