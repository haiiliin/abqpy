from __future__ import annotations

from .AFXProcedure import AFXProcedure


class AFXStep:
    """Abaqus."""

    def __init__(self, prompt: str, owner: AFXProcedure):
        """Constructor.

        Parameters
        ----------
        prompt : str
            Prompt.
        owner : AFXProcedure
            Owner.
        """

    def onCancel(self):
        """Called when the step is cancelled.

        Reimplemented in AFXCreateSketchStep, AFXDialogStep, AFXEditSketchStep, AFXOrderedPickStep, and
        AFXPickStep.
        """

    def onDone(self):
        """Called when the step completes."""

    def onExecute(self):
        """Called to execute the steps returned by getFirstStep and getNextStep.

        Reimplemented in AFXCreateSketchStep, AFXDialogStep, AFXEditSketchStep, AFXOrderedPickStep, and
        AFXPickStep.
        """

    def onResume(self):
        """Called when the step is resumed.

        Reimplemented in AFXCreateSketchStep, AFXDialogStep, AFXEditSketchStep, and AFXPickStep.
        """

    def onSuspend(self):
        """Called when the step is suspended.

        Reimplemented in AFXCreateSketchStep, AFXDialogStep, AFXEditSketchStep, and AFXPickStep.
        """

    def onValueChanged(self):
        """Called when the step's value changes."""

    def reset(self):
        """Allows a step to reset any of its data (if needed) when looping.

        Reimplemented in AFXOrderedPickStep, and AFXPickStep. By clicking on Send, you accept that Dassault
        Systèmes will process your personal data and may contact you for further information. [Privacy
        Policy](
        https://www.3ds.com/privacy-policy).
        Total Results: Results per page This page cannot be found. The page might not exist or is
        temporarily unavailable. Try again or try searching for the topic. Use this form to provide feedback
        on this help topic. To get product support or to provide product feedback, go to [Frequently Asked
        Questions](
        https://3ds.one/PO).
        For support for online purchased solutions, go to [Online Purchase Support](https://3ds.one/Q8). *
        Required Subject: Feedback on User Assistance * I acknowledge I have read and I hereby accept the
        [privacy policy](
        https://www.3ds.com/privacy-policy)
        under which my personal data will be used by Dassault Systèmes. Thank you for your comments. We will contact you if we have questions regarding your feedback. Sincerely, The Dassault Systèmes User Assistance Team Dialog for Cookie Allow to use Cookie for saving your settings ? Drag to outliner or Upload Close
        """
