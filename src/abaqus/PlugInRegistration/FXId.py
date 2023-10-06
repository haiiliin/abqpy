from __future__ import annotations

from .FXObject import FXObject


class FXId(FXObject):
    """Encapsulates server side resource."""

    def create(self):
        """Create resource.

        Reimplemented in FXBitmap, FXColorBar, FXColorSelector, FXColorWell, FXColorWheel, FXComboBox,
        FXComposite, FXCursor, FXDirBox, FXDirList, FXDockTitle, FXDriveBox, FXFileList, FXFont,
        FXFontSelector, FXGLCanvas, FXGLContext, FXGLViewer, FXGLVisual, FXGroupBox, FXHeader, FXIcon,
        FXIconList, FXImage, FXImageView, FXLabel, FXList, FXListBox, FXMDIChild, FXMenuButton,
        FXMenuCaption, FXMenuCascade, FXProgressBar, FXMenuTitle, FXOptionMenu, FXPrintDialog, FXRootWindow,
        FXScrollWindow, FXShell, FXSpinner, FXStatusline, FXTabBar, FXTable, FXText, FXTextField,
        FXToggleButton, FXToolbarShell, FXTooltip, FXTopWindow, FXTreeList, FXTreeListBox, FXVisual,
        FXWindow, AFXManagerMenuPane, AFXMainWindow, AFXPromptArea, AFXBaseTable, AFXColorButton,
        AFXColorFlyout, AFXComboBox, AFXDialog, AFXFloatSpinner, AFXFlyoutButton, AFXListBox, AFXNote,
        AFXOptionTreeItem, AFXPrimFloatSpinner, AFXProgressBar, AFXSpinner, AFXTable, AFXTextField, and
        AFXVerticalAligner.
        """

    def destroy(self):
        """Destroy resource.

        Reimplemented in FXBitmap, FXComboBox, FXComposite, FXCursor, FXDirBox, FXDirList, FXDriveBox,
        FXFileList, FXFont, FXGLCanvas, FXGLContext, FXGLVisual, FXIcon, FXImage, FXListBox, FXMenuCascade,
        FXOptionMenu, FXRootWindow, FXTreeList, FXTreeListBox, FXVisual, FXWindow, AFXManagerMenuCascade,
        AFXColorFlyout, and AFXTable.
        """

    def detach(self):
        """Detach resource.

        Reimplemented in FXBitmap, FXColorBar, FXColorWell, FXColorWheel, FXComboBox, FXComposite, FXCursor,
        FXDirBox, FXDirList, FXDockTitle, FXDriveBox, FXFileList, FXFont, FXGLCanvas, FXGLContext,
        FXGLViewer, FXGLVisual, FXGroupBox, FXHeader, FXIcon, FXIconList, FXImage, FXImageView, FXLabel,
        FXList, FXListBox, FXMDIChild, FXMenuButton, FXMenuCaption, FXMenuCascade, FXProgressBar,
        FXMenuTitle, FXOptionMenu, FXRootWindow, FXStatusline, FXTable, FXText, FXToggleButton, FXTooltip,
        FXTopWindow, FXTreeList, FXTreeListBox, FXVisual, FXWindow, AFXBaseTable, AFXColorFlyout,
        AFXFlyoutButton, AFXNote, and AFXTable.
        """

    def getApp(self):
        """Get application."""

    def getUserData(self):
        """Get user data pointer."""

    def id(self):
        """Get XID handle.

        Reimplemented in FXFont.
        """

    def setUserData(self, ptr: str):
        """Set user data pointer.

        Parameters
        ----------
        ptr : str
        """
