from __future__ import annotations

from .AFXObjectKeyword import AFXObjectKeyword
from .AFXProcedure import AFXProcedure
from .AFXStep import AFXStep


class AFXCreateSketchStep(AFXStep):
    """This class is used to provide pick steps in GUI procedures."""

    def __init__(
        self, owner: AFXProcedure, keyword: AFXObjectKeyword, sheetSize: float, prompt: str = "'Create a sketch'"
    ):
        """Constructor.

        Parameters
        ----------
        owner : AFXProcedure
            Procedure creating the step.
        keyword : AFXObjectKeyword
            Object kwd containing pick variable. Part of AFXGuiCommand.
        sheetSize : float
            Sketch sheet size when creating.
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
