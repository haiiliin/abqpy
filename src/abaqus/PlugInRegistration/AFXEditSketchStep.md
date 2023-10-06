This class is used to provide pick steps in GUI procedures.

![](../SIMACAERefImages/gui-afxeditsketchstep.png)

### AFXEditSketchStep

###   

### AFXEditSketchStep(owner, sketchName, prompt='Edit a sketch')  
![](../IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| owner | AFXProcedure |   | Procedure creating the step. |
| sketchName | String |   | Name of sketch to edit, blank if create. |
| prompt | String | 'Edit a sketch' | Step's prompt displayed in prompt area. |

### onCancel

###   

### onCancel()  
![](../IconsReference/butix_top_wline.png)

Called when the step is cancelled.

Reimplemented from AFXStep.

### onExecute

###   

### onExecute()  
![](../IconsReference/butix_top_wline.png)

Called to execute the steps returned by getFirstStep and getNextStep.

Reimplemented from AFXStep.

### onResume

###   

### onResume()  
![](../IconsReference/butix_top_wline.png)

Called when the step is resumed.

Reimplemented from AFXStep.

### onSuspend

###   

### onSuspend()  
![](../IconsReference/butix_top_wline.png)

Called when the step is suspended.

Reimplemented from AFXStep.



 |