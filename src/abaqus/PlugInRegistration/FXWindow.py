from __future__ import annotations

from typing_extensions import Self

from .FXColor import FXColor
from .FXComposite import FXComposite
from .FXDrawable import FXDrawable
from .FXObject import FXObject

#: Default layout mode.
LAYOUT_NORMAL: int = hash("LAYOUT_NORMAL")

#: Pack on top side (default).
LAYOUT_SIDE_TOP: int = hash("LAYOUT_SIDE_TOP")

#: Pack on bottom side.
LAYOUT_SIDE_BOTTOM: int = hash("LAYOUT_SIDE_BOTTOM")

#: Pack on left side.
LAYOUT_SIDE_LEFT: int = hash("LAYOUT_SIDE_LEFT")

#: Pack on right side.
LAYOUT_SIDE_RIGHT: int = hash("LAYOUT_SIDE_RIGHT")

#: Matrix column is stretchable.
LAYOUT_FILL_COLUMN: int = hash("LAYOUT_FILL_COLUMN")

#: Matrix row is stretchable.
LAYOUT_FILL_ROW: int = hash("LAYOUT_FILL_ROW")

#: Stick on left (default).
LAYOUT_LEFT: int = hash("LAYOUT_LEFT")

#: Stick on right.
LAYOUT_RIGHT: int = hash("LAYOUT_RIGHT")

#: Center horizontally.
LAYOUT_CENTER_X: int = hash("LAYOUT_CENTER_X")

#: X fixed.
LAYOUT_FIX_X: int = hash("LAYOUT_FIX_X")

#: Stick on top (default).
LAYOUT_TOP: int = hash("LAYOUT_TOP")

#: Stick on bottom.
LAYOUT_BOTTOM: int = hash("LAYOUT_BOTTOM")

#: Center vertically.
LAYOUT_CENTER_Y: int = hash("LAYOUT_CENTER_Y")

#: Y fixed CAE: Copied from FOX 1.4.34 to support dockable tool bars.
LAYOUT_FIX_Y: int = hash("LAYOUT_FIX_Y")

#: Dock on same galley if it fits.
LAYOUT_DOCK_SAME: int = hash("LAYOUT_DOCK_SAME")

#: Dock on next galley LAYOUT_RESERVED_1 = 0x00000040, LAYOUT_RESERVED_2 = 0x00000080,
LAYOUT_DOCK_NEXT: int = hash("LAYOUT_DOCK_NEXT")

#: CAE End.
LAYOUT_RESERVED_1: int = hash("LAYOUT_RESERVED_1")

#: Width fixed.
LAYOUT_FIX_WIDTH: int = hash("LAYOUT_FIX_WIDTH")

#: height fixed
LAYOUT_FIX_HEIGHT: int = hash("LAYOUT_FIX_HEIGHT")

#: Minimum width is the default.
LAYOUT_MIN_WIDTH: int = hash("LAYOUT_MIN_WIDTH")

#: Minimum height is the default.
LAYOUT_MIN_HEIGHT: int = hash("LAYOUT_MIN_HEIGHT")

#: Stretch or shrink horizontally.
LAYOUT_FILL_X: int = hash("LAYOUT_FILL_X")

#: Stretch or shrink vertically.
LAYOUT_FILL_Y: int = hash("LAYOUT_FILL_Y")

#: Explicit placement.
LAYOUT_EXPLICIT: int = hash("LAYOUT_EXPLICIT")

#: Default is no frame.
FRAME_NONE: int = hash("FRAME_NONE")

#: Sunken border.
FRAME_SUNKEN: int = hash("FRAME_SUNKEN")

#: Raised border.
FRAME_RAISED: int = hash("FRAME_RAISED")

#: Thick border.
FRAME_THICK: int = hash("FRAME_THICK")

#: A groove or etched-in border.
FRAME_GROOVE: int = hash("FRAME_GROOVE")

#: A ridge or embossed border.
FRAME_RIDGE: int = hash("FRAME_RIDGE")

#: Simple line border.
FRAME_LINE: int = hash("FRAME_LINE")

#: Regular raised/thick border.
FRAME_NORMAL: int = hash("FRAME_NORMAL")

#: Default is each its own size.
PACK_NORMAL: int = hash("PACK_NORMAL")

#: Uniform height.
PACK_UNIFORM_HEIGHT: int = hash("PACK_UNIFORM_HEIGHT")

#: Uniform width.
PACK_UNIFORM_WIDTH: int = hash("PACK_UNIFORM_WIDTH")

#: Default.
BACKGROUND_NORMAL: int = hash("BACKGROUND_NORMAL")

#: Horizontal gradient background.
BACKGROUND_H_GRADIENT: int = hash("BACKGROUND_H_GRADIENT")

#: Vertical gradient background.
BACKGROUND_V_GRADIENT: int = hash("BACKGROUND_V_GRADIENT")

#: plain background
BACKGROUND_PLAIN: int = hash("BACKGROUND_PLAIN")


class FXWindow(FXDrawable):
    """Base class for all windows."""

    def __init__(self, p: FXComposite, opts: int = 0, x: int = 0, y: int = 0, w: int = 0, h: int = 0):
        """Constructor.

        Parameters
        ----------
        p : FXComposite

        opts : int

        x : int

        y : int

        w : int

        h : int
        """

    def canFocus(self):
        """Return True if this window is a control capable of receiving the focus.

        Reimplemented in FXArrowButton, FXButton, FXCanvas, FXCheckButton, FXColorWell, FXDockHandler,
        FXIconList, FXImageView, FXList, FXMDIChild, FXMenuButton, FXMenuCascade, FXMenuCommand,
        FXMenuTitle, FXOption, FXOptionMenu, FXRadioButton, FXSlider, FXTabItem, FXTable, FXText,
        FXTextField, FXToggleButton, FXToolbarTab, FXTreeList, AFXBaseTable, AFXFloatSpinner,
        AFXFlyoutButton, AFXFlyoutItem, and AFXSlider.
        """

    def childAtIndex(self, index: int):
        """Return the child window at specified index, or NULL if the index is negative or out of range
        Reimplemented in AFXOptionTreeItem.

        Parameters
        ----------
        index : int
        """

    def containsChild(self, child: Self):
        """Return True if specified window is a child of this window.

        Parameters
        ----------
        child : Self
        """

    def create(self):
        """Create all of the server-side resources for this window.

        Reimplemented from FXId. Reimplemented in FXColorBar, FXColorSelector, FXColorWell, FXColorWheel,
        FXComboBox, FXComposite, FXDirBox, FXDirList, FXDockTitle, FXDriveBox, FXFileList, FXFontSelector,
        FXGLCanvas, FXGLViewer, FXGroupBox, FXHeader, FXIconList, FXImageView, FXLabel, FXList, FXListBox,
        FXMDIChild, FXMenuButton, FXMenuCaption, FXMenuCascade, FXProgressBar, FXMenuTitle, FXOptionMenu,
        FXPrintDialog, FXRootWindow, FXScrollWindow, FXShell, FXSpinner, FXStatusline, FXTabBar, FXTable,
        FXText, FXTextField, FXToggleButton, FXToolbarShell, FXTooltip, FXTopWindow, FXTreeList,
        FXTreeListBox, AFXManagerMenuPane, AFXMainWindow, AFXPromptArea, AFXBaseTable, AFXColorButton,
        AFXColorFlyout, AFXComboBox, AFXDialog, AFXFloatSpinner, AFXFlyoutButton, AFXListBox, AFXNote,
        AFXOptionTreeItem, AFXPrimFloatSpinner, AFXProgressBar, AFXSpinner, AFXTable, AFXTextField, and
        AFXVerticalAligner.
        """

    def destroy(self):
        """Destroy the server-side resources for this window.

        Reimplemented from FXId. Reimplemented in FXComboBox, FXComposite, FXDirBox, FXDirList, FXDriveBox,
        FXFileList, FXGLCanvas, FXListBox, FXMenuCascade, FXOptionMenu, FXRootWindow, FXTreeList,
        FXTreeListBox, AFXManagerMenuCascade, AFXColorFlyout, and AFXTable.
        """

    def detach(self):
        """Detach the server-side resources for this window.

        Reimplemented from FXId. Reimplemented in FXColorBar, FXColorWell, FXColorWheel, FXComboBox,
        FXComposite, FXDirBox, FXDirList, FXDockTitle, FXDriveBox, FXFileList, FXGLCanvas, FXGLViewer,
        FXGroupBox, FXHeader, FXIconList, FXImageView, FXLabel, FXList, FXListBox, FXMDIChild, FXMenuButton,
        FXMenuCaption, FXMenuCascade, FXProgressBar, FXMenuTitle, FXOptionMenu, FXRootWindow, FXStatusline,
        FXTable, FXText, FXToggleButton, FXTooltip, FXTopWindow, FXTreeList, FXTreeListBox, AFXBaseTable,
        AFXColorFlyout, AFXFlyoutButton, AFXNote, and AFXTable.
        """

    def disable(self):
        """Disable the window from receiving mouse and keyboard events.

        Reimplemented in FXArrowButton, FXComboBox, FXGroupBox, FXLabel, FXListBox, FXMenuCaption,
        FXScrollCorner, FXSlider, FXSpinner, FXText, FXTextField, FXToolbarTab, FXTreeListBox,
        AFXAutoComputeGroup, AFXManagerMenuDB, AFXColorButton, AFXColorFlyout, AFXComboBox, AFXFloatSpinner,
        AFXFlyoutButton, AFXList, AFXListBox, AFXNote, AFXOptionTreeItem, AFXPrimFloatSpinner, AFXSlider,
        AFXSpinner, AFXTable, and AFXTextField.
        """

    def enable(self):
        """Enable the window to receive mouse and keyboard events.

        Reimplemented in FXArrowButton, FXComboBox, FXGroupBox, FXLabel, FXListBox, FXMenuCaption,
        FXScrollCorner, FXSlider, FXSpinner, FXText, FXTextField, FXToolbarTab, FXTreeListBox,
        AFXAutoComputeGroup, AFXManagerMenuDB, AFXColorButton, AFXColorFlyout, AFXComboBox, AFXFloatSpinner,
        AFXFlyoutButton, AFXList, AFXListBox, AFXNote, AFXOptionTreeItem, AFXPrimFloatSpinner, AFXSlider,
        AFXSpinner, AFXTable, and AFXTextField.
        """

    def forceRefresh(self):
        """Force a GUI update of this window and its children."""

    def getBackColor(self):
        """Get background color.

        Reimplemented in FXComboBox, and FXListBox.
        """

    def getCursorPosition(self):
        """Returns a sequence of (status, x, y, mouseButtonState) representing the relative location of the
        cursor in the widget."""

    def getDefaultHeight(self):
        """Return the default height of this window.

        Reimplemented in FX4Splitter, FXArrowButton, FXCheckButton, FXColorBar, FXColorWell, FXColorWheel,
        FXComboBox, FXComposite, FXDial, FXDockSite, FXDockTitle, FXDragCorner, FXFrame, FXGroupBox,
        FXHeader, FXHorizontalFrame, FXLabel, FXList, FXListBox, FXMDIDeleteButton, FXMDIRestoreButton,
        FXMDIMaximizeButton, FXMDIMinimizeButton, FXMDIWindowButton, FXMDIChild, FXMatrix, FXMenuButton,
        FXMenuCaption, FXMenuCommand, FXProgressBar, FXMenuSeparator, FXMenuTitle, FXOption, FXOptionMenu,
        FXPacker, FXPopup, FXRadioButton, FXRootWindow, FXScrollArea, FXScrollbar, FXHorizontalSeparator,
        FXVerticalSeparator, FXSlider, FXSpinner, FXSplitter, FXStatusbar, FXStatusline, FXSwitcher,
        FXTabBar, FXTabBook, FXTable, FXText, FXTextField, FXToggleButton, FXToolbar, FXToolbarGrip,
        FXToolbarShell, FXToolbarTab, FXTooltip, FXTopWindow, FXTreeList, FXTreeListBox, FXVerticalFrame,
        AFXMainWindow, AFXToolbarGroup, AFXBaseTable, AFXList, AFXOptionTreeList, AFXPrimFloatSpinner,
        AFXProgressBar, AFXSlider, AFXTable, AFXTreeTable, and AFXVerticalAligner.
        """

    def getDefaultWidth(self):
        """Return the default width of this window.

        Reimplemented in FX4Splitter, FXArrowButton, FXCheckButton, FXColorBar, FXColorWell, FXColorWheel,
        FXComboBox, FXComposite, FXDial, FXDockSite, FXDockTitle, FXDragCorner, FXFrame, FXGroupBox,
        FXHeader, FXHorizontalFrame, FXLabel, FXList, FXListBox, FXMDIDeleteButton, FXMDIRestoreButton,
        FXMDIMaximizeButton, FXMDIMinimizeButton, FXMDIWindowButton, FXMDIChild, FXMatrix, FXMenuButton,
        FXMenuCaption, FXMenuCommand, FXProgressBar, FXMenuSeparator, FXMenuTitle, FXOption, FXOptionMenu,
        FXPacker, FXPopup, FXRadioButton, FXRootWindow, FXScrollArea, FXScrollbar, FXHorizontalSeparator,
        FXVerticalSeparator, FXSlider, FXSpinner, FXSplitter, FXStatusbar, FXStatusline, FXSwitcher,
        FXTabBar, FXTabBook, FXTable, FXText, FXTextField, FXToggleButton, FXToolbar, FXToolbarGrip,
        FXToolbarShell, FXToolbarTab, FXTooltip, FXTopWindow, FXTreeList, FXTreeListBox, FXVerticalFrame,
        AFXMainWindow, AFXToolbarGroup, AFXBaseTable, AFXOptionTreeItem, AFXOptionTreeList,
        AFXPrimFloatSpinner, AFXProgressBar, AFXSlider, AFXTable, AFXTextField, AFXTreeTable, and
        AFXVerticalAligner.
        """

    def getFirst(self):
        """Return a pointer to this window's first child window , if any.

        Reimplemented in AFXOptionTreeItem.
        """

    def getHeightForWidth(self, givenwidth: int):
        """Return height for given width. Reimplemented in FXDockSite.

        Parameters
        ----------
        givenwidth : int
        """

    def getKey(self):
        """Return window key."""

    def getLast(self):
        """Return a pointer to this window's last child window, if any.

        Reimplemented in AFXOptionTreeItem.
        """

    def getLayoutHints(self):
        """Get layout hints for this window."""

    def getNext(self):
        """Return a pointer to the next (sibling) window, if any.

        Reimplemented in AFXOptionTreeItem.
        """

    def getOwner(self):
        """Return a pointer to the owner window.

        Reimplemented in AFXMenuCascade, AFXMenuCommand, AFXMenuPane, AFXMenuTitle, AFXToolbarGroup, and
        AFXToolboxGroup.
        """

    def getParent(self):
        """Return a pointer to the parent window.

        Reimplemented in AFXOptionTreeItem.
        """

    def getPrev(self):
        """Return a pointer to the previous (sibling) window , if any.

        Reimplemented in AFXOptionTreeItem.
        """

    def getRoot(self):
        """Return a pointer to the root window."""

    def getSelector(self):
        """Get the message identifier for this window."""

    def getShell(self):
        """Return a pointer to the shell window."""

    def getTarget(self):
        """Get the message target object for this window, if any."""

    def getWidthForHeight(self, givenheight: int):
        """Return width for given height. Reimplemented in FXDockSite.

        Parameters
        ----------
        givenheight : int
        """

    def getX(self):
        """Get this window's x-coordinate, in the parent's coordinate system."""

    def getY(self):
        """Get this window's y-coordinate, in the parent's coordinate system."""

    def grab(self, confineTo: Self | None = None):
        """Grab the mouse to this window; future mouse events will be reported to this window even while the
        cursor goes outside of this window.

        Parameters
        ----------
        confineTo : Self | None
        """

    def grabbed(self):
        """Return True if the window has been grabbed."""

    def hasFocus(self):
        """Return True if this window has the focus."""

    def hide(self):
        """Hide this window.

        Reimplemented in FXTopWindow, AFXManagerMenuDB, AFXMenuTitle, AFXToolbarGroup,
        AFXToolbarGroupRender, AFXToolbarGroupVisibility, AFXDialog, AFXFlyoutItem, AFXMessageDialog,
        AFXOptionTreeItem, and AFXProgressBar.
        """

    def indexOfChild(self, window: Self):
        """Return the index (starting from zero) of the specified child window, or -1 if the window is not a
        child or NULL.

        Parameters
        ----------
        window : Self
        """

    def isActive(self):
        """Return True if the window is active.

        Reimplemented in AFXToolbarGroup.
        """

    def isChildOf(self, window: Self):
        """Return True if specified window is this window's parent.

        Parameters
        ----------
        window : Self
        """

    def isDefault(self):
        """Return True if this is the default window."""

    def isEnabled(self):
        """Return True if this window is able to receive mouse and keyboard events."""

    def isInitial(self):
        """Return True if this is the initial default window."""

    def linkAfter(self, sibling: Self):
        """Relink this window after sibling in the window list.

        Parameters
        ----------
        sibling : Self
        """

    def linkBefore(self, sibling: Self):
        """Relink this window before sibling in the window list.

        Parameters
        ----------
        sibling : Self
        """

    def move(self, x: int, y: int):
        """Move this window to the specified position in the parent's coordinates. Reimplemented in FXMDIChild,
        FXRootWindow, and FXTopWindow.

        Parameters
        ----------
        x : int

        y : int
        """

    def numChildren(self):
        """Return the number of child windows for this window.

        Reimplemented in AFXOptionTreeItem.
        """

    def position(self, x: int, y: int, w: int, h: int):
        """Move and resize this window in the parent's coordinates. Reimplemented in FXIconList, FXMDIChild,
        FXRootWindow, FXText, and FXTopWindow.

        Parameters
        ----------
        x : int

        y : int

        w : int

        h : int
        """

    def recalc(self):
        """Mark this window's layout as dirty.

        Reimplemented in FXIconList, FXList, FXMDIClient, FXRootWindow, FXShell, FXTable, FXText,
        FXTreeList, AFXBaseTable, AFXSlider, and AFXTable.
        """

    def repaint(self, x: int, y: int, w: int, h: int):
        """If marked but not yet painted, paint the given area.

        Parameters
        ----------
        x : int

        y : int

        w : int

        h : int
        """

    def resize(self, w: int, h: int):
        """Resize this window to the specified width and height. Reimplemented from FXDrawable. Reimplemented in
        FXIconList, FXMDIChild, FXRootWindow, FXText, and FXTopWindow.

        Parameters
        ----------
        w : int

        h : int
        """

    def setBackColor(self, clr: FXColor):
        """Set window background color. Reimplemented in FXComboBox, and FXListBox.

        Parameters
        ----------
        clr : FXColor
        """

    def setCursorPosition(self, x: int, y: int):
        """Warp the cursor to the new position.

        Parameters
        ----------
        x : int

        y : int
        """

    def setFocus(self):
        """Move the focus to this window.

        Reimplemented in FXButton, FXColorWell, FXIconList, FXList, FXMenuCascade, FXMenuCommand,
        FXMenuTitle, FXOption, FXPopup, FXRootWindow, FXShell, FXTable, FXText, FXTextField, FXTopWindow,
        FXTreeList, AFXBaseTable, AFXFlyoutItem, and AFXTextField.
        """

    def setHeight(self, h: int):
        """Set the window height.

        Parameters
        ----------
        h : int
        """

    def setInitial(self, enable: bool = True):
        """Make this window the initial default window.

        Parameters
        ----------
        enable : bool
        """

    def setKey(self, k: int):
        """Change window key.

        Parameters
        ----------
        k : int
        """

    def setLayoutHints(self, lout: int):
        """Set layout hints for this window.

        Parameters
        ----------
        lout : int
        """

    def setSelector(self, sel: int):
        """Set the message identifier for this window.

        Parameters
        ----------
        sel : int
        """

    def setTarget(self, t: FXObject):
        """Set the message target object for this window.

        Parameters
        ----------
        t : FXObject
        """

    def setWidth(self, w: int):
        """Set the window width.

        Parameters
        ----------
        w : int
        """

    def setX(self, x: int):
        """Set this window's x-coordinate, in the parent's coordinate system.

        Parameters
        ----------
        x : int
        """

    def setY(self, y: int):
        """Set this window's y-coordinate, in the parent's coordinate system.

        Parameters
        ----------
        y : int
        """

    def show(self):
        """Show this window.

        Reimplemented in FXTooltip, FXTopWindow, AFXMenuTitle, AFXToolbarGroup, AFXToolbarGroupRender,
        AFXToolbarGroupVisibility, AFXDialog, AFXFileDialog, AFXMessageDialog, AFXOptionTreeItem,
        AFXProgressBar, and AFXSlider.
        """

    def shown(self):
        """Return True if the window is shown."""

    def translateCoordinatesTo(self, tox: int, toy: int, towindow: Self, fromx: int, fromy: int):
        """Translate coordinates from this window's coordinate space to towindow's coordinate space.

        Parameters
        ----------
        tox : int

        toy : int

        towindow : Self

        fromx : int

        fromy : int
        """

    def ungrab(self):
        """Release the mouse grab."""

    def update(self, x: int, y: int, w: int, h: int):
        """Mark the specified rectangle dirty, i.e. to be repainted.

        Parameters
        ----------
        x : int

        y : int

        w : int

        h : int
        """
