from __future__ import annotations

from .FXIcon import FXIcon


class FXFileItem:
    """|"""

    def __init__(self, text: str, bi: FXIcon | None = None, mi: FXIcon | None = None, ptr: str = "None"):
        """Constructor.

        Parameters
        ----------
        text : str

        bi : FXIcon | None

        mi : FXIcon | None

        ptr : str

        """

    def getDate(self):
        """Return the date for this item."""

    def getSize(self):
        """Return the file size for this item."""

    def isBlockdev(self):
        """Return True if this is a block device item."""

    def isChardev(self):
        """Return True if this is a character device item."""

    def isDirectory(self):
        """Return True if this is a directory item. Reimplemented in AFXFileItem."""

    def isExecutable(self):
        """Return True if this is an executable item."""

    def isFifo(self):
        """Return True if this is an FIFO item."""

    def isFile(self):
        """Return True if this is a file item."""

    def isSocket(self):
        """Return True if this is a socket."""

    def isSymlink(self):
        """Return True if this is a symbolic link item."""
