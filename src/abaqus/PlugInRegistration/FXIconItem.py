from __future__ import annotations

from .FXObject import FXObject

#: Extended selection mode.
ICONLIST_EXTENDEDSELECT: int = hash("ICONLIST_EXTENDEDSELECT")

#: At most one selected item.
ICONLIST_SINGLESELECT: int = hash("ICONLIST_SINGLESELECT")

#: Always exactly one selected item.
ICONLIST_BROWSESELECT: int = hash("ICONLIST_BROWSESELECT")

#: Multiple selection mode.
ICONLIST_MULTIPLESELECT: int = hash("ICONLIST_MULTIPLESELECT")

#: Automatically size item spacing.
ICONLIST_AUTOSIZE: int = hash("ICONLIST_AUTOSIZE")

#: List mode.
ICONLIST_DETAILED: int = hash("ICONLIST_DETAILED")

#: Mini Icon mode.
ICONLIST_MINI_ICONS: int = hash("ICONLIST_MINI_ICONS")

#: Big Icon mode.
ICONLIST_BIG_ICONS: int = hash("ICONLIST_BIG_ICONS")

#: Row-wise mode.
ICONLIST_ROWS: int = hash("ICONLIST_ROWS")

#: Column-wise mode.
ICONLIST_COLUMNS: int = hash("ICONLIST_COLUMNS")


class FXIconItem(FXObject):
    """Icon item."""
