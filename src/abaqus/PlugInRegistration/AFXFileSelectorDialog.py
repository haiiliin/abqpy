from __future__ import annotations

from .AFXBoolKeyword import AFXBoolKeyword
from .AFXFileDialog import AFXFileDialog
from .AFXIntTarget import AFXIntTarget
from .AFXStringTarget import AFXStringTarget
from .FXWindow import FXWindow

#: A single file, existing or not (to save to).
AFXSELECTFILE_ANY: int = hash("AFXSELECTFILE_ANY")

#: An existing file (to load).
AFXSELECTFILE_EXISTING: int = hash("AFXSELECTFILE_EXISTING")

#: Multiple existing files.
AFXSELECTFILE_MULTIPLE: int = hash("AFXSELECTFILE_MULTIPLE")

#: Multiple existing files or directories.
AFXSELECTFILE_MULTIPLE_ALL: int = hash("AFXSELECTFILE_MULTIPLE_ALL")

#: Existing directory.
AFXSELECTFILE_DIRECTORY: int = hash("AFXSELECTFILE_DIRECTORY")


class AFXFileSelectorDialog(AFXFileDialog):
    """Abaqus."""

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
        """Constructor typically used to create a dialog box that is posted from another dialog box (e.g. from a
        "Select..." button); a target is used for the pathName. If the dialog box allows multiple selection, the
        pathName target contains comma-separated path names of all selected files.

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
