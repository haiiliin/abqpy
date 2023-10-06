from __future__ import annotations

from .AFXObjectKeyword import AFXObjectKeyword
from .AFXProcedure import AFXProcedure
from .AFXStep import AFXStep
from .AFXTupleKeyword import AFXTupleKeyword
from .constants import ARRAY, ONE


class AFXPickStep(AFXStep):
    """This class is used to provide pick steps in GUI procedures."""

    def __init__(
        self,
        owner: AFXProcedure,
        keyword: AFXObjectKeyword,
        prompt: str,
        entitiesToPick: int,
        numberToPick=ONE,
        highlightLevel: int = 1,
        sequenceStyle=ARRAY,
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
        numberToPick : pickAmountEnum
            How many entities to pick.
        highlightLevel : int
            Highlight level.
        sequenceStyle : sequenceStyleEnum
            Sequence style of picked variables in the command.
        """

    def addElementSetSelection(self, name: str):
        """Adds an element set to the step's selections.

        Parameters
        ----------
        name : str
            Name of set.
        """

    def addGeometrySetSelection(self, name: str):
        """Adds a geometry set to the step's selections.

        Parameters
        ----------
        name : str
            Name of set.
        """

    def addNodeSetSelection(self, name: str):
        """Adds a node set to the step's selections.

        Parameters
        ----------
        name : str
            Name of set.
        """

    def addPointKeyIn(self, keyword: AFXTupleKeyword):
        """Creates a textfield on the prompt line as an alternative method of specifying a point.

        Parameters
        ----------
        keyword : AFXTupleKeyword
            Keyword
        """

    def addSurfaceSelection(self, name: str):
        """Adds a surface to the step's selections.

        Parameters
        ----------
        name : str
            Name of surface.
        """

    def allowRepeatedSelections(self, value: bool = True):
        """Allows the picking of prior selections (from prior pick steps of the procedure).

        Parameters
        ----------
        value : bool
            If True, allow repeated selections between steps.
        """

    def onCancel(self):
        """Called when the step is cancelled.

        Reimplemented from AFXStep. Reimplemented in AFXOrderedPickStep.
        """

    def onExecute(self):
        """Called to execute the steps returned by getFirstStep and getNextStep.

        Reimplemented from AFXStep. Reimplemented in AFXOrderedPickStep.
        """

    def onResume(self):
        """Called when the step is resumed.

        Reimplemented from AFXStep.
        """

    def onSuspend(self):
        """Called when the step is suspended.

        Reimplemented from AFXStep.
        """

    def reset(self):
        """Allows a step to reset any of its data (if needed) when looping.

        Reimplemented from AFXStep. Reimplemented in AFXOrderedPickStep.
        """

    def setEdgeRefinements(self, refinement: int):
        """Sets the refinements to be used when picking edges.

        Parameters
        ----------
        refinement : int
            Refinement flag.
        """

    def setElementEdgeRefinements(self, refinement: int):
        """Sets the refinements to be used when picking element edges.

        Parameters
        ----------
        refinement : int
            Refinement flag.
        """

    def setElementFaceRefinements(self, refinement: int):
        """Sets the refinements to be used when picking element faces.

        Parameters
        ----------
        refinement : int
            Refinement flag.
        """

    def setElementRefinements(self, refinement: int):
        """Sets the refinements to be used when picking elements.

        Parameters
        ----------
        refinement : int
            Refinement flag.
        """

    def setFaceRefinements(self, refinement: int):
        """Sets the refinements to be used when picking faces.

        Parameters
        ----------
        refinement : int
            Refinement flag.
        """

    def setInstanceRefinements(self, refinement: int):
        """Sets the refinements to be used when picking instances.

        Parameters
        ----------
        refinement : int
            Refinement flag.
        """

    def setNodeRefinements(self, refinement: int):
        """Sets the refinements to be used when picking nodes.

        Parameters
        ----------
        refinement : int
            Refinement flag.
        """

    def setSketchRefinements(self, refinement: int):
        """Sets the refinements to be used when picking sketches.

        Parameters
        ----------
        refinement : int
            Refinement flag.
        """

    def setXyRefinements(self, refinement: int):
        """Sets the refinements to be used when picking xy objects.

        Parameters
        ----------
        refinement : int
            Refinement flag.
        """
