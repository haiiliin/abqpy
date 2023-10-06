from __future__ import annotations


class AFXIntTarget:
    """|"""

    def __init__(self, initialValue: int = 0):
        """Constructor.

        Parameters
        ----------
        initialValue : int
            Initial value.
        """

    def getTypeName(self):
        """Returns the name of the target type ("Int"). Implements AFXTarget."""

    def getValue(self):
        """Returns the target's current value."""

    def setValue(self, newValue: int):
        """Sets the target's current value.

        Parameters
        ----------
        newValue : int
            New value.
        """
