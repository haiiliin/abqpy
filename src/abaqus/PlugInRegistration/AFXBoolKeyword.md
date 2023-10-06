This class is designed for command keywords that have Boolean values.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxboolkeyword.png)

### AFXBoolKeyword(command, name, booleanType=ON_OFF, isRequired=False, defaultValue=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| command | AFXCommand |   | Host command. |
| name | String |   | Keyword name. |
| booleanType | Type | ON_OFF | Type of boolean used in the command. |
| isRequired | Bool | False | True if the keyword is a required argument of the command. |
| defaultValue | Bool | False | Default value. |

### getTypeName()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the name of the keyword type.

Implements AFXKeyword.

### getValue()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the keyword's current value.

### getValueAsString()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the text string that represents the keyword's current value.

Implements AFXKeyword.

### isValueChanged()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the keyword value differs from its previous value.

Implements AFXKeyword.

### setDefaultValue(defaultValue)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword's default value.

| **Argument** | **Type** | **Default** | **Description** |
| defaultValue | Bool |   | Default value. |

### setDefaultValueByString(defaultValueString)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword's default value (returns True if the given text string is valid).

| **Argument** | **Type** | **Default** | **Description** |
| defaultValueString | String |   | Default value in text string form. |

### setDefaultValueByString(defaultValueString)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword's default value (returns True if the given text string is valid).

| **Argument** | **Type** | **Default** | **Description** |
| defaultValueString | String |   | Default value in text string form. |

### setValue(newValue)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword's current value.

| **Argument** | **Type** | **Default** | **Description** |
| newValue | Bool |   | New value. |

### setValueByString(newValueString)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword's current value (returns True if the given text string is valid).

| **Argument** | **Type** | **Default** | **Description** |
| newValueString | String |   | New value in text string form. |

### setValueByString(newValueString)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword's current value (returns True if the given text string is valid).

| **Argument** | **Type** | **Default** | **Description** |
| newValueString | String |   | New value in text string form. |

### setValueToDefault(ignoreUnspecified=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword value to its default.

| **Argument** | **Type** | **Default** | **Description** |
| ignoreUnspecified | Bool | False | Not used. |

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


**Flags for the type of the boolean.**

| **ON_OFF** | 

Keyword value will be ON or OFF.

 |
| **TRUE_FALSE** | 

Keyword value will be True or False.

 |