from __future__ import annotations

from .FXObject import FXObject


class AFXColumnItems(FXObject):
    """Abaqus."""

    def __init__(self, referenceColumn: int, tgt: FXObject | None = None, sel: int = 0, opts: int = 0):
        """Constructor for use with a keyword.

        Parameters
        ----------
        referenceColumn : int
            Index of the reference column.
        tgt : FXObject | None
            Message target.
        sel : int
            Message ID.
        opts : int
            Selection options (not used).
        """

    def getReferenceColumn(self):
        """Returns the index of the table reference column."""

    def getSelector(self):
        """Returns the message ID."""

    def getTarget(self):
        """Returns the message target."""

    def setReferenceColumn(self, index: int):
        """Sets the table reference column, whose selected items will be sent to the target.

        Parameters
        ----------
        index : int
            Table column index.
        """

    def setSelector(self, sel: int):
        """Sets the message ID.

        Parameters
        ----------
        sel : int
            New message ID.
        """

    def setTarget(self, tgt: FXObject):
        """Sets the message target.

        Parameters
        ----------
        tgt : FXObject
            New message target.
        """
