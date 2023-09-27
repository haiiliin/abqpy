AFXDataDialog

This class is the base class for all data dialogs, which collect data from the user and typically collaborate with modes to process the data.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxdatadialog.png)

### AFXDataDialog(mode, title, actionButtonIds=0, opts=DIALOG_NORMAL, x=0, y=0, w=0, h=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor that creates a dialog box that occludes the main window.

| **Argument** | **Type** | **Default** | **Description** |
| mode | AFXGuiMode |   | Host mode. |
| title | String |   | Title string. |
| actionButtonIds | Int | 0 | ID's of action buttons to be created. |
| opts | Int | DIALOG_NORMAL | Options and hints. |
| x | Int | 0 | X coordinate of origin. |
| y | Int | 0 | Y coordinate of origin. |
| w | Int | 0 | Width of the widget. |
| h | Int | 0 | Height of the widget. |

### AFXDataDialog(mode, owner, title, actionButtonIds=0, opts=DIALOG_NORMAL, x=0, y=0, w=0, h=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor that creates a dialog box that occludes its owner widget.

| **Argument** | **Type** | **Default** | **Description** |
| mode | AFXGuiMode |   | Host mode. |
| owner | FXWindow |   | Owner widget. |
| title | String |   | Title string. |
| actionButtonIds | Int | 0 | ID's of action buttons to be created. |
| opts | Int | DIALOG_NORMAL | Options and hints. |
| x | Int | 0 | X coordinate of origin. |
| y | Int | 0 | Y coordinate of origin. |
| w | Int | 0 | Width of the widget. |
| h | Int | 0 | Height of the widget. |

### addTransition(target, op, value, tgt, sel, ptr=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Adds a finite state transition to the dialog box. When the expression "target.getValue() op value" evaluates to True, an sel message will be sent to the tgt object.

| **Argument** | **Type** | **Default** | **Description** |
| target | AFXIntTarget |   | Target. |
| op | AFXTransition::Operator |   | Operator type. |
| value | Int |   | Reference value. |
| tgt | FXObject |   | Message target. |
| sel | Int |   | Message selector. |
| ptr | String | None | Message data. |

### addTransition(target, op, value, tgt, sel, ptr=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Adds a finite state transition to the dialog box. When the expression "target.getValue() op value" evaluates to True, an sel message will be sent to the tgt object.

| **Argument** | **Type** | **Default** | **Description** |
| target | AFXFloatTarget |   | Target. |
| op | AFXTransition::Operator |   | Operator type. |
| value | Float |   | Reference value. |
| tgt | FXObject |   | Message target. |
| sel | Int |   | Message selector. |
| ptr | String | None | Message data. |

### addTransition(keyword, op, value, tgt, sel, ptr=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Adds a finite state transition to the dialog box. When the expression "keyword.getValue() op value" evaluates to True, an sel message will be sent to the tgt object.

| **Argument** | **Type** | **Default** | **Description** |
| keyword | AFXTogglableKeyword |   | Keyword. |
| op | AFXTransition::Operator |   | Operator type. |
| value | Int |   | Reference value. |
| tgt | FXObject |   | Message target. |
| sel | Int |   | Message selector. |
| ptr | String | None | Message data. |

### addTransition(keyword, op, value, tgt, sel, ptr=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Adds a finite state transition to the dialog box. When the expression "keyword.getValue() op value" evaluates to True, an sel message will be sent to the tgt object.

| **Argument** | **Type** | **Default** | **Description** |
| keyword | AFXIntKeyword |   | Keyword. |
| op | AFXTransition::Operator |   | Operator type. |
| value | Int |   | Reference value. |
| tgt | FXObject |   | Message target. |
| sel | Int |   | Message selector. |
| ptr | String | None | Message data. |

### addTransition(keyword, op, value, tgt, sel, ptr=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Adds a finite state transition to the dialog box. When the expression "keyword.getValue() op value" evaluates to True, an sel message will be sent to the tgt object.

| **Argument** | **Type** | **Default** | **Description** |
| keyword | AFXFloatKeyword |   | Keyword. |
| op | AFXTransition::Operator |   | Operator type. |
| value | Float |   | Reference value. |
| tgt | FXObject |   | Message target. |
| sel | Int |   | Message selector. |
| ptr | String | None | Message data. |

### addTransition(keyword, op, value, tgt, sel, ptr=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Adds a finite state transition to the dialog box. When the expression "keyword.getValue() op value" evaluates to True, an sel message will be sent to the tgt object.

| **Argument** | **Type** | **Default** | **Description** |
| keyword | AFXBoolKeyword |   | Keyword. |
| op | AFXTransition::Operator |   | Operator type. |
| value | Bool |   | Reference value. |
| tgt | FXObject |   | Message target. |
| sel | Int |   | Message selector. |
| ptr | String | None | Message data. |

### bailout()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Performs checks to determine whether it is OK to cancel the dialog box. The implementaton of this class always returns True, and the derived class should reimplement this method to perform specific checks.

Reimplemented from AFXDialog.

### getMode()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the dialog box's host mode.

### onKeywordError(kwd)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Handles the error that occurs when the given keyword or target contains invalid contents. This method will select the contents of the widget that is set for the keyword or target (with setWidgetForKeyword()). If no such widget is specified explicitly, it will select the contents of the widget that has the keyword or target as its message target.

| **Argument** | **Type** | **Default** | **Description** |
| kwd | FXObject |   | Object that contains invalid contents. |

### onTableError(tableKwd, row, col)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Handles the error that occurs when the given table keyword or target contains an invalid element. This method will select the contents of the widget that is set for the element of the keyword or target (with setWidgetForKeyword()). If no such widget is specified explicitly, it will select the contents of the widget that has the keyword or target as its message target.

| **Argument** | **Type** | **Default** | **Description** |
| tableKwd | FXObject |   | Object that contains invalid element. |
| row | Int |   | Row index. |
| col | Int |   | Column index. |

### onTupleError(tupleKwd, index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Handles the error that occurs when the given tuple keyword or target contains an invalid element. This method will select the contents of the widget that is set for the element of the keyword or target (with setWidgetForKeyword()). If no such widget is specified explicitly, it will select the contents of the widget that has the keyword or target as its message target.

| **Argument** | **Type** | **Default** | **Description** |
| tupleKwd | FXObject |   | Object that contains invalid element. |
| index | Int |   | Element index. |

### processUpdates()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Performs state processing during the GUI update cycles. This class provides an empty implementation of this method, and the derived class should redefine the method if it needs to process state updating.

###   
Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

### 

**Message ID's.**

| **ID\_UPDATE\_STATE** | 

Used to update the state.

 |

###   
Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

### 

**Flags for data dialog box options.**

| **DATADIALOG_BAILOUT** | 

Perform bailout checks when the Cancel button is clicked.

 |

By clicking on Send, you accept that Dassault Systèmes will process your personal data and may contact you for further information.

[Privacy Policy](https://www.3ds.com/privacy-policy).

Total Results:

Results per page

This page cannot be found.

The page might not exist or is temporarily unavailable. Try again or try searching for the topic.