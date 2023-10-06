from __future__ import annotations

from .FXChore import FXChore
from .FXColor import FXColor
from .FXFont import FXFont
from .FXInputHandle import FXInputHandle
from .FXObject import FXObject
from .FXTimer import FXTimer
from .FXWindow import FXWindow
from .SOCKET import SOCKET

#: Inactive.
INPUT_NONE: int = hash("INPUT_NONE")

#: Read input fd.
INPUT_READ: int = hash("INPUT_READ")

#: Write input fd.
INPUT_WRITE: int = hash("INPUT_WRITE")

#: Except input fd.
INPUT_EXCEPT: int = hash("INPUT_EXCEPT")

#: Non modal event loop (dispatch normally).
MODAL_FOR_NONE: int = hash("MODAL_FOR_NONE")

#: Modal dialog (beep if outside of modal dialog).
MODAL_FOR_WINDOW: int = hash("MODAL_FOR_WINDOW")

#: Modal for popup (always dispatch to popup).
MODAL_FOR_POPUP: int = hash("MODAL_FOR_POPUP")

#: Arrow cursor.
DEF_ARROW_CURSOR: int = hash("DEF_ARROW_CURSOR")

#: Reverse arrow cursor.
DEF_RARROW_CURSOR: int = hash("DEF_RARROW_CURSOR")

#: Text cursor.
DEF_TEXT_CURSOR: int = hash("DEF_TEXT_CURSOR")

#: Horizontal split cursor.
DEF_HSPLIT_CURSOR: int = hash("DEF_HSPLIT_CURSOR")

#: Vertical split cursor.
DEF_VSPLIT_CURSOR: int = hash("DEF_VSPLIT_CURSOR")

#: Cross split cursor.
DEF_XSPLIT_CURSOR: int = hash("DEF_XSPLIT_CURSOR")

#: Color swatch drag cursor.
DEF_SWATCH_CURSOR: int = hash("DEF_SWATCH_CURSOR")

#: Move cursor.
DEF_MOVE_CURSOR: int = hash("DEF_MOVE_CURSOR")

#: Resize horizontal edge.
DEF_DRAGH_CURSOR: int = hash("DEF_DRAGH_CURSOR")

#: Resize vertical edge.
DEF_DRAGV_CURSOR: int = hash("DEF_DRAGV_CURSOR")

#: Resize upper-leftcorner.
DEF_DRAGTL_CURSOR: int = hash("DEF_DRAGTL_CURSOR")

#: Resize bottom-right corner.
DEF_DRAGBR_CURSOR: int = hash("DEF_DRAGBR_CURSOR")

#: Resize upper-right corner.
DEF_DRAGTR_CURSOR: int = hash("DEF_DRAGTR_CURSOR")

#: Resize bottom-left corner.
DEF_DRAGBL_CURSOR: int = hash("DEF_DRAGBL_CURSOR")

#: Drag and drop stop.
DEF_DNDSTOP_CURSOR: int = hash("DEF_DNDSTOP_CURSOR")

#: Drag and drop copy.
DEF_DNDCOPY_CURSOR: int = hash("DEF_DNDCOPY_CURSOR")

#: Drag and drop move.
DEF_DNDMOVE_CURSOR: int = hash("DEF_DNDMOVE_CURSOR")

#: Drag and drop link.
DEF_DNDLINK_CURSOR: int = hash("DEF_DNDLINK_CURSOR")

#: Cross hair cursor.
DEF_CROSSHAIR_CURSOR: int = hash("DEF_CROSSHAIR_CURSOR")

#: North-east cursor.
DEF_CORNERNE_CURSOR: int = hash("DEF_CORNERNE_CURSOR")

#: North-west cursor.
DEF_CORNERNW_CURSOR: int = hash("DEF_CORNERNW_CURSOR")

#: South-east cursor.
DEF_CORNERSE_CURSOR: int = hash("DEF_CORNERSE_CURSOR")

#: South-west cursor.
DEF_CORNERSW_CURSOR: int = hash("DEF_CORNERSW_CURSOR")

#: Rotate cursor.
DEF_ROTATE_CURSOR: int = hash("DEF_ROTATE_CURSOR")


class FXApp(FXObject):
    """Application Object."""

    #: Terminate the application normally.
    ID_QUIT: int = hash("ID_QUIT")

    #: Dump the current widget tree.
    ID_DUMP: int = hash("ID_DUMP")

    def __init__(self, name: str = "Application", vendor: str = "FoxDefault"):
        """Copyright notice of library. Construct application object; the name and vendor strings are used as
        keys into the registry database for this application's settings.

        Parameters
        ----------
        name : str

        vendor : str
        """

    def addChore(self, tgt: FXObject, sel: int):
        """Add a idle processing message to be sent to target object when the system becomes idle, i.e. there
        are no events to be processed.

        Parameters
        ----------
        tgt : FXObject

        sel : int
        """

    def addInput(self, fd: FXInputHandle, mode: int, tgt: FXObject, sel: int):
        """Add a file descriptor fd to be watched for activity as determined by mode, where mode is a bitwise OR
        (INPUT_READ, INPUT_WRITE, INPUT_EXCEPT). A message of type SEL_IO_READ, SEL_IO_WRITE, or SEL_IO_EXCEPT
        will be sent to the target when the specified activity is detected on the file descriptor. On Windows, a
        Win32 event, not a file descriptor, must be specified. The client code for this interface must be
        platform-dependent. See addSocket below for a portable interface. CAE.

        Parameters
        ----------
        fd : FXInputHandle

        mode : int

        tgt : FXObject

        sel : int
        """

    def addSocket(self, sd: SOCKET, mode: int, tgt: FXObject, sel: int):
        """CAE Add a socket descriptor sd to be watched for activity as determined by mode, where mode is a
        bitwise OR (INPUT_READ, INPUT_WRITE, INPUT_EXCEPT). A message of type SEL_IO_READ, SEL_IO_WRITE, or
        SEL_IO_EXCEPT will be sent to the target when the specified activity is detected on the socket
        descriptor. This is identical to addInput on Unix. It behaves the same on Windows.

        Parameters
        ----------
        sd : SOCKET

        mode : int

        tgt : FXObject

        sel : int
        """

    def addTimeout(self, ms: int, tgt: FXObject, sel: int):
        """Add timeout message to be sent to target object in ms milliseconds; the timer fires only once after
        the interval expires.

        Parameters
        ----------
        ms : int

        tgt : FXObject

        sel : int
        """

    def beep(self):
        """Beep."""

    def beginWaitCursor(self):
        """Begin of wait-cursor block; wait-cursor blocks may be nested."""

    def create(self):
        """Create application's windows.

        Reimplemented in AFXApp.
        """

    def endWaitCursor(self):
        """End of wait-cursor block."""

    def forceRefresh(self):
        """Force GUI refresh."""

    def getAppName(self):
        """Get application name."""

    def getBorderColor(self):
        """Obtain default colors."""

    def getMainWindow(self):
        """Get main window, if any."""

    def getMonoVisual(self):
        """Get monochrome visual."""

    def getNormalFont(self):
        """Return default font."""

    def getRoot(self):
        """Get root Window."""

    def getTypingSpeed(self):
        """Obtain application-wide settings."""

    def init(self, argc: int, argv: str, connect: bool = True):
        """Initialize application. Parses and removes common command line arguments, reads the registry.
        Finally, if connect is True, it opens the display.

        Parameters
        ----------
        argc : int

        argv : str

        connect : bool
        """

    def peekEvent(self):
        """Peek to determine if there's an event."""

    def refresh(self):
        """Schedule a refresh."""

    def removeChore(self, c: FXChore):
        """Remove idle processing message.

        Parameters
        ----------
        c : FXChore
        """

    def removeInput(self, fd: FXInputHandle, mode: int):
        """Remove input message and target object for the specified file descriptor and mode, which is a bitwise
        OR of (INPUT_READ, INPUT_WRITE, INPUT_EXCEPT).

        Parameters
        ----------
        fd : FXInputHandle

        mode : int
        """

    def removeSocket(self, sd: SOCKET, mode: int):
        """CAE Remove input message and target object for the specified socket descriptor and mode, which is a
        bitwise OR of (INPUT_READ, INPUT_WRITE, INPUT_EXCEPT).

        Parameters
        ----------
        sd : SOCKET

        mode : int
        """

    def removeTimeout(self, t: FXTimer):
        """Remove timeout, returns NULL.

        Parameters
        ----------
        t : FXTimer
        """

    def repaint(self):
        """Paint all windows marked for repainting.

        On return all the applications windows have been painted.
        """

    def run(self):
        """Run the main application event loop until stop() is called, and return the exit code passed as
        argument to stop().

        Reimplemented in AFXApp.
        """

    def runOneEvent(self):
        """Perform one event dispatch."""

    def runUntil(self, condition: int):
        """Run an event loop till some flag becomes non-zero. Reimplemented in AFXApp.

        Parameters
        ----------
        condition : int
        """

    def runWhileEvents(self, window: FXWindow | None = None):
        """Run event loop while there are events are available in the queue. Returns 1 when all events in the
        queue have been handled, and 0 when the event loop was terminated due to stop() or stopModal(). Except
        for the modal window and its children, user input to all windows is blocked; if the modal window is NULL
        all user input is blocked.

        Parameters
        ----------
        window : FXWindow | None
        """

    def setBorderColor(self, color: FXColor):
        """Change default colors.

        Parameters
        ----------
        color : FXColor
        """

    def setNormalFont(self, font: FXFont):
        """Change default font.

        Parameters
        ----------
        font : FXFont
        """

    def setTypingSpeed(self, speed: int):
        """Change application-wide settings.

        Parameters
        ----------
        speed : int
        """

    def stop(self, value: int = 0):
        """Terminate the outermost event loop, and all inner modal loops; All more deeper nested event loops
        will be terminated with code equal to 0, while the outermost event loop will return code equal to value.

        Parameters
        ----------
        value : int
        """
