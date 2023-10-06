DialogBox window. When receiving ID\_CANCEL or ID\_ACCEPT, the DialogBox breaks out of the modal loop and returns False or True, respectively. To close the DialogBox when not running modally, simply send it ID_HIDE.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fxdialogbox.png)

### FXDialogBox(a, name, opts=DECOR\_TITLE| DECOR\_BORDER, x=0, y=0, w=0, h=0, pl=10, pr=10, pt=10, pb=10, hs=4, vs=4)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Construct free-floating dialog.

| **Argument** | **Type** | **Default** | **Description** |
| a | FXApp |   |   |
| name | String |   |   |
| opts | Int | DECOR\_TITLE| DECOR\_BORDER |   |
| x | Int | 0 |   |
| y | Int | 0 |   |
| w | Int | 0 |   |
| h | Int | 0 |   |
| pl | Int | 10 |   |
| pr | Int | 10 |   |
| pt | Int | 10 |   |
| pb | Int | 10 |   |
| hs | Int | 4 |   |
| vs | Int | 4 |   |

### FXDialogBox(owner, name, opts=DECOR\_TITLE| DECOR\_BORDER, x=0, y=0, w=0, h=0, pl=10, pr=10, pt=10, pb=10, hs=4, vs=4)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Construct dialog which will always float over the owner window.

| **Argument** | **Type** | **Default** | **Description** |
| owner | FXWindow |   |   |
| name | String |   |   |
| opts | Int | DECOR\_TITLE| DECOR\_BORDER |   |
| x | Int | 0 |   |
| y | Int | 0 |   |
| w | Int | 0 |   |
| h | Int | 0 |   |
| pl | Int | 10 |   |
| pr | Int | 10 |   |
| pt | Int | 10 |   |
| pb | Int | 10 |   |
| hs | Int | 4 |   |
| vs | Int | 4 |   |

### execute(placement=PLACEMENT_CURSOR)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Run modal invocation of the dialog.

Reimplemented in FXInputDialog, and FXReplaceDialog.

| **Argument** | **Type** | **Default** | **Description** |
| placement | Int | PLACEMENT_CURSOR |   |

### Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


| **ID_CANCEL** | 

Closes the dialog, cancel the entry.

 |
| **ID_ACCEPT** | 

Closes the dialog, accept the entry.

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