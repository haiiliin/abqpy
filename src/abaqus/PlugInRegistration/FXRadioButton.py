from __future__ import annotations

from .constants import DEFAULT_PAD
from .FXComposite import FXComposite
from .FXLabel import FXLabel
from .FXObject import FXObject

#: Automatically gray out when not updated.
RADIOBUTTON_AUTOGRAY: int = hash("RADIOBUTTON_AUTOGRAY")

#: Automatically hide when not updated.
RADIOBUTTON_AUTOHIDE: int = hash("RADIOBUTTON_AUTOHIDE")

#: Normal radio button style.
RADIOBUTTON_NORMAL: int = hash("RADIOBUTTON_NORMAL")


class FXRadioButton(FXLabel):
    """A radio button is a tri-state button.

    Normally, it is either True or False; a third state MAYBE may be set to indicate that no selection has
    been made yet by the user, or that the state is ambiguous. When pressed, the radio button sets its state
    to True and sends a SEL_COMMAND to its target, and the message data set to the state of the radio
    button, of the type FXbool. If the radio button is contained inside a group box, the other radio buttons
    in the group box will be set to False and will send a message as well.
    """

    def __init__(
        self,
        p: FXComposite,
        text: str,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = RADIOBUTTON_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = DEFAULT_PAD,
        pr: int = DEFAULT_PAD,
        pt: int = DEFAULT_PAD,
        pb: int = DEFAULT_PAD,
    ):
        """Construct new radio button.

        Parameters
        ----------
        p : FXComposite

        text : str

        tgt : FXObject | None

        sel : int

        opts : int

        x : int

        y : int

        w : int

        h : int

        pl : int

        pr : int

        pt : int

        pb : int
        """

    def canFocus(self):
        """Returns True because a radio button can receive focus.

        Reimplemented from FXWindow.
        """

    def getCheck(self):
        """Get radio button state (True, False or MAYBE)."""

    def getDefaultHeight(self):
        """Get default height.

        Reimplemented from FXLabel.
        """

    def getDefaultWidth(self):
        """Get default width.

        Reimplemented from FXLabel.
        """

    def setCheck(self, s: bool = True):
        """Set radio button state (True, False or MAYBE).

        Parameters
        ----------
        s : bool
        """
