from __future__ import annotations

from .FXLabel import FXLabel

#: Automatically gray out when no target.
MENUBUTTON_AUTOGRAY: int = hash("MENUBUTTON_AUTOGRAY")

#: Automatically hide when no target.
MENUBUTTON_AUTOHIDE: int = hash("MENUBUTTON_AUTOHIDE")

#: Toolbar style.
MENUBUTTON_TOOLBAR: int = hash("MENUBUTTON_TOOLBAR")

#: CAE - Combobox style.
MENUBUTTON_COMBOBOX: int = hash("MENUBUTTON_COMBOBOX")

#: Popup window appears below menu button.
MENUBUTTON_DOWN: int = hash("MENUBUTTON_DOWN")

#: Popup window appears above menu button.
MENUBUTTON_UP: int = hash("MENUBUTTON_UP")

#: Popup window to the left of the menu button.
MENUBUTTON_LEFT: int = hash("MENUBUTTON_LEFT")

#: Popup window to the right of the menu button.
MENUBUTTON_RIGHT: int = hash("MENUBUTTON_RIGHT")

#: Do not show arrows.
MENUBUTTON_NOARROWS: int = hash("MENUBUTTON_NOARROWS")

#: Popup attaches to the left side of the menu button.
MENUBUTTON_ATTACH_LEFT: int = hash("MENUBUTTON_ATTACH_LEFT")

#: Popup attaches to the top of the menu button.
MENUBUTTON_ATTACH_TOP: int = hash("MENUBUTTON_ATTACH_TOP")

#: Popup attaches to the right side of the menu button.
MENUBUTTON_ATTACH_RIGHT: int = hash("MENUBUTTON_ATTACH_RIGHT")

#: Popup attaches to the bottom of the menu button.
MENUBUTTON_ATTACH_BOTTOM: int = hash("MENUBUTTON_ATTACH_BOTTOM")

#: Popup attaches to the center of the menu button.
MENUBUTTON_ATTACH_CENTER: int = hash("MENUBUTTON_ATTACH_CENTER")

#: Popup attaches to both sides of the menu button.
MENUBUTTON_ATTACH_BOTH: int = hash("MENUBUTTON_ATTACH_BOTH")


class FXMenuButton(FXLabel):
    """A menu button posts a popup menu when clicked.

    There are many ways to control the placement where the popup will appear; first, the popup may be placed
    on either of the four sides relative to the menu button; this is controlled by the flags
    MENUBUTTON_DOWN, etc. Next, there are several attachment modes; the popup's left/bottom edge may attach
    to the menu button's left/top edge, or the popup's right/top edge may attach to the menu button's
    right/bottom edge, or both. Also, the popup may apear centered relative to the menu button. Finally, a
    small offset may be specified to displace the location of the popup by a few pixels so as to account for
    borders and so on. Normally, the menu button shows an arrow pointing to the direction where the popup is
    set to appear; this can be turned off by passing the option MENUBUTTON_NOARROWS.
    """
