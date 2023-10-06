from __future__ import annotations

from .AFXCommand import AFXCommand
from .AFXKeyword import AFXKeyword
from .constants import FLOAT_DEFAULT


class AFXFloatKeyword(AFXKeyword):
    """This class is designed for the command keywords that have floating-point values."""

    def __init__(
        self,
        command: AFXCommand,
        name: str,
        isRequired: bool = False,
        defaultValue: float = FLOAT_DEFAULT,
        precision: int = 6,
    ):
        """Constructor.

        Parameters
        ----------
        command : AFXCommand
            Host command.
        name : str
            Keyword name.
        isRequired : bool
            True if the keyword is a required argument of the command.
        defaultValue : float
            Default value.
        precision : int
            Precision for converting the keyword's floating-point value to a text string.
        """

    def getPrecision(self):
        """Returns the precision that is used for converting the keyword's floating-point value to a text
        string."""

    def getTypeName(self):
        """Returns the name of the keyword type.

        Implements AFXKeyword.
        """

    def getValue(self):
        """Returns the keyword's current value, or zero if the content expression is invalid."""

    def getValueAsString(self):
        """Returns the text string that represents the keyword's current value.

        Implements AFXKeyword.
        """

    def isValueChanged(self):
        """Returns True if the keyword value differs from its previous value.

        Implements AFXKeyword.
        """

    def setDefaultValue(self, defaultValue: float):
        """Sets the keyword's default value.

        Parameters
        ----------
        defaultValue : float
            Default value.
        """

    def setPrecision(self, precision: int):
        """Sets the precision that is used for converting the keyword's floating-point value to a text string.

        Parameters
        ----------
        precision : int
        """

    def setValue(self, newValue: float):
        """Sets the keyword's current value.

        Parameters
        ----------
        newValue : float
            New value.
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

        Implements AFXKeyword.
        """

    def syncPreviousValue(self):
        """Sets the keyword's previous value to its current value.

        Implements AFXKeyword.
        """
