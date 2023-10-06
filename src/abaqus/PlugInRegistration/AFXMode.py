from __future__ import annotations

from .FXObject import FXObject


class AFXMode(FXObject):
    """This class is the base class for modes."""

    #: Activates the mode.
    ID_ACTIVATE: int = hash("ID_ACTIVATE")

    #: Commits the mode.
    ID_COMMIT: int = hash("ID_COMMIT")

    #: Cancels the mode.
    ID_CANCEL: int = hash("ID_CANCEL")

    #: Deactivates the mode.
    ID_DEACTIVATE: int = hash("ID_DEACTIVATE")

    #: Gets the next step/dialog box.
    ID_GET_NEXT: int = hash("ID_GET_NEXT")

    #: Resumes the mode.
    ID_RESUME: int = hash("ID_RESUME")

    #: Sets defaults.
    ID_SET_DEFAULTS: int = hash("ID_SET_DEFAULTS")

    #: Suspends the mode.
    ID_SUSPEND: int = hash("ID_SUSPEND")

    #: Indicates that a command is activated.
    ID_CMD_ACTIVATED: int = hash("ID_CMD_ACTIVATED")

    #: Indicates that a command is deactivated.
    ID_CMD_DEACTIVATED: int = hash("ID_CMD_DEACTIVATED")

    #: Indicates that a command is modified.
    ID_CMD_MODIFIED: int = hash("ID_CMD_MODIFIED")

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
