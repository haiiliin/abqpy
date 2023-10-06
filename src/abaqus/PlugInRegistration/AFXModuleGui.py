from __future__ import annotations

from .AFXGuiObjectManager import AFXGuiObjectManager


class AFXModuleGui(AFXGuiObjectManager):
    """This is the base class for module GUIs and provides an interface for module GUI management."""

    #: Displays a part primary object.
    PART: int = hash("PART")

    #: Displays an assembly primary object.
    ASSEMBLY: int = hash("ASSEMBLY")

    #: Displays an ODB primary object.
    ODB: int = hash("ODB")

    #: Displays an XY plot primary object.
    XY_PLOT: int = hash("XY_PLOT")

    #: Displays a sketch primary object.
    SKETCH: int = hash("SKETCH")

    def __init__(self, moduleName: str, displayTypes: int):
        """Constructor.

        Parameters
        ----------
        moduleName : str
            Name used to identify this module.
        displayTypes : int
            Types of primary objects that this module may display.
        """

    def activate(self):
        """Activates the module during switch processing (allows for module specific activation
        requirements)."""

    def deactivate(self):
        """Deactivates the module when switching out (allows for module specific deactivation requirements)."""

    def getModuleName(self):
        """Returns the name of the module given on construction."""

    def getTypesToDisplay(self):
        """Returns the type of the primary objects which may be displayed when this module is active (this
        currently assumes a single type)."""

    def hide(self, location: int):
        """Deactivates and hides the module's GUI components in the menubar, toolbar and toolbox.

        Parameters
        ----------
        location : int
            Location where gui components are placed.
        """

    def show(self, location: int):
        """Activates and shows the module's GUI components in the menubar, toolbar and toolbox.

        Parameters
        ----------
        location : int
            Location where gui components are placed.
        """
