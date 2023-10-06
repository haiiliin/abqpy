from __future__ import annotations

from .AFXDialog import AFXDialog
from .AFXGuiMode import AFXGuiMode
from .AFXGuiObjectManager import AFXGuiObjectManager
from .FXObject import FXObject


class AFXForm(AFXGuiMode):
    """Abaqus."""

    def __init__(self, owner: AFXGuiObjectManager):
        """Constructor.

        Parameters
        ----------
        owner : AFXGuiObjectManager
            Owner (a module or a toolset) of the form.
        """

    def activate(self):
        """Performs the necessary tasks when the form is activated.

        Reimplemented from AFXGuiMode.
        """

    def cancel(self, tgt: FXObject | None = None, msg: int = 0):
        """Requests a cancellation of the form. When the cancel operation completes, successfully or not, the
        target will be sent the given message. The message data pointer will be non-zero for successful
        cancellation and zero if the cancel operation was abandoned for some purpose.

        Parameters
        ----------
        tgt : FXObject | None
            Completion message target.
        msg : int
            Completion message ID.
        """

    def commit(self):
        """Performs the necessary tasks when the form is committed.

        Implements AFXGuiMode.
        """

    def continueMode(self):
        """Used to get the next dialog box in the mode.

        Implements AFXGuiMode.
        """

    def deactivateIfNeeded(self):
        """Deactivates the form if the user pressed the OK button of the currently posted dialog box.

        This method is called after the commands are processed successfully.
        """

    def getFirstDialog(self):
        """Returns the first dialog box to be posted."""

    def getNextDialog(self, previousDialog: AFXDialog):
        """Returns the next dialog box to be posted.

        Parameters
        ----------
        previousDialog : AFXDialog
            Previous dialog box.
        """

    def issueCommands(self, writeToReplay: bool = True, writeToJournal: bool = False):
        """Generates commands based on the current state, sends the commands, and deactivates the form if
        necessary. If the commands did not complete successfully, a dialog box will be posted with an error
        message.

        Parameters
        ----------
        writeToReplay : bool
            True if commands should be written to the replay file; False if not.
        writeToJournal : bool
            True if commands should be written to the journal file; False if not.
        """

    def setModal(self, postModalDialogs: bool):
        """Sets the modal state; if True, dialogs will be posted as modal. By default the form posts dialogs as
        non-modal.

        Parameters
        ----------
        postModalDialogs : bool
            True if the form should post dialogs as modal.
        """
