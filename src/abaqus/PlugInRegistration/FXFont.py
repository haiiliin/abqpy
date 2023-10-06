from __future__ import annotations
from .FXApp import FXApp
from .FXFontDesc import FXFontDesc
from .FXId import FXId


class FXFont(FXId):
    """Font class"""

    def __init__(self, a: FXApp, nm: str):
        """Construct a font with given X11 font string.

        Parameters
        ----------
        a : FXApp

        nm : str

        """

    def create(self):
        """Create the font. Reimplemented from FXId."""

    def destroy(self):
        """Destroy the font. Reimplemented from FXId."""

    def detach(self):
        """Detach the font. Reimplemented from FXId."""

    def getEncoding(self):
        """Get character set encoding."""

    def getFontAscent(self):
        """Ascent from baseline."""

    def getFontDesc(self, fontdesc: FXFontDesc):
        """Get font description.

        Parameters
        ----------
        fontdesc : FXFontDesc

        """

    def getFontDescent(self):
        """Descent from baseline."""

    def getFontHeight(self):
        """Height of highest character in font."""

    def getFontLeading(self):
        """Get font leading [that is lead-ing as in Pb!]."""

    def getFontSpacing(self):
        """Get font line spacing."""

    def getFontWidth(self):
        """Width of widest character in font."""

    def getHints(self):
        """Get hints."""

    def getMaxChar(self):
        """Get last character glyph in font."""

    def getMinChar(self):
        """Get first character glyph in font."""

    def getName(self):
        """Get face name."""

    def getSetWidth(self):
        """Get setwidth."""

    def getSize(self):
        """Get size in deci-points."""

    def getSlant(self):
        """Get slant."""

    def getTextHeight(self, text: str, n: int):
        """Calculate height of given text in this font.

        Parameters
        ----------
        text : str
            The string whose height is being evaluated.
        n : int
            The number of characters in 'text,' starting from the left end, for which the height will be returned.
        """

    def getTextWidth(self, text: str, n: int):
        """Calculate width of given text in this font.

        Parameters
        ----------
        text : str
            The string whose width is being evaluated.
        n : int
            The number of characters in 'text,' starting from the left end, for which the width will be returned.
        """

    def getWeight(self):
        """Get font weight."""

    def hasChar(self, ch: int):
        """See if font has glyph for ch.

        Parameters
        ----------
        ch : int

        """

    def isFontMono(self):
        """Find out if the font is monotype or proportional."""

    def leftBearing(self, ch: str):
        """Left bearing.

        Parameters
        ----------
        ch : str

        """

    def rightBearing(self, ch: str):
        """Right bearing.

        Parameters
        ----------
        ch : str

        """

    def setFontDesc(self, fontdesc: FXFontDesc):
        """Change font description.

        Parameters
        ----------
        fontdesc : FXFontDesc

        """
