from __future__ import annotations

from .AFXMode import AFXMode
from .FXObject import FXObject


class AFXCommand(FXObject):
    """This class is the abstract base class for command classes that are processed by modes."""

    def __init__(self, mode: AFXMode, method: str, objectName: str = "''", registerQuery: bool = False):
        """Constructor.

        Parameters
        ----------
        mode : AFXMode
            Host mode.
        method : str
            Method.
        objectName : str
            Object name.
        registerQuery : bool
            True if a query should be registered when the command is used for the GUI.
        """

    def activate(self):
        """Activates the command; active commands will be processed during command generation."""

    def deactivate(self):
        """Deactivates the command; inactive commands will not be processed during command generation."""

    def getCommandString(self):
        """Returns the command string based on the current values of the active keywords."""

    def getExpandedObjectName(self):
        """Returns the expanded object name that has all the "%s"'s replaced by the current names."""

    def getKeyword(self, index: int):
        """Returns the keyword at the given index (returns 0 if the index is out-of-bounds).

        Parameters
        ----------
        index : int
            Keyword index (0-based).
        """

    def getMethod(self):
        """Returns the command's method."""

    def getNumKeywords(self):
        """Returns the number of keywords."""

    def getObjectName(self):
        """Returns the object name (which is not expanded and may include "%s"'s)."""

    def isActive(self):
        """Returns True if the command is active."""

    def isQueryNeeded(self):
        """Returns True if the command needs to register a query for kernel state."""

    def isRequired(self):
        """Returns True if this command is going to be sent even if none of its keywords has been modified,
        otherwise returns False."""

    def setKeywordValuesToDefaults(self, ignoreUnspecified: bool = False):
        """Sets the values of all keywords to their defaults.

        Parameters
        ----------
        ignoreUnspecified : bool
            Ignore setting the value if the default is unspecified.
        """

    def setKeywordValuesToPrevious(self):
        """Sets the values of all keywords to their previous values."""

    def setMethod(self, method: str):
        """Sets the command's method.

        Parameters
        ----------
        method : str
            Method.
        """

    def setObjectName(self, objectName: str):
        """Sets the object name.

        Parameters
        ----------
        objectName : str
            Object name.
        """

    def setRequired(self, val: bool):
        """Sets this command as required or optional; if True the command will always be sent, if False the
        command will be sent only if it has modified keywords or if it has no keywords.

        Parameters
        ----------
        val : bool
        """

    def syncKeywordPreviousValues(self):
        """Synchronizes the current values and previous values of all keywords."""

    def verify(self):
        """Throws an exception if any of the keywords contain invalid data."""
