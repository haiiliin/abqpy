from __future__ import annotations

from .AFXCommand import AFXCommand
from .AFXKeyword import AFXKeyword


class AFXObjectKeyword(AFXKeyword):
    """This class is designed for the command keywords that have objects as values."""

    def __init__(self, command: AFXCommand, name: str, isRequired: bool = False, defaultValue: str = "''"):
        """Constructor.

        Parameters
        ----------
        command : AFXCommand
            Host command.
        name : str
            Keyword name.
        isRequired : bool
            True if the keyword is a required argument of the command.
        defaultValue : str
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

    def setDefaultValue(self, defaultValue: str):
        """Sets the keyword's default value.

        Parameters
        ----------
        defaultValue : str
            Default value.
        """

    def setValue(self, newValue: str):
        """Sets the keyword's current value.

        Parameters
        ----------
        newValue : str
            New value.
        """

    def setValueToDefault(self, ignoreUnspecified: bool = False):
        """Sets the keyword value to its default.

        Parameters
        ----------
        ignoreUnspecified : bool
            If set to True, ignore setting the value if the default is unspecified.
        """

    def setValueToPrevious(self):
        """Sets the keyword value to its previous value.

        Implements AFXKeyword.
        """

    def syncPreviousValue(self):
        """Sets the keyword's previous value to its current value.

        Implements AFXKeyword. By clicking on Send, you accept that Dassault Systèmes will process your
        personal data and may contact you for further information. [Privacy Policy](
        https://www.3ds.com/privacy-policy).
        Total Results: Results per page This page cannot be found. The page might not exist or is
        temporarily unavailable. Try again or try searching for the topic. Use this form to provide feedback
        on this help topic. To get product support or to provide product feedback, go to [Frequently Asked
        Questions](
        https://3ds.one/PO).
        For support for online purchased solutions, go to [Online Purchase Support](https://3ds.one/Q8). *
        Required Subject: Feedback on User Assistance * I acknowledge I have read and I hereby accept the
        [privacy policy](
        https://www.3ds.com/privacy-policy)
        under which my personal data will be used by Dassault Systèmes.
        """
