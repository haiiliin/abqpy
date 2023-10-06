from __future__ import annotations

from .AFXDataDialog import AFXDataDialog
from .AFXProcedure import AFXProcedure
from .AFXStep import AFXStep


class AFXDialogStep(AFXStep):
    """This class provides dialog steps in GUI procedures."""

    def __init__(self, owner: AFXProcedure, dialog: AFXDataDialog):
        """Constructor that supplies a default prompt for the prompt area.

        Parameters
        ----------
        owner : AFXProcedure
            Procedure creating the step.
        dialog : AFXDataDialog
            Dialog box to be posted in this step.
        """

    def onCancel(self):
        """Called when the step is cancelled.

        Reimplemented from AFXStep.
        """

    def onExecute(self):
        """Called to execute steps returned by getFirstStep and getNextStep.

        Reimplemented from AFXStep.
        """

    def onResume(self):
        """Called when the step is resumed.

        Reimplemented from AFXStep.
        """

    def onSuspend(self):
        """Called when the step is suspended.

        Reimplemented from AFXStep. By clicking on Send, you accept that Dassault Systèmes will process your
        personal data and may contact you for further information. [Privacy Policy](
        https://www.3ds.com/privacy-policy).
        Total Results: Results per page This page cannot be found. The page might not exist or is temporarily unavailable. Try again or try searching for the topic.
        """
