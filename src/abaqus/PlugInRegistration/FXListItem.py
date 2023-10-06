from __future__ import annotations

from .FXObject import FXObject

#: Extended selection mode allows for drag-selection of ranges of items.
LIST_EXTENDEDSELECT: int = hash("LIST_EXTENDEDSELECT")

#: Single selection mode allows up to one item to be selected.
LIST_SINGLESELECT: int = hash("LIST_SINGLESELECT")

#: Browse selection mode enforces one single item to be selected at all times.
LIST_BROWSESELECT: int = hash("LIST_BROWSESELECT")

#: Multiple selection mode is used for selection of individual items.
LIST_MULTIPLESELECT: int = hash("LIST_MULTIPLESELECT")

#: Automatically select under cursor.
LIST_AUTOSELECT: int = hash("LIST_AUTOSELECT")


class FXListItem(FXObject):
    """List item."""
