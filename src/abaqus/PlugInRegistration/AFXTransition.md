Abaqus

GUI Toolkit Reference

All Classes

AFXTransition

This class is designed for the finite state transition that the GUI (mostly the dialog boxes) can define to perform actions according to state changes. The first three arguments of the constructors (keyword, op, and refValue) define an expression (keyword.getValue() op refValue). The current value of the keyword is compared with the reference value. When the expression evaluates to True, a message with the given selector will be sent to the specified message target.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxtransition.png)

### AFXTransition(boolKeyword, op, refValue, tgt, sel, ptr=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| boolKeyword | AFXBoolKeyword |   | Keyword. |
| op | Operator |   | Operator type. |
| refValue | Bool |   | Reference value. |
| tgt | FXObject |   | Message target. |
| sel | Int |   | Message selector. |
| ptr | String | None | Message data. |

### AFXTransition(floatKeyword, op, refValue, tgt, sel, ptr=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| floatKeyword | AFXFloatKeyword |   | Keyword. |
| op | Operator |   | Operator type. |
| refValue | Float |   | Reference value. |
| tgt | FXObject |   | Message target. |
| sel | Int |   | Message selector. |
| ptr | String | None | Message data. |

### AFXTransition(intKeyword, op, refValue, tgt, sel, ptr=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| intKeyword | AFXIntKeyword |   | Keyword. |
| op | Operator |   | Operator type. |
| refValue | Int |   | Reference value. |
| tgt | FXObject |   | Message target. |
| sel | Int |   | Message selector. |
| ptr | String | None | Message data. |

### AFXTransition(togKeyword, op, refValue, tgt, sel, ptr=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| togKeyword | AFXTogglableKeyword |   | Keyword. |
| op | Operator |   | Operator type. |
| refValue | Bool |   | Reference value. |
| tgt | FXObject |   | Message target. |
| sel | Int |   | Message selector. |
| ptr | String | None | Message data. |

### AFXTransition(floatTarget, op, refValue, tgt, sel, ptr=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| floatTarget | AFXFloatTarget |   | Target. |
| op | Operator |   | Operator type. |
| refValue | Float |   | Reference value. |
| tgt | FXObject |   | Message target. |
| sel | Int |   | Message selector. |
| ptr | String | None | Message data. |

### AFXTransition(intTarget, op, refValue, tgt, sel, ptr=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| intTarget | AFXIntTarget |   | Target. |
| op | Operator |   | Operator type. |
| refValue | Int |   | Reference value. |
| tgt | FXObject |   | Message target. |
| sel | Int |   | Message selector. |
| ptr | String | None | Message data. |

### process(sender)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True and sends a message if the expression defined by the constructor arguments evaluates to True; returns False without performing any actions if otherwise.

| **Argument** | **Type** | **Default** | **Description** |
| sender | FXObject |   | Message sender. |

###   
Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

### 

**Flags for specifying transition operators.**

| **EQ** | 

Equal to.

 |
| **NE** | 

Not equal to.

 |
| **LT** | 

Less than.

 |
| **LE** | 

Less than or equal to.

 |
| **GT** | 

Greater than.

 |
| **GE** | 

Greater than or equal to.

 |

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