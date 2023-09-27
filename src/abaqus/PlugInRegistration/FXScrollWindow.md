The scroll window widget scrolls an arbitrary child window. Use the scroll window when parts of the user interface itself need to be scrolled, for example when applications need to run on small screens.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fxscrollwindow.png)

### FXScrollWindow(p, opts=0, x=0, y=0, w=0, h=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Construct a scroll window.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   |   |
| opts | Int | 0 |   |
| x | Int | 0 |   |
| y | Int | 0 |   |
| w | Int | 0 |   |
| h | Int | 0 |   |

### contentWindow()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return a pointer to the contents window.

### create()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Create server-side resources.

Reimplemented from FXComposite.

### getContentHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return the height of the contents.

Reimplemented from FXScrollArea.

Reimplemented in AFXOptionTreeList.

### getContentWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return the width of the contents.

Reimplemented from FXScrollArea.

Reimplemented in AFXOptionTreeList.

### moveContents(x, y)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Move contents to the specified position.

Reimplemented from FXScrollArea.

Reimplemented in AFXOptionTreeList.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   |   |
| y | Int |   |   |