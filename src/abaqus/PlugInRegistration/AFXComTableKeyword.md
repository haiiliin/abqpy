This class manages values which are sent as tables in a command.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxcomtablekeyword.png)

### AFXComTableKeyword(command, name, isRequired=False, minLength=0, maxLength=-1, opts=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| command | AFXCommand |   | Host command. |
| name | String |   | Keyword name. |
| isRequired | Bool | False | True if this keyword is a required argument. |
| minLength | Int | 0 | Minimum (and default) row length. |
| maxLength | Int | -1 | Maximum row length (-1 => unlimited). |
| opts | Int | 0 | Options. |

### equal(index, a, b)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the two table element values compare equal (index not used).

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index (not used). |
| a | String |   | First value. |
| b | String |   | Second value. |

### getColumnStyle(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the style of the column elements. Will never return AFXTABLE\_STYLE\_DEFAULT!

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Column index. |

### getColumnType(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the type of the column elements. Will never return AFXTABLE\_TYPE\_DEFAULT!

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Column index. |

### getDefaultStyle()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default style for the table elements.

### getDefaultType()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default type for the table elements.

### getDefaultValues()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default values for this table.

### getFormattedValue(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the formatted value of the table element, suitable for placing in a command. If the element has AFXTABLE_EVALUATE style, and its contents are invalid, an exception will be thrown.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index. |
| column | Int |   | Column index. |

### getMaxNumColumns()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the maximum number of columns, or -1 for unbounded.

### getMinNumColumns()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the minimum number of columns.

### getNumColumns(row)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of columns in the row.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index. |

### getNumRows()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of rows in the table.

### getRow(row)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns a string with the contents of a table row.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index. |

### getTypeName()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the name of the table keyword type.

Implements AFXKeyword.

Reimplemented in AFXTableKeyword.

### getValue(row, column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the value of a table element.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index. |
| column | Int |   | Column index. |

### getValueAsDouble()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the keyword's value as a float; returns False upon failure.

### getValueAsInt()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the keyword's value as an integer; returns False upon failure.

### getValueAsString()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the formatted string that represents the current keyword value in a command.

Implements AFXKeyword.

### getValueForBlank(column)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the element value substituted for blank for the column.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |

### getValues()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns a string containing values of the tuple elements. as entered by the user.

### getValuesForBlanks()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns a string with values substituted for blanks for all table columns.

### insertColumns(index, numColumns)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Inserts columns starting at the given index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Starting index. |
| numColumns | Int |   | Number of columns to insert. |

### insertRows(index, numRows)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Inserts rows starting at the given index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Starting index. |
| numRows | Int |   | Number of rows to insert. |

### isValueChanged()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the keyword value differs from its previous value.

Implements AFXKeyword.

### removeColumns(index, numColumns)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Removes columns starting at the given index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Starting index. |
| numColumns | Int |   | Number of columns to remove. |

### removeRows(index, numRows)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Removes rows starting at the given index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Starting index. |
| numRows | Int |   | Number of rows to remove. |

### setColumnStyle(index, style)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the style of the column elements.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Column index. |
| style | Int |   | New column style. |

### setColumnType(index, type)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the type of the column elements.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Column index. |
| type | Int |   | New column type. |

### setDefaultStyle(style)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default style for the table elements.

| **Argument** | **Type** | **Default** | **Description** |
| style | Int |   | New default style. |

### setDefaultType(type)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default type for table elements.

| **Argument** | **Type** | **Default** | **Description** |
| type | Int |   | New default type. |

### setDefaultValues(values)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default values for this table.

| **Argument** | **Type** | **Default** | **Description** |
| values | String |   | Sequence string with default values. |

### setMaxNumColumns(length)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the maximum number of columns.

| **Argument** | **Type** | **Default** | **Description** |
| length | Int |   | New maximum number of columns, or -1 for unbounded. |

### setMinNumColumns(length)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the minimum number of columns.

| **Argument** | **Type** | **Default** | **Description** |
| length | Int |   | New minimum length. |

### setNumColumnsRange(minLength, maxLength)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the allowable range for the number of columns.

| **Argument** | **Type** | **Default** | **Description** |
| minLength | Int |   | New minimum number of columns. |
| maxLength | Int |   | New maximum number of columns, or -1 for unbounded. |

### setRow(row, seq)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the contents of a table row.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index. |
| seq | String |   | Sequence with elements. |

### setValue(row, column, value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the value of a table element.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   | Row index. |
| column | Int |   | Column index. |
| value | String |   | New value. |

### setValueForBlank(column, value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the element value substituted for blank for the column.

| **Argument** | **Type** | **Default** | **Description** |
| column | Int |   | Column index. |
| value | String |   | New value. |

### setValues(values)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets all values for the table elements.

| **Argument** | **Type** | **Default** | **Description** |
| values | String |   | Table string with new values. |

### setValuesForBlanks(values)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the values substituted for blanks for all table columns.

| **Argument** | **Type** | **Default** | **Description** |
| values | String |   | String containing comma-separated values. |

### setValueToDefault(ignoreUnspecified=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword value to its default.

| **Argument** | **Type** | **Default** | **Description** |
| ignoreUnspecified | Bool | False | Should ignore if default is an unspecified value. |

### setValueToPrevious()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword value to its previous value.

Implements AFXKeyword.

### syncPreviousValue()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword's previous value to its current value.

Implements AFXKeyword.

###   
Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

### 

**Message ID's.**

| **ID_TABLE** | 

ID for AFXTable widgets.

 |
| **ID_VALUE** | 

ID for widgets exchanging array strings.

 |
| **ID_PRINTSNIPPET** | 

For debugging.

 |

###   
Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

### 

**Flags for table options.**

| **AFXTABLE\_TYPE\_ANY** | 

Any type is accepted.

 |
| **AFXTABLE\_TYPE\_DEFAULT** | 

Column type is the same as the table default type.

 |
| **AFXTABLE\_TYPE\_INT** | 

Column stores integer numbers.

 |
| **AFXTABLE\_TYPE\_FLOAT** | 

Column stores floating-point numbers.

 |
| **AFXTABLE\_TYPE\_STRING** | 

Column stores string values.

 |
| **AFXTABLE\_TYPE\_BOOL** | 

Column stores True or False.

 |
| **AFXTABLE\_TYPE\_MASK** | 

Mask for column types.

 |
| **AFXTABLE\_ALLOW\_EMPTY** | 

Allow empty values for the column elements.

 |
| **AFXTABLE\_DEFAULT\_IF_EMPTY** | 

Always substitute the default for empty values.

 |
| **AFXTABLE_EVALUATE** | 

Evaluate integer and float elements.

 |
| **AFXTABLE\_STYLE\_DEFAULT** | 

Use table default column style.

 |
| **AFXTABLE\_STYLE\_MASK** | 

Mask for column styles.

 |