This class manages values which are sent as tuples in a command.

Widgets used to edit the whole tuple should have their message ID set to 0. It is also possible to edit individual elements of the tuple. In order to edit the N-th tuple element, the widget's message ID should be set to N (N is 1-based).

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxtuplekeyword.png)

### AFXTupleKeyword(command, name, isRequired=False, minLength=0, maxLength=-1, opts=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| command | AFXCommand |   | Host command. |
| name | String |   | Keyword name. |
| isRequired | Bool | False | True if this keyword is a required argument. |
| minLength | Int | 0 | Minimum (and default) tuple length. |
| maxLength | Int | -1 | Maximum tuple length (-1 => unlimited). |
| opts | Int | 0 | Options. |

### equal(index, a, b)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the two tuple element values compare equal (index is not used).

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index (not used). |
| a | String |   | First value. |
| b | String |   | Second value. |

### getDefaultStyle()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default style for elements.

### getDefaultType()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default type for elements.

### getDefaultValues()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default values for this tuple.

### getElementStyle(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the style of one element. Will never return AFXTUPLE\_STYLE\_DEFAULT!

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index. |

### getElementType(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the type of one element. Will never return AFXTUPLE\_TYPE\_DEFAULT!

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index. |

### getFormattedValue(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the formatted value of the tuple element, suitable for placing in a command. If the element has AFXTUPLE_EVALUATE style and its contents are invalid, an exception will be thrown.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index. |

### getLength()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the length of the tuple.

### getMaxLength()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the maximum length of this tuple, or -1 for unbounded length.

### getMinLength()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the minimum length of this tuple.

### getTypeName()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the name of the tuple keyword type.

Implements AFXKeyword.

### getValue(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the value of a tuple element.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index. |

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

### getValueForBlank(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the value substituted for blank tuple element.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index. |

### getValues()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns a string containing values (separated by commas) of the tuple elements.

### getValuesForBlanks()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns a string containing values substituted for blanks for the tuple elements.

### insertElements(index, numCols)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Inserts elements starting at the given index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Starting index. |
| numCols | Int |   | Number of elements to insert. |

### isValueChanged()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the keyword value differs from its previous value.

Implements AFXKeyword.

### removeElements(index, numCols)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Removes elements starting at the given index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Starting index. |
| numCols | Int |   | Number of elements to remove. |

### setDefaultStyle(style)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default style for elements.

| **Argument** | **Type** | **Default** | **Description** |
| style | Int |   | New default element style. |

### setDefaultType(type)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default type for elements.

| **Argument** | **Type** | **Default** | **Description** |
| type | Int |   | New default type. |

### setDefaultValues(values)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the default values for this tuple.

| **Argument** | **Type** | **Default** | **Description** |
| values | String |   | Sequence string with default values. |

### setElementStyle(index, style)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the style of one element.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index. |
| style | Int |   | New element style. |

### setElementType(index, type)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the type of one element.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index. |
| type | Int |   | New element type. |

### setLengthRange(minLength, maxLength)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the range of allowable tuple lengths.

| **Argument** | **Type** | **Default** | **Description** |
| minLength | Int |   | New minimum length. |
| maxLength | Int |   | New maximum length, or -1 for unbounded length. |

### setMaxLength(length)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the maximum length of this tuple.

| **Argument** | **Type** | **Default** | **Description** |
| length | Int |   | New maximum length, or -1 for unbounded length. |

### setMinLength(length)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the minimum length of this tuple.

| **Argument** | **Type** | **Default** | **Description** |
| length | Int |   | New minimum length. |

### setValue(index, value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the value of the tuple element; returns False upon failure.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index. |
| value | String |   | New value. |

### setValueForBlank(index, value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the value substituted for a blank tuple element.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index. |
| value | String |   | New value. |

### setValues(values)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets values for all tuple elements (use commas to separate values within the string).

| **Argument** | **Type** | **Default** | **Description** |
| values | String |   | Tuple string with new values. |

### setValuesForBlanks(values)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets all values substituted for blanks for the tuple elements.

| **Argument** | **Type** | **Default** | **Description** |
| values | String |   | Tuple string with values. |

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

### Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Message ID's.**

| **ID_PRINTSNIPPET** | 

For debugging.

 |

### Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Flags for tuple keyword options.**

| **AFXTUPLE\_TYPE\_ANY** | 

Any type is accepted.

 |
| **AFXTUPLE\_TYPE\_DEFAULT** | 

Element type is the same as the tuple default type.

 |
| **AFXTUPLE\_TYPE\_INT** | 

Element is an integer number.

 |
| **AFXTUPLE\_TYPE\_FLOAT** | 

Element is a floating-point number.

 |
| **AFXTUPLE\_TYPE\_STRING** | 

Element is a string.

 |
| **AFXTUPLE\_TYPE\_BOOL** | 

Element is True or False.

 |
| **AFXTUPLE\_TYPE\_MASK** | 

Mask for element types.

 |
| **AFXTUPLE\_ALLOW\_EMPTY** | 

Allow empty values for the element.

 |
| **AFXTUPLE\_DEFAULT\_IF_EMPTY** | 

Always substitute the default for an empty value.

 |
| **AFXTUPLE_EVALUATE** | 

Evaluate integer and float elements.

 |
| **AFXTUPLE\_STYLE\_DEFAULT** | 

Use tuple default element style.

 |
| **AFXTUPLE\_STYLE\_MASK** | 

Mask for element styles.

 |