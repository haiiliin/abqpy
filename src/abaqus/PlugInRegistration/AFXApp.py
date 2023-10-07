from __future__ import annotations

from .AFXMainWindow import AFXMainWindow
from .FXApp import FXApp


class AFXApp(FXApp):
    """This class is responsible for providing some high-level GUI control methods."""

    #: Used to query whether the GUI is locked.
    ID_QUERY_GUILOCK: int = hash("ID_QUERY_GUILOCK")

    #: Used to change the cursor.
    ID_SHOW_HOURGLASS: int = hash("ID_SHOW_HOURGLASS")

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

    def getAFXMainWindow(self) -> AFXMainWindow:  # type: ignore
        """Returns a pointer to the AFXMainWindow."""

    def getBasePrerelease(self) -> bool:  # type: ignore
        """Returns True if the base product is a prerelease."""

    def getBaseProductName(self) -> str:  # type: ignore
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

    def getKernelInitializationCommand(self) -> str:  # type: ignore
        """Returns the command string that will be issued upon application startup."""

    def getPrerelease(self) -> bool:  # type: ignore
        """Returns True if this is a prerelease."""

    def getProductName(self) -> str:  # type: ignore
        """Returns the product name."""

    def getVersionNumbers(self) -> tuple[int, int, int]:  # type: ignore
        """Returns the major, minor, and update numbers."""

    def init(self, argc: int, argv: str, *args, **kwargs):
        """Initializes the application and connects to the kernel.

        Parameters
        ----------
        argc : int

        argv : str
        """

    def isLocked(self) -> bool:  # type: ignore
        """Returns True if the GUI is locked or False if otherwise.

        Reimplemented from FXApp.
        """

    def isProductCAE(self) -> bool:  # type: ignore
        """Returns True if the base product is Abaqus/CAE."""

    def isProductViewer(self) -> bool:  # type: ignore
        """Returns True if the base product is Abaqus/Viewer."""

    def isLearningEdition(self) -> bool:  # type: ignore
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
