This class is the base class for all target objects.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxtarget.png)

### AFXTarget()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

### connect(value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Associates the data with a string variable.

| **Argument** | **Type** | **Default** | **Description** |
| value | String |   | Variable to be associated with. |

### connect(value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Associates the data with a floating-point variable.

| **Argument** | **Type** | **Default** | **Description** |
| value | Float |   | Variable to be associated with. |

### connect(value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Associates the data with an integer variable.

| **Argument** | **Type** | **Default** | **Description** |
| value | Int |   | Variable to be associated with. |

### getSelector()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the message ID of this target object.

### getTarget()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the target of this target object.

### getType()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the target type; this method is deprecated in Abaqus 6.6, and its use should be replaced by getTypeName().

### getTypeName()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the name of the target type.

Implemented in AFXFloatTarget, AFXIntTarget, and AFXStringTarget.

### setSelector(msgId)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the message ID of this target object.

| **Argument** | **Type** | **Default** | **Description** |
| msgId | Int |   | Message ID. |

### setTarget(target)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the target of this target object.

| **Argument** | **Type** | **Default** | **Description** |
| target | FXObject |   | Target. |

### Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Flags for the type of target.**

| **UNSPECIFIED** | 

Unspecified.

 |
| **INT** | 

Integer.

 |
| **FLOAT** | 

Float.

 |
| **STRING** | 

String.

 |

By clicking on Send, you accept that Dassault Systèmes will process your personal data and may contact you for further information.

[Privacy Policy](https://www.3ds.com/privacy-policy).

Total Results:

Results per page