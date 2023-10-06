Abaqus

GUI Toolkit Reference

All Classes

FXWindow

Base class for all windows

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fxwindow.png)

### FXWindow(p, opts=0, x=0, y=0, w=0, h=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   |   |
| opts | Int | 0 |   |
| x | Int | 0 |   |
| y | Int | 0 |   |
| w | Int | 0 |   |
| h | Int | 0 |   |

### canFocus()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if this window is a control capable of receiving the focus.

Reimplemented in FXArrowButton, FXButton, FXCanvas, FXCheckButton, FXColorWell, FXDockHandler, FXIconList, FXImageView, FXList, FXMDIChild, FXMenuButton, FXMenuCascade, FXMenuCommand, FXMenuTitle, FXOption, FXOptionMenu, FXRadioButton, FXSlider, FXTabItem, FXTable, FXText, FXTextField, FXToggleButton, FXToolbarTab, FXTreeList, AFXBaseTable, AFXFloatSpinner, AFXFlyoutButton, AFXFlyoutItem, and AFXSlider.

### childAtIndex(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return the child window at specified index, or NULL if the index is negative or out of range

Reimplemented in AFXOptionTreeItem.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   |   |

### containsChild(child)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if specified window is a child of this window.

| **Argument** | **Type** | **Default** | **Description** |
| child | FXWindow |   |   |

### create()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Create all of the server-side resources for this window.

Reimplemented from FXId.

Reimplemented in FXColorBar, FXColorSelector, FXColorWell, FXColorWheel, FXComboBox, FXComposite, FXDirBox, FXDirList, FXDockTitle, FXDriveBox, FXFileList, FXFontSelector, FXGLCanvas, FXGLViewer, FXGroupBox, FXHeader, FXIconList, FXImageView, FXLabel, FXList, FXListBox, FXMDIChild, FXMenuButton, FXMenuCaption, FXMenuCascade, FXProgressBar, FXMenuTitle, FXOptionMenu, FXPrintDialog, FXRootWindow, FXScrollWindow, FXShell, FXSpinner, FXStatusline, FXTabBar, FXTable, FXText, FXTextField, FXToggleButton, FXToolbarShell, FXTooltip, FXTopWindow, FXTreeList, FXTreeListBox, AFXManagerMenuPane, AFXMainWindow, AFXPromptArea, AFXBaseTable, AFXColorButton, AFXColorFlyout, AFXComboBox, AFXDialog, AFXFloatSpinner, AFXFlyoutButton, AFXListBox, AFXNote, AFXOptionTreeItem, AFXPrimFloatSpinner, AFXProgressBar, AFXSpinner, AFXTable, AFXTextField, and AFXVerticalAligner.

### destroy()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Destroy the server-side resources for this window.

Reimplemented from FXId.

Reimplemented in FXComboBox, FXComposite, FXDirBox, FXDirList, FXDriveBox, FXFileList, FXGLCanvas, FXListBox, FXMenuCascade, FXOptionMenu, FXRootWindow, FXTreeList, FXTreeListBox, AFXManagerMenuCascade, AFXColorFlyout, and AFXTable.

### detach()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Detach the server-side resources for this window.

Reimplemented from FXId.

Reimplemented in FXColorBar, FXColorWell, FXColorWheel, FXComboBox, FXComposite, FXDirBox, FXDirList, FXDockTitle, FXDriveBox, FXFileList, FXGLCanvas, FXGLViewer, FXGroupBox, FXHeader, FXIconList, FXImageView, FXLabel, FXList, FXListBox, FXMDIChild, FXMenuButton, FXMenuCaption, FXMenuCascade, FXProgressBar, FXMenuTitle, FXOptionMenu, FXRootWindow, FXStatusline, FXTable, FXText, FXToggleButton, FXTooltip, FXTopWindow, FXTreeList, FXTreeListBox, AFXBaseTable, AFXColorFlyout, AFXFlyoutButton, AFXNote, and AFXTable.

### disable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Disable the window from receiving mouse and keyboard events.

Reimplemented in FXArrowButton, FXComboBox, FXGroupBox, FXLabel, FXListBox, FXMenuCaption, FXScrollCorner, FXSlider, FXSpinner, FXText, FXTextField, FXToolbarTab, FXTreeListBox, AFXAutoComputeGroup, AFXManagerMenuDB, AFXColorButton, AFXColorFlyout, AFXComboBox, AFXFloatSpinner, AFXFlyoutButton, AFXList, AFXListBox, AFXNote, AFXOptionTreeItem, AFXPrimFloatSpinner, AFXSlider, AFXSpinner, AFXTable, and AFXTextField.

### enable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Enable the window to receive mouse and keyboard events.

Reimplemented in FXArrowButton, FXComboBox, FXGroupBox, FXLabel, FXListBox, FXMenuCaption, FXScrollCorner, FXSlider, FXSpinner, FXText, FXTextField, FXToolbarTab, FXTreeListBox, AFXAutoComputeGroup, AFXManagerMenuDB, AFXColorButton, AFXColorFlyout, AFXComboBox, AFXFloatSpinner, AFXFlyoutButton, AFXList, AFXListBox, AFXNote, AFXOptionTreeItem, AFXPrimFloatSpinner, AFXSlider, AFXSpinner, AFXTable, and AFXTextField.

### forceRefresh()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Force a GUI update of this window and its children.

### getBackColor()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get background color.

Reimplemented in FXComboBox, and FXListBox.

### getCursorPosition()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns a sequence of (status, x, y, mouseButtonState) representing the relative location of the cursor in the widget.

### getDefaultHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return the default height of this window.

Reimplemented in FX4Splitter, FXArrowButton, FXCheckButton, FXColorBar, FXColorWell, FXColorWheel, FXComboBox, FXComposite, FXDial, FXDockSite, FXDockTitle, FXDragCorner, FXFrame, FXGroupBox, FXHeader, FXHorizontalFrame, FXLabel, FXList, FXListBox, FXMDIDeleteButton, FXMDIRestoreButton, FXMDIMaximizeButton, FXMDIMinimizeButton, FXMDIWindowButton, FXMDIChild, FXMatrix, FXMenuButton, FXMenuCaption, FXMenuCommand, FXProgressBar, FXMenuSeparator, FXMenuTitle, FXOption, FXOptionMenu, FXPacker, FXPopup, FXRadioButton, FXRootWindow, FXScrollArea, FXScrollbar, FXHorizontalSeparator, FXVerticalSeparator, FXSlider, FXSpinner, FXSplitter, FXStatusbar, FXStatusline, FXSwitcher, FXTabBar, FXTabBook, FXTable, FXText, FXTextField, FXToggleButton, FXToolbar, FXToolbarGrip, FXToolbarShell, FXToolbarTab, FXTooltip, FXTopWindow, FXTreeList, FXTreeListBox, FXVerticalFrame, AFXMainWindow, AFXToolbarGroup, AFXBaseTable, AFXList, AFXOptionTreeList, AFXPrimFloatSpinner, AFXProgressBar, AFXSlider, AFXTable, AFXTreeTable, and AFXVerticalAligner.

### getDefaultWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return the default width of this window.

Reimplemented in FX4Splitter, FXArrowButton, FXCheckButton, FXColorBar, FXColorWell, FXColorWheel, FXComboBox, FXComposite, FXDial, FXDockSite, FXDockTitle, FXDragCorner, FXFrame, FXGroupBox, FXHeader, FXHorizontalFrame, FXLabel, FXList, FXListBox, FXMDIDeleteButton, FXMDIRestoreButton, FXMDIMaximizeButton, FXMDIMinimizeButton, FXMDIWindowButton, FXMDIChild, FXMatrix, FXMenuButton, FXMenuCaption, FXMenuCommand, FXProgressBar, FXMenuSeparator, FXMenuTitle, FXOption, FXOptionMenu, FXPacker, FXPopup, FXRadioButton, FXRootWindow, FXScrollArea, FXScrollbar, FXHorizontalSeparator, FXVerticalSeparator, FXSlider, FXSpinner, FXSplitter, FXStatusbar, FXStatusline, FXSwitcher, FXTabBar, FXTabBook, FXTable, FXText, FXTextField, FXToggleButton, FXToolbar, FXToolbarGrip, FXToolbarShell, FXToolbarTab, FXTooltip, FXTopWindow, FXTreeList, FXTreeListBox, FXVerticalFrame, AFXMainWindow, AFXToolbarGroup, AFXBaseTable, AFXOptionTreeItem, AFXOptionTreeList, AFXPrimFloatSpinner, AFXProgressBar, AFXSlider, AFXTable, AFXTextField, AFXTreeTable, and AFXVerticalAligner.

### getFirst()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return a pointer to this window's first child window , if any.

Reimplemented in AFXOptionTreeItem.

### getHeightForWidth(givenwidth)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return height for given width.

Reimplemented in FXDockSite.

| **Argument** | **Type** | **Default** | **Description** |
| givenwidth | Int |   |   |

### getKey()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return window key.

### getLast()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return a pointer to this window's last child window, if any.

Reimplemented in AFXOptionTreeItem.

### getLayoutHints()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get layout hints for this window.

### getNext()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return a pointer to the next (sibling) window, if any.

Reimplemented in AFXOptionTreeItem.

### getOwner()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return a pointer to the owner window.

Reimplemented in AFXMenuCascade, AFXMenuCommand, AFXMenuPane, AFXMenuTitle, AFXToolbarGroup, and AFXToolboxGroup.

### getParent()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return a pointer to the parent window.

Reimplemented in AFXOptionTreeItem.

### getPrev()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return a pointer to the previous (sibling) window , if any.

Reimplemented in AFXOptionTreeItem.

### getRoot()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return a pointer to the root window.

### getSelector()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get the message identifier for this window.

### getShell()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return a pointer to the shell window.

### getTarget()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get the message target object for this window, if any.

### getWidthForHeight(givenheight)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return width for given height.

Reimplemented in FXDockSite.

| **Argument** | **Type** | **Default** | **Description** |
| givenheight | Int |   |   |

### getX()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get this window's x-coordinate, in the parent's coordinate system.

### getY()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get this window's y-coordinate, in the parent's coordinate system.

### grab(confineTo=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Grab the mouse to this window; future mouse events will be reported to this window even while the cursor goes outside of this window

| **Argument** | **Type** | **Default** | **Description** |
| confineTo | FXWindow | None |   |

### grabbed()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if the window has been grabbed.

### hasFocus()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if this window has the focus.

### hide()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Hide this window.

Reimplemented in FXTopWindow, AFXManagerMenuDB, AFXMenuTitle, AFXToolbarGroup, AFXToolbarGroupRender, AFXToolbarGroupVisibility, AFXDialog, AFXFlyoutItem, AFXMessageDialog, AFXOptionTreeItem, and AFXProgressBar.

### indexOfChild(window)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return the index (starting from zero) of the specified child window, or -1 if the window is not a child or NULL

| **Argument** | **Type** | **Default** | **Description** |
| window | FXWindow |   |   |

### isActive()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if the window is active.

Reimplemented in AFXToolbarGroup.

### isChildOf(window)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if specified window is this window's parent.

| **Argument** | **Type** | **Default** | **Description** |
| window | FXWindow |   |   |

### isDefault()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if this is the default window.

### isEnabled()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if this window is able to receive mouse and keyboard events.

### isInitial()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if this is the initial default window.

### linkAfter(sibling)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Relink this window after sibling in the window list.

| **Argument** | **Type** | **Default** | **Description** |
| sibling | FXWindow |   |   |

### linkBefore(sibling)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Relink this window before sibling in the window list.

| **Argument** | **Type** | **Default** | **Description** |
| sibling | FXWindow |   |   |

### move(x, y)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Move this window to the specified position in the parent's coordinates.

Reimplemented in FXMDIChild, FXRootWindow, and FXTopWindow.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   |   |
| y | Int |   |   |

### numChildren()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return the number of child windows for this window.

Reimplemented in AFXOptionTreeItem.

### position(x, y, w, h)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Move and resize this window in the parent's coordinates.

Reimplemented in FXIconList, FXMDIChild, FXRootWindow, FXText, and FXTopWindow.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   |   |
| y | Int |   |   |
| w | Int |   |   |
| h | Int |   |   |

### recalc()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Mark this window's layout as dirty.

Reimplemented in FXIconList, FXList, FXMDIClient, FXRootWindow, FXShell, FXTable, FXText, FXTreeList, AFXBaseTable, AFXSlider, and AFXTable.

### repaint()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

If marked but not yet painted, paint the entire window.

### repaint(x, y, w, h)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

If marked but not yet painted, paint the given area.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   |   |
| y | Int |   |   |
| w | Int |   |   |
| h | Int |   |   |

### resize(w, h)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Resize this window to the specified width and height.

Reimplemented from FXDrawable.

Reimplemented in FXIconList, FXMDIChild, FXRootWindow, FXText, and FXTopWindow.

| **Argument** | **Type** | **Default** | **Description** |
| w | Int |   |   |
| h | Int |   |   |

### setBackColor(clr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set window background color.

Reimplemented in FXComboBox, and FXListBox.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor |   |   |

### setCursorPosition(x, y)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Warp the cursor to the new position.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   |   |
| y | Int |   |   |

### setFocus()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Move the focus to this window.

Reimplemented in FXButton, FXColorWell, FXIconList, FXList, FXMenuCascade, FXMenuCommand, FXMenuTitle, FXOption, FXPopup, FXRootWindow, FXShell, FXTable, FXText, FXTextField, FXTopWindow, FXTreeList, AFXBaseTable, AFXFlyoutItem, and AFXTextField.

### setHeight(h)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the window height.

| **Argument** | **Type** | **Default** | **Description** |
| h | Int |   |   |

### setInitial(enable=True)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Make this window the initial default window.

| **Argument** | **Type** | **Default** | **Description** |
| enable | Bool | True |   |

### setKey(k)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change window key.

| **Argument** | **Type** | **Default** | **Description** |
| k | Int |   |   |

### setLayoutHints(lout)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set layout hints for this window.

| **Argument** | **Type** | **Default** | **Description** |
| lout | Int |   |   |

### setSelector(sel)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the message identifier for this window.

| **Argument** | **Type** | **Default** | **Description** |
| sel | Int |   |   |

### setTarget(t)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the message target object for this window.

| **Argument** | **Type** | **Default** | **Description** |
| t | FXObject |   |   |

### setWidth(w)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the window width.

| **Argument** | **Type** | **Default** | **Description** |
| w | Int |   |   |

### setX(x)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set this window's x-coordinate, in the parent's coordinate system.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   |   |

### setY(y)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set this window's y-coordinate, in the parent's coordinate system.

| **Argument** | **Type** | **Default** | **Description** |
| y | Int |   |   |

### show()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Show this window.

Reimplemented in FXTooltip, FXTopWindow, AFXMenuTitle, AFXToolbarGroup, AFXToolbarGroupRender, AFXToolbarGroupVisibility, AFXDialog, AFXFileDialog, AFXMessageDialog, AFXOptionTreeItem, AFXProgressBar, and AFXSlider.

### shown()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if the window is shown.

### translateCoordinatesTo(tox, toy, towindow, fromx, fromy)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Translate coordinates from this window's coordinate space to towindow's coordinate space.

| **Argument** | **Type** | **Default** | **Description** |
| tox | Int |   |   |
| toy | Int |   |   |
| towindow | FXWindow |   |   |
| fromx | Int |   |   |
| fromy | Int |   |   |

### ungrab()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Release the mouse grab.

### update()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Mark the entire window client area dirty.

### update(x, y, w, h)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Mark the specified rectangle dirty, i.e. to be repainted.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   |   |
| y | Int |   |   |
| w | Int |   |   |
| h | Int |   |   |

### Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Layout hints for child widgets**

| **LAYOUT_NORMAL** | 

Default layout mode.

 |
| **LAYOUT\_SIDE\_TOP** | 

Pack on top side (default).

 |
| **LAYOUT\_SIDE\_BOTTOM** | 

Pack on bottom side.

 |
| **LAYOUT\_SIDE\_LEFT** | 

Pack on left side.

 |
| **LAYOUT\_SIDE\_RIGHT** | 

Pack on right side.

 |
| **LAYOUT\_FILL\_COLUMN** | 

Matrix column is stretchable.

 |
| **LAYOUT\_FILL\_ROW** | 

Matrix row is stretchable.

 |
| **LAYOUT_LEFT** | 

Stick on left (default).

 |
| **LAYOUT_RIGHT** | 

Stick on right.

 |
| **LAYOUT\_CENTER\_X** | 

Center horizontally.

 |
| **LAYOUT\_FIX\_X** | 

X fixed.

 |
| **LAYOUT_TOP** | 

Stick on top (default).

 |
| **LAYOUT_BOTTOM** | 

Stick on bottom.

 |
| **LAYOUT\_CENTER\_Y** | 

Center vertically.

 |
| **LAYOUT\_FIX\_Y** | 

Y fixed CAE: Copied from FOX 1.4.34 to support dockable tool bars.

 |
| **LAYOUT\_DOCK\_SAME** | 

Dock on same galley if it fits.

 |
| **LAYOUT\_DOCK\_NEXT** | 

Dock on next galley LAYOUT\_RESERVED\_1 = 0x00000040, LAYOUT\_RESERVED\_2 = 0x00000080,

 |
| **LAYOUT\_RESERVED\_1** | 

CAE End.

 |
| **LAYOUT\_FIX\_WIDTH** | 

Width fixed.

 |
| **LAYOUT\_FIX\_HEIGHT** | 

height fixed

 |
| **LAYOUT\_MIN\_WIDTH** | 

Minimum width is the default.

 |
| **LAYOUT\_MIN\_HEIGHT** | 

Minimum height is the default.

 |
| **LAYOUT\_FILL\_X** | 

Stretch or shrink horizontally.

 |
| **LAYOUT\_FILL\_Y** | 

Stretch or shrink vertically.

 |
| **LAYOUT_EXPLICIT** | 

Explicit placement.

 |


**Frame border appearance styles (for subclasses)**

| **FRAME_NONE** | 

Default is no frame.

 |
| **FRAME_SUNKEN** | 

Sunken border.

 |
| **FRAME_RAISED** | 

Raised border.

 |
| **FRAME_THICK** | 

Thick border.

 |
| **FRAME_GROOVE** | 

A groove or etched-in border.

 |
| **FRAME_RIDGE** | 

A ridge or embossed border.

 |
| **FRAME_LINE** | 

Simple line border.

 |
| **FRAME_NORMAL** | 

Regular raised/thick border.

 |


**Packing style (for packers)**

| **PACK_NORMAL** | 

Default is each its own size.

 |
| **PACK\_UNIFORM\_HEIGHT** | 

Uniform height.

 |
| **PACK\_UNIFORM\_WIDTH** | 

Uniform width.

 |


**BackgroundStyle**

| **BACKGROUND_NORMAL** | 

Default.

 |
| **BACKGROUND\_H\_GRADIENT** | 

Horizontal gradient background.

 |
| **BACKGROUND\_V\_GRADIENT** | 

Vertical gradient background.

 |
| **BACKGROUND_PLAIN** | 

plain background

 |

By clicking on Send, you accept that Dassault Systèmes will process your personal data and may contact you for further information.

[Privacy Policy](https://www.3ds.com/privacy-policy).

Total Results:

Results per page

This page cannot be found.

The page might not exist or is temporarily unavailable. Try again or try searching for the topic.