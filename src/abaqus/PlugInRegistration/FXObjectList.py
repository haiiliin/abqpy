from __future__ import annotations

from typing_extensions import Self

from .FXObject import FXObject


class FXObjectList:
    """List of pointers to objects."""

    def __init__(self, orig: Self):
        """Copy constructor.

        Parameters
        ----------
        orig : Self
        """

    def append(self, p: FXObject):
        """Append element.

        Parameters
        ----------
        p : FXObject
        """

    def clear(self):
        """Remove all elements."""

    def findb(self, p: FXObject, pos: int = 2147483647):
        """Find object in list, searching backward; return position or -1.

        Parameters
        ----------
        p : FXObject

        pos : int
        """

    def findf(self, p: FXObject, pos: int = 0):
        """Find object in list, searching forward; return position or -1.

        Parameters
        ----------
        p : FXObject

        pos : int
        """

    def insert(self, pos: int, p: FXObject):
        """Insert element at certain position.

        Parameters
        ----------
        pos : int

        p : FXObject
        """

    def no(self):
        """Return number of elements."""

    def remove(self, pos: int):
        """Remove element at pos.

        Parameters
        ----------
        pos : int
        """

    def size(self):
        """Return size of list.

        By clicking on Send, you accept that Dassault Systèmes will process your personal data and may
        contact you for further information. [Privacy Policy](
        https://www.3ds.com/privacy-policy).
        Total Results: Results per page
        """
