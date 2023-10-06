from __future__ import annotations

from typing_extensions import Self

from .FXWindow import FXWindow


class FXComposite(FXWindow):
    """Base composite."""

    def __init__(self, p: Self, opts: int = 0, x: int = 0, y: int = 0, w: int = 0, h: int = 0):
        """Constructor.

        Parameters
        ----------
        p : Self

        opts : int

        x : int

        y : int

        w : int

        h : int
        """

    def create(self):
        """Create server-side resources.

        Reimplemented from FXWindow. Reimplemented in FXColorSelector, FXComboBox, FXDirBox, FXDirList,
        FXDriveBox, FXFileList, FXFontSelector, FXGroupBox, FXIconList, FXImageView, FXList, FXListBox,
        FXMDIChild, FXPrintDialog, FXRootWindow, FXScrollWindow, FXShell, FXSpinner, FXTabBar, FXTable,
        FXText, FXToolbarShell, FXTooltip, FXTopWindow, FXTreeList, FXTreeListBox, AFXManagerMenuPane,
        AFXMainWindow, AFXPromptArea, AFXBaseTable, AFXColorButton, AFXColorFlyout, AFXComboBox, AFXDialog,
        AFXFloatSpinner, AFXListBox, AFXNote, AFXOptionTreeItem, AFXPrimFloatSpinner, AFXSpinner, AFXTable,
        AFXTextField, and AFXVerticalAligner.
        """

    def destroy(self):
        """Destroy server-side resources.

        Reimplemented from FXWindow. Reimplemented in FXComboBox, FXDirBox, FXDirList, FXDriveBox,
        FXFileList, FXListBox, FXRootWindow, FXTreeList, FXTreeListBox, AFXColorFlyout, and AFXTable.
        """

    def detach(self):
        """Detach server-side resources.

        Reimplemented from FXWindow. Reimplemented in FXComboBox, FXDirBox, FXDirList, FXDriveBox,
        FXFileList, FXGroupBox, FXIconList, FXImageView, FXList, FXListBox, FXMDIChild, FXRootWindow,
        FXTable, FXText, FXTooltip, FXTopWindow, FXTreeList, FXTreeListBox, AFXBaseTable, AFXColorFlyout,
        AFXNote, and AFXTable.
        """

    def getDefaultHeight(self):
        """Return default height.

        Reimplemented from FXWindow. Reimplemented in FX4Splitter, FXComboBox, FXDockSite, FXGroupBox,
        FXHorizontalFrame, FXList, FXListBox, FXMDIChild, FXMatrix, FXPacker, FXPopup, FXRootWindow,
        FXScrollArea, FXSpinner, FXSplitter, FXStatusbar, FXSwitcher, FXTabBar, FXTabBook, FXTable, FXText,
        FXToolbar, FXToolbarShell, FXTooltip, FXTopWindow, FXTreeList, FXTreeListBox, FXVerticalFrame,
        AFXMainWindow, AFXToolbarGroup, AFXBaseTable, AFXList, AFXOptionTreeList, AFXPrimFloatSpinner,
        AFXSlider, AFXTable, AFXTreeTable, and AFXVerticalAligner.
        """

    def getDefaultWidth(self):
        """Return default width.

        Reimplemented from FXWindow. Reimplemented in FX4Splitter, FXComboBox, FXDockSite, FXGroupBox,
        FXHorizontalFrame, FXList, FXListBox, FXMDIChild, FXMatrix, FXPacker, FXPopup, FXRootWindow,
        FXScrollArea, FXSpinner, FXSplitter, FXStatusbar, FXSwitcher, FXTabBar, FXTabBook, FXTable, FXText,
        FXToolbar, FXToolbarShell, FXTooltip, FXTopWindow, FXTreeList, FXTreeListBox, FXVerticalFrame,
        AFXMainWindow, AFXToolbarGroup, AFXBaseTable, AFXOptionTreeItem, AFXOptionTreeList,
        AFXPrimFloatSpinner, AFXSlider, AFXTable, AFXTextField, AFXTreeTable, and AFXVerticalAligner.
        """

    def maxChildHeight(self):
        """Return the height of the tallest child window."""

    def maxChildWidth(self):
        """Return the width of the widest child window.

        By clicking on Send, you accept that Dassault Systèmes will process your personal data and may
        contact you for further information. [Privacy Policy](
        https://www.3ds.com/privacy-policy).
        Total Results: Results per page This page cannot be found. The page might not exist or is temporarily unavailable. Try again or try searching for the topic.
        """
