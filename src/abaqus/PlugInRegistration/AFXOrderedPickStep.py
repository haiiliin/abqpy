from __future__ import annotations

from .AFXObjectKeyword import AFXObjectKeyword
from .AFXPickStep import AFXPickStep
from .AFXProcedure import AFXProcedure


class AFXOrderedPickStep(AFXPickStep):
    """This class is used to provide pick steps in GUI procedures."""

    def __init__(
        self, owner: AFXProcedure, keyword: AFXObjectKeyword, prompt: str, entitiesToPick: int, highlightLevel: int = 1
    ):
        """Constructor.

        Parameters
        ----------
        owner : AFXProcedure
            Procedure creating the step.
        keyword : AFXObjectKeyword
            Object kwd containing pick variable. Part of AFXGuiCommand.
        prompt : str
            Step's prompt displayed in prompt area.
        entitiesToPick : int
            Type of entities to pick.
        highlightLevel : int
            Highlight level.
        """

    def onCancel(self):
        """Called when the step is cancelled.

        Reimplemented from AFXPickStep.
        """

    def onExecute(self):
        """Called to execute the steps returned by getFirstStep and getNextStep.

        Reimplemented from AFXPickStep.
        """

    def reset(self):
        """Allows a step to reset any of its data (if needed) when looping.

        Reimplemented from AFXPickStep.
        """
