from __future__ import annotations

from .FXComposite import FXComposite
from .FXObject import FXObject

#: Split horizontally.
SPLITTER_HORIZONTAL: int = hash("SPLITTER_HORIZONTAL")

#: Split vertically.
SPLITTER_VERTICAL: int = hash("SPLITTER_VERTICAL")

#: Reverse-anchored.
SPLITTER_REVERSED: int = hash("SPLITTER_REVERSED")

#: Track continuous during split.
SPLITTER_TRACKING: int = hash("SPLITTER_TRACKING")

#: Normal splitter style.
SPLITTER_NORMAL: int = hash("SPLITTER_NORMAL")


class FXSplitter(FXComposite):
    """Splitter window is used to interactively repartition two or more subpanes.

    Space may be subdivided horizontally or vertically. When the splitter is itself resized, the right-most
    (bottom-most) child window will be resized unless the splitter window is reversed; if the splitter is
    reversed, the left-most (top-most) child window will be resized instead. The splitter widget sends a
    SEL_CHANGED to its target during the resizing of the panes; at the end of the resize interaction, it
    sends a SEL_COMMAND to signify that the resize operation is complete. Normally, children are resizable
    from 0 upwards; however, if the child in a horizontally oriented splitter has LAYOUT_FILL_X in
    combination with LAYOUT_FIX_WIDTH, it will not be made smaller than its default width, except when the
    child is the last visible widget (or first when the option SPLITTER_REVERSED has been passed to the
    splitter). In a vertically oriented splitter, children with LAYOUT_FILL_Y and LAYOUT_FIX_HEIGHT
    behave analogously. These options only affect interactive resizing.
    """

    def __init__(
        self,
        p: FXComposite,
        tgt: FXObject,
        sel: int,
        opts: int = SPLITTER_NORMAL,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
    ):
        """Construct new splitter widget, which will notify target about size changes.

        Parameters
        ----------
        p : FXComposite

        tgt : FXObject

        sel : int

        opts : int

        x : int

        y : int

        w : int

        h : int
        """

    def getDefaultHeight(self):
        """Get default height.

        Reimplemented from FXComposite.
        """

    def getDefaultWidth(self):
        """Get default width.

        Reimplemented from FXComposite.
        """

    def getSplitterStyle(self):
        """Return current splitter style."""

    def setSplitterStyle(self, style: int):
        """Change splitter style.

        Parameters
        ----------
        style : int
        """
