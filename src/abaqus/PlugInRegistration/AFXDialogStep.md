This class provides dialog steps in GUI procedures.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxdialogstep.png)

### AFXDialogStep(owner, dialog, prompt)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor that takes a prompt for the prompt area.

| **Argument** | **Type** | **Default** | **Description** |
| owner | AFXProcedure |   | Procedure creating the step. |
| dialog | AFXDataDialog |   | Dialog box to be posted in this step. |
| prompt | String |   |   |

### AFXDialogStep(owner, dialog)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor that supplies a default prompt for the prompt area.

| **Argument** | **Type** | **Default** | **Description** |
| owner | AFXProcedure |   | Procedure creating the step. |
| dialog | AFXDataDialog |   | Dialog box to be posted in this step. |

### onCancel()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Called when the step is cancelled.

Reimplemented from AFXStep.

### onExecute()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Called to execute steps returned by getFirstStep and getNextStep.

Reimplemented from AFXStep.

### onResume()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Called when the step is resumed.

Reimplemented from AFXStep.

### onSuspend()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Called when the step is suspended.

Reimplemented from AFXStep.

By clicking on Send, you accept that Dassault Systèmes will process your personal data and may contact you for further information.

[Privacy Policy](https://www.3ds.com/privacy-policy).

Total Results:

Results per page

This page cannot be found.

The page might not exist or is temporarily unavailable. Try again or try searching for the topic.