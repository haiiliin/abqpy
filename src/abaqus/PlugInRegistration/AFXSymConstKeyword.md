This class is designed for the command keywords that have symbolic constant values.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxsymconstkeyword.png)

### AFXSymConstKeyword(command, name, isRequired=False, defaultValue=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| command | AFXCommand |   | Host command. |
| name | String |   | Keyword name. |
| isRequired | Bool | False | True if the keyword is a required argument of the command. |
| defaultValue | Int | 0 | Default value. |

### getTypeName()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the name of the keyword type.

Reimplemented from AFXIntKeyword.

### getValueAsString()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the text string that represents the keyword's current value.

Reimplemented from AFXIntKeyword.

### setDefaultValue(defaultValue)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword's default value.

| **Argument** | **Type** | **Default** | **Description** |
| defaultValue | Int |   | Default value. |

### setDefaultValueByString(defaultValueString)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword's default value (returns True if the given text string is valid).

| **Argument** | **Type** | **Default** | **Description** |
| defaultValueString | String |   | Default value in text string form. |

### setDefaultValueByString(defaultValueString)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword's default value (returns True if the given text string is valid).

| **Argument** | **Type** | **Default** | **Description** |
| defaultValueString | String |   | Default value in text string form. |

### setValue(newValue)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword's current value.

| **Argument** | **Type** | **Default** | **Description** |
| newValue | Int |   | New value. |

### setValueByString(newValueString)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword's current value (returns True if the given text string is valid).

| **Argument** | **Type** | **Default** | **Description** |
| newValueString | String |   | New value in text string form. |

### setValueByString(newValueString)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword's current value (returns True if the given text string is valid).

| **Argument** | **Type** | **Default** | **Description** |
| newValueString | String |   | New value in text string form. |

### setValueToDefault(ignoreUnspecified=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword value to its default.

| **Argument** | **Type** | **Default** | **Description** |
| ignoreUnspecified | Bool | False | Ignore setting the value if the default is unspecified. |