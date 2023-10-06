from __future__ import annotations

from .AFXCommand import AFXCommand
from .AFXIntKeyword import AFXIntKeyword


class AFXSymConstKeyword(AFXIntKeyword):
    """This class is designed for the command keywords that have symbolic constant values."""

    def __init__(self, command: AFXCommand, name: str, isRequired: bool = False, defaultValue: int = 0):
        """Constructor.

        Parameters
        ----------
        command : AFXCommand
            Host command.
        name : str
            Keyword name.
        isRequired : bool
            True if the keyword is a required argument of the command.
        defaultValue : int
            Default value.
        """

    def getTypeName(self):
        """Returns the name of the keyword type.

        Reimplemented from AFXIntKeyword.
        """

    def getValueAsString(self):
        """Returns the text string that represents the keyword's current value.

        Reimplemented from AFXIntKeyword.
        """

    def setDefaultValue(self, defaultValue: int):
        """Sets the keyword's default value.

        Parameters
        ----------
        defaultValue : int
            Default value.
        """

    def setDefaultValueByString(self, defaultValueString: str):
        """Sets the keyword's default value (returns True if the given text string is valid).

        Parameters
        ----------
        defaultValueString : str
            Default value in text string form.
        """

    def setValue(self, newValue: int):
        """Sets the keyword's current value.

        Parameters
        ----------
        newValue : int
            New value.
        """

    def setValueByString(self, newValueString: str):
        """Sets the keyword's current value (returns True if the given text string is valid).

        Parameters
        ----------
        newValueString : str
            New value in text string form.
        """

    def setValueToDefault(self, ignoreUnspecified: bool = False):
        """Sets the keyword value to its default.

        Parameters
        ----------
        ignoreUnspecified : bool
            Ignore setting the value if the default is unspecified.
        """
