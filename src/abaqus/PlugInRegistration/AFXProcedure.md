This class provides the basis for writing procedures.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxprocedure.png)

### AFXProcedure(owner, type=NORMAL)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| owner | AFXGuiObjectManager |   | Owner (a module or a toolset) of the procedure. |
| type | typeEnum | NORMAL |   |

### activate()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Activates the mode.

Reimplemented from AFXGuiMode.

### cancel(tgt=None, msg=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Tries to cancel the procedure depending on checkCancel results.

| **Argument** | **Type** | **Default** | **Description** |
| tgt | FXObject | None | Completion message target. |
| msg | Int | 0 | Completion message ID. |

### checkBackup()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns 1 if ok to backup else returns 0.

### checkCancel()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns BAILOUT\_NOTOK, BAILOUT\_OK, BAILOUT\_WIP (writes to the message area), or BAILOUT\_SAVE (use the 3 button save dialog box).

### commit()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Commits the procedure when the current dialog box calls either done or value changed.

Implements AFXGuiMode.

### continueMode()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Used to get the next step in the mode.

Implements AFXGuiMode.

### deactivate()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

deactivates the mode.

Reimplemented from AFXGuiMode.

### getCurrentStep()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the current step.

### getFirstStep()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the first step to be executed in the procedure.

### getLoopStep()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the step to which the procedure should loop back after processing its commands; if zero is returned (the default behavior) the procedure will not loop.

### getNextStep(previousStep)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the next step to be executed; if zero is returned the procedure will process its commands.

| **Argument** | **Type** | **Default** | **Description** |
| previousStep | AFXStep |   | Previous step. |

### getNumSteps()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of steps in the step stack.

### handleException(exc)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

This method is called if an error occurs while issuing commands. It can be reimplemented in derived classes to perform special error handling.

| **Argument** | **Type** | **Default** | **Description** |
| exc | nex_Exception |   | Exception. |

### onBackup()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Called when a procedure backs up a step.

### onCancel()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Called when a procedure cancels.

### onCmdBackup(sender, sel, ptr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Message handler for handling backup button activation.

| **Argument** | **Type** | **Default** | **Description** |
| sender | FXObject |   | Sender. |
| sel | Int |   | Selector. |
| ptr | String |   | Data. |

### onCmdHandle2BtnBailout(sender, sel, ptr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Message handler for handling the user 2 button bailout choice.

| **Argument** | **Type** | **Default** | **Description** |
| sender | FXObject |   | Sender. |
| sel | Int |   | Selector. |
| ptr | String |   | Data. |

### onCmdHandleBailout(sender, sel, ptr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Message handler for handling the user 3 button bailout choice.

| **Argument** | **Type** | **Default** | **Description** |
| sender | FXObject |   | Sender. |
| sel | Int |   | Selector. |
| ptr | String |   | Data. |

### onResume()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Called when a procedure resumes.

### onSuspend()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Called when a procedure suspends.

### onValueChanged()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Called when a procedure's step changes in value.

### setCurrentDb(db)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the current dialog box of the mode. Procedures will have this set by AFXDialogStep.

| **Argument** | **Type** | **Default** | **Description** |
| db | AFXDialog |   | Dialog box. |

### setSelectionOptions(pickDepth=CLOSEST, pickScope=ALL, dragShape=RECTANGLE, dragScope=INSIDE_CROSSING, isoLines=True)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the selection options to be used for picking.

| **Argument** | **Type** | **Default** | **Description** |
| pickDepth | pickDepthEnum | CLOSEST | Depth into the screen of picking. |
| pickScope | pickScopeEnum | ALL | Entity type. |
| dragShape | dragShapeEnum | RECTANGLE | Drag-window shape. |
| dragScope | dragScopeEnum | INSIDE_CROSSING | Drag-window scope. |
| isoLines | Bool | True | If True, show isolines on surfaces. |

### verifyCurrentKeywordValues()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Checks whether keywords of active commands for the current dialog box contain valid data and, if not, posts a dialog box with an error message.

Reimplemented from AFXGuiMode.

### Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Message ID's.**

| **ID\_HANDLE\_2BTN_BAILOUT** | 

ID for handling bailout.

 |
| **ID_BACKUP** | 

ID for the backup button.

 |


**Flags for the drag scope.**

| **INSIDE** | 

Pick entities inside the drag shape only.

 |
| **INSIDE_CROSSING** | 

Pick entities inside and crossing the drag shape.

 |
| **CROSSING** | 

Pick entities crossing the drag shape only.

 |
| **OUTSIDE_CROSSING** | 

Pick entities outside and crossing the drag shape.

 |
| **OUTSIDE** | 

Pick entities outside the drag shape only.

 |


**Flags for the drag shape.**

| **RECTANGLE** | 

Use rectangular drag shape.

 |
| **CIRCLE** | 

Use circular drag shape.

 |
| **POLYGON** | 

Use polygonal drag shape.

 |


**Flags for the pick depth.**

| **CLOSEST** | 

Only pick the entity closest to the screen.

 |
| **INFINITE** | 

Pick entities at any depth.

 |


**Flags for the pick scope.**

| **INTERIOR** | 

Pick only interior entities.

 |
| **EXTERIOR** | 

Pick only exterior entities.

 |
| **ALL** | 

Pick all entities.

 |


**Flags for the activate action.**

| **NORMAL** | 

Cancel the currently running procedure (default).

 |
| **SUBPROCEDURE** | 

Suspend the currently running procedure.

 |