Abaqus

GUI Toolkit Reference

All Classes

AFXColumnItems

This class connects the selected items in a single column of an AFXTable to a keyword (typically a tuple keyword).

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxcolumnitems.png)

### AFXColumnItems(table, referenceColumn, opts=0)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| table | AFXTable | | Table to use. |
| referenceColumn | Int | | Index of the reference column. |
| opts | Int | 0 | Selection options (not used). |

### AFXColumnItems(referenceColumn, tgt=None, sel=0, opts=0)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor for use with a keyword.

| **Argument** | **Type** | **Default** | **Description** |
| referenceColumn | Int | | Index of the reference column. |
| tgt | FXObject | None | Message target. |
| sel | Int | 0 | Message ID. |
| opts | Int | 0 | Selection options (not used). |

### getReferenceColumn()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the index of the table reference column.

### getSelector()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the message ID.

### getTarget()

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the message target.

### setReferenceColumn(index)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the table reference column, whose selected items will be sent to the target.

| **Argument** | **Type** | **Default** | **Description** |
| index | Int | | Table column index. |

### setSelector(sel)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the message ID.

| **Argument** | **Type** | **Default** | **Description** |
| sel | Int | | New message ID. |

### setTarget(tgt)

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the message target.

| **Argument** | **Type** | **Default** | **Description** |
| tgt | FXObject | | New message target. |

### Class flags

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

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
