from typing import Any, Tuple


class AFXApp:
    """
    A class for providing high-level GUI control methods.

    """
    def __init__(self, appName: str = "Abaqus/CAE", vendorName: str = "SIMULIA", productName: str = "", majorNumber: int = -1, minorNumber: int = -1, updateNumber: int = -1, prerelease: bool = False):
        """
        Constructor.

        Parameters
        ----------
        appName : str, optional
            Application registry key. (default is "Abaqus/CAE")
        vendorName : str, optional
            Vendor registry key. (default is "SIMULIA")
        productName : str, optional
            Product name. (default is "")
        majorNumber : int, optional
            Version number. (default is -1)
        minorNumber : int, optional
            Release number. (default is -1)
        updateNumber : int, optional
            Update number. (default is -1)
        prerelease : bool, optional
            Official/Prerelease flag. (default is False)
        """
        pass

    def create(self):
        """
        Creates windows for the application.
        """
        pass

    def getAFXMainWindow(self) -> Any:
        """
        Returns a pointer to the AFXMainWindow.
        """
        pass

    def getBasePrerelease(self) -> bool:
        """
        Returns True if the base product is a prerelease.
        """
        pass

    def getBaseProductName(self) -> str:
        """
        Returns the base product name.
        """
        pass

    def getBaseVersionNumbers(self, majorNumber: int, minorNumber: int, updateNumber: int):
        """
        Returns the base product's major, minor, and update numbers.

        Parameters
        ----------
        majorNumber : int
            Version number.
        minorNumber : int
            Release number.
        updateNumber : int
            Update number.
        """
        pass

    def getKernelInitializationCommand(self) -> str:
        """
        Returns the command string that will be issued upon application startup.
        """
        pass

    def getPrerelease(self) -> bool:
        """
        Returns True if this is a prerelease.
        """
        pass

    def getProductName(self) -> str:
        """
        Returns the product name.
        """
        pass

    def getVersionNumbers(self) -> Tuple[int, int, int]:
        """
        Returns the major, minor, and update numbers.
        """
        pass

    def init(self, argc: int, argv: str):
        """
        Initializes the application and connects to the kernel.

        Parameters
        ----------
        argc : int
            The number of command line arguments.
        argv : str
            The command line arguments.
        """
        pass

    def isLocked(self) -> bool:
        """
        Returns True if the GUI is locked or False if otherwise.
        """
        pass

    def isProductCAE(self) -> bool:
        """
        Returns True if the base product is Abaqus/CAE.
        """
        pass

    def isProductViewer(self) -> bool:
        """
        Returns True if the base product is Abaqus/Viewer.
        """
        pass

    def isLearningEdition(self) -> bool:
        """
        Returns True if the base product is a learning edition.
        """
        pass

    def lock(self):
        """
        Locks the GUI (normally used during command and mode processing).
        """
        pass

    def run(self):
        """
        Runs the main application event loop until stop() is called.
        """
        pass

    def runUntil(self, condition: int):
        """
        Run an event loop till some flag becomes non-zero.

        Parameters
        ----------
        condition : int
        """
        pass

    def unlock(self):
        """
        Unlocks the GUI.
        """
        pass
