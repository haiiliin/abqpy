This class contains a progress bar, which can present work-in-progress in a number of different styles.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxprogressbar.png)

### AFXProgressBar(p, tgt=None, sel=0, opts=FRAME\_SUNKEN| FRAME\_THICK, x=0, y=0, w=0, h=0, pl=DEFAULT\_PAD, pr=DEFAULT\_PAD, pt=DEFAULT\_PAD, pb=DEFAULT\_PAD)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   | Parent widget. |
| tgt | FXObject | None | Message target. |
| sel | Int | 0 | Message ID. |
| opts | Int | FRAME\_SUNKEN| FRAME\_THICK | Options and hints. |
| x | Int | 0 | X coordinate of origin. |
| y | Int | 0 | Y coordinate of origin. |
| w | Int | 0 | Width of the widget. |
| h | Int | 0 | Height of the widget. |
| pl | Int | DEFAULT_PAD | Left padding (margin). |
| pr | Int | DEFAULT_PAD | Right padding (margin). |
| pt | Int | DEFAULT_PAD | Top padding (margin). |
| pb | Int | DEFAULT_PAD | Bottom padding (margin). |

### create()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Creates the progress bar.

Reimplemented from FXProgressBar.

### getBarStyle()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the progress bar style.

Reimplemented from FXProgressBar.

### getDefaultHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default height.

Reimplemented from FXProgressBar.

### getDefaultWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the default width.

Reimplemented from FXProgressBar.

### getNumCursorBoxes()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the number of cursor boxes displayed.

### getProgress()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the current progress amount.

Reimplemented from FXProgressBar.

### getTotal()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the total progress amount.

Reimplemented from FXProgressBar.

### hide()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Hides the progress bar.

Reimplemented from FXWindow.

### hideNumber()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Hides the progress bar iteration or percentage text.

Reimplemented from FXProgressBar.

### setBarStyle(style)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the progress bar style.

| **Argument** | **Type** | **Default** | **Description** |
| style | Int |   | Style flag. |

### setNumCursorBoxes(nb)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the number of cursor boxes to display.

| **Argument** | **Type** | **Default** | **Description** |
| nb | Int |   | Number of boxes. |

### setProgress(value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the current progress amount that is used by a progress bar in either iteration or percentage mode; the progress amount is ingored by a progress bar in scanner mode.

Reimplemented from FXProgressBar.

| **Argument** | **Type** | **Default** | **Description** |
| value | Int |   |   |

### setTotal(value)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the total progress amount that is used by a progress bar in either iteration or percentage mode; the progress amount is ingored by a progress bar in scanner mode.

Reimplemented from FXProgressBar.

| **Argument** | **Type** | **Default** | **Description** |
| value | Int |   |   |

### show()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Shows the progress bar.

Reimplemented from FXWindow.

### showNumber(style=AFXPROGRESSBAR_PERCENTAGE)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Shows the progress iteration or percentage text.

| **Argument** | **Type** | **Default** | **Description** |
| style | Int | AFXPROGRESSBAR_PERCENTAGE | Style flag. |

### Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

### Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Flags for progress bar styles.**

| **AFXPROGRESSBAR_PERCENTAGE** | 

Percentage complete mode.

 |
| **AFXPROGRESSBAR_HORIZONTAL** | 

Horizontal display.

 |
| **AFXPROGRESSBAR_VERTICAL** | 

Vertical display.

 |
| **AFXPROGRESSBAR_SCANNER** | 

Scanner mode.

 |
| **AFXPROGRESSBAR_ITERATOR** | 

Iterator mode.

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