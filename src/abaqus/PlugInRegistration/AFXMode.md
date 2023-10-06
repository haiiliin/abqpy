Abaqus

GUI Toolkit Reference

All Classes

AFXMode

This class is the base class for modes.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxmode.png)

### AFXMode()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

### getCommand(index)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the command at the given index (returns 0 if the index is out-of-bounds).

| **Argument** | **Type** | **Default** | **Description** |
| index | Int |   | Command index (0-based). |

### getNumCommands()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of commands associated with the mode.

### isActive()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the mode is active.

### Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Message ID's.**

| **ID_ACTIVATE** | 

Activates the mode.

 |
| **ID_COMMIT** | 

Commits the mode.

 |
| **ID_CANCEL** | 

Cancels the mode.

 |
| **ID_DEACTIVATE** | 

Deactivates the mode.

 |
| **ID\_GET\_NEXT** | 

Gets the next step/dialog box.

 |
| **ID_RESUME** | 

Resumes the mode.

 |
| **ID\_SET\_DEFAULTS** | 

Sets defaults.

 |
| **ID_SUSPEND** | 

Suspends the mode.

 |
| **ID\_CMD\_ACTIVATED** | 

Indicates that a command is activated.

 |
| **ID\_CMD\_DEACTIVATED** | 

Indicates that a command is deactivated.

 |
| **ID\_CMD\_MODIFIED** | 

Indicates that a command is modified.

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

Thank you for your comments. We will contact you if we have questions regarding your feedback.

Sincerely,  
The Dassault Systèmes User Assistance Team

Dialog for Cookie

Allow to use Cookie for saving your settings ?