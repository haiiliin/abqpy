from __future__ import annotations

from .AFXDataComponent import AFXDataComponent
from .constants import DEFAULT_PAD
from .FXComposite import FXComposite
from .FXExponent import FXExponent
from .FXFont import FXFont
from .FXObject import FXObject
from .FXPacker import FXPacker

#: Value field is a string.
AFXTEXTFIELD_STRING: int = hash("AFXTEXTFIELD_STRING")

#: Value field is an integer.
AFXTEXTFIELD_INTEGER: int = hash("AFXTEXTFIELD_INTEGER")

#: Value field is a double.
AFXTEXTFIELD_FLOAT: int = hash("AFXTEXTFIELD_FLOAT")

#: Value fields consist of the real and imaginay components of a complex number.
AFXTEXTFIELD_COMPLEX: int = hash("AFXTEXTFIELD_COMPLEX")

#: Use a check button instead of a label.
AFXTEXTFIELD_CHECKBUTTON: int = hash("AFXTEXTFIELD_CHECKBUTTON")

#: Use a radio button instead of a label.
AFXTEXTFIELD_RADIOBUTTON: int = hash("AFXTEXTFIELD_RADIOBUTTON")

#: Orient label or button above text field.
AFXTEXTFIELD_VERTICAL: int = hash("AFXTEXTFIELD_VERTICAL")

#: Configure text field to the read-only state.
AFXTEXTFIELD_READONLY: int = hash("AFXTEXTFIELD_READONLY")

#: Allow IME (Japanese etc.) input.
AFXTEXTFIELD_IME: int = hash("AFXTEXTFIELD_IME")


class AFXTextField(FXPacker, AFXDataComponent):
    """This class contains a label that precedes a text field that allows the user to enter in text."""

    #: ID for setting imaginary values.
    ID_SETIMAGINARYVALUE: int = hash("ID_SETIMAGINARYVALUE")

    #: ID for getting imaginary values.
    ID_GETIMAGINARYVALUE: int = hash("ID_GETIMAGINARYVALUE")

    #: ID for the check/radio button.
    ID_BUTTON: int = hash("ID_BUTTON")

    #: ID for the text field.
    ID_TEXT: int = hash("ID_TEXT")

    #: ID for the text field with imaginary part.
    ID_IMG_TEXT: int = hash("ID_IMG_TEXT")

    def __init__(
        self,
        p: FXComposite,
        ncols: int,
        labelText: str,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = AFXTEXTFIELD_STRING,
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
            Left padding (margin).
        pr : int
            Right padding (margin).
        pt : int
            Top padding (margin).
        pb : int
            Bottom padding (margin).
        """

    def create(self):
        """Creates the text field.

        Reimplemented from FXComposite.
        """

    def disable(self):
        """Disables the text field.

        Reimplemented from FXWindow.
        """

    def enable(self):
        """Enables the text field.

        Reimplemented from FXWindow.
        """

    def getCheck(self):
        """Returns the state of the check button or the radio button."""

    def getCursorPos(self):
        """Returns the cursor position."""

    def getDefaultWidth(self):
        """Returns the default width of the text field.

        Reimplemented from FXPacker.
        """

    def getExponentType(self):
        """Returns the exponent type of the text field for real and complex types."""

    def getImaginaryText(self):
        """Returns the imaginary text for the complex text field."""

    def getJustify(self):
        """Returns the text justification mode."""

    def getLabelFont(self):
        """Returns the label's font."""

    def getLabelText(self):
        """Returns the label text."""

    def getNumColumns(self):
        """Returns the number of columns."""

    def getPrecision(self):
        """Returns the precision of the text field for real and complex types."""

    def getText(self):
        """Returns the text."""

    def getValueType(self):
        """Returns the value type (AFXTEXTFIELD_FLOAT, etc.) of the text field."""

    def isEditable(self):
        """Returns True if the text in the input field may be edited."""

    def isReadOnlyState(self):
        """Returns True if the text field appears in the read-only state."""

    def isVerticalLayout(self):
        """Returns True if the layout orientation is vertical."""

    def setCheck(self, state: bool):
        """Sets the state of the check button or the radio button.

        Parameters
        ----------
        state : bool
            Check state.
        """

    def setCheckButtonSelector(self, sel: int):
        """Sets the message ID of the check button or the radio button.

        Parameters
        ----------
        sel : int
            Selector.
        """

    def setCheckButtonTarget(self, checkVal: bool = False):
        """Sets the message target of the check button or the radio button.

        Parameters
        ----------
        checkVal : bool
            Check state.
        """

    def setCursorPos(self, pos: int):
        """Sets the cursor position.

        Parameters
        ----------
        pos : int
            Position.
        """

    def setEditable(self, edit: bool = True):
        """Sets the editable state for the text field.

        Parameters
        ----------
        edit : bool
            If True, text can be edited.
        """

    def setExponentType(self, e: FXExponent):
        """Sets the exponent type of the text field for real and complex types.

        Parameters
        ----------
        e : FXExponent
            Exponent type.
        """

    def setFocus(self):
        """Moves the focus to the text field.

        Reimplemented from FXWindow.
        """

    def setFocusAndSelection(self):
        """Sets the focus to the input field and selects its contents."""

    def setFocusToCheckButton(self):
        """Moves the focus to the check button or the radio button (if existed) of the widget."""

    def setFocusToImaginaryTextField(self):
        """Moves the focus to the input field for the imaginary part."""

    def setFocusToTextField(self):
        """Moves the focus to the input field of the widget."""

    def setImaginaryFocusAndSelection(self):
        """Sets the focus to the input field for the imaginary part and selects its contents."""

    def setImaginaryText(self, text: str):
        """Sets the imaginary text for the complex text field.

        Parameters
        ----------
        text : str
            Imaginary text field text.
        """

    def setJustify(self, mode: int):
        """Sets the text justification mode.

        Parameters
        ----------
        mode : int
            Justification flag.
        """

    def setLabelFont(self, fnt: FXFont):
        """Sets the label's text font.

        Parameters
        ----------
        fnt : FXFont
            Label font.
        """

    def setLabelText(self, txt: str):
        """Sets the label text.

        Parameters
        ----------
        txt : str
            Label text.
        """

    def setNumColumns(self, cols: int):
        """Sets the number of columns. Note: The column width is based on the width of "m" of the font used.

        Parameters
        ----------
        cols : int
            Number of columns.
        """

    def setPrecision(self, p: int):
        """Sets the precision of the text field for real and complex types. Limitation: If an AFXTextField
        widget uses an AFXFloatKeyword object as its target, the widget must have AFXTEXTFIELD_FLOAT as one of
        its options for the precision setting to take effect.

        Parameters
        ----------
        p : int
            Precision.
        """

    def setReadOnlyState(self, readonly: bool = True):
        """Sets the read-only state of the text field.

        Parameters
        ----------
        readonly : bool
            Read-only state.
        """

    def setSelection(self, pos: int, len: int):
        """Select the specified number of characters starting at given position.

        Parameters
        ----------
        pos : int
            Position.
        len : int
            Length.
        """

    def setText(self, text: str):
        """Sets the text in the input field.

        Parameters
        ----------
        text : str
            Text field text.
        """

    def setValueType(self, type: int):
        """Sets the value type (AFXTEXTFIELD_FLOAT, etc.) of the text field.

        Parameters
        ----------
        type : int
            Value type.
        """

    def setVerticalLayout(self, vertical: bool):
        """Sets the layout orientation of the text field.

        Parameters
        ----------
        vertical : bool
            Vertical flag.
        """
