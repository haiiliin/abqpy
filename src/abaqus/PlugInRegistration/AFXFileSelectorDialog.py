from __future__ import annotations

from .AFXBoolKeyword import AFXBoolKeyword
from .AFXFileDialog import AFXFileDialog
from .AFXIntTarget import AFXIntTarget
from .AFXStringTarget import AFXStringTarget
from .constants import AFXSELECTFILE_ANY
from .FXWindow import FXWindow


class AFXFileSelectorDialog(AFXFileDialog):
    """Abaqus"""

    def __init__(
        self,
        owner: FXWindow,
        title: str,
        pathNameTgt: AFXStringTarget,
        readOnlyKw: AFXBoolKeyword,
        mode: int = AFXSELECTFILE_ANY,
        patterns: str = "*",
        patternIndexTgt: AFXIntTarget | None = None,
    ):
        """Constructor typically used to create a dialog box that is posted from another dialog box (e.g. from a "Select..." button); a target is used for the pathName. If the dialog box allows multiple selection, the pathName target contains comma-separated path names of all selected files.

        Parameters
        ----------
        owner : FXWindow
            Owner
        title : str
            Dialog box title.
        pathNameTgt : AFXStringTarget
            Path name target.
        readOnlyKw : AFXBoolKeyword
            Read-only keyword.
        mode : int
            File selection mode.
        patterns : str
            File filter patterns.
        patternIndexTgt : AFXIntTarget | None
            Index used to select a file filter pattern when the dialog box is posted.
        """
