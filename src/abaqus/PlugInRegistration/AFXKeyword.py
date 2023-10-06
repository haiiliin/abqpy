from __future__ import annotations

from .AFXCommand import AFXCommand
from .FXDataTarget import FXDataTarget


class AFXKeyword(FXDataTarget):
    """Abaqus."""

    #: Used to activate the keyword.
    ID_ACTIVATE: int = hash("ID_ACTIVATE")

    #: Used to deactivate the keyword.
    ID_DEACTIVATE: int = hash("ID_DEACTIVATE")

    def __init__(self, command: AFXCommand, name: str, isRequired: bool = False):
        """Constructor.

        Parameters
        ----------
        command : AFXCommand
            Host command, or NULL to create a keyword not associated with a command.
        name : str
            Keyword name.
        isRequired : bool
            True if the keyword is a required argument of the command.
        """

    def activate(self):
        """Activates the keyword; active keywords will be processed during command generation."""

    def deactivate(self):
        """Deactivates the keyword; inactive keywords will not be processed during command generation."""

    def getCommandSnippet(self):
        """Returns the command snippet of the keyword based on its current value."""

    def getName(self):
        """Returns the keyword name."""

    def getSetupCommands(self):
        """Returns the keyword's variable initilization commands (part of the generated command string)."""

    def getTypeName(self):
        """Returns the keyword type name.

        Implemented in AFXBoolKeyword, AFXComSymConstKeyword, AFXComTableKeyword, AFXFloatKeyword,
        AFXIntKeyword, AFXObjectKeyword, AFXStringKeyword, AFXSymConstKeyword, AFXTogglableKeyword,
        AFXTupleKeyword, and AFXTableKeyword.
        """

    def getValueAsString(self):
        """Returns the text string that represents the current keyword value.

        Implemented in AFXBoolKeyword, AFXComSymConstKeyword, AFXComTableKeyword, AFXFloatKeyword,
        AFXIntKeyword, AFXObjectKeyword, AFXStringKeyword, AFXSymConstKeyword, AFXTogglableKeyword, and
        AFXTupleKeyword.
        """

    def isActive(self):
        """Returns True if the keyword is active."""

    def isRequired(self):
        """Returns True if the keyword is a required argument of the host command; or returns False if the
        keyword is optional."""

    def isValueChanged(self):
        """Returns True if the keyword value differs from its previous value.

        Implemented in AFXBoolKeyword, AFXComSymConstKeyword, AFXComTableKeyword, AFXFloatKeyword,
        AFXIntKeyword, AFXObjectKeyword, AFXStringKeyword, AFXTogglableKeyword, and AFXTupleKeyword.
        """

    def setRequired(self, val: bool):
        """Sets this object as a required keyword of the host command.

        Parameters
        ----------
        val : bool
        """

    def setSetupCommands(self, cmds: str):
        """Sets variable initialization commands needed by the keyword.

        Parameters
        ----------
        cmds : str
        """

    def setValueToDefault(self, ignoreUnspecified: bool = False):
        """Sets the keyword value to its default.

        Parameters
        ----------
        ignoreUnspecified : bool
            Ignore setting the value if the default is unspecified.
        """

    def setValueToPrevious(self):
        """Sets the keyword value to its previous value.

        Implemented in AFXBoolKeyword, AFXComSymConstKeyword, AFXComTableKeyword, AFXFloatKeyword,
        AFXIntKeyword, AFXObjectKeyword, AFXStringKeyword, AFXTogglableKeyword, and AFXTupleKeyword.
        """

    def syncPreviousValue(self):
        """Sets the keyword's previous value to its current value.

        Implemented in AFXBoolKeyword, AFXComSymConstKeyword, AFXComTableKeyword, AFXFloatKeyword,
        AFXIntKeyword, AFXObjectKeyword, AFXStringKeyword, AFXTogglableKeyword, and AFXTupleKeyword.
        """
