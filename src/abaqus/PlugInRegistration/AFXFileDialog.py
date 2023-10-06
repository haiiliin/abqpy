from __future__ import annotations

from .AFXBoolKeyword import AFXBoolKeyword
from .AFXDialog import AFXDialog
from .AFXIntTarget import AFXIntTarget
from .AFXStringTarget import AFXStringTarget
from .FXObject import FXObject
from .FXWindow import FXWindow

#: A single file, existing or not (to save to).
AFXSELECTFILE_ANY: int = hash("AFXSELECTFILE_ANY")


class AFXFileDialog(AFXDialog):
    """AFXFileDialog."""

    def __init__(
        self,
        title: str,
        pathNameTgt: AFXStringTarget,
        readOnlyKw: AFXBoolKeyword,
        tgt: FXObject | None = None,
        sel: int = 0,
        mode: int = AFXSELECTFILE_ANY,
        patterns: str = "*",
        patternIndexTgt: AFXIntTarget | None = None,
    ):
        """Constructor that creates a dialog box that always occludes the main window when overlapping with the
        main window. The constructor expects a string target for storing the selected file name. If the dialog
        box allows multiple selection, the string target contains comma-separated path names of all selected
        files.

        Parameters
        ----------
        title : str
            Dialog title.
        pathNameTgt : AFXStringTarget
            Path name target.
        readOnlyKw : AFXBoolKeyword
            Read-only keyword.
        tgt : FXObject | None
            Message target.
        sel : int
            Message ID.
        mode : int
            File selection mode.
        patterns : str
            File filter patterns.
        patternIndexTgt : AFXIntTarget | None
            Index used to select a file filter pattern when the dialog box is posted.
        """

    def getCurrentPattern(self):
        """Returns the current pattern number."""

    def getDirectory(self):
        """Returns the current directory."""

    def getFileBoxStyle(self):
        """Return file list style."""

    def getFilename(self):
        """Returns the file name."""

    def getFilenames(self):
        """Returns an empty-string terminated list of selected file names, or 0 if none is selected."""

    def getItemSpace(self):
        """Returns the inter-item spacing (in pixels)."""

    def getPattern(self):
        """Returns the file pattern."""

    def getPatternList(self):
        """Returns the list of patterns."""

    def getPatternText(self, patno: int):
        """Returns the pattern text for a given pattern number.

        Parameters
        ----------
        patno : int
        """

    def getPressedButtonId(self):
        """Returns the ID of the button that the user pressed in the dialog box."""

    def getReadOnly(self):
        """Returns the read-only state."""

    def getReadOnlyPatterns(self):
        """Returns the patterns that force the enabling of the read-only button."""

    def getSelectMode(self):
        """Returns the file selection mode."""

    def setCurrentPattern(self, n: int):
        """Sets the current active pattern.

        Parameters
        ----------
        n : int
        """

    def setDirectory(self, path: str):
        """Sets the current directory.

        Parameters
        ----------
        path : str
        """

    def setFileBoxStyle(self, style: int):
        """Sets the file list style.

        Parameters
        ----------
        style : int
        """

    def setFilename(self, path: str):
        """Sets the file name.

        Parameters
        ----------
        path : str
        """

    def setItemSpace(self, s: int):
        """Sets the inter-item spacing (in pixels).

        Parameters
        ----------
        s : int
        """

    def setPattern(self, ptrn: str):
        """Sets the file pattern.

        Parameters
        ----------
        ptrn : str
        """

    def setPatternList(self, patterns: str):
        """Sets the list of file patterns.

        Parameters
        ----------
        patterns : str
        """

    def setPatternListMaxVisible(self, maxVisible: int):
        """Sets the maximum number of visible items for the file pattern list.

        Parameters
        ----------
        maxVisible : int
        """

    def setPatternText(self, patno: int, text: str):
        """Sets the pattern text for a pattern number.

        Parameters
        ----------
        patno : int

        text : str
        """

    def setReadOnly(self, state: bool):
        """Sets the initial state of read-only button.

        Parameters
        ----------
        state : bool
        """

    def setReadOnlyPatterns(self, patterns: str):
        """Sets the patterns that force the display of the read-only button; separate the entries by a newline
        character .

        Parameters
        ----------
        patterns : str
        """

    def setSelectMode(self, mode: int):
        """Sets the file selection mode.

        Parameters
        ----------
        mode : int
        """

    def show(self):
        """Posts the dialog box.

        Reimplemented from AFXDialog.
        """

    def showModal(self, occludedWindow: FXWindow | None = None):
        """Posts the dialog box as a modal dialog box. The dialog box is centered against the given widget or
        its owner widget if 0 is given.

        Parameters
        ----------
        occludedWindow : FXWindow | None
            Widget to be occluded (0 for the owner widget).
        """

    def shownReadOnly(self):
        """Returns True if the read-only button is shown."""

    def showReadOnly(self, show: bool):
        """Shows the read-only button.

        Parameters
        ----------
        show : bool
        """
