Splitter window is used to interactively repartition two or more subpanes. Space may be subdivided horizontally or vertically. When the splitter is itself resized, the right-most (bottom-most) child window will be resized unless the splitter window is reversed; if the splitter is reversed, the left-most (top-most) child window will be resized instead. The splitter widget sends a SEL\_CHANGED to its target during the resizing of the panes; at the end of the resize interaction, it sends a SEL\_COMMAND to signify that the resize operation is complete. Normally, children are resizable from 0 upwards; however, if the child in a horizontally oriented splitter has LAYOUT\_FILL\_X in combination with LAYOUT\_FIX\_WIDTH, it will not be made smaller than its default width, except when the child is the last visible widget (or first when the option SPLITTER\_REVERSED has been passed to the splitter). In a vertically oriented splitter, children with LAYOUT\_FILL\_Y and LAYOUT\_FIX_HEIGHT behave analogously. These options only affect interactive resizing.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fxsplitter.png)

### FXSplitter(p, opts=SPLITTER_NORMAL, x=0, y=0, w=0, h=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Construct new splitter widget.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   |   |
| opts | Int | SPLITTER_NORMAL |   |
| x | Int | 0 |   |
| y | Int | 0 |   |
| w | Int | 0 |   |
| h | Int | 0 |   |

### FXSplitter(p, tgt, sel, opts=SPLITTER_NORMAL, x=0, y=0, w=0, h=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Construct new splitter widget, which will notify target about size changes.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   |   |
| tgt | FXObject |   |   |
| sel | Int |   |   |
| opts | Int | SPLITTER_NORMAL |   |
| x | Int | 0 |   |
| y | Int | 0 |   |
| w | Int | 0 |   |
| h | Int | 0 |   |

### getDefaultHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get default height.

Reimplemented from FXComposite.

### getDefaultWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get default width.

Reimplemented from FXComposite.

### getSplitterStyle()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return current splitter style.

### setSplitterStyle(style)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change splitter style.

| **Argument** | **Type** | **Default** | **Description** |
| style | Int |   |   |

### Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Splitter options**

| **SPLITTER_HORIZONTAL** | 

Split horizontally.

 |
| **SPLITTER_VERTICAL** | 

Split vertically.

 |
| **SPLITTER_REVERSED** | 

Reverse-anchored.

 |
| **SPLITTER_TRACKING** | 

Track continuous during split.

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