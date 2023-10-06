from __future__ import annotations

from .AFXCommand import AFXCommand
from .AFXKeyword import AFXKeyword

#: Any type is accepted.
AFXTUPLE_TYPE_ANY: int = hash("AFXTUPLE_TYPE_ANY")

#: Element type is the same as the tuple default type.
AFXTUPLE_TYPE_DEFAULT: int = hash("AFXTUPLE_TYPE_DEFAULT")

#: Element is an integer number.
AFXTUPLE_TYPE_INT: int = hash("AFXTUPLE_TYPE_INT")

#: Element is a floating-point number.
AFXTUPLE_TYPE_FLOAT: int = hash("AFXTUPLE_TYPE_FLOAT")

#: Element is a string.
AFXTUPLE_TYPE_STRING: int = hash("AFXTUPLE_TYPE_STRING")

#: Element is True or False.
AFXTUPLE_TYPE_BOOL: int = hash("AFXTUPLE_TYPE_BOOL")

#: Mask for element types.
AFXTUPLE_TYPE_MASK: int = hash("AFXTUPLE_TYPE_MASK")

#: Allow empty values for the element.
AFXTUPLE_ALLOW_EMPTY: int = hash("AFXTUPLE_ALLOW_EMPTY")

#: Always substitute the default for an empty value.
AFXTUPLE_DEFAULT_IF_EMPTY: int = hash("AFXTUPLE_DEFAULT_IF_EMPTY")

#: Evaluate integer and float elements.
AFXTUPLE_EVALUATE: int = hash("AFXTUPLE_EVALUATE")

#: Use tuple default element style.
AFXTUPLE_STYLE_DEFAULT: int = hash("AFXTUPLE_STYLE_DEFAULT")

#: Mask for element styles.
AFXTUPLE_STYLE_MASK: int = hash("AFXTUPLE_STYLE_MASK")


class AFXTupleKeyword(AFXKeyword):
    """This class manages values which are sent as tuples in a command."""

    #: For debugging.
    ID_PRINTSNIPPET: int = hash("ID_PRINTSNIPPET")

    def __init__(
        self,
        command: AFXCommand,
        name: str,
        isRequired: bool = False,
        minLength: int = 0,
        maxLength: int = -1,
        opts: int = 0,
    ):
        """Constructor.

        Parameters
        ----------
        command : AFXCommand
            Host command.
        name : str
            Keyword name.
        isRequired : bool
            True if this keyword is a required argument.
        minLength : int
            Minimum (and default) tuple length.
        maxLength : int
            Maximum tuple length (-1 => unlimited).
        opts : int
            Options.
        """

    def equal(self, index: int, a: str, b: str):
        """Returns True if the two tuple element values compare equal (index is not used).

        Parameters
        ----------
        index : int
            Element index (not used).
        a : str
            First value.
        b : str
            Second value.
        """

    def getDefaultStyle(self):
        """Returns the default style for elements."""

    def getDefaultType(self):
        """Returns the default type for elements."""

    def getDefaultValues(self):
        """Returns the default values for this tuple."""

    def getElementStyle(self, index: int):
        """Returns the style of one element. Will never return AFXTUPLE_STYLE_DEFAULT!

        Parameters
        ----------
        index : int
            Element index.
        """

    def getElementType(self, index: int):
        """Returns the type of one element. Will never return AFXTUPLE_TYPE_DEFAULT!

        Parameters
        ----------
        index : int
            Element index.
        """

    def getFormattedValue(self, index: int):
        """Returns the formatted value of the tuple element, suitable for placing in a command. If the element
        has AFXTUPLE_EVALUATE style and its contents are invalid, an exception will be thrown.

        Parameters
        ----------
        index : int
            Element index.
        """

    def getLength(self):
        """Returns the length of the tuple."""

    def getMaxLength(self):
        """Returns the maximum length of this tuple, or -1 for unbounded length."""

    def getMinLength(self):
        """Returns the minimum length of this tuple."""

    def getTypeName(self):
        """Returns the name of the tuple keyword type.

        Implements AFXKeyword.
        """

    def getValue(self, index: int):
        """Returns the value of a tuple element.

        Parameters
        ----------
        index : int
            Element index.
        """

    def getValueAsDouble(self):
        """Returns the keyword's value as a float; returns False upon failure."""

    def getValueAsInt(self):
        """Returns the keyword's value as an integer; returns False upon failure."""

    def getValueAsString(self):
        """Returns the formatted string that represents the current keyword value in a command.

        Implements AFXKeyword.
        """

    def getValueForBlank(self, index: int):
        """Returns the value substituted for blank tuple element.

        Parameters
        ----------
        index : int
            Element index.
        """

    def getValues(self):
        """Returns a string containing values (separated by commas) of the tuple elements."""

    def getValuesForBlanks(self):
        """Returns a string containing values substituted for blanks for the tuple elements."""

    def insertElements(self, index: int, numCols: int):
        """Inserts elements starting at the given index.

        Parameters
        ----------
        index : int
            Starting index.
        numCols : int
            Number of elements to insert.
        """

    def isValueChanged(self):
        """Returns True if the keyword value differs from its previous value.

        Implements AFXKeyword.
        """

    def removeElements(self, index: int, numCols: int):
        """Removes elements starting at the given index.

        Parameters
        ----------
        index : int
            Starting index.
        numCols : int
            Number of elements to remove.
        """

    def setDefaultStyle(self, style: int):
        """Sets the default style for elements.

        Parameters
        ----------
        style : int
            New default element style.
        """

    def setDefaultType(self, type: int):
        """Sets the default type for elements.

        Parameters
        ----------
        type : int
            New default type.
        """

    def setDefaultValues(self, values: str):
        """Sets the default values for this tuple.

        Parameters
        ----------
        values : str
            Sequence string with default values.
        """

    def setElementStyle(self, index: int, style: int):
        """Sets the style of one element.

        Parameters
        ----------
        index : int
            Element index.
        style : int
            New element style.
        """

    def setElementType(self, index: int, type: int):
        """Sets the type of one element.

        Parameters
        ----------
        index : int
            Element index.
        type : int
            New element type.
        """

    def setLengthRange(self, minLength: int, maxLength: int):
        """Sets the range of allowable tuple lengths.

        Parameters
        ----------
        minLength : int
            New minimum length.
        maxLength : int
            New maximum length, or -1 for unbounded length.
        """

    def setMaxLength(self, length: int):
        """Sets the maximum length of this tuple.

        Parameters
        ----------
        length : int
            New maximum length, or -1 for unbounded length.
        """

    def setMinLength(self, length: int):
        """Sets the minimum length of this tuple.

        Parameters
        ----------
        length : int
            New minimum length.
        """

    def setValue(self, index: int, value: str):
        """Sets the value of the tuple element; returns False upon failure.

        Parameters
        ----------
        index : int
            Element index.
        value : str
            New value.
        """

    def setValueForBlank(self, index: int, value: str):
        """Sets the value substituted for a blank tuple element.

        Parameters
        ----------
        index : int
            Element index.
        value : str
            New value.
        """

    def setValues(self, values: str):
        """Sets values for all tuple elements (use commas to separate values within the string).

        Parameters
        ----------
        values : str
            Tuple string with new values.
        """

    def setValuesForBlanks(self, values: str):
        """Sets all values substituted for blanks for the tuple elements.

        Parameters
        ----------
        values : str
            Tuple string with values.
        """

    def setValueToDefault(self, ignoreUnspecified: bool = False):
        """Sets the keyword value to its default.

        Parameters
        ----------
        ignoreUnspecified : bool
            Should ignore if default is an unspecified value.
        """

    def setValueToPrevious(self):
        """Sets the keyword value to its previous value.

        Implements AFXKeyword.
        """

    def syncPreviousValue(self):
        """Sets the keyword's previous value to its current value.

        Implements AFXKeyword.
        """
