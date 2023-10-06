from __future__ import annotations

from .FXLabel import FXLabel


class FXMenuButton(FXLabel):
    """A menu button posts a popup menu when clicked. There are many ways to control the placement where the popup will appear; first, the popup may be placed on either of the four sides relative to the menu button; this is controlled by the flags MENUBUTTON\_DOWN, etc. Next, there are several attachment modes; the popup's left/bottom edge may attach to the menu button's left/top edge, or the popup's right/top edge may attach to the menu button's right/bottom edge, or both. Also, the popup may apear centered relative to the menu button. Finally, a small offset may be specified to displace the location of the popup by a few pixels so as to account for borders and so on. Normally, the menu button shows an arrow pointing to the direction where the popup is set to appear; this can be turned off by passing the option MENUBUTTON\_NOARROWS."""
