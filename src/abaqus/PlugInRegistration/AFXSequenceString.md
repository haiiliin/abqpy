This class supports parsing and modification of strings containing sequences of elements separated with some separator character.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxsequencestring.png)

### AFXSequenceString(value='', sep=',')  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| value | String | '' | String with initial sequence values. |
| sep | String | ',' | Separator character for sequence elements. |

### AFXSequenceString()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Undefined copy constructor (this class has no copy semantics).

### forceNumElements(num, fill)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Forces the content string to contain a tuple with the given number of elements.

| **Argument** | **Type** | **Default** | **Description** |
| num | Int |   | New number of elements. |
| fill | String |   | String to insert in empty spaces. |

### getContentString()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns a string containing values of the sequence elements.

Reimplemented in AFX2DArrayConstString.

### getElementSeparator()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the element separator character.

### getLength(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the length in characters of a sequence element.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index. |

### getNumElements()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of elements in this sequence.

### getPosition(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the position in the content string of the beginning character of the sequence element.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index. |

### getValue(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the value of a sequence element.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index. |

### insert(index, numElements, val)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Inserts many copies of an element.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index at which inserting begins. |
| numElements | Int |   | Number of elements to insert. |
| val | String |   | Value for the new elements. |

### isValidSequence()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if this object contains a valid sequence.

### remove(index, numElements)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Removes elements starting at the given index.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index at which removal begins. |
| numElements | Int |   | Number of elements to remove. |

### setContentString(seqstr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Resets all values for the sequence elements.

| **Argument** | **Type** | **Default** | **Description** |
| seqstr | String |   | Sequence string with new values. |

### setElementSeparator(sep)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the element separator character.

| **Argument** | **Type** | **Default** | **Description** |
| sep | String |   | Separator character. |

### setLength(index, length)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the length of the sequence element.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index. |
| length | Int |   | New length (in characters). |

### setPosition(index, position)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the position of the sequence element.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index. |
| position | Int |   | New position within the string. |

### setValue(index, value, replaceAll=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the value of a sequence element.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index. |
| value | String |   | New value. |
| replaceAll | Bool | False | If False (default), leading and trailing spaces will be preserved, otherwise, all space between separators will be replaced with the new value. |

### trimWhiteSpace(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Adjusts the position and length of the element to trim leading and trailing white spaces.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Element index. |