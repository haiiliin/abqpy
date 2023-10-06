from __future__ import annotations

from .constants import NOTE_INFORMATION
from .FXComposite import FXComposite


class AFXNote:
    """Abaqus"""

    def __init__(self, p: FXComposite, message: str, opts: int = NOTE_INFORMATION, x: int = 0, y: int = 0):
        """Constructor.

        Parameters
        ----------
        p : FXComposite
            Parent widget.
        message : str
            Note message string.
        opts : int
            Options and hints.
        x : int
            X coordinate of origin.
        y : int
            Y coordinate of origin.
        """

    def create(self):
        """Creates the note. Reimplemented from FXComposite."""

    def detach(self):
        """Detaches the server-resources of the note. Reimplemented from FXComposite."""

    def disable(self):
        """Disables the note. Reimplemented from FXWindow."""

    def enable(self):
        """Enables the note. Reimplemented from FXWindow."""

    def getText(self):
        """Returns the note's message string."""

    def setText(self, message: str):
        """Sets the note's message string.

        Parameters
        ----------
        message : str
            Message.
        """
