The Matrix layout manager automatically arranges its child windows in rows and columns. If the matrix style is MATRIX\_BY\_ROWS, then the matrix will have the given number of rows and the number of columns grows as more child windows are added; if the matrix style is MATRIX\_BY\_COLUMNS, then the number of columns is fixed and the number of rows grows as more children are added. If all children in a row (column) have the LAYOUT\_FILL\_ROW (LAYOUT\_FILL\_COLUMN) hint set, then the row (column) will be stretchable as the matrix layout manager itself is resized. If more than one row (column) is stretchable, the space is apportioned to each stretchable row (column) proportionally. Within each cell of the matrix, all other layout hints are observed. For example, a child having LAYOUT\_CENTER\_Y and LAYOUT\_FILL\_X hints will be centered in the Y-direction, while being stretched in the X-direction. Empty cells can be obtained by simply placing a borderless FXFrame widget as a space-holder.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fxmatrix.png)

### FXMatrix(p, n=1, opts=MATRIX\_BY\_ROWS, x=0, y=0, w=0, h=0, pl=DEFAULT\_SPACING, pr=DEFAULT\_SPACING, pt=DEFAULT\_SPACING, pb=DEFAULT\_SPACING, hs=DEFAULT\_SPACING, vs=DEFAULT\_SPACING)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Construct a matrix layout manager with n rows or columns.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   |   |
| n | Int | 1 |   |
| opts | Int | MATRIX\_BY\_ROWS |   |
| x | Int | 0 |   |
| y | Int | 0 |   |
| w | Int | 0 |   |
| h | Int | 0 |   |
| pl | Int | DEFAULT_SPACING |   |
| pr | Int | DEFAULT_SPACING |   |
| pt | Int | DEFAULT_SPACING |   |
| pb | Int | DEFAULT_SPACING |   |
| hs | Int | DEFAULT_SPACING |   |
| vs | Int | DEFAULT_SPACING |   |

### getDefaultHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default height.

Reimplemented from FXPacker.

### getDefaultWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default width.

Reimplemented from FXPacker.

### getNumColumns()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return the number of columns.

### getNumRows()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return the number of rows.

### setNumColumns(nc)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change the number of columns.

| **Argument** | **Type** | **Default** | **Description** |
| nc | Int |   |   |

### setNumRows(nr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change the number of rows.

| **Argument** | **Type** | **Default** | **Description** |
| nr | Int |   |   |

###   
Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

### 

**Matrix packing options**

| **MATRIX\_BY\_ROWS** | 

Fixed number of rows, add columns as needed.

 |
| **MATRIX\_BY\_COLUMNS** | 

Fixed number of columns, adding rows as needed.

 |