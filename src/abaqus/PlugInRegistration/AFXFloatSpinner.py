from __future__ import annotations

from .AFXDataComponent import AFXDataComponent
from .constants import DEFAULT_PAD
from .FXComposite import FXComposite
from .FXFont import FXFont
from .FXObject import FXObject
from .FXPacker import FXPacker

#: Use a check button instead of a label.
AFXFLOATSPINNER_CHECKBUTTON: int = hash("AFXFLOATSPINNER_CHECKBUTTON")

#: Use a radio button instead of a label.
AFXFLOATSPINNER_RADIOBUTTON: int = hash("AFXFLOATSPINNER_RADIOBUTTON")

#: Orient label or button above spinner.
AFXFLOATSPINNER_VERTICAL: int = hash("AFXFLOATSPINNER_VERTICAL")

#: Configure spinner to the read-only state.
AFXFLOATSPINNER_READONLY: int = hash("AFXFLOATSPINNER_READONLY")


class AFXFloatSpinner(FXPacker, AFXDataComponent):
    """Convenience class for creating a labeled spinner.

    The label field can be a label or check button (AFXFLOATSPINNER_CHECKBUTTON option).
    """

    #: ID for the check or radio button.
    ID_BUTTON: int = hash("ID_BUTTON")

    #: ID for the spinner.
    ID_SPINNER: int = hash("ID_SPINNER")

    def __init__(
        self,
        p: FXComposite,
        ncols: int,
        labelText: str,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = 0,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = DEFAULT_PAD,
        pr: int = DEFAULT_PAD,
        pt: int = DEFAULT_PAD,
        pb: int = DEFAULT_PAD,
    ):
        """Constructor.

        Parameters
        ----------
        p : FXComposite
            Parent widget.
        ncols : int
            Number of columns in the spinner.
        labelText : str
            Label preceeding spinner.
        tgt : FXObject | None
            Message target.
        sel : int
            Message ID.
        opts : int
            Options and hints.
        x : int
            X coordinate of origin.
        y : int
            Y coordinate of origin.
        w : int
            Width of the widget.
        h : int
            Height of the widget.
        pl : int
            Left padding.
        pr : int
            Right padding.
        pt : int
            Top padding.
        pb : int
            Bottom padding.
        """

    def canFocus(self):
        """Returns True if the spinner can recieve focus.

        Reimplemented from FXWindow.
        """

    def create(self):
        """Creates the spinner.

        Reimplemented from FXComposite.
        """

    def disable(self):
        """Disables the spinner.

        Reimplemented from FXWindow.
        """

    def enable(self):
        """Enables the spinner.

        Reimplemented from FXWindow.
        """

    def getCheck(self):
        """Returns the state of the check button or the radio button."""

    def getHelpText(self):
        """Returns the status line help text."""

    def getIncrement(self):
        """Returns the spinner increment."""

    def getLabelFont(self):
        """Returns the label font."""

    def getLabelText(self):
        """Returns the label string."""

    def getRange(self):
        """Returns a sequence of floats (low, high) representing the widget's allowable minimum and maximum
        values."""

    def getTipText(self):
        """Returns the tool tip message."""

    def getValue(self):
        """Returns the spinner value."""

    def isCheckStateChanged(self):
        """Returns True if the state of the check button or the radio button has changed by the user since it
        was programmatically set last time."""

    def isEditable(self):
        """Returns True if the input field of spinner may be edited."""

    def isReadOnlyState(self):
        """Returns True if the spinner is set to the read-only state."""

    def setCheck(self, state: bool):
        """Sets the state of the check button or the radio button.

        Parameters
        ----------
        state : bool
            Button state.
        """

    def setCheckButtonSelector(self, sel: int):
        """Sets the message ID of the check button or the radio button.

        Parameters
        ----------
        sel : int
            Selector.
        """

    def setCheckButtonTarget(self, tgt: FXObject):
        """Sets the message target of the check button or the radio button.

        Parameters
        ----------
        tgt : FXObject
            Target.
        """

    def setEditable(self, edit: bool = True):
        """Sets the editable state for the input field of spinner.

        Parameters
        ----------
        edit : bool
            Editable state.
        """

    def setHelpText(self, text: str):
        """Sets the status line help text.

        Parameters
        ----------
        text : str
            Help text.
        """

    def setIncrement(self, incr: float):
        """Sets the spinner increment.

        Parameters
        ----------
        incr : float
            Increment.
        """

    def setLabelFont(self, fnt: FXFont):
        """Sets the label font.

        Parameters
        ----------
        fnt : FXFont
            Label font.
        """

    def setLabelText(self, txt: str):
        """Sets the label string.

        Parameters
        ----------
        txt : str
            Label text.
        """

    def setRange(self, low: float, high: float):
        """Sets the spinner range.

        Parameters
        ----------
        low : float
            Minimum value.
        high : float
            Maximum value.
        """

    def setReadOnlyState(self, edit: bool = True):
        """Sets the read-only state of the spinner.

        Parameters
        ----------
        edit : bool
            Read-only state.
        """

    def setTipText(self, text: str):
        """Sets the tool tip message.

        Parameters
        ----------
        text : str
            Tooltip text.
        """

    def setValue(self, val: float, notify: bool = False):
        """Sets the spinner value.

        Parameters
        ----------
        val : float
            Value.
        notify : bool
            Notification flag.
        """
