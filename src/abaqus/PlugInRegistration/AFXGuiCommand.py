from __future__ import annotations

from .AFXCommand import AFXCommand
from .AFXGuiMode import AFXGuiMode


class AFXGuiCommand(AFXCommand):
    """This class is designed for the GUI commands processed by modes."""

    def __init__(self, mode: AFXGuiMode, method: str, objectName: str = "''", registerQuery: bool = False):
        """Constructor.

        Parameters
        ----------
        mode : AFXGuiMode
            Host mode.
        method : str
            Method.
        objectName : str
            Object name.
        registerQuery : bool
            True if a query should be registered so that the command's keyword values can be updated based on the kernel state.
        """

    def getMode(self):
        """Retrieves the command's mode."""
