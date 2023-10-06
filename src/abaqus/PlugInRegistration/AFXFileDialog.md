AFXFileDialog

This class contains a file selection dialog box.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxfiledialog.png)

### AFXFileDialog(owner, title, pathNameKw, readOnlyKw, tgt=None, sel=0, mode=AFXSELECTFILE_ANY, patterns=*, patternIndexTgt=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor that creates a dialog box that always occludes its owner widget when overlapping with the widget. The constructor expects a string keyword for storing the selected file name. If the dialog box allows multiple selection, the string keyword contains comma-separated path names of all selected files.

| **Argument** | **Type** | **Default** | **Description** |
| owner | FXWindow |   | Parent widget. |
| title | String |   | Dialog title. |
| pathNameKw | AFXStringKeyword |   | Path name keyword. |
| readOnlyKw | AFXBoolKeyword |   | Read-only keyword. |
| tgt | FXObject | None | Message target. |
| sel | Int | 0 | Message ID. |
| mode | Int | AFXSELECTFILE_ANY | File selection mode. |
| patterns | String | * | File filter patterns. |
| patternIndexTgt | AFXIntTarget | None | Index used to select a file filter pattern when the dialog box is posted. |

### AFXFileDialog(title, pathNameKw, readOnlyKw, tgt=None, sel=0, mode=AFXSELECTFILE_ANY, patterns=*, patternIndexTgt=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor that creates a dialog box that always occludes the main window when overlapping with the main window. The constructor expects a string keyword for storing the selected file name. If the dialog box allows multiple selection, the string keyword contains comma-separated path names of all selected files.

| **Argument** | **Type** | **Default** | **Description** |
| title | String |   | Dialog title. |
| pathNameKw | AFXStringKeyword |   | Path name keyword. |
| readOnlyKw | AFXBoolKeyword |   | Read-only keyword. |
| tgt | FXObject | None | Message target. |
| sel | Int | 0 | Message ID. |
| mode | Int | AFXSELECTFILE_ANY | File selection mode. |
| patterns | String | * | File filter patterns. |
| patternIndexTgt | AFXIntTarget | None | Index used to select a file filter pattern when the dialog box is posted. |

### AFXFileDialog(owner, title, pathNameTgt, readOnlyKw, tgt=None, sel=0, mode=AFXSELECTFILE_ANY, patterns=*, patternIndexTgt=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor that creates a dialog box that always occludes its owner widget when overlapping with the widget. The constructor expects a string target for storing the selected file name. If the dialog box allows multiple selection, the string target contains comma-separated path names of all selected files.

| **Argument** | **Type** | **Default** | **Description** |
| owner | FXWindow |   | Parent widget. |
| title | String |   | Dialog title. |
| pathNameTgt | AFXStringTarget |   | Path name target. |
| readOnlyKw | AFXBoolKeyword |   | Read-only keyword. |
| tgt | FXObject | None | Message target. |
| sel | Int | 0 | Message ID. |
| mode | Int | AFXSELECTFILE_ANY | File selection mode. |
| patterns | String | * | File filter patterns. |
| patternIndexTgt | AFXIntTarget | None | Index used to select a file filter pattern when the dialog box is posted. |

### AFXFileDialog(title, pathNameTgt, readOnlyKw, tgt=None, sel=0, mode=AFXSELECTFILE_ANY, patterns=*, patternIndexTgt=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor that creates a dialog box that always occludes the main window when overlapping with the main window. The constructor expects a string target for storing the selected file name. If the dialog box allows multiple selection, the string target contains comma-separated path names of all selected files.

| **Argument** | **Type** | **Default** | **Description** |
| title | String |   | Dialog title. |
| pathNameTgt | AFXStringTarget |   | Path name target. |
| readOnlyKw | AFXBoolKeyword |   | Read-only keyword. |
| tgt | FXObject | None | Message target. |
| sel | Int | 0 | Message ID. |
| mode | Int | AFXSELECTFILE_ANY | File selection mode. |
| patterns | String | * | File filter patterns. |
| patternIndexTgt | AFXIntTarget | None | Index used to select a file filter pattern when the dialog box is posted. |

### getCurrentPattern()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the current pattern number.

### getDirectory()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the current directory.

### getFileBoxStyle()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return file list style.

### getFilename()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the file name.

### getFilenames()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns an empty-string terminated list of selected file names, or 0 if none is selected.

### getItemSpace()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the inter-item spacing (in pixels).

### getPattern()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the file pattern.

### getPatternList()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the list of patterns.

### getPatternText(patno)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the pattern text for a given pattern number.

| **Argument** | **Type** | **Default** | **Description** |
| patno | Int |   |   |

### getPressedButtonId()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the ID of the button that the user pressed in the dialog box.

### getReadOnly()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the read-only state.

### getReadOnlyPatterns()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the patterns that force the enabling of the read-only button.

### getSelectMode()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the file selection mode.

### setCurrentPattern(n)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the current active pattern.

| **Argument** | **Type** | **Default** | **Description** |
| n | Int |   |   |

### setDirectory(path)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the current directory.

| **Argument** | **Type** | **Default** | **Description** |
| path | String |   |   |

### setFileBoxStyle(style)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the file list style.

| **Argument** | **Type** | **Default** | **Description** |
| style | Int |   |   |

### setFilename(path)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the file name.

| **Argument** | **Type** | **Default** | **Description** |
| path | String |   |   |

### setItemSpace(s)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the inter-item spacing (in pixels).

| **Argument** | **Type** | **Default** | **Description** |
| s | Int |   |   |

### setPattern(ptrn)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the file pattern.

| **Argument** | **Type** | **Default** | **Description** |
| ptrn | String |   |   |

### setPatternList(patterns)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the list of file patterns.

| **Argument** | **Type** | **Default** | **Description** |
| patterns | String |   |   |

### setPatternListMaxVisible(maxVisible)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the maximum number of visible items for the file pattern list.

| **Argument** | **Type** | **Default** | **Description** |
| maxVisible | Int |   |   |

### setPatternText(patno, text)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the pattern text for a pattern number.

| **Argument** | **Type** | **Default** | **Description** |
| patno | Int |   |   |
| text | String |   |   |

### setReadOnly(state)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the initial state of read-only button.

| **Argument** | **Type** | **Default** | **Description** |
| state | Bool |   |   |

### setReadOnlyPatterns(patterns)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the patterns that force the display of the read-only button; separate the entries by a newline character

.

| **Argument** | **Type** | **Default** | **Description** |
| patterns | String |   |   |

### setSelectMode(mode)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Sets the file selection mode.

| **Argument** | **Type** | **Default** | **Description** |
| mode | Int |   |   |

### show()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Posts the dialog box.

Reimplemented from AFXDialog.

### showModal(occludedWindow=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Posts the dialog box as a modal dialog box. The dialog box is centered against the given widget or its owner widget if 0 is given.

| **Argument** | **Type** | **Default** | **Description** |
| occludedWindow | FXWindow | None | Widget to be occluded (0 for the owner widget). |

### shownReadOnly()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the read-only button is shown.

### showReadOnly(show)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Shows the read-only button.

| **Argument** | **Type** | **Default** | **Description** |
| show | Bool |   |   |
