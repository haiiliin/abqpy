from __future__ import annotations

from .constants import DEFAULT_PAD
from .FXComposite import FXComposite
from .FXLabel import FXLabel
from .FXObject import FXObject

#: Automatically gray out when not updated.
CHECKBUTTON_AUTOGRAY: int = hash("CHECKBUTTON_AUTOGRAY")

#: Automatically hide when not updated.
CHECKBUTTON_AUTOHIDE: int = hash("CHECKBUTTON_AUTOHIDE")

#: Normal check button.
CHECKBUTTON_NORMAL: int = hash("CHECKBUTTON_NORMAL")


class FXCheckButton(FXLabel):
    """A check button is a tri-state button.

    Normally, it is either True or False, and toggles between True or False whenever it is pressed. A third
    state MAYBE may be set to indicate that no selection has been made yet by the user, or that the state is
    ambiguous. When pressed, the check button sends a SEL_COMMAND to its target, and the message data
    represents the state of the check button.
    """

    def __init__(
        self,
        p: FXComposite,
        text: str,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = CHECKBUTTON_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = DEFAULT_PAD,
        pr: int = DEFAULT_PAD,
        pt: int = DEFAULT_PAD,
        pb: int = DEFAULT_PAD,
    ):
        """Construct new check button.

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
        """Returns True because a check button can receive focus.

        Reimplemented from FXWindow.
        """

    def getCheck(self):
        """Get check button state (True, False or MAYBE).

        Reimplemented in AFXCheckButton.
        """

    def getDefaultHeight(self):
        """Get default height.

        Reimplemented from FXLabel.
        """

    def getDefaultWidth(self):
        """Get default width.

        Reimplemented from FXLabel.
        """

    def setCheck(self, state: bool = True):
        """Set check button state (True, False or MAYBE).

        Parameters
        ----------
        state : bool
        """
