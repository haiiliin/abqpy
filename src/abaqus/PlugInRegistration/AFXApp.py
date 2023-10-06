from __future__ import annotations

from .FXApp import FXApp


class AFXApp(FXApp):
    """This class is responsible for providing some high-level GUI control methods."""

    def __init__(
        self,
        appName: str = "Abaqus/CAE",
        vendorName: str = "SIMULIA",
        productName: str = "''",
        majorNumber: int = -1,
        minorNumber: int = -1,
        updateNumber: int = -1,
        prerelease: bool = False,
    ):
        """Constructor.

        Parameters
        ----------
        appName : str
            Application registry key.
        vendorName : str
            Vendor registry key.
        productName : str
            Product name.
        majorNumber : int
            Version number.
        minorNumber : int
            Release number.
        updateNumber : int
            Update number.
        prerelease : bool
            Official/Prerelease flag.
        """

    def create(self):
        """Creates windows for the application.

        Reimplemented from FXApp.
        """

    def getAFXMainWindow(self):
        """Returns a pointer to the AFXMainWindow."""

    def getBasePrerelease(self):
        """Returns True if the base product is a prerelease."""

    def getBaseProductName(self):
        """Returns the base product name."""

    def getBaseVersionNumbers(self, majorNumber: int, minorNumber: int, updateNumber: int):
        """Returns the base product's major, minor, and update numbers.

        Parameters
        ----------
        majorNumber : int
            Version number.
        minorNumber : int
            Release number.
        updateNumber : int
            Update number.
        """

    def getKernelInitializationCommand(self):
        """Returns the command string that will be issued upon application startup."""

    def getPrerelease(self):
        """Returns True if this is a prerelease."""

    def getProductName(self):
        """Returns the product name."""

    def getVersionNumbers(self):
        """Returns the major, minor, and update numbers."""

    def init(self, argc: int, argv: str):
        """Initializes the application and connects to the kernel.

        Parameters
        ----------
        argc : int

        argv : str
        """

    def isLocked(self):
        """Returns True if the GUI is locked or False if otherwise.

        Reimplemented from FXApp.
        """

    def isProductCAE(self):
        """Returns True if the base product is Abaqus/CAE."""

    def isProductViewer(self):
        """Returns True if the base product is Abaqus/Viewer."""

    def isLearningEdition(self):
        """Returns True if the base product is a learning edition."""

    def lock(self):
        """Locks the GUI (normally used during command and mode processing)."""

    def run(self):
        """Runs the main application event loop until stop() is called,.

        Reimplemented from FXApp.
        """

    def runUntil(self, condition: int):
        """Run an event loop till some flag becomes non-zero. Reimplemented from FXApp.

        Parameters
        ----------
        condition : int
        """

    def unlock(self):
        """Unlocks the GUI."""
