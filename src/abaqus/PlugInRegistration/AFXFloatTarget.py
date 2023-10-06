from __future__ import annotations


class AFXFloatTarget:
    """|"""

    def __init__(self, initialValue: float = 0.0):
        """Constructor.

        Parameters
        ----------
        initialValue : float
            Initial value.
        """

    def getTypeName(self):
        """Returns the name of the target type ("Float"). Implements AFXTarget."""

    def getValue(self):
        """Returns the target's current value."""

    def setValue(self, newValue: float):
        """Sets the target's current value.

        Parameters
        ----------
        newValue : float
            New value.
        """
