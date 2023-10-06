from __future__ import annotations

from .constants import SPLITTER_NORMAL
from .FXComposite import FXComposite
from .FXObject import FXObject


class FXSplitter:
    """Abaqus"""

    def __init__(
        self,
        p: FXComposite,
        tgt: FXObject,
        sel: int,
        opts: int = SPLITTER_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
    ):
        """Construct new splitter widget, which will notify target about size changes.

        Parameters
        ----------
        p : FXComposite

        tgt : FXObject

        sel : int

        opts : int

        x : int

        y : int

        w : int

        h : int

        """

    def getDefaultHeight(self):
        """Get default height. Reimplemented from FXComposite."""

    def getDefaultWidth(self):
        """Get default width. Reimplemented from FXComposite."""

    def getSplitterStyle(self):
        """Return current splitter style."""

    def setSplitterStyle(self, style: int):
        """Change splitter style.

        Parameters
        ----------
        style : int

        """
