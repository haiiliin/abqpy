from __future__ import annotations


class AFXMode:
    """Abaqus"""

    def __init__(self):
        """Constructor."""

    def getCommand(self, index: int):
        """Returns the command at the given index (returns 0 if the index is out-of-bounds).

        Parameters
        ----------
        index : int
            Command index (0-based).
        """

    def getNumCommands(self):
        """Returns the number of commands associated with the mode."""

    def isActive(self):
        """Returns True if the mode is active."""
