from __future__ import annotations
from .constants import AFXFLYOUT_NORMAL
from .FXComposite import FXComposite
from .FXLabel import FXLabel
from .FXPopup import FXPopup


class AFXFlyoutButton(FXLabel):
    """This class contains a button that acts like a regular FXButton when pressed and released quickly but displays a popup menu when pressed and held for a short time duration."""

    def __init__(
        self,
        p: FXComposite,
        pup: FXPopup | None = None,
        act: int = 0,
        opts: int = AFXFLYOUT_NORMAL,
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
        pup : FXPopup | None
            Popup containing flyout items.
        act : int
            Current button index (0-based).
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
        """Returns True (because a flyout button can receive focus). Reimplemented from FXWindow."""

    def create(self):
        """Creates the flyout button. Reimplemented from FXLabel."""

    def detach(self):
        """Detaches server-side resources for the flyout button. Reimplemented from FXLabel."""

    def disable(self):
        """Disables the flyout button. Reimplemented from FXLabel."""

    def enable(self):
        """Enables the flyout button. Reimplemented from FXLabel."""

    def getButtonStyle(self):
        """Returns the flyout button style."""

    def getCurrentItem(self):
        """Returns the current item."""

    def getPane(self):
        """Returns the popup menu."""

    def getState(self):
        """Returns the flyout button state."""

    def setButtonStyle(self, style: int):
        """Sets the flyout button style.

        Parameters
        ----------
        style : int
            Button style (see Flags for flyout button options.)
        """

    def setCurrentItem(self, index: int, setCheck: bool = False):
        """Sets the current item and depresses the button if setCheck is True. The specified item index is 0-based, and only valid items are counted (items such as separators are not counted).

        Parameters
        ----------
        index : int
            Index.
        setCheck : bool
            Value of check button.
        """

    def setPane(self, pup: FXPopup):
        """Sets the popup menu.

        Parameters
        ----------
        pup : FXPopup
            Popup menu.
        """

    def setState(self, state: int):
        """Sets the flyout button state.

        Parameters
        ----------
        state : int
            State (see FXButton's Button state bits).
        """
