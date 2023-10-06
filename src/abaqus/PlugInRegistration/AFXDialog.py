from __future__ import annotations

from .FXApp import FXApp
from .FXComposite import FXComposite
from .FXDialogBox import FXDialogBox
from .FXIcon import FXIcon
from .FXObject import FXObject
from .FXWindow import FXWindow

#: Creates the action area horizontally at the bottom of the dialog box.
DIALOG_ACTIONS_BOTTOM: int = hash("DIALOG_ACTIONS_BOTTOM")

#: Creates the action area vertically at the right side of the dialog box.
DIALOG_ACTIONS_RIGHT: int = hash("DIALOG_ACTIONS_RIGHT")

#: Do not create the action area.
DIALOG_ACTIONS_NONE: int = hash("DIALOG_ACTIONS_NONE")

#: Creates a separator in the action area.
DIALOG_ACTIONS_SEPARATOR: int = hash("DIALOG_ACTIONS_SEPARATOR")

#: Deletes the dialog box when unposted.
DIALOG_UNPOST_DELETE: int = hash("DIALOG_UNPOST_DELETE")

#: Destroys the dialog box when unposted.
DIALOG_UNPOST_DESTROY: int = hash("DIALOG_UNPOST_DESTROY")

#: Do nothing when unposted.
DIALOG_UNPOST_NOTHING: int = hash("DIALOG_UNPOST_NOTHING")

#: Default dialog box options.
DIALOG_NORMAL: int = hash("DIALOG_NORMAL")


class AFXDialog(FXDialogBox):
    """AFXDialog."""

    #: OK button ID.
    ID_CLICKED_OK: int = hash("ID_CLICKED_OK")

    #: Contiue button ID.
    ID_CLICKED_CONTINUE: int = hash("ID_CLICKED_CONTINUE")

    #: Yes button ID.
    ID_CLICKED_YES: int = hash("ID_CLICKED_YES")

    #: Yes to All button ID.
    ID_CLICKED_YES_TO_ALL: int = hash("ID_CLICKED_YES_TO_ALL")

    #: Apply button ID.
    ID_CLICKED_APPLY: int = hash("ID_CLICKED_APPLY")

    #: Defaults button ID.
    ID_CLICKED_DEFAULTS: int = hash("ID_CLICKED_DEFAULTS")

    #: No button ID.
    ID_CLICKED_NO: int = hash("ID_CLICKED_NO")

    #: Cacncel button ID.
    ID_CLICKED_CANCEL: int = hash("ID_CLICKED_CANCEL")

    #: Dismiss button ID.
    ID_CLICKED_DISMISS: int = hash("ID_CLICKED_DISMISS")

    #: Adds an Apply button to action area.
    APPLY: int = hash("APPLY")

    #: Adds a Cancel button to action area.
    CANCEL: int = hash("CANCEL")

    #: Adds a Continue button to action area.
    CONTINUE: int = hash("CONTINUE")

    #: Adds a Defaults button to action area.
    DEFAULTS: int = hash("DEFAULTS")

    #: Adds a Dismiss button to action area.
    DISMISS: int = hash("DISMISS")

    #: Adds a No button to action area.
    NO: int = hash("NO")

    #: Adds an OK button to action area.
    OK: int = hash("OK")

    #: Adds a Yes button to action area.
    YES: int = hash("YES")

    #: Adds a Yes to All button to action area.
    YES_TO_ALL: int = hash("YES_TO_ALL")

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

    def appendActionButton(self, buttonID):
        """Adds a standard action button in the action area of the dialog box.

        Parameters
        ----------
        buttonID : ButtonID
            Button ID.
        """

    def bailout(self):
        """Performs checks to determine whether it is OK to cancel the dialog box.

        The implementaton of this class always returns True, and the derived class should reimplement this
        method to perform specific checks. Reimplemented in AFXDataDialog.
        """

    def create(self):
        """Creates the dialog box.

        Reimplemented from FXTopWindow.
        """

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
        """Returns the action button with the specified message ID; returns 0 if none of the action buttons has
        the message ID.

        Parameters
        ----------
        sel : int
            Message ID.
        """

    def getUnpostHints(self):
        """Returns the action that the poster should perform on this dialog box when it is unposted.

        Possible return values are: DIALOG_UNPOST_DELETE - delete the C++ dialog box object together with the associated window. (default) DIALOG_UNPOST_DESTROY - keep the C++ dialog box object, but destroy the associated window to release resources. DIALOG_UNPOST_NOTHING - do nothing.
        """

    def hide(self):
        """Unpost the dialog box.

        Reimplemented from FXTopWindow. Reimplemented in AFXManagerMenuDB, and AFXMessageDialog.
        """

    def onKeywordError(self, kwd: FXObject):
        """Handles the error that occurs when the given keyword or target contains invalid contents. This method
        will select the contents of the widget that has the keyword or target as its message target.

        Parameters
        ----------
        kwd : FXObject
            Object that contains invalid contents.
        """

    def onTableError(self, tableKwd: FXObject, row: int, col: int):
        """Handles the error that occurs when the given table keyword or target contains an invalid element.
        This method will select the contents of the widget that has the keyword or target as its message target.

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
        This method will select the contents of the widget that has the keyword or target as its message target.

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
        """Posts the dialog box.

        Reimplemented from FXTopWindow. Reimplemented in AFXFileDialog, and AFXMessageDialog.
        """

    def showModal(self, occludedWindow: FXWindow | None = None):
        """Posts the dialog box as a modal dialog box. The dialog box is centered against the given widget or
        its owner widget if 0 is given.

        Parameters
        ----------
        occludedWindow : FXWindow | None
            Widget to be occluded (0 for the owner widget).
        """
