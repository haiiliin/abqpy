from __future__ import annotations

from .constants import PLACEMENT_CURSOR
from .FXApp import FXApp
from .FXWindow import FXWindow


class FXDialogBox:
    """Abaqus"""

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
