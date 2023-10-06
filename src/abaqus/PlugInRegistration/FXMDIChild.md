The MDI child window contains the application work area in a Multiple Document Interface application.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fxmdichild.png)

### FXMDIChild(p, name, ic=None, mn=None, opts=0, x=0, y=0, w=0, h=0)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Construct MDI Child window with given name and icon.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXMDIClient | | |
| name | String | | |
| ic | FXIcon | None | |
| mn | FXMenuPane | None | |
| opts | Int | 0 | |
| x | Int | 0 | |
| y | Int | 0 | |
| w | Int | 0 | |
| h | Int | 0 | |

### canFocus()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

MDI Child can receive focus.

Reimplemented from FXWindow.

### contentWindow()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return content window.

### create()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Create window.

Reimplemented from FXComposite.

### detach()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Detach window.

Reimplemented from FXComposite.

### getDefaultHeight()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default height.

Reimplemented from FXComposite.

### getDefaultWidth()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Compute default size.

Reimplemented from FXComposite.

### getFont()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get title font.

### getHiliteColor()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get colors.

### getIconX()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return iconified position.

### getMDINext()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get next MDI Child.

### getMDIPrev()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get previous MDI Child.

### getNormalX()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return normal (restored) position.

### getTitle()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get current title.

### getWindowIcon()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get window icon.

### getWindowMenu()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get window menu.

### isMaximized()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if maximized.

### isMinimized()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if minimized.

### maximize(notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Maximize MDI Child.

| **Argument** | **Type** | **Default** | **Description** |
| notify | Bool | False | |

### minimize(notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Minimize/iconify MDI Child.

| **Argument** | **Type** | **Default** | **Description** |
| notify | Bool | False | |

### move(x, y)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Move this window to the specified position in the parent's coordinates.

Reimplemented from FXWindow.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int | | |
| y | Int | | |

### position(x, y, w, h)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Move and resize this window in the parent's coordinates.

Reimplemented from FXWindow.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int | | |
| y | Int | | |
| w | Int | | |
| h | Int | | |

### resize(w, h)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Resize this window to the specified width and height.

Reimplemented from FXWindow.

| **Argument** | **Type** | **Default** | **Description** |
| w | Int | | |
| h | Int | | |

### restore(notify=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Restore MDI Child to normal.

| **Argument** | **Type** | **Default** | **Description** |
| notify | Bool | False | |

### setFont(fnt)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set title font.

| **Argument** | **Type** | **Default** | **Description** |
| fnt | FXFont | | |

### setHiliteColor(clr)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change colors.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor | | |

### setIconX(x)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change iconified position.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int | | |

### setNormalX(x)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change normal (restored) position.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int | | |

### setTitle(name)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change MDI Child's title.

| **Argument** | **Type** | **Default** | **Description** |
| name | String | | |

### setWindowIcon(icon)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set window icon.

| **Argument** | **Type** | **Default** | **Description** |
| icon | FXIcon | | |

### setWindowMenu(menu)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set window menu.

| **Argument** | **Type** | **Default** | **Description** |
| menu | FXPopup | | |

### Global flags

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

**MDI Child Window styles**

| **MDI_NORMAL** |

Normal display mode.

|
| **MDI_MAXIMIZED** |

Window appears maximized.

|
| **MDI_MINIMIZED** |

Window is iconified or minimized.

|
