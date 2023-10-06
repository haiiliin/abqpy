from __future__ import annotations

from .AFXDataComponent import AFXDataComponent
from .FXComposite import FXComposite
from .FXObject import FXObject
from .FXPacker import FXPacker

#: Slider shown horizontally.
AFXSLIDER_HORIZONTAL: int = hash("AFXSLIDER_HORIZONTAL")

#: Slider shown vertically.
AFXSLIDER_VERTICAL: int = hash("AFXSLIDER_VERTICAL")

#: Slider has arrow head pointing up.
AFXSLIDER_ARROW_UP: int = hash("AFXSLIDER_ARROW_UP")

#: Slider has arrow head pointing down.
AFXSLIDER_ARROW_DOWN: int = hash("AFXSLIDER_ARROW_DOWN")

#: Slider has arrow head pointing left.
AFXSLIDER_ARROW_LEFT: int = hash("AFXSLIDER_ARROW_LEFT")

#: Slider has arrow head pointing right.
AFXSLIDER_ARROW_RIGHT: int = hash("AFXSLIDER_ARROW_RIGHT")

#: Slider is inside the slot rather than overhanging.
AFXSLIDER_INSIDE_BAR: int = hash("AFXSLIDER_INSIDE_BAR")

#: Show slider value.
AFXSLIDER_SHOW_VALUE: int = hash("AFXSLIDER_SHOW_VALUE")

#: Show slider above its title.
AFXSLIDER_ABOVE_TITLE: int = hash("AFXSLIDER_ABOVE_TITLE")

#: Show slider after its title.
AFXSLIDER_AFTER_TITLE: int = hash("AFXSLIDER_AFTER_TITLE")

#: Default slider options--slider is horizontal, inside the slot, and shown above its title label.
AFXSLIDER_NORMAL: int = hash("AFXSLIDER_NORMAL")


class AFXSlider(FXPacker, AFXDataComponent):
    """This class provides a slider, which allows the user to specify a value by dragging its value
    indicator."""

    #: ID for the slider.
    ID_SLIDER: int = hash("ID_SLIDER")

    #: Last ID for this class.
    ID_LAST: int = hash("ID_LAST")

    def __init__(
        self,
        p: FXComposite,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = AFXSLIDER_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = 0,
        pr: int = 0,
        pt: int = 0,
        pb: int = 0,
    ):
        """Constructor.

        Parameters
        ----------
        p : FXComposite
            Parent widget.
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

    def canFocus(self):
        """Returns True because a slider can receive focus.

        Reimplemented from FXWindow.
        """

    def disable(self):
        """Disables the slider.

        Reimplemented from FXWindow.
        """

    def enable(self):
        """Enables the slider.

        Reimplemented from FXWindow.
        """

    def getDecimalPlaces(self):
        """Returns the number of decimal points displayed."""

    def getDefaultHeight(self):
        """Returns the default height.

        Reimplemented from FXPacker.
        """

    def getDefaultWidth(self):
        """Returns the default width.

        Reimplemented from FXPacker.
        """

    def getIncrement(self):
        """Returns the slider's auto-increment/decrement value."""

    def getMaxLabelText(self):
        """Returns the maximum label's text."""

    def getMinLabelText(self):
        """Returns the minimum label's text."""

    def getRange(self):
        """Returns a sequence of ints (low, high) representing the widget's allowable minimum and maximum
        values."""

    def getSliderStyle(self):
        """Returns the slider's style."""

    def getTipText(self):
        """Returns the slider's tip text."""

    def getTitleLabelJustify(self):
        """Returns the title label's justification mode."""

    def getTitleLabelText(self):
        """Returns the title label's text."""

    def getValue(self):
        """Returns the slider's value."""

    def recalc(self):
        """Recalculates the slider.

        Redefined to handle slider movement. Reimplemented from FXWindow.
        """

    def setDecimalPlaces(self, dp: int):
        """Sets the number of decimal points displayed.

        Parameters
        ----------
        dp : int
            Number of decimal places.
        """

    def setIncrement(self, inc: int):
        """Sets the slider's auto-increment/decrement value.

        Parameters
        ----------
        inc : int
            Increment.
        """

    def setMaxLabelText(self, text: str):
        """Sets the maximum label's text.

        Parameters
        ----------
        text : str
            Max label text.
        """

    def setMinLabelText(self, text: str):
        """Sets the minimum label's text.

        Parameters
        ----------
        text : str
            Min label text.
        """

    def setRange(self, lo: int, hi: int):
        """Sets the slider's maximum and minimum values.

        Parameters
        ----------
        lo : int
            Minimum value.
        hi : int
            Maximum value.
        """

    def setSliderStyle(self, style: int):
        """Sets the slider's style.

        Parameters
        ----------
        style : int
            Style flag.
        """

    def setTipText(self, text: str):
        """Sets the slider's tip text.

        Parameters
        ----------
        text : str
            Tip text.
        """

    def setTitleLabelJustify(self, mode: int):
        """Sets the title label's justification mode.

        Parameters
        ----------
        mode : int
            Justification mode.
        """

    def setTitleLabelText(self, text: str):
        """Sets the title label's text.

        Parameters
        ----------
        text : str
            Title text.
        """

    def setValue(self, value: int):
        """Sets the slider's value.

        Parameters
        ----------
        value : int
            Value.
        """

    def show(self):
        """Shows the slider.

        Reimplemented from FXWindow.
        """
