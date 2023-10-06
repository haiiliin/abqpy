from __future__ import annotations

from .constants import PLACEMENT_CURSOR
from .FXTopWindow import FXTopWindow
from .FXWindow import FXWindow


class FXDialogBox(FXTopWindow):
    """DialogBox window. When receiving ID\_CANCEL or ID\_ACCEPT, the DialogBox breaks out of the modal loop and returns False or True, respectively. To close the DialogBox when not running modally, simply send it ID_HIDE."""

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
