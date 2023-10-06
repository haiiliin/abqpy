from __future__ import annotations

from .FXObject import FXObject

#: Extended selection mode allows for drag-selection of ranges of items.
TREELIST_EXTENDEDSELECT: int = hash("TREELIST_EXTENDEDSELECT")

#: Single selection mode allows up to one item to be selected.
TREELIST_SINGLESELECT: int = hash("TREELIST_SINGLESELECT")

#: Browse selection mode enforces one single item to be selected at all times.
TREELIST_BROWSESELECT: int = hash("TREELIST_BROWSESELECT")

#: Multiple selection mode is used for selection of individual items.
TREELIST_MULTIPLESELECT: int = hash("TREELIST_MULTIPLESELECT")

#: Automatically select under cursor.
TREELIST_AUTOSELECT: int = hash("TREELIST_AUTOSELECT")

#: Lines shown.
TREELIST_SHOWS_LINES: int = hash("TREELIST_SHOWS_LINES")

#: Boxes to expand shown.
TREELIST_SHOWS_BOXES: int = hash("TREELIST_SHOWS_BOXES")

#: Display root boxes also.
TREELIST_ROOT_BOXES: int = hash("TREELIST_ROOT_BOXES")

#: Display check boxes.
TREELIST_CHECK_BOXES: int = hash("TREELIST_CHECK_BOXES")

#: Propagate checked state to children and parents.
TREELIST_PROPAGATE_CHECKS: int = hash("TREELIST_PROPAGATE_CHECKS")


class FXTreeItem(FXObject):
    """Tree list Item."""
