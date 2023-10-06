from __future__ import annotations

from .constants import DEFAULT_PAD
from .FXComposite import FXComposite
from .FXIcon import FXIcon
from .FXLabel import FXLabel
from .FXObject import FXObject

#: Button is up.
STATE_UP: int = hash("STATE_UP")

#: Button is down.
STATE_DOWN: int = hash("STATE_DOWN")

#: Button is engaged.
STATE_ENGAGED: int = hash("STATE_ENGAGED")

#: Same as STATE_UP (used for check buttons or radio buttons).
STATE_UNCHECKED: int = hash("STATE_UNCHECKED")

#: Same as STATE_ENGAGED (used for check buttons or radio buttons).
STATE_CHECKED: int = hash("STATE_CHECKED")

#: Automatically gray out when not updated.
BUTTON_AUTOGRAY: int = hash("BUTTON_AUTOGRAY")

#: Automatically hide button when not updated.
BUTTON_AUTOHIDE: int = hash("BUTTON_AUTOHIDE")

#: Toolbar style button \[flat look\].
BUTTON_TOOLBAR: int = hash("BUTTON_TOOLBAR")

#: May become default button when receiving focus.
BUTTON_DEFAULT: int = hash("BUTTON_DEFAULT")

#: This button is the initial default button.
BUTTON_INITIAL: int = hash("BUTTON_INITIAL")

#: Normal button style.
BUTTON_NORMAL: int = hash("BUTTON_NORMAL")


class FXButton(FXLabel):
    """A button provides a push button, with optional icon and/or text label.

    When pressed, the button widget sends a SEL_COMMAND to its target.
    """

    def __init__(
        self,
        p: FXComposite,
        text: str,
        ic: FXIcon | None = None,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = BUTTON_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = DEFAULT_PAD,
        pr: int = DEFAULT_PAD,
        pt: int = DEFAULT_PAD,
        pb: int = DEFAULT_PAD,
    ):
        """Construct button with text and icon.

        Parameters
        ----------
        p : FXComposite

        text : str

        ic : FXIcon | None

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
        """Returns True because a button can receive focus.

        Reimplemented from FXWindow. Reimplemented in AFXFlyoutItem.
        """

    def getButtonStyle(self):
        """Get the button style flags."""

    def getState(self):
        """Get the button state."""

    def setButtonStyle(self, style: int):
        """Set the button style flags.

        Parameters
        ----------
        style : int
        """

    def setDefault(self, enable: bool = True):
        """Set as default button. Reimplemented from FXWindow.

        Parameters
        ----------
        enable : bool
        """

    def setState(self, s: int):
        """Set the button state.

        Parameters
        ----------
        s : int
        """
