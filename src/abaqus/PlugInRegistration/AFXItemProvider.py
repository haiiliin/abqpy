from __future__ import annotations

from .FXObject import FXObject


class AFXItemProvider(FXObject):
    """This class provides a way to supply items to widgets, such as AFXComboBox and AFXList."""

    def __init__(self, initialItems: str = "''"):
        """Constructor.

        Parameters
        ----------
        initialItems : str
            Sequence string with initial items.
        """

    def append(self, ch: str):
        """Appends a character to the item string.

        Parameters
        ----------
        ch : str
        """

    def empty(self):
        """Returns True if the item string is empty."""

    def getItems(self):
        """Returns a sequence string that contains all of the provider's items."""

    def getVersion(self):
        """Returns the version of provider's items."""

    def reset(self, sz: int = 0):
        """Clears the contents of the item string and reallocates space.

        Parameters
        ----------
        sz : int
        """

    def setItems(self, newItems: str):
        """Sets all of the providers's items, clearing any previous items first.

        Parameters
        ----------
        newItems : str
            Sequence string with new items.
        """
