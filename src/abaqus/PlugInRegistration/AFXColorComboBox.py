from __future__ import annotations

from .constants import DEFAULT_SPACING
from .FXColor import FXColor
from .FXComposite import FXComposite
from .FXFont import FXFont
from .FXObject import FXObject
from .FXPacker import FXPacker

#: Orient label above button.
AFXCOLORBUTTON_VERTICAL: int = hash("AFXCOLORBUTTON_VERTICAL")


class AFXColorComboBox(FXPacker):
    """This class contains a label that precedes a color well, which allows the user to bring up a color dialog
    box by double clicking.

    When connected to an AFXStringKeyword, this widget will assign the value of the button's current color
    to the keyword in hex format (for example, "FF0000").
    """

    def AFXColorButton(
        self,
        p: FXComposite,
        text: str,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = 0,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = DEFAULT_SPACING,
        pr: int = DEFAULT_SPACING,
        pt: int = DEFAULT_SPACING,
        pb: int = DEFAULT_SPACING,
    ):
        """Constructor.

        Parameters
        ----------
        p : FXComposite
            Parent widget.
        text : str
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
            Width of the widget.
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
        """Creates the color button widget.

        Reimplemented from FXComposite.
        """

    def disable(self):
        """Disables the color button.

        Reimplemented from FXWindow.
        """

    def enable(self):
        """Enables the color button.

        Reimplemented from FXWindow.
        """

    def getHelpText(self):
        """Returns the status line help text."""

    def getLabelFont(self):
        """Returns the label font."""

    def getLabelText(self):
        """Returns the label string."""

    def getRGBA(self):
        """Returns the color of the button."""

    def getTipText(self):
        """Returns the tool tip message."""

    def setHelpText(self, text: str):
        """Sets the status line help text.

        Parameters
        ----------
        text : str
        """

    def setLabelFont(self, fnt: FXFont):
        """Sets the label font.

        Parameters
        ----------
        fnt : FXFont
        """

    def setLabelText(self, txt: str):
        """Sets the label string.

        Parameters
        ----------
        txt : str
        """

    def setRGBA(self, clr: FXColor):
        """Sets the color of the button.

        Parameters
        ----------
        clr : FXColor
        """

    def setTipText(self, text: str):
        """Sets the tool tip message.

        Parameters
        ----------
        text : str
        """
