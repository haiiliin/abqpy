from __future__ import annotations

from .FXApp import FXApp
from .FXFontDesc import FXFontDesc
from .FXId import FXId

#: Default pitch.
FONTPITCH_DEFAULT: int = hash("FONTPITCH_DEFAULT")

#: Fixed pitch, mono-spaced.
FONTPITCH_FIXED: int = hash("FONTPITCH_FIXED")

#: Variable pitch, proportional spacing.
FONTPITCH_VARIABLE: int = hash("FONTPITCH_VARIABLE")

#: Don't care which font.
FONTHINT_DONTCARE: int = hash("FONTHINT_DONTCARE")

#: Fancy fonts.
FONTHINT_DECORATIVE: int = hash("FONTHINT_DECORATIVE")

#: Monospace typewriter font.
FONTHINT_MODERN: int = hash("FONTHINT_MODERN")

#: Variable width times-like font, serif.
FONTHINT_ROMAN: int = hash("FONTHINT_ROMAN")

#: Script or cursive.
FONTHINT_SCRIPT: int = hash("FONTHINT_SCRIPT")

#: Helvetica/swiss type font, sans-serif.
FONTHINT_SWISS: int = hash("FONTHINT_SWISS")

#: System font.
FONTHINT_SYSTEM: int = hash("FONTHINT_SYSTEM")

#: X11 Font string.
FONTHINT_X11: int = hash("FONTHINT_X11")

#: Scalable fonts.
FONTHINT_SCALABLE: int = hash("FONTHINT_SCALABLE")

#: Polymorphic fonts.
FONTHINT_POLYMORPHIC: int = hash("FONTHINT_POLYMORPHIC")

#: Don't care about slant.
FONTSLANT_DONTCARE: int = hash("FONTSLANT_DONTCARE")

#: Regular straight up.
FONTSLANT_REGULAR: int = hash("FONTSLANT_REGULAR")

#: Italics.
FONTSLANT_ITALIC: int = hash("FONTSLANT_ITALIC")

#: Oblique slant.
FONTSLANT_OBLIQUE: int = hash("FONTSLANT_OBLIQUE")

#: Reversed italic.
FONTSLANT_REVERSE_ITALIC: int = hash("FONTSLANT_REVERSE_ITALIC")

#: Reversed oblique.
FONTSLANT_REVERSE_OBLIQUE: int = hash("FONTSLANT_REVERSE_OBLIQUE")

#: Don't care character encoding.
FONTENCODING_DEFAULT: int = hash("FONTENCODING_DEFAULT")

#: Cyrillic (almost obsolete).
FONTENCODING_ISO_8859_5: int = hash("FONTENCODING_ISO_8859_5")

#: Russian.
FONTENCODING_KOI8_R: int = hash("FONTENCODING_KOI8_R")

#: Ukrainian.
FONTENCODING_KOI8_U: int = hash("FONTENCODING_KOI8_U")

#: Latin 1 (West European).
FONTENCODING_LATIN1: int = hash("FONTENCODING_LATIN1")

#: Latin 2 (East European).
FONTENCODING_LATIN2: int = hash("FONTENCODING_LATIN2")

#: Latin 3 (South European).
FONTENCODING_LATIN3: int = hash("FONTENCODING_LATIN3")

#: Latin 4 (North European).
FONTENCODING_LATIN4: int = hash("FONTENCODING_LATIN4")

#: Latin 5 (Turkish).
FONTENCODING_LATIN5: int = hash("FONTENCODING_LATIN5")

#: Latin 6 (Nordic).
FONTENCODING_LATIN6: int = hash("FONTENCODING_LATIN6")

#: Latin 7 (Baltic Rim).
FONTENCODING_LATIN7: int = hash("FONTENCODING_LATIN7")

#: Latin 8 (Celtic).
FONTENCODING_LATIN8: int = hash("FONTENCODING_LATIN8")

#: Latin 9 AKA Latin 0.
FONTENCODING_LATIN9: int = hash("FONTENCODING_LATIN9")

#: Latin 10.
FONTENCODING_LATIN10: int = hash("FONTENCODING_LATIN10")

#: Latin 1.
FONTENCODING_USASCII: int = hash("FONTENCODING_USASCII")

#: Latin 1 (West European).
FONTENCODING_WESTEUROPE: int = hash("FONTENCODING_WESTEUROPE")

#: Latin 2 (East European).
FONTENCODING_EASTEUROPE: int = hash("FONTENCODING_EASTEUROPE")

#: Latin 3 (South European).
FONTENCODING_SOUTHEUROPE: int = hash("FONTENCODING_SOUTHEUROPE")

#: Latin 4 (North European).
FONTENCODING_NORTHEUROPE: int = hash("FONTENCODING_NORTHEUROPE")

#: Cyrillic.
FONTENCODING_CYRILLIC: int = hash("FONTENCODING_CYRILLIC")

#: Cyrillic.
FONTENCODING_RUSSIAN: int = hash("FONTENCODING_RUSSIAN")

#: Arabic.
FONTENCODING_ARABIC: int = hash("FONTENCODING_ARABIC")

#: Greek.
FONTENCODING_GREEK: int = hash("FONTENCODING_GREEK")

#: Hebrew.
FONTENCODING_HEBREW: int = hash("FONTENCODING_HEBREW")

#: Latin 5 (Turkish).
FONTENCODING_TURKISH: int = hash("FONTENCODING_TURKISH")

#: Latin 6 (Nordic).
FONTENCODING_NORDIC: int = hash("FONTENCODING_NORDIC")

#: Thai.
FONTENCODING_THAI: int = hash("FONTENCODING_THAI")

#: Latin 7 (Baltic Rim).
FONTENCODING_BALTIC: int = hash("FONTENCODING_BALTIC")

#: Latin 8 (Celtic).
FONTENCODING_CELTIC: int = hash("FONTENCODING_CELTIC")

#: Don't care about weight.
FONTWEIGHT_DONTCARE: int = hash("FONTWEIGHT_DONTCARE")

#: Thin.
FONTWEIGHT_THIN: int = hash("FONTWEIGHT_THIN")

#: Extra light.
FONTWEIGHT_EXTRALIGHT: int = hash("FONTWEIGHT_EXTRALIGHT")

#: Light.
FONTWEIGHT_LIGHT: int = hash("FONTWEIGHT_LIGHT")

#: Normal or regular weight.
FONTWEIGHT_NORMAL: int = hash("FONTWEIGHT_NORMAL")

#: Normal or regular weight.
FONTWEIGHT_REGULAR: int = hash("FONTWEIGHT_REGULAR")

#: Medium bold face.
FONTWEIGHT_MEDIUM: int = hash("FONTWEIGHT_MEDIUM")

#: Demi bold face.
FONTWEIGHT_DEMIBOLD: int = hash("FONTWEIGHT_DEMIBOLD")

#: Bold face.
FONTWEIGHT_BOLD: int = hash("FONTWEIGHT_BOLD")

#: Extra.
FONTWEIGHT_EXTRABOLD: int = hash("FONTWEIGHT_EXTRABOLD")

#: Heavy.
FONTWEIGHT_HEAVY: int = hash("FONTWEIGHT_HEAVY")

#: Black.
FONTWEIGHT_BLACK: int = hash("FONTWEIGHT_BLACK")

#: Don't care about set width.
FONTSETWIDTH_DONTCARE: int = hash("FONTSETWIDTH_DONTCARE")

#: Ultra condensed printing.
FONTSETWIDTH_ULTRACONDENSED: int = hash("FONTSETWIDTH_ULTRACONDENSED")

#: Extra condensed.
FONTSETWIDTH_EXTRACONDENSED: int = hash("FONTSETWIDTH_EXTRACONDENSED")

#: Condensed.
FONTSETWIDTH_CONDENSED: int = hash("FONTSETWIDTH_CONDENSED")

#: Narrow.
FONTSETWIDTH_NARROW: int = hash("FONTSETWIDTH_NARROW")

#: Compressed.
FONTSETWIDTH_COMPRESSED: int = hash("FONTSETWIDTH_COMPRESSED")

#: Semi-condensed.
FONTSETWIDTH_SEMICONDENSED: int = hash("FONTSETWIDTH_SEMICONDENSED")

#: Medium printing.
FONTSETWIDTH_MEDIUM: int = hash("FONTSETWIDTH_MEDIUM")

#: Normal printing.
FONTSETWIDTH_NORMAL: int = hash("FONTSETWIDTH_NORMAL")

#: Regular printing.
FONTSETWIDTH_REGULAR: int = hash("FONTSETWIDTH_REGULAR")

#: Semi expanded.
FONTSETWIDTH_SEMIEXPANDED: int = hash("FONTSETWIDTH_SEMIEXPANDED")

#: Expanded.
FONTSETWIDTH_EXPANDED: int = hash("FONTSETWIDTH_EXPANDED")

#: Wide.
FONTSETWIDTH_WIDE: int = hash("FONTSETWIDTH_WIDE")

#: Extra expanded.
FONTSETWIDTH_EXTRAEXPANDED: int = hash("FONTSETWIDTH_EXTRAEXPANDED")

#: Ultra expanded.
FONTSETWIDTH_ULTRAEXPANDED: int = hash("FONTSETWIDTH_ULTRAEXPANDED")


class FXFont(FXId):
    """Font class."""

    def __init__(self, a: FXApp, nm: str):
        """Construct a font with given X11 font string.

        Parameters
        ----------
        a : FXApp

        nm : str
        """

    def create(self):
        """Create the font.

        Reimplemented from FXId.
        """

    def destroy(self):
        """Destroy the font.

        Reimplemented from FXId.
        """

    def detach(self):
        """Detach the font.

        Reimplemented from FXId.
        """

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
