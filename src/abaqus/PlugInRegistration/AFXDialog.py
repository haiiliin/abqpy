from __future__ import annotations

from .constants import DIALOG_NORMAL
from .FXApp import FXApp
from .FXComposite import FXComposite
from .FXIcon import FXIcon
from .FXObject import FXObject
from .FXWindow import FXWindow


class AFXDialog:
    """AFXDialog"""

    def __init__(
        self,
        app: FXApp,
        title: str,
        actionButtonIds: int = 0,
        opts: int = DIALOG_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
    ):
        """Constructor that creates a dialog box that may be occluded by any other windows of the application.

        Parameters
        ----------
        app : FXApp
            Application.
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

    def appendActionButton(self, buttonID: ButtonID):
        """Adds a standard action button in the action area of the dialog box.

        Parameters
        ----------
        buttonID : ButtonID
            Button ID.
        """

    def bailout(self):
        """Performs checks to determine whether it is OK to cancel the dialog box. The implementaton of this class always returns True, and the derived class should reimplement this method to perform specific checks. Reimplemented in AFXDataDialog."""

    def create(self):
        """Creates the dialog box. Reimplemented from FXTopWindow."""

    def createButton(self, parent: FXComposite, text: str, icon: FXIcon, tgt: FXObject, sel: int, opts: int):
        """Creates an action area button.

        Parameters
        ----------
        parent : FXComposite
            Parent widget.
        text : str
            Label string.
        icon : FXIcon
            Icon.
        tgt : FXObject
            Message target.
        sel : int
            Message ID.
        opts : int
            Options and hints.
        """

    def getActionButton(self, sel: int):
        """Returns the action button with the specified message ID; returns 0 if none of the action buttons has the message ID.

        Parameters
        ----------
        sel : int
            Message ID.
        """

    def getUnpostHints(self):
        """Returns the action that the poster should perform on this dialog box when it is unposted. Possible return values are: DIALOG_UNPOST_DELETE - delete the C++ dialog box object together with the associated window. (default) DIALOG_UNPOST_DESTROY - keep the C++ dialog box object, but destroy the associated window to release resources. DIALOG_UNPOST_NOTHING - do nothing."""

    def hide(self):
        """Unpost the dialog box. Reimplemented from FXTopWindow. Reimplemented in AFXManagerMenuDB, and AFXMessageDialog."""

    def onKeywordError(self, kwd: FXObject):
        """Handles the error that occurs when the given keyword or target contains invalid contents. This method will select the contents of the widget that has the keyword or target as its message target.

        Parameters
        ----------
        kwd : FXObject
            Object that contains invalid contents.
        """

    def onTableError(self, tableKwd: FXObject, row: int, col: int):
        """Handles the error that occurs when the given table keyword or target contains an invalid element. This method will select the contents of the widget that has the keyword or target as its message target.

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
        """Handles the error that occurs when the given tuple keyword or target contains an invalid element. This method will select the contents of the widget that has the keyword or target as its message target.

        Parameters
        ----------
        tupleKwd : FXObject
            Object that contains invalid element.
        index : int
            Element index.
        """

    def selectContents(self, widget: FXWindow):
        """Selects the contents of the given widget.

        Parameters
        ----------
        widget : FXWindow
            Widget to select.
        """

    def selectTableElement(self, widget: FXWindow, row: int, col: int):
        """Selects the given (row,col) element in the 2D array of elements displayed by the given widget.

        Parameters
        ----------
        widget : FXWindow
            Widget to select.
        row : int
            Row index.
        col : int
            Column index.
        """

    def selectTupleElement(self, widget: FXWindow, index: int):
        """Selects the element at the given index in the sequence of elements displayed by the given widget.

        Parameters
        ----------
        widget : FXWindow
            Widget to select.
        index : int
            Element index.
        """

    def setOnPopdownTarget(self, target: FXObject):
        """Sets the object to be notified when the dialog box is unposted.

        Parameters
        ----------
        target : FXObject
            Object to be notified when the dialog box is unposted.
        """

    def setUnpostHints(self, hints: int):
        """Sets the action that the poster should perform on this dialog box when it is unposted.

        Parameters
        ----------
        hints : int

        """

    def show(self):
        """Posts the dialog box. Reimplemented from FXTopWindow. Reimplemented in AFXFileDialog, and AFXMessageDialog."""

    def showModal(self, occludedWindow: FXWindow | None = None):
        """Posts the dialog box as a modal dialog box. The dialog box is centered against the given widget or its owner widget if 0 is given.

        Parameters
        ----------
        occludedWindow : FXWindow | None
            Widget to be occluded (0 for the owner widget).
        """
