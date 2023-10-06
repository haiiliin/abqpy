from __future__ import annotations

from .FXComposite import FXComposite
from .FXIcon import FXIcon
from .FXMenuCaption import FXMenuCaption
from .FXObject import FXObject

#: Normal, unchecked state.
MENUSTATE_NORMAL: int = hash("MENUSTATE_NORMAL")

#: Checked with a checkmark.
MENUSTATE_CHECKED: int = hash("MENUSTATE_CHECKED")

#: Checked with a bullet.
MENUSTATE_RCHECKED: int = hash("MENUSTATE_RCHECKED")


class FXMenuCommand(FXMenuCaption):
    """The menu command widget is used to invoke a command in the application from a menu.

    Menu commands may reflect the state of the application by graying out, becoming hidden, or by a check
    mark or bullit.
    """

    def __init__(
        self,
        p: FXComposite,
        text: str,
        ic: FXIcon | None = None,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = 0,
    ):
        """Construct a menu command.

        Parameters
        ----------
        p : FXComposite

        text : str

        ic : FXIcon | None

        tgt : FXObject | None

        sel : int

        opts : int
        """

    def canFocus(self):
        """Yes it can receive the focus.

        Reimplemented from FXWindow.
        """

    def check(self):
        """Place checkmark next to text."""

    def checkRadio(self):
        """Place radio bullit next to text."""

    def getAccelText(self):
        """Return accelarator text."""

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXMenuCaption.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXMenuCaption.
        """

    def isChecked(self):
        """Return True if checked."""

    def isRadioChecked(self):
        """Return True if radio-checked."""

    def setAccelText(self, text: str):
        """Set accelerator text.

        Parameters
        ----------
        text : str
        """

    def uncheck(self):
        """Uncheck the item."""

    def uncheckRadio(self):
        """Uncheck radio bullit."""
