"""This section lists various auxiliary GUI toolkit functions."""

from __future__ import annotations

from typing import Callable

from .AFXApp import AFXApp
from .AFXModuleGui import AFXModuleGui
from .FXBMPIcon import FXBMPIcon
from .FXFont import FXFont
from .FXGIFIcon import FXGIFIcon
from .FXObject import FXObject
from .FXPNGIcon import FXPNGIcon
from .FXXPMIcon import FXXPMIcon


def addExitCallback(callback: Callable):
    """Registers a callback function to be called when the application is about to exit.

    Parameters
    ----------
    callback : Callable
        The function to be called when the application is about to exit.
    """


def afxCreateIcon(fileName: str) -> FXBMPIcon | FXGIFIcon | FXPNGIcon | FXXPMIcon:  # type: ignore
    """Returns an icon created by reading the specified file, which can be in one of these formats: BMP, GIF,
    PNG, XPM. The file format is assumed from the file extension (which is not case sensitive). Returns 0 if the
    file cannot be opened.

    Parameters
    ----------
    fileName : str
        File name.
    """
    ...


def afxCreateBMPIcon(fileName: str) -> FXBMPIcon:  # type: ignore
    """Returns an icon created by reading the specified file in BMP format. Returns 0 if the file cannot be
    opened.

    Parameters
    ----------
    fileName : str
        File name.
    """
    ...


def afxCreateGIFIcon(fileName: str) -> FXGIFIcon:  # type: ignore
    """Returns an icon created by reading the specified file in GIF format. Returns 0 if the file cannot be
    opened.

    Parameters
    ----------
    fileName : str
        File name.
    """
    ...


def afxCreatePNGIcon(fileName: str) -> FXPNGIcon:  # type: ignore
    """Returns an icon created by reading the specified file in PNG format. Returns 0 if the file cannot be
    opened.

    Parameters
    ----------
    fileName : str
        File name.
    """
    ...


def afxCreateXPMIcon(fileName: str) -> FXXPMIcon:  # type: ignore
    """Returns an icon created by reading the specified file in XPM format. Returns 0 if the file cannot be
    opened.

    Parameters
    ----------
    fileName : str
        File name.
    """
    ...


def afxGetIcon(fileName: str, size: str):
    """Enables you to use Abaqus/CAE icons in your customization. Set the _size_ argument to 1 for normal-sized
    icons or to 0 for small icons.

    Parameters
    ----------
    fileName : str
        File name.
    size : str
        Icon size.
    """


def displayURL(url: str):
    """Displays the specified URL in a web browser. Returns the status of the call. This call will use an open web browser if there is one. This method can be accessed via webBrowser.displayURL from module uti. See also [openWithURL](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAEGUIRefHtml/pt01ch01gob125.htm?contextscope=all#gui-auxiliary-openwithurl).

    Parameters
    ----------
    url : str
        The URL of the page to be displayed.
    """


def getAFXApp() -> AFXApp:  # type: ignore
    """Returns the application object."""
    ...


def getAFXAliasMap():
    """Returns the alias map."""


FONT_PROPORTIONAL: int = hash("FONT_PROPORTIONAL")
FONT_MONOSPACE: int = hash("FONT_MONOSPACE")
FONT_REGULAR: int = hash("FONT_REGULAR")
FONT_BOLD: int = hash("FONT_BOLD")
FONT_ITALIC: int = hash("FONT_ITALIC")
FONT_BASE: int = hash("FONT_BASE")
FONT_SMALL: int = hash("FONT_SMALL")


def getAFXFont(opts: int = FONT_PROPORTIONAL) -> FXFont:  # type: ignore
    """Returns the specified font.

    Parameters
    ----------
    opts : int
        Type of font to get. Possible choices are FONT_PROPORTIONAL, FONT_MONOSPACE, FONT_REGULAR, FONT_BOLD, FONT_ITALIC, FONT_BASE, or FONT_SMALL.
    """
    ...


def afxGetColorHexSpecFromID(colorId: int) -> str:  # type: ignore
    """Returns the equivalent hex string for the specified color index.

    Parameters
    ----------
    colorId : int
        The index of the color to be converted to a hex string. For example, green would be FXRGB(0, 255,0). See the Colors appendix of the Abaqus GUI Toolkit User's Guide for details.
    """
    ...


def afxGetColorHexSpecFromName(colorName: str) -> str:  # type: ignore
    """Returns the equivalent hex string for the specified color name.

    Parameters
    ----------
    colorName : str
        The name of the color to be converted to a hex string. For example, 'Red'. See the Colors appendix of the Abaqus GUI Toolkit User's Guide for details.
    """
    ...


def getCurrentContext() -> dict:  # type: ignore
    """Returns the current GUI context dictionary, which contains the following keys: _mdbName_, _viewportName_,
    _objectPath_, _objectType_, _modelName_, and _moduleName_.

    You can be notified of context changes by using the [registerCurrentContext](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAEGUIRefHtml/pt01ch01gob125.htm?contextscope=all#gui-auxiliary-registercurrentcontext) function.
    """
    ...


def getCurrentModuleGui() -> AFXModuleGui:  # type: ignore
    """Returns the current moduleGui object.

    You can call that object's getModuleName method to check its name.
    """
    ...


def getCursorPosition() -> tuple[bool, float, float, int]:  # type: ignore
    """Returns a tuple of status,x,y,buttonState.

    The status (TRUE or FALSE) indicates the success of the call. The x and y values represent the position
    of the cursor in the window's coordinate system (origin is in the upper left, positive Y points
    downward). This method is defined in FXWindow, so it may be called on any object derived from FXWindow.
    """
    ...


def getDisplayedObjectType() -> str:  # type: ignore
    """Returns the type of the object displayed in the current viewport.

    Possible return values are: PART, ASSEMBLY, ODB, XY_PLOT, SKETCH, or None.
    """
    ...


def getSeparator(parent, count: int):
    """Returns the nth (specified by the count argument) separator widget of the parent.

    Parameters
    ----------
    parent : Widget
        The widget to be searched (children are not traversed).
    count : int
        The number of the separator (e.g. specify 2 to get the second separator).
    """


def getWidgetFromText(parent, text: str) -> FXObject:  # type: ignore
    """Returns a widget whose label or tip text matches the specified text and is also a child of the specified
    widget.

    Parameters
    ----------
    parent : Widget
        The widget at which the search begins (children are traversed too).
    text : str
        The text to be matched (must be an exact match).
    """
    ...


def openWithURL(url: str):
    """Displays the specified URL in a web browser. Returns the status of the call. This call will always open a new web browser. This method can be accessed via webBrowser.openWithURL from module uti. See also [displayURL](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAEGUIRefHtml/pt01ch01gob125.htm?contextscope=all#gui-auxiliary-displayurl).

    Parameters
    ----------
    url : str
        The URL of the page to be displayed.
    """


def registerCurrentContext(callbackFunction: Callable):
    """Registers a query on the current context. The specified callback function will be invoked when the current viewport or displayed object changes. Use the getCurrentContext method to get the values of the current objects. Note that [unregisterCurrentContext](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAEGUIRefHtml/pt01ch01gob125.htm?contextscope=all#gui-auxiliary-unregistercurrentcontext) should be called with the same argument to unregister the query when it is no longer needed.

    Parameters
    ----------
    callbackFunction : Callable
        Function to be called when the current context changes.
    """


def removeExitCallback(callback: Callable):
    """Unregisters a callback function to be called when the application is about to exit. The function must
    have been previously registered using addExitCallback.

    Parameters
    ----------
    callback : Callable
        The function to be removed from the callback list.
    """


def sendCommand(writeToJournal: bool, command: str, writeToReplay: bool = True):
    """Sends a command string to the kernel. **Note:** The _writeToJournal_ argument should not usually be
    necessary. If the command is a built-in Abaqus Scripting Interface command, it will be written to the
    journal file automatically. If the command is not a built-in Abaqus Scripting Interface command but it
    changes the mdb using built-in Abaqus Scripting Interface commands, the changes to the mdb will be written
    to the journal file automatically. However, if the command is not a built-in Abaqus Scripting Interface
    command and it makes changes to the mdb that would not otherwise be written to the journal file, the command
    it should use the journalMethodCall function to write it to the journal file.

    Parameters
    ----------
    writeToJournal : bool
        If True, the command will be written to the journal file.
    command : str
        Command string.
    writeToReplay : bool
        If True, the command will be written to the replay file.
    """


def setCurrentModel(modelName: str):
    """Sets the current model to the specified model name.

    Parameters
    ----------
    modelName : str
        The name of the model to be made current.
    """


def setSwitchModuleHook(callbackFunction: Callable):
    """Sets a function that will be called whenever the user switches into a GUI module. When the user switches
    into a GUI module, the specified function will be called, passing it the name (shown in the Module combo
    box) of the new module. Note that the setSwitchModuleHook function does not take keyword arguments and, if
    necessary, it may be called multiple times.

    Parameters
    ----------
    callbackFunction : Callable
        The function to be called when a GUI module is switched into. Note that you cannot issue a kernel command from within this function or it will cause the application to lock up.
    """


def shutdown():
    """Exits Abaqus/CAE.

    This is equivalent to selecting File->Exit.
    """


def switchModule(moduleName: str):
    """Switches into a GUI module.

    Parameters
    ----------
    moduleName : str
        Module to switch into.
    """


def unregisterCurrentContext(callbackFunction: Callable):
    """Unregisters a query on the current context. The specified callback function should be the same argument
    that was used to register the query.

    Parameters
    ----------
    callbackFunction : Callable
        Function to be called when the current context changes.
    """
