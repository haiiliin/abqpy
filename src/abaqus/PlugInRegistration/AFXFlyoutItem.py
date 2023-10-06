from __future__ import annotations

from .FXButton import FXButton
from .FXComposite import FXComposite
from .FXIcon import FXIcon
from .FXObject import FXObject


class AFXFlyoutItem(FXButton):
    """This class contains a button that is placed in the popup menu of the flyout button."""

    def __init__(
        self,
        p: FXComposite,
        text: str,
        ic: FXIcon | None = None,
        tgt: FXObject | None = None,
        sel: int = 0,
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
        text : str
            Label string.
        ic : FXIcon | None
            Icon.
        tgt : FXObject | None
            Message target.
        sel : int
            Message ID.
        x : int
            X coordinate of origin.
        y : int
            Y c coordinate of origin.
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
        """Returns True (because a flyout item can receive focus).

        Reimplemented from FXButton.
        """

    def hide(self):
        """Hides the flyout item.

        Reimplemented from FXWindow.
        """

    def setIcon(self, ic: FXIcon):
        """Sets the icon for the flyout item. Reimplemented from FXLabel.

        Parameters
        ----------
        ic : FXIcon
        """
