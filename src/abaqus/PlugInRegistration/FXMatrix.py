from __future__ import annotations

from .constants import DEFAULT_SPACING
from .FXComposite import FXComposite
from .FXPacker import FXPacker

#: Fixed number of rows, add columns as needed.
MATRIX_BY_ROWS: int = hash("MATRIX_BY_ROWS")

#: Fixed number of columns, adding rows as needed.
MATRIX_BY_COLUMNS: int = hash("MATRIX_BY_COLUMNS")


class FXMatrix(FXPacker):
    """The Matrix layout manager automatically arranges its child windows in rows and columns.

    If the matrix style is MATRIX_BY_ROWS, then the matrix will have the given number of rows and the
    number of columns grows as more child windows are added; if the matrix style is MATRIX_BY_COLUMNS,
    then the number of columns is fixed and the number of rows grows as more children are added. If all
    children in a row (column) have the LAYOUT_FILL_ROW (LAYOUT_FILL_COLUMN) hint set, then the row
    (column) will be stretchable as the matrix layout manager itself is resized. If more than one row
    (column) is stretchable, the space is apportioned to each stretchable row (column) proportionally.
    Within each cell of the matrix, all other layout hints are observed. For example, a child having
    LAYOUT_CENTER_Y and LAYOUT_FILL_X hints will be centered in the Y-direction, while being stretched
    in the X-direction. Empty cells can be obtained by simply placing a borderless FXFrame widget as a
    space-holder.
    """

    def __init__(
        self,
        p: FXComposite,
        n: int = 1,
        opts: int = MATRIX_BY_ROWS,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        pl: int = DEFAULT_SPACING,
        pr: int = DEFAULT_SPACING,
        pt: int = DEFAULT_SPACING,
        pb: int = DEFAULT_SPACING,
        hs: int = DEFAULT_SPACING,
        vs: int = DEFAULT_SPACING,
    ):
        """Construct a matrix layout manager with n rows or columns.

        Parameters
        ----------
        p : FXComposite

        n : int

        opts : int

        x : int

        y : int

        w : int

        h : int

        pl : int

        pr : int

        pt : int

        pb : int

        hs : int

        vs : int
        """

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXPacker.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXPacker.
        """

    def getNumColumns(self):
        """Return the number of columns."""

    def getNumRows(self):
        """Return the number of rows."""

    def setNumColumns(self, nc: int):
        """Change the number of columns.

        Parameters
        ----------
        nc : int
        """

    def setNumRows(self, nr: int):
        """Change the number of rows.

        Parameters
        ----------
        nr : int
        """
