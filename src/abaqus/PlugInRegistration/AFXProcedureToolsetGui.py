from __future__ import annotations


class AFXProcedureToolsetGui:
    """This is the base class for toolset GUIs used in procedure steps (e.g. the Sketch toolset) and provides an interface for managing the toolset's GUI items. In conjuction with the AFXProcedureToolsetGuiData class, it provides a mechanism to overlay menubar, toolbar, and toolbox GUI items while the step executes."""

    def __init__(self, toolsetName: str):
        """Constructor.

        Parameters
        ----------
        toolsetName : str
            Toolset name passed in from derived toolsets.
        """

    def swapInToolsetItems(self):
        """Swaps in the toolset's GUI items."""

    def swapOutToolsetItems(self):
        """Swaps out the toolset's GUI items."""
