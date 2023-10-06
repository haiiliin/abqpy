from __future__ import annotations

from .FXObject import FXObject


class FXDataTarget(FXObject):
    """A Data Target allows a valuator widget such as a Slider or Text Field to be directly connected with a
    variable in the program.

    Whenever the valuator control changes, the variable connected through the data target is automatically
    updated; conversely, whenever the program changes a variable, all the connected valuator widgets will be
    updated to reflect this new value on the display. Data Targets also allow connecting Radio Buttons, Menu
    Commands, and so on to a variable. In this case, the new value of the connected variable is computed by
    substracting ID_OPTION from the message ID.
    """

    #: Will cause the FXDataTarget to ask sender for value.
    ID_VALUE: int = hash("ID_VALUE")

    #: ID_OPTION+i will set the value to i where -10000<=i<=10000.
    ID_OPTION: int = hash("ID_OPTION")

    def __init__(self, value: str, tgt: FXObject | None = None, sel: int = 0):
        """Associate with string variable.

        Parameters
        ----------
        value : str

        tgt : FXObject | None

        sel : int
        """

    def connect(self):
        """Associate with nothing."""

    def getData(self):
        """Return pointer to data its connected to."""

    def getSelector(self):
        """Get the message identifier for this data target."""

    def getTarget(self):
        """Get the message target object for this data target, if any."""

    def getType(self):
        """Return type of data its connected to."""

    def setSelector(self, sel: int):
        """Set the message identifier for this data target.

        Parameters
        ----------
        sel : int
        """

    def setTarget(self, t: FXObject):
        """Set the message target object for this data target.

        Parameters
        ----------
        t : FXObject
        """
