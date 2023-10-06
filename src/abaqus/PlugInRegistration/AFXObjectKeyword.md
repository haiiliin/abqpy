Abaqus

GUI Toolkit Reference

All Classes

AFXObjectKeyword

This class is designed for the command keywords that have objects as values.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxobjectkeyword.png)

### AFXObjectKeyword(command, name, isRequired=False, defaultValue='')  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| command | AFXCommand |   | Host command. |
| name | String |   | Keyword name. |
| isRequired | Bool | False | True if the keyword is a required argument of the command. |
| defaultValue | String | '' | Default value. |

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
| defaultValue | String |   | Default value. |

### setValue(newValue)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword's current value.

| **Argument** | **Type** | **Default** | **Description** |
| newValue | String |   | New value. |

### setValueToDefault(ignoreUnspecified=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword value to its default.

| **Argument** | **Type** | **Default** | **Description** |
| ignoreUnspecified | Bool | False | If set to True, ignore setting the value if the default is unspecified. |

### setValueToPrevious()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword value to its previous value.

Implements AFXKeyword.

### syncPreviousValue()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the keyword's previous value to its current value.

Implements AFXKeyword.

By clicking on Send, you accept that Dassault Systèmes will process your personal data and may contact you for further information.

[Privacy Policy](https://www.3ds.com/privacy-policy).

Total Results:

Results per page

This page cannot be found.

The page might not exist or is temporarily unavailable. Try again or try searching for the topic.

Use this form to provide feedback on this help topic. To get product support or to provide product feedback, go to [Frequently Asked Questions](https://3ds.one/PO). For support for online purchased solutions, go to [Online Purchase Support](https://3ds.one/Q8).

\* Required

Subject:

Feedback on User Assistance

*

I acknowledge I have read and I hereby accept the [privacy policy](https://www.3ds.com/privacy-policy) under which my personal data will be used by Dassault Systèmes.