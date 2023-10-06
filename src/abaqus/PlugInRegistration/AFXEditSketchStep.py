from __future__ import annotations

from .AFXProcedure import AFXProcedure
from .AFXStep import AFXStep


class AFXEditSketchStep(AFXStep):
    """This class is used to provide pick steps in GUI procedures."""

    def __init__(self, owner: AFXProcedure, sketchName: str, prompt: str = "'Edit a sketch'"):
        """Constructor.

        Parameters
        ----------
        owner : AFXProcedure
            Procedure creating the step.
        sketchName : str
            Name of sketch to edit, blank if create.
        prompt : str
            Step's prompt displayed in prompt area.
        """

    def onCancel(self):
        """Called when the step is cancelled.

        Reimplemented from AFXStep.
        """

    def onExecute(self):
        """Called to execute the steps returned by getFirstStep and getNextStep.

        Reimplemented from AFXStep.
        """

    def onResume(self):
        """Called when the step is resumed.

        Reimplemented from AFXStep.
        """

    def onSuspend(self):
        """Called when the step is suspended.

        Reimplemented from AFXStep.
        """
