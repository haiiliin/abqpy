from __future__ import annotations


class AFXSequenceString:
    """This class supports parsing and modification of strings containing sequences of elements separated with
    some separator character."""

    def __init__(self):
        """Undefined copy constructor (this class has no copy semantics)."""

    def forceNumElements(self, num: int, fill: str):
        """Forces the content string to contain a tuple with the given number of elements.

        Parameters
        ----------
        num : int
            New number of elements.
        fill : str
            String to insert in empty spaces.
        """

    def getContentString(self):
        """Returns a string containing values of the sequence elements.

        Reimplemented in AFX2DArrayConstString.
        """

    def getElementSeparator(self):
        """Returns the element separator character."""

    def getLength(self, index: int):
        """Returns the length in characters of a sequence element.

        Parameters
        ----------
        index : int
            Element index.
        """

    def getNumElements(self):
        """Returns the number of elements in this sequence."""

    def getPosition(self, index: int):
        """Returns the position in the content string of the beginning character of the sequence element.

        Parameters
        ----------
        index : int
            Element index.
        """

    def getValue(self, index: int):
        """Returns the value of a sequence element.

        Parameters
        ----------
        index : int
            Element index.
        """

    def insert(self, index: int, numElements: int, val: str):
        """Inserts many copies of an element.

        Parameters
        ----------
        index : int
            Element index at which inserting begins.
        numElements : int
            Number of elements to insert.
        val : str
            Value for the new elements.
        """

    def isValidSequence(self):
        """Returns True if this object contains a valid sequence."""

    def remove(self, index: int, numElements: int):
        """Removes elements starting at the given index.

        Parameters
        ----------
        index : int
            Element index at which removal begins.
        numElements : int
            Number of elements to remove.
        """

    def setContentString(self, seqstr: str):
        """Resets all values for the sequence elements.

        Parameters
        ----------
        seqstr : str
            Sequence string with new values.
        """

    def setElementSeparator(self, sep: str):
        """Sets the element separator character.

        Parameters
        ----------
        sep : str
            Separator character.
        """

    def setLength(self, index: int, length: int):
        """Sets the length of the sequence element.

        Parameters
        ----------
        index : int
            Element index.
        length : int
            New length (in characters).
        """

    def setPosition(self, index: int, position: int):
        """Sets the position of the sequence element.

        Parameters
        ----------
        index : int
            Element index.
        position : int
            New position within the string.
        """

    def setValue(self, index: int, value: str, replaceAll: bool = False):
        """Sets the value of a sequence element.

        Parameters
        ----------
        index : int
            Element index.
        value : str
            New value.
        replaceAll : bool
            If False (default), leading and trailing spaces will be preserved, otherwise, all space between separators will be replaced with the new value.
        """

    def trimWhiteSpace(self, index: int):
        """Adjusts the position and length of the element to trim leading and trailing white spaces.

        Parameters
        ----------
        index : int
            Element index.
        """
