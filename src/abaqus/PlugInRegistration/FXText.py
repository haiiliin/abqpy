from __future__ import annotations

from .FXColor import FXColor
from .FXComposite import FXComposite
from .FXFont import FXFont
from .FXObject import FXObject
from .FXScrollArea import FXScrollArea

#: Text is NOT editable.
TEXT_READONLY: int = hash("TEXT_READONLY")

#: Wrap at word breaks.
TEXT_WORDWRAP: int = hash("TEXT_WORDWRAP")

#: Overstrike mode.
TEXT_OVERSTRIKE: int = hash("TEXT_OVERSTRIKE")

#: Fixed wrap columns.
TEXT_FIXEDWRAP: int = hash("TEXT_FIXEDWRAP")

#: Insert spaces for tabs.
TEXT_NO_TABS: int = hash("TEXT_NO_TABS")

#: Autoindent.
TEXT_AUTOINDENT: int = hash("TEXT_AUTOINDENT")

#: Show active line.
TEXT_SHOWACTIVE: int = hash("TEXT_SHOWACTIVE")

#: Select characters.
SELECT_CHARS: int = hash("SELECT_CHARS")

#: Select words.
SELECT_WORDS: int = hash("SELECT_WORDS")

#: Select lines.
SELECT_LINES: int = hash("SELECT_LINES")


class FXText(FXScrollArea):
    """Multiline text widget."""

    def __init__(
        self,
        p: FXComposite,
        tgt: FXObject | None = None,
        sel: int = 0,
        opts: int = 0,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
    ):
        """Construct multi-line text widget.

        Parameters
        ----------
        p : FXComposite

        tgt : FXObject | None

        sel : int

        opts : int

        x : int

        y : int

        w : int

        h : int
        """

    def appendText(self, text: str, n: int, notify: bool = False):
        """Append n characters of text at the end of the buffer.

        Parameters
        ----------
        text : str

        n : int

        notify : bool
        """

    def canFocus(self):
        """Returns True because a text widget can receive focus.

        Reimplemented from FXWindow.
        """

    def create(self):
        """Create server-side resources.

        Reimplemented from FXComposite.
        """

    def detach(self):
        """Detach server-side resources.

        Reimplemented from FXComposite.
        """

    def disable(self):
        """Disable the text widget.

        Reimplemented from FXWindow.
        """

    def enable(self):
        """Enable the text widget.

        Reimplemented from FXWindow.
        """

    def getBarColor(self):
        """Return bar color."""

    def getBarColumns(self):
        """Return number of columns used for line numbers."""

    def getChar(self, pos: int):
        """Get character at position in text buffer.

        Parameters
        ----------
        pos : int
        """

    def getContentHeight(self):
        """Get default height.

        Reimplemented from FXScrollArea.
        """

    def getContentWidth(self):
        """Get default width.

        Reimplemented from FXScrollArea.
        """

    def getCursorCol(self):
        """Return cursor row, i.e. indent position."""

    def getCursorColor(self):
        """Return cursor color."""

    def getCursorPos(self):
        """Return the cursor position."""

    def getCursorRow(self):
        """Return cursor row."""

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXScrollArea.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXScrollArea.
        """

    def getFont(self):
        """Return text font."""

    def getLength(self):
        """Return length of buffer."""

    def getMarginBottom(self):
        """Return bottom margin."""

    def getMarginLeft(self):
        """Return left margin."""

    def getMarginRight(self):
        """Return right margin."""

    def getMarginTop(self):
        """Return top margin."""

    def getNumberColor(self):
        """Return line number color."""

    def getPosAt(self, x: int, y: int):
        """Return text position at given visible x,y coordinate.

        Parameters
        ----------
        x : int

        y : int
        """

    def getSelBackColor(self):
        """Return selected background color."""

    def getSelEndPos(self):
        """Return selendpos."""

    def getSelStartPos(self):
        """Return selstartpos."""

    def getSelTextColor(self):
        """Return selected text color."""

    def getText(self, text: str, n: int):
        """Retrieve text into buffer.

        Parameters
        ----------
        text : str

        n : int
        """

    def getTextColor(self):
        """Return text color."""

    def getTopLine(self):
        """Return position of top line."""

    def getVisCols(self):
        """Return number of visible columns."""

    def getVisRows(self):
        """Return number of visible rows."""

    def insertText(self, pos: int, text: str, n: int, notify: bool = False):
        """Insert n characters of text at position pos into the buffer.

        Parameters
        ----------
        pos : int

        text : str

        n : int

        notify : bool
        """

    def isEditable(self):
        """Return True if text is editable."""

    def isModified(self):
        """Return True if text was modified."""

    def isPosSelected(self, pos: int):
        """Return True if position pos is selected.

        Parameters
        ----------
        pos : int
        """

    def killSelection(self, notify: bool = False):
        """Unselect the text.

        Parameters
        ----------
        notify : bool
        """

    def lineEnd(self, pos: int):
        """Return position of end of line containing position pos.

        Parameters
        ----------
        pos : int
        """

    def lineStart(self, pos: int):
        """Return position of begin of line containing position pos.

        Parameters
        ----------
        pos : int
        """

    def makePositionVisible(self, pos: int):
        """Scroll text to make the given position visible.

        Parameters
        ----------
        pos : int
        """

    def moveContents(self, x: int, y: int):
        """Scroll the contents. Reimplemented from FXScrollArea.

        Parameters
        ----------
        x : int

        y : int
        """

    def nextLine(self, pos: int, nl: int = 1):
        """Return start of next line.

        Parameters
        ----------
        pos : int

        nl : int
        """

    def nextRow(self, pos: int, nr: int = 1):
        """Return start of next row.

        Parameters
        ----------
        pos : int

        nr : int
        """

    def position(self, x: int, y: int, w: int, h: int):
        """Move and resize this window in the parent's coordinates. Reimplemented from FXWindow.

        Parameters
        ----------
        x : int

        y : int

        w : int

        h : int
        """

    def prevLine(self, pos: int, nl: int = 1):
        """Return start of previous line.

        Parameters
        ----------
        pos : int

        nl : int
        """

    def prevRow(self, pos: int, nr: int = 1):
        """Return start of previous row.

        Parameters
        ----------
        pos : int

        nr : int
        """

    def recalc(self):
        """Need to recalculate size.

        Reimplemented from FXWindow.
        """

    def removeText(self, pos: int, n: int, notify: bool = False):
        """Remove n characters of text at position pos from the buffer.

        Parameters
        ----------
        pos : int

        n : int

        notify : bool
        """

    def replaceText(self, pos: int, m: int, text: str, n: int, notify: bool = False):
        """Replace m characters at pos by n characters.

        Parameters
        ----------
        pos : int

        m : int

        text : str

        n : int

        notify : bool
        """

    def resize(self, w: int, h: int):
        """Resize this window to the specified width and height. Reimplemented from FXWindow.

        Parameters
        ----------
        w : int

        h : int
        """

    def rowEnd(self, pos: int):
        """Return row end.

        Parameters
        ----------
        pos : int
        """

    def rowStart(self, pos: int):
        """Return row start.

        Parameters
        ----------
        pos : int
        """

    def setBarColor(self, clr: FXColor):
        """Change bar color.

        Parameters
        ----------
        clr : FXColor
        """

    def setBarColumns(self, cols: int):
        """Change number of columns used for line numbers.

        Parameters
        ----------
        cols : int
        """

    def setBottomLine(self, pos: int):
        """Make line containing pos the bottom line.

        Parameters
        ----------
        pos : int
        """

    def setCursorCol(self, col: int, notify: bool = False):
        """Set cursor column.

        Parameters
        ----------
        col : int

        notify : bool
        """

    def setCursorColor(self, clr: FXColor):
        """Change cursor color.

        Parameters
        ----------
        clr : FXColor
        """

    def setCursorPos(self, pos: int, notify: bool = False):
        """Set the cursor position.

        Parameters
        ----------
        pos : int

        notify : bool
        """

    def setCursorRow(self, row: int, notify: bool = False):
        """Set cursor row.

        Parameters
        ----------
        row : int

        notify : bool
        """

    def setEditable(self, edit: bool = True):
        """Set editable flag.

        Parameters
        ----------
        edit : bool
        """

    def setFont(self, fnt: FXFont):
        """Change text font.

        Parameters
        ----------
        fnt : FXFont
        """

    def setMarginBottom(self, pb: int):
        """Change bottom margin.

        Parameters
        ----------
        pb : int
        """

    def setMarginLeft(self, pl: int):
        """Change left margin.

        Parameters
        ----------
        pl : int
        """

    def setMarginRight(self, pr: int):
        """Change right margin.

        Parameters
        ----------
        pr : int
        """

    def setMarginTop(self, pt: int):
        """Change top margin.

        Parameters
        ----------
        pt : int
        """

    def setModified(self, mod: bool = True):
        """Set modified flag.

        Parameters
        ----------
        mod : bool
        """

    def setNumberColor(self, clr: FXColor):
        """Change line number color.

        Parameters
        ----------
        clr : FXColor
        """

    def setSelBackColor(self, clr: FXColor):
        """Change selected background color.

        Parameters
        ----------
        clr : FXColor
        """

    def setSelection(self, pos: int, len: int, notify: bool = False):
        """Select len characters starting at given position pos.

        Parameters
        ----------
        pos : int

        len : int

        notify : bool
        """

    def setSelTextColor(self, clr: FXColor):
        """Change selected text color.

        Parameters
        ----------
        clr : FXColor
        """

    def setText(self, text: str, n: int, notify: bool = False):
        """Change the text in the buffer to new text.

        Parameters
        ----------
        text : str

        n : int

        notify : bool
        """

    def setTextColor(self, clr: FXColor):
        """Change text color.

        Parameters
        ----------
        clr : FXColor
        """

    def setTopLine(self, pos: int):
        """Make line containing pos the top line.

        Parameters
        ----------
        pos : int
        """

    def setVisCols(self, cols: int):
        """Change number of visible columns.

        Parameters
        ----------
        cols : int
        """

    def setVisRows(self, rows: int):
        """Change number of visible rows.

        Parameters
        ----------
        rows : int
        """
