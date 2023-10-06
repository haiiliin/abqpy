from __future__ import annotations

from .AFXCommand import AFXCommand
from .AFXKeyword import AFXKeyword

#: Any type is accepted.
AFXTABLE_TYPE_ANY: int = hash("AFXTABLE_TYPE_ANY")

#: Column type is the same as the table default type.
AFXTABLE_TYPE_DEFAULT: int = hash("AFXTABLE_TYPE_DEFAULT")

#: Column stores integer numbers.
AFXTABLE_TYPE_INT: int = hash("AFXTABLE_TYPE_INT")

#: Column stores floating-point numbers.
AFXTABLE_TYPE_FLOAT: int = hash("AFXTABLE_TYPE_FLOAT")

#: Column stores string values.
AFXTABLE_TYPE_STRING: int = hash("AFXTABLE_TYPE_STRING")

#: Column stores True or False.
AFXTABLE_TYPE_BOOL: int = hash("AFXTABLE_TYPE_BOOL")

#: Mask for column types.
AFXTABLE_TYPE_MASK: int = hash("AFXTABLE_TYPE_MASK")

#: Allow empty values for the column elements.
AFXTABLE_ALLOW_EMPTY: int = hash("AFXTABLE_ALLOW_EMPTY")

#: Always substitute the default for empty values.
AFXTABLE_DEFAULT_IF_EMPTY: int = hash("AFXTABLE_DEFAULT_IF_EMPTY")

#: Evaluate integer and float elements.
AFXTABLE_EVALUATE: int = hash("AFXTABLE_EVALUATE")

#: Use table default column style.
AFXTABLE_STYLE_DEFAULT: int = hash("AFXTABLE_STYLE_DEFAULT")

#: Mask for column styles.
AFXTABLE_STYLE_MASK: int = hash("AFXTABLE_STYLE_MASK")


class AFXComTableKeyword(AFXKeyword):
    """This class manages values which are sent as tables in a command."""

    #: ID for AFXTable widgets.
    ID_TABLE: int = hash("ID_TABLE")

    #: ID for widgets exchanging array strings.
    ID_VALUE: int = hash("ID_VALUE")

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
            Minimum (and default) row length.
        maxLength : int
            Maximum row length (-1 => unlimited).
        opts : int
            Options.
        """

    def equal(self, index: int, a: str, b: str):
        """Returns True if the two table element values compare equal (index not used).

        Parameters
        ----------
        index : int
            Element index (not used).
        a : str
            First value.
        b : str
            Second value.
        """

    def getColumnStyle(self, index: int):
        """Returns the style of the column elements. Will never return AFXTABLE_STYLE_DEFAULT!

        Parameters
        ----------
        index : int
            Column index.
        """

    def getColumnType(self, index: int):
        """Returns the type of the column elements. Will never return AFXTABLE_TYPE_DEFAULT!

        Parameters
        ----------
        index : int
            Column index.
        """

    def getDefaultStyle(self):
        """Returns the default style for the table elements."""

    def getDefaultType(self):
        """Returns the default type for the table elements."""

    def getDefaultValues(self):
        """Returns the default values for this table."""

    def getFormattedValue(self, row: int, column: int):
        """Returns the formatted value of the table element, suitable for placing in a command. If the element
        has AFXTABLE_EVALUATE style, and its contents are invalid, an exception will be thrown.

        Parameters
        ----------
        row : int
            Row index.
        column : int
            Column index.
        """

    def getMaxNumColumns(self):
        """Returns the maximum number of columns, or -1 for unbounded."""

    def getMinNumColumns(self):
        """Returns the minimum number of columns."""

    def getNumColumns(self, row: int):
        """Returns the number of columns in the row.

        Parameters
        ----------
        row : int
            Row index.
        """

    def getNumRows(self):
        """Returns the number of rows in the table."""

    def getRow(self, row: int):
        """Returns a string with the contents of a table row.

        Parameters
        ----------
        row : int
            Row index.
        """

    def getTypeName(self):
        """Returns the name of the table keyword type.

        Implements AFXKeyword. Reimplemented in AFXTableKeyword.
        """

    def getValue(self, row: int, column: int):
        """Returns the value of a table element.

        Parameters
        ----------
        row : int
            Row index.
        column : int
            Column index.
        """

    def getValueAsDouble(self):
        """Returns the keyword's value as a float; returns False upon failure."""

    def getValueAsInt(self):
        """Returns the keyword's value as an integer; returns False upon failure."""

    def getValueAsString(self):
        """Returns the formatted string that represents the current keyword value in a command.

        Implements AFXKeyword.
        """

    def getValueForBlank(self, column: int):
        """Returns the element value substituted for blank for the column.

        Parameters
        ----------
        column : int
            Column index.
        """

    def getValues(self):
        """Returns a string containing values of the tuple elements.

        as entered by the user.
        """

    def getValuesForBlanks(self):
        """Returns a string with values substituted for blanks for all table columns."""

    def insertColumns(self, index: int, numColumns: int):
        """Inserts columns starting at the given index.

        Parameters
        ----------
        index : int
            Starting index.
        numColumns : int
            Number of columns to insert.
        """

    def insertRows(self, index: int, numRows: int):
        """Inserts rows starting at the given index.

        Parameters
        ----------
        index : int
            Starting index.
        numRows : int
            Number of rows to insert.
        """

    def isValueChanged(self):
        """Returns True if the keyword value differs from its previous value.

        Implements AFXKeyword.
        """

    def removeColumns(self, index: int, numColumns: int):
        """Removes columns starting at the given index.

        Parameters
        ----------
        index : int
            Starting index.
        numColumns : int
            Number of columns to remove.
        """

    def removeRows(self, index: int, numRows: int):
        """Removes rows starting at the given index.

        Parameters
        ----------
        index : int
            Starting index.
        numRows : int
            Number of rows to remove.
        """

    def setColumnStyle(self, index: int, style: int):
        """Sets the style of the column elements.

        Parameters
        ----------
        index : int
            Column index.
        style : int
            New column style.
        """

    def setColumnType(self, index: int, type: int):
        """Sets the type of the column elements.

        Parameters
        ----------
        index : int
            Column index.
        type : int
            New column type.
        """

    def setDefaultStyle(self, style: int):
        """Sets the default style for the table elements.

        Parameters
        ----------
        style : int
            New default style.
        """

    def setDefaultType(self, type: int):
        """Sets the default type for table elements.

        Parameters
        ----------
        type : int
            New default type.
        """

    def setDefaultValues(self, values: str):
        """Sets the default values for this table.

        Parameters
        ----------
        values : str
            Sequence string with default values.
        """

    def setMaxNumColumns(self, length: int):
        """Sets the maximum number of columns.

        Parameters
        ----------
        length : int
            New maximum number of columns, or -1 for unbounded.
        """

    def setMinNumColumns(self, length: int):
        """Sets the minimum number of columns.

        Parameters
        ----------
        length : int
            New minimum length.
        """

    def setNumColumnsRange(self, minLength: int, maxLength: int):
        """Sets the allowable range for the number of columns.

        Parameters
        ----------
        minLength : int
            New minimum number of columns.
        maxLength : int
            New maximum number of columns, or -1 for unbounded.
        """

    def setRow(self, row: int, seq: str):
        """Sets the contents of a table row.

        Parameters
        ----------
        row : int
            Row index.
        seq : str
            Sequence with elements.
        """

    def setValue(self, row: int, column: int, value: str):
        """Sets the value of a table element.

        Parameters
        ----------
        row : int
            Row index.
        column : int
            Column index.
        value : str
            New value.
        """

    def setValueForBlank(self, column: int, value: str):
        """Sets the element value substituted for blank for the column.

        Parameters
        ----------
        column : int
            Column index.
        value : str
            New value.
        """

    def setValues(self, values: str):
        """Sets all values for the table elements.

        Parameters
        ----------
        values : str
            Table string with new values.
        """

    def setValuesForBlanks(self, values: str):
        """Sets the values substituted for blanks for all table columns.

        Parameters
        ----------
        values : str
            String containing comma-separated values.
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
