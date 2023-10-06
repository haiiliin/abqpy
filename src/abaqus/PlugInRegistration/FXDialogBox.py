from __future__ import annotations

from .FXTopWindow import PLACEMENT_CURSOR, FXTopWindow
from .FXWindow import FXWindow


class FXDialogBox(FXTopWindow):
    """DialogBox window.

    When receiving ID_CANCEL or ID_ACCEPT, the DialogBox breaks out of the modal loop and returns False or
    True, respectively. To close the DialogBox when not running modally, simply send it ID_HIDE.
    """

    #: Closes the dialog, cancel the entry.
    ID_CANCEL: int = hash("ID_CANCEL")

    #: Closes the dialog, accept the entry.
    ID_ACCEPT: int = hash("ID_ACCEPT")

    def __init__(
        self,
        owner: FXWindow,
        name: str,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = 10,
        pr: int = 10,
        pt: int = 10,
        pb: int = 10,
        hs: int = 4,
        vs: int = 4,
    ):
        """Construct dialog which will always float over the owner window.

        Parameters
        ----------
        owner : FXWindow

        name : str

        x : int

        y : int

        w : int

        h : int

        pl : int

        pr : int

        pt : int

        pb : int

        hs : int

        vs : int
        """

    def execute(self, placement: int = PLACEMENT_CURSOR):
        """Run modal invocation of the dialog. Reimplemented in FXInputDialog, and FXReplaceDialog.

        Parameters
        ----------
        placement : int
        """
