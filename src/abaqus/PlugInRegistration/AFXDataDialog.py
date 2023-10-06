from __future__ import annotations

from .AFXBoolKeyword import AFXBoolKeyword
from .AFXDialog import AFXDialog
from .AFXGuiMode import AFXGuiMode
from .AFXTransition import AFXTransition
from .constants import DIALOG_NORMAL
from .FXObject import FXObject
from .FXWindow import FXWindow

#: Perform bailout checks when the Cancel button is clicked.
DATADIALOG_BAILOUT: int = hash("DATADIALOG_BAILOUT")


class AFXDataDialog(AFXDialog):
    """AFXDataDialog."""

    #: Used to update the state.
    ID_UPDATE_STATE: int = hash("ID_UPDATE_STATE")

    def __init__(
        self,
        mode: AFXGuiMode,
        owner: FXWindow,
        title: str,
        actionButtonIds: int = 0,
        opts: int = DIALOG_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
    ):
        """Constructor that creates a dialog box that occludes its owner widget.

        Parameters
        ----------
        mode : AFXGuiMode
            Host mode.
        owner : FXWindow
            Owner widget.
        title : str
            Title string.
        actionButtonIds : int
            ID's of action buttons to be created.
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
        """

    def addTransition(
        self,
        keyword: AFXBoolKeyword,
        op: AFXTransition.Operator,
        value: bool,
        tgt: FXObject,
        sel: int,
        ptr: str = "None",
    ):
        """Adds a finite state transition to the dialog box. When the expression "keyword.getValue() op value"
        evaluates to True, an sel message will be sent to the tgt object.

        Parameters
        ----------
        keyword : AFXBoolKeyword
            Keyword.
        op : FXTransition.Operator
            Operator type.
        value : bool
            Reference value.
        tgt : FXObject
            Message target.
        sel : int
            Message selector.
        ptr : str
            Message data.
        """

    def bailout(self):
        """Performs checks to determine whether it is OK to cancel the dialog box.

        The implementaton of this class always returns True, and the derived class should reimplement this
        method to perform specific checks. Reimplemented from AFXDialog.
        """

    def getMode(self):
        """Returns the dialog box's host mode."""

    def onKeywordError(self, kwd: FXObject):
        """Handles the error that occurs when the given keyword or target contains invalid contents. This method
        will select the contents of the widget that is set for the keyword or target (with
        setWidgetForKeyword()). If no such widget is specified explicitly, it will select the contents of the
        widget that has the keyword or target as its message target.

        Parameters
        ----------
        kwd : FXObject
            Object that contains invalid contents.
        """

    def onTableError(self, tableKwd: FXObject, row: int, col: int):
        """Handles the error that occurs when the given table keyword or target contains an invalid element.
        This method will select the contents of the widget that is set for the element of the keyword or target
        (with setWidgetForKeyword()). If no such widget is specified explicitly, it will select the contents of
        the widget that has the keyword or target as its message target.

        Parameters
        ----------
        tableKwd : FXObject
            Object that contains invalid element.
        row : int
            Row index.
        col : int
            Column index.
        """

    def onTupleError(self, tupleKwd: FXObject, index: int):
        """Handles the error that occurs when the given tuple keyword or target contains an invalid element.
        This method will select the contents of the widget that is set for the element of the keyword or target
        (with setWidgetForKeyword()). If no such widget is specified explicitly, it will select the contents of
        the widget that has the keyword or target as its message target.

        Parameters
        ----------
        tupleKwd : FXObject
            Object that contains invalid element.
        index : int
            Element index.
        """

    def processUpdates(self):
        """Performs state processing during the GUI update cycles.

        This class provides an empty implementation of this method, and the derived class should redefine
        the method if it needs to process state updating.
        """
