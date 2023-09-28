class AFXBoolKeyword:
    """
    A class for defining boolean keywords.
    """

    def __init__(self, command: AFXCommand, name: str, booleanType: Type = bool, isRequired: bool = False, defaultValue: bool = False):
        """
        Constructor.

        Parameters
        ----------
        command : AFXCommand
            Host command.
        name : str
            Keyword name.
        booleanType : Type, optional
            Type of boolean used in the command. (default is bool)
        isRequired : bool, optional
            True if the keyword is a required argument of the command. (default is False)
        defaultValue : bool, optional
            Default value. (default is False)
        """
        pass

    def getTypeName(self) -> str:
        """
        Returns the name of the keyword type.

        Returns
        -------
        str
            The name of the keyword type.
        """
        pass

    def getValue(self) -> bool:
        """
        Returns the keyword's current value.

        Returns
        -------
        bool
            The keyword's current value.
        """
        pass

    def getValueAsString(self) -> str:
        """
        Returns the text string that represents the keyword's current value.

        Returns
        -------
        str
            The text string that represents the keyword's current value.
        """
        pass

    def isValueChanged(self) -> bool:
        """
        Returns True if the keyword value differs from its previous value.

        Returns
        -------
        bool
            True if the keyword value differs from its previous value.
        """
        pass

    def setDefaultValue(self, defaultValue: bool) -> None:
        """
        Sets the keyword's default value.

        Parameters
        ----------
        defaultValue : bool
            Default value.
        """
        pass

    def setDefaultValueByString(self, defaultValueString: str) -> bool:
        """
        Sets the keyword's default value (returns True if the given text string is valid).

        Parameters
        ----------
        defaultValueString : str
            Default value in text string form.

        Returns
        -------
        bool
            True if the given text string is valid.
        """
        pass

    def setValue(self, newValue: bool) -> None:
        """
        Sets the keyword's current value.

        Parameters
        ----------
        newValue : bool
            New value.
        """
        pass

    def setValueByString(self, newValueString: str) -> bool:
        """
        Sets the keyword's current value (returns True if the given text string is valid).

        Parameters
        ----------
        newValueString : str
            New value in text string form.

        Returns
        -------
        bool
            True if the given text string is valid.
        """
        pass

    def setValueToDefault(self, ignoreUnspecified: bool = False) -> None:
        """
        Sets the keyword value to its default.

        Parameters
        ----------
        ignoreUnspecified : bool, optional
            Not used. (default is False)
        """
        pass

    def setValueToPrevious(self) -> None:
        """
        Sets the keyword value to its previous value.
        """
        pass

    def syncPreviousValue(self) -> None:
        """
        Sets the keyword's previous value to its current value.
        """
        pass
    