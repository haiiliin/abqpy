from __future__ import annotations

from .AFXDialog import AFXDialog
from .AFXGuiMode import AFXGuiMode
from .AFXGuiObjectManager import AFXGuiObjectManager
from .AFXStep import AFXStep
from .FXObject import FXObject


class AFXProcedure(AFXGuiMode):
    """This class provides the basis for writing procedures."""

    #: ID for handling bailout.
    ID_HANDLE_2BTN_BAILOUT: int = hash("ID_HANDLE_2BTN_BAILOUT")

    #: ID for the backup button.
    ID_BACKUP: int = hash("ID_BACKUP")

    #: Pick entities inside the drag shape only.
    INSIDE: int = hash("INSIDE")

    #: Pick entities inside and crossing the drag shape.
    INSIDE_CROSSING: int = hash("INSIDE_CROSSING")

    #: Pick entities crossing the drag shape only.
    CROSSING: int = hash("CROSSING")

    #: Pick entities outside and crossing the drag shape.
    OUTSIDE_CROSSING: int = hash("OUTSIDE_CROSSING")

    #: Pick entities outside the drag shape only.
    OUTSIDE: int = hash("OUTSIDE")

    #: Use rectangular drag shape.
    RECTANGLE: int = hash("RECTANGLE")

    #: Use circular drag shape.
    CIRCLE: int = hash("CIRCLE")

    #: Use polygonal drag shape.
    POLYGON: int = hash("POLYGON")

    #: Only pick the entity closest to the screen.
    CLOSEST: int = hash("CLOSEST")

    #: Pick entities at any depth.
    INFINITE: int = hash("INFINITE")

    #: Pick only interior entities.
    INTERIOR: int = hash("INTERIOR")

    #: Pick only exterior entities.
    EXTERIOR: int = hash("EXTERIOR")

    #: Pick all entities.
    ALL: int = hash("ALL")

    #: Cancel the currently running procedure (default).
    NORMAL: int = hash("NORMAL")

    #: Suspend the currently running procedure.
    SUBPROCEDURE: int = hash("SUBPROCEDURE")

    def __init__(self, owner: AFXGuiObjectManager, type=NORMAL):
        """Constructor.

        Parameters
        ----------
        owner : AFXGuiObjectManager
            Owner (a module or a toolset) of the procedure.
        type : typeEnum
        """

    def activate(self):
        """Activates the mode.

        Reimplemented from AFXGuiMode.
        """

    def cancel(self, tgt: FXObject | None = None, msg: int = 0):
        """Tries to cancel the procedure depending on checkCancel results.

        Parameters
        ----------
        tgt : FXObject | None
            Completion message target.
        msg : int
            Completion message ID.
        """

    def checkBackup(self):
        """Returns 1 if ok to backup else returns 0."""

    def checkCancel(self):
        """Returns BAILOUT_NOTOK, BAILOUT_OK, BAILOUT_WIP (writes to the message area), or BAILOUT_SAVE (use the
        3 button save dialog box)."""

    def commit(self):
        """Commits the procedure when the current dialog box calls either done or value changed.

        Implements AFXGuiMode.
        """

    def continueMode(self):
        """Used to get the next step in the mode.

        Implements AFXGuiMode.
        """

    def deactivate(self):
        """Deactivates the mode.

        Reimplemented from AFXGuiMode.
        """

    def getCurrentStep(self):
        """Returns the current step."""

    def getFirstStep(self):
        """Returns the first step to be executed in the procedure."""

    def getLoopStep(self):
        """Returns the step to which the procedure should loop back after processing its commands; if zero is
        returned (the default behavior) the procedure will not loop."""

    def getNextStep(self, previousStep: AFXStep):
        """Returns the next step to be executed; if zero is returned the procedure will process its commands.

        Parameters
        ----------
        previousStep : AFXStep
            Previous step.
        """

    def getNumSteps(self):
        """Returns the number of steps in the step stack."""

    def handleException(self, exc):
        """This method is called if an error occurs while issuing commands. It can be reimplemented in derived
        classes to perform special error handling.

        Parameters
        ----------
        exc : nex_Exception
            Exception.
        """

    def onBackup(self):
        """Called when a procedure backs up a step."""

    def onCancel(self):
        """Called when a procedure cancels."""

    def onCmdBackup(self, sender: FXObject, sel: int, ptr: str):
        """Message handler for handling backup button activation.

        Parameters
        ----------
        sender : FXObject
            Sender.
        sel : int
            Selector.
        ptr : str
            Data.
        """

    def onCmdHandle2BtnBailout(self, sender: FXObject, sel: int, ptr: str):
        """Message handler for handling the user 2 button bailout choice.

        Parameters
        ----------
        sender : FXObject
            Sender.
        sel : int
            Selector.
        ptr : str
            Data.
        """

    def onCmdHandleBailout(self, sender: FXObject, sel: int, ptr: str):
        """Message handler for handling the user 3 button bailout choice.

        Parameters
        ----------
        sender : FXObject
            Sender.
        sel : int
            Selector.
        ptr : str
            Data.
        """

    def onResume(self):
        """Called when a procedure resumes."""

    def onSuspend(self):
        """Called when a procedure suspends."""

    def onValueChanged(self):
        """Called when a procedure's step changes in value."""

    def setCurrentDb(self, db: AFXDialog):
        """Sets the current dialog box of the mode. Procedures will have this set by AFXDialogStep.

        Parameters
        ----------
        db : AFXDialog
            Dialog box.
        """

    def setSelectionOptions(
        self,
        pickDepth=CLOSEST,
        pickScope=ALL,
        dragShape=RECTANGLE,
        dragScope=INSIDE_CROSSING,
        isoLines: bool = True,
    ):
        """Sets the selection options to be used for picking.

        Parameters
        ----------
        pickDepth : pickDepthEnum
            Depth into the screen of picking.
        pickScope : pickScopeEnum
            Entity type.
        dragShape : dragShapeEnum
            Drag-window shape.
        dragScope : dragScopeEnum
            Drag-window scope.
        isoLines : bool
            If True, show isolines on surfaces.
        """

    def verifyCurrentKeywordValues(self):
        """Checks whether keywords of active commands for the current dialog box contain valid data and, if not,
        posts a dialog box with an error message.

        Reimplemented from AFXGuiMode.
        """
