Abaqus

GUI Toolkit Reference

All Classes

AFXForm

This class is the abstract base class for forms.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxform.png)

### AFXForm(owner)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| owner | AFXGuiObjectManager | | Owner (a module or a toolset) of the form. |

### activate()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Performs the necessary tasks when the form is activated.

Reimplemented from AFXGuiMode.

### cancel(tgt=None, msg=0)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Requests a cancellation of the form. When the cancel operation completes, successfully or not, the target will be sent the given message. The message data pointer will be non-zero for successful cancellation and zero if the cancel operation was abandoned for some purpose.

| **Argument** | **Type** | **Default** | **Description** |
| tgt | FXObject | None | Completion message target. |
| msg | Int | 0 | Completion message ID. |

### commit()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Performs the necessary tasks when the form is committed.

Implements AFXGuiMode.

### continueMode()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Used to get the next dialog box in the mode.

Implements AFXGuiMode.

### deactivateIfNeeded()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Deactivates the form if the user pressed the OK button of the currently posted dialog box. This method is called after the commands are processed successfully.

### getFirstDialog()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the first dialog box to be posted.

### getNextDialog(previousDialog)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the next dialog box to be posted.

| **Argument** | **Type** | **Default** | **Description** |
| previousDialog | AFXDialog | | Previous dialog box. |

### issueCommands(writeToReplay=True, writeToJournal=False)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Generates commands based on the current state, sends the commands, and deactivates the form if necessary. If the commands did not complete successfully, a dialog box will be posted with an error message.

| **Argument** | **Type** | **Default** | **Description** |
| writeToReplay | Bool | True | True if commands should be written to the replay file; False if not. |
| writeToJournal | Bool | False | True if commands should be written to the journal file; False if not. |

### setModal(postModalDialogs)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the modal state; if True, dialogs will be posted as modal. By default the form posts dialogs as non-modal.

| **Argument** | **Type** | **Default** | **Description** |
| postModalDialogs | Bool | | True if the form should post dialogs as modal. |

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

-

I acknowledge I have read and I hereby accept the [privacy policy](https://www.3ds.com/privacy-policy) under which my personal data will be used by Dassault Systèmes.
