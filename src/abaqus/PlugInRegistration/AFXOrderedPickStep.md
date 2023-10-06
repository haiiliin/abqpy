| 

This class is used to provide pick steps in GUI procedures.

![](../SIMACAERefImages/gui-afxorderedpickstep.png)

### AFXOrderedPickStep

###   

### AFXOrderedPickStep(owner, keyword, prompt, entitiesToPick, highlightLevel=1)  
![](../IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| owner | AFXProcedure |   | Procedure creating the step. |
| keyword | AFXObjectKeyword |   | Object kwd containing pick variable. Part of AFXGuiCommand. |
| prompt | String |   | Step's prompt displayed in prompt area. |
| entitiesToPick | Int |   | Type of entities to pick. |
| highlightLevel | Int | 1 | Highlight level. |

### onCancel

###   

### onCancel()  
![](../IconsReference/butix_top_wline.png)

Called when the step is cancelled.

Reimplemented from AFXPickStep.

### onExecute

###   

### onExecute()  
![](../IconsReference/butix_top_wline.png)

Called to execute the steps returned by getFirstStep and getNextStep.

Reimplemented from AFXPickStep.

### reset

###   

### reset()  
![](../IconsReference/butix_top_wline.png)

Allows a step to reset any of its data (if needed) when looping.

Reimplemented from AFXPickStep.



 |