"""The following methods provide access to the standard message dialogs."""

from __future__ import annotations

from .FXObject import FXObject
from .FXWindow import FXWindow


def showAFXDismissableWarningDialog(owner: FXWindow, message: str, tgt: FXObject | None = None, sel: int = 0):
    """Posts a modal dismissable warning dialog box that has a "Show this dialog next time" check button, via
    which the user can request not to see a specific type of messages in the future. The dialog box has a
    getCheckButtonState method that can be called to get the state of the check button in the dialog box.

    Parameters
    ----------
    owner : FXWindow
        Window over which the dialog box is to be centered.
    message : str
        Text to be displayed in the dialog box.
    tgt : FXObject
        Message target.
    sel : int
        Message ID.
    """


def showAFXErrorDialog(owner: FXWindow, message: str, tgt: FXObject | None = None, sel: int = 0):
    """Shows an error dialog box.

    Parameters
    ----------
    owner : FXWindow
        Window over which the dialog box is to be centered.
    message : str
        Text to be displayed in the dialog box.
    tgt : FXObject
        Message target.
    sel : int
        Message ID.
    """


def showAFXItemsWarningDialog(
    owner: FXWindow, topMessage: str, items: str, bottomMessage: str, tgt: FXObject | None = None, sel: int = 0
):
    """Shows a modal warning dialog box that has a scrollable list of items and two messages: one placed above and one below the list. .

    Parameters
    ----------
    owner : FXWindow
        Window over which the dialog box is to be centered.
    topMessage : str
        Text to be displayed on top of the list of items.
    items : str
        A String containing a comma-separated list of items to be displayed between the topMessage and bottomMessage.
    bottomMessage : str
        Text to be displayed below the list of items.
    tgt : FXObject
        Message target.
    sel : int
        Message ID.
    """


def showAFXWarningDialog(owner: FXWindow, message: str, tgt: FXObject | None = None, sel: int = 0):
    """Shows a warning dialog box.

    Parameters
    ----------
    owner : FXWindow
        Window over which the dialog box is to be centered.
    message : str
        Text to be displayed in the dialog box.
    tgt : FXObject
        Message target.
    sel : int
        Message ID.
    """


def showAFXInformationDialog(owner: FXWindow, message: str, tgt: FXObject | None = None, sel: int = 0):
    """Shows an information dialog box.

    Parameters
    ----------
    owner : FXWindow
        Window over which the dialog box is to be centered.
    message : str
        Text to be displayed in the dialog box.
    tgt : FXObject
        Message target.
    sel : int
        Message ID.
    """
