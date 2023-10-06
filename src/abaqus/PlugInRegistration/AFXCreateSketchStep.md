This class is used to provide pick steps in GUI procedures.

![](../SIMACAERefImages/gui-afxcreatesketchstep.png)

### AFXCreateSketchStep

###

### AFXCreateSketchStep(owner, keyword, sheetSize, prompt='Create a sketch')

![](../IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| owner | AFXProcedure | | Procedure creating the step. |
| keyword | AFXObjectKeyword | | Object kwd containing pick variable. Part of AFXGuiCommand. |
| sheetSize | float | | Sketch sheet size when creating. |
| prompt | String | 'Create a sketch' | Step's prompt displayed in prompt area. |

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
