from __future__ import annotations

from .AFXDataComponent import AFXDataComponent
from .constants import DEFAULT_PAD
from .FXComposite import FXComposite
from .FXFont import FXFont
from .FXObject import FXObject
from .FXPacker import FXPacker

#: Use a check button instead of a label.
AFXSPINNER_CHECKBUTTON: int = hash("AFXSPINNER_CHECKBUTTON")

#: Use a radio button instead of a label.
AFXSPINNER_RADIOBUTTON: int = hash("AFXSPINNER_RADIOBUTTON")

#: Orient label or button above spinner.
AFXSPINNER_VERTICAL: int = hash("AFXSPINNER_VERTICAL")

#: Configure spinner to the read-only state.
AFXSPINNER_READONLY: int = hash("AFXSPINNER_READONLY")


class AFXSpinner(FXPacker, AFXDataComponent):
    """This class contains a label that precedes a spin box that allows the user to specify a value by clicking
    on its arrow buttons."""

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
            Number of columns.
        labelText : str
            Label string.
        tgt : FXObject | None
            Message target.
        sel : int
            Message ID
        opts : int
            Options and hints.
        x : int
            X coordinate of the origin.
        y : int
            Y coordinate of the origin.
        w : int
            Width of the widget.
        h : int
            Height of the widget.
        pl : int
            Left padding (margin).
        pr : int
            Right padding (margin).
        pt : int
            Top padding (margin).
        pb : int
            Bottom padding (margin).
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
        """Returns a sequence of ints (low, high) representing the widget's allowable minimum and maximum
        values."""

    def getTipText(self):
        """Returns the tool tip message."""

    def getValue(self):
        """Returns the spinner value."""

    def isEditable(self):
        """Returns True if the text in the text field may be edited."""

    def isReadOnlyState(self):
        """Returns True if the spinner appears in the read-only state."""

    def setCheck(self, state: bool):
        """Sets the state of the check button or the radio button.

        Parameters
        ----------
        state : bool
            State.
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
        """Sets the editable state for the input field.

        Parameters
        ----------
        edit : bool
            If True, input field is editable.
        """

    def setHelpText(self, text: str):
        """Sets the status line help text.

        Parameters
        ----------
        text : str
            Help text.
        """

    def setIncrement(self, incr: int):
        """Sets the spinner increment.

        Parameters
        ----------
        incr : int
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

    def setRange(self, low: int, high: int):
        """Sets the spinner range.

        Parameters
        ----------
        low : int
            Minimum value.
        high : int
            Maximum value.
        """

    def setReadOnlyState(self, readonly: bool = True):
        """Sets the read-only state of the spinner.

        Parameters
        ----------
        readonly : bool
            State.
        """

    def setTipText(self, text: str):
        """Sets the tool tip message.

        Parameters
        ----------
        text : str
            Tooltip text.
        """

    def setValue(self, val: int, notify: bool = False):
        """Sets the spinner's value.

        Parameters
        ----------
        val : int
            Value.
        notify : bool
            Notification flag.
        """
