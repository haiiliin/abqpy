from __future__ import annotations

from .FXWindow import FXWindow

#: Automatically gray out when not updated.
MENU_AUTOGRAY: int = hash("MENU_AUTOGRAY")

#: Automatically hide button when not updated.
MENU_AUTOHIDE: int = hash("MENU_AUTOHIDE")


class FXMenuCaption(FXWindow):
    """The menu caption is a widget which can be used as a caption above a number of menu commands in a menu."""
