from __future__ import annotations

from .FXComposite import FXComposite


class FXShell(FXComposite):
    """A child of the Root window."""

    def create(self):
        """Create server-side resources.

        Reimplemented from FXComposite. Reimplemented in FXPrintDialog, FXToolbarShell, FXTooltip,
        FXTopWindow, AFXManagerMenuPane, AFXMainWindow, and AFXDialog.
        """

    def recalc(self):
        """Mark this window's layout as dirty.

        Reimplemented from FXWindow.
        """
