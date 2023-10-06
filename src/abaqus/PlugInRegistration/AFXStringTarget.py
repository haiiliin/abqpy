from __future__ import annotations


class AFXStringTarget:
    """|"""

    def __init__(self, initialValue: str = "''"):
        """Constructor.

        Parameters
        ----------
        initialValue : str
            Initial value.
        """

    def getTypeName(self):
        """Returns the name of the target type ("String"). Implements AFXTarget."""

    def getValue(self):
        """Returns the target's current value."""

    def setValue(self, newValue: str):
        """Sets the target's current value.

        Parameters
        ----------
        newValue : str
            New value.
        """
