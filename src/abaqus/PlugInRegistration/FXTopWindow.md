Abstract base class for all top-level windows

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fxtopwindow.png)

### create()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Create server-side resources.

Reimplemented from FXShell.

Reimplemented in FXPrintDialog, FXToolbarShell, AFXMainWindow, and AFXDialog.

### deiconify()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deiconify window.

### detach()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Detach the server-side resources for this window.

Reimplemented from FXComposite.

### getDecorations()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return current title and border decorations.

### getDefaultHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return the default height of this window.

Reimplemented from FXComposite.

Reimplemented in FXToolbarShell, and AFXMainWindow.

### getDefaultWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return the default width of this window.

Reimplemented from FXComposite.

Reimplemented in FXToolbarShell, and AFXMainWindow.

### getHSpacing()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return horizontal spacing between children.

### getIcon()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return window icon.

### getMiniIcon()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return window mini (title) icon.

### getPackingHints()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return packing hints for children.

### getPadBottom()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get bottom interior padding.

### getPadLeft()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get left interior padding.

### getPadRight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get right interior padding.

### getPadTop()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get top interior padding.

### getTitle()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return window title.

### getVSpacing()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return vertical spacing between children.

### hide()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Hide this window.

Reimplemented from FXWindow.

Reimplemented in AFXManagerMenuDB, AFXDialog, and AFXMessageDialog.

### iconify()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Iconify window.

### isIconified()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if window has been iconified.

### killFocus()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Remove the focus from this window.

Reimplemented from FXShell.

### move(x, y)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Move this window to the specified position in the parent's coordinates.

Reimplemented from FXWindow.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   |   |
| y | Int |   |   |

### place(placement)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Position the window based on placement.

| **Argument** | **Type** | **Default** | **Description** |
| placement | Int |   |   |

### position(x, y, w, h)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Move and resize this window in the parent's coordinates.

Reimplemented from FXWindow.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   |   |
| y | Int |   |   |
| w | Int |   |   |
| h | Int |   |   |

### resize(w, h)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Resize this window to the specified width and height.

Reimplemented from FXWindow.

| **Argument** | **Type** | **Default** | **Description** |
| w | Int |   |   |
| h | Int |   |   |

### setDecorations(decorations)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change title and border decorations.

| **Argument** | **Type** | **Default** | **Description** |
| decorations | Int |   |   |

### setFocus()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Move the focus to this window.

Reimplemented from FXShell.

### setHSpacing(hs)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change horizontal spacing between children.

| **Argument** | **Type** | **Default** | **Description** |
| hs | Int |   |   |

### setIcon(ic)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change window icon.

| **Argument** | **Type** | **Default** | **Description** |
| ic | FXIcon |   |   |

### setMiniIcon(ic)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change window mini (title) icon.

| **Argument** | **Type** | **Default** | **Description** |
| ic | FXIcon |   |   |

### setPackingHints(ph)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change packing hints for children.

| **Argument** | **Type** | **Default** | **Description** |
| ph | Int |   |   |

### setPadBottom(pb)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change bottom padding.

| **Argument** | **Type** | **Default** | **Description** |
| pb | Int |   |   |

### setPadLeft(pl)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change left padding.

| **Argument** | **Type** | **Default** | **Description** |
| pl | Int |   |   |

### setPadRight(pr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change right padding.

| **Argument** | **Type** | **Default** | **Description** |
| pr | Int |   |   |

### setPadTop(pt)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change top padding.

| **Argument** | **Type** | **Default** | **Description** |
| pt | Int |   |   |

### setTitle(name)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change window title.

| **Argument** | **Type** | **Default** | **Description** |
| name | String |   |   |

### setVSpacing(vs)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change vertical spacing between children.

| **Argument** | **Type** | **Default** | **Description** |
| vs | Int |   |   |

### show(placement)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Show this window with given placement.

| **Argument** | **Type** | **Default** | **Description** |
| placement | Int |   |   |

### show()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Show this window.

Reimplemented from FXWindow.

Reimplemented in AFXDialog, AFXFileDialog, and AFXMessageDialog.

###   
Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

### 

| **ID_ICONIFY** | 

Iconify the window.

 |
| **ID_DEICONIFY** | 

Deiconify the window.

 |
| **ID\_QUERY\_DOCK** | 

Toolbar asks to dock.

 |

###   
Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

### 

**Title and border decorations**

| **DECOR_NONE** | 

Borderless window.

 |
| **DECOR_TITLE** | 

Window title.

 |
| **DECOR_MINIMIZE** | 

Minimize button.

 |
| **DECOR_MAXIMIZE** | 

Maximize button.

 |
| **DECOR_CLOSE** | 

Close button.

 |
| **DECOR_BORDER** | 

Border.

 |
| **DECOR_RESIZE** | 

Resize handles.

 |
| **DECOR_MENU** | 

Window menu.

 |

### 

**Initial window placement**

| **PLACEMENT_DEFAULT** | 

Place it at the default size and location.

 |
| **PLACEMENT_VISIBLE** | 

Place window to be fully visible.

 |
| **PLACEMENT_CURSOR** | 

Place it under the cursor position.

 |
| **PLACEMENT_OWNER** | 

Place it centered on its owner.

 |
| **PLACEMENT_SCREEN** | 

Place it centered on the screen.

 |
| **PLACEMENT_MAXIMIZED** | 

Place it maximized to the screen size.

 |