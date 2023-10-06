This class creates a container to be used for groups in the toolbar. It creates a vertical separator after the group. It will use utility methods so the group is correctly managed.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxtoolbargroup.png)

### AFXToolbarGroup(owner, name='', title='')

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| owner | AFXGuiObjectManager | | Creator of the group. |
| name | String | '' | English toolset name. |
| title | String | '' | Name appearing in the title bar when the group is floating. |

### getDefaultHeight()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default height.

Reimplemented from FXToolbar.

### getDefaultWidth()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default width.

Reimplemented from FXToolbar.

### getName()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the English identifier for the group.

### getOwner()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the creator of the group.

Reimplemented from FXWindow.

### getTitle()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the name appearing in the title bar when the group is floating.

### hide()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Hide this window.

Reimplemented from FXWindow.

Reimplemented in AFXToolbarGroupRender, and AFXToolbarGroupVisibility.

### isActive()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if the window is active.

Reimplemented from FXWindow.

### layout()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Calculates layout.

Reimplemented from FXToolbar.

### setName(name)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the English identifier for the group.

| **Argument** | **Type** | **Default** | **Description** |
| name | String | | |

### setTitle(title)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the name appearing in the title bar when the group is floating.

| **Argument** | **Type** | **Default** | **Description** |
| title | String | | |

### show()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Show this window.

Reimplemented from FXWindow.

Reimplemented in AFXToolbarGroupRender, and AFXToolbarGroupVisibility.
