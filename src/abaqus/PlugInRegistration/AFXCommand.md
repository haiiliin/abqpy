This class is the abstract base class for command classes that are processed by modes.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxcommand.png)

### AFXCommand(mode, method, objectName='', registerQuery=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| mode | AFXMode |   | Host mode. |
| method | String |   | Method. |
| objectName | String | '' | Object name. |
| registerQuery | Bool | False | True if a query should be registered when the command is used for the GUI. |

### activate()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Activates the command; active commands will be processed during command generation.

### deactivate()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deactivates the command; inactive commands will not be processed during command generation.

### getCommandString()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the command string based on the current values of the active keywords.

### getExpandedObjectName()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the expanded object name that has all the "%s"'s replaced by the current names.

### getKeyword(name)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the keyword with the given name (returns 0 if none is found).

| **Argument** | **Type** | **Default** | **Description** |
| name | String |   | Keyword name. |

### getKeyword(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the keyword at the given index (returns 0 if the index is out-of-bounds).

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Keyword index (0-based). |

### getMethod()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the command's method.

### getNumKeywords()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of keywords.

### getObjectName()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the object name (which is not expanded and may include "%s"'s).

### isActive()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the command is active.

### isQueryNeeded()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the command needs to register a query for kernel state.

### isRequired()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if this command is going to be sent even if none of its keywords has been modified, otherwise returns False.

### setKeywordValuesToDefaults(ignoreUnspecified=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the values of all keywords to their defaults.

| **Argument** | **Type** | **Default** | **Description** |
| ignoreUnspecified | Bool | False | Ignore setting the value if the default is unspecified. |

### setKeywordValuesToPrevious()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the values of all keywords to their previous values.

### setMethod(method)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the command's method.

| **Argument** | **Type** | **Default** | **Description** |
| method | String |   | Method. |

### setObjectName(objectName)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the object name.

| **Argument** | **Type** | **Default** | **Description** |
| objectName | String |   | Object name. |

### setRequired(val)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets this command as required or optional; if True the command will always be sent, if False the command will be sent only if it has modified keywords or if it has no keywords.

| **Argument** | **Type** | **Default** | **Description** |
| val | Bool |   |   |

### syncKeywordPreviousValues()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Synchronizes the current values and previous values of all keywords.

### verify()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Throws an exception if any of the keywords contain invalid data.