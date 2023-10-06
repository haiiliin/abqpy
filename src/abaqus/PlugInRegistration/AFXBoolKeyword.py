from __future__ import annotations

from .AFXCommand import AFXCommand
from .AFXKeyword import AFXKeyword


class AFXBoolKeyword(AFXKeyword):
    """This class is designed for command keywords that have Boolean values."""

    #: Keyword value will be ON or OFF.
    ON_OFF: int = hash("ON_OFF")

    #: Keyword value will be True or False.
    TRUE_FALSE: int = hash("TRUE_FALSE")

    def __init__(
        self,
        command: AFXCommand,
        name: str,
        booleanType=ON_OFF,
        isRequired: bool = False,
        defaultValue: bool = False,
    ):
        """Constructor.

        Parameters
        ----------
        command : AFXCommand
            Host command.
        name : str
            Keyword name.
        booleanType : Type
            Type of boolean used in the command.
        isRequired : bool
            True if the keyword is a required argument of the command.
        defaultValue : bool
            Default value.
        """

    def getTypeName(self):
        """Returns the name of the keyword type.

        Implements AFXKeyword.
        """

    def getValue(self):
        """Returns the keyword's current value."""

    def getValueAsString(self):
        """Returns the text string that represents the keyword's current value.

        Implements AFXKeyword.
        """

    def isValueChanged(self):
        """Returns True if the keyword value differs from its previous value.

        Implements AFXKeyword.
        """

    def setDefaultValue(self, defaultValue: bool):
        """Sets the keyword's default value.

        Parameters
        ----------
        defaultValue : bool
            Default value.
        """

    def setDefaultValueByString(self, defaultValueString: str):
        """Sets the keyword's default value (returns True if the given text string is valid).

        Parameters
        ----------
        defaultValueString : str
            Default value in text string form.
        """

    def setValue(self, newValue: bool):
        """Sets the keyword's current value.

        Parameters
        ----------
        newValue : bool
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
            Not used.
        """

    def setValueToPrevious(self):
        """Sets the keyword value to its previous value.

        Implements AFXKeyword.
        """

    def syncPreviousValue(self):
        """Sets the keyword's previous value to its current value.

        Implements AFXKeyword.
        """
