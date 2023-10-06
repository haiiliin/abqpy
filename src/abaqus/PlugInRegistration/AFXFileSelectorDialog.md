Abaqus

GUI Toolkit Reference

All Classes

AFXFileSelectorDialog

This class extends the FXFileDialog class and is designed to work with the mode infrastructure.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxfileselectordialog.png)

### AFXFileSelectorDialog(form, title, pathNameKw, readOnlyKw, mode=AFXSELECTFILE_ANY, patterns=*, patternIndexTgt=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor typically used to create a dialog box that is posted by a mode (e.g. by getFirstDialog); a keyword is used for the pathName. If the dialog box allows multiple selection, the pathName keyword contains comma-separated path names of all selected files.

| **Argument** | **Type** | **Default** | **Description** |
| form | AFXForm |   | Form. |
| title | String |   | Dialog box title. |
| pathNameKw | AFXStringKeyword |   | Path name keyword. |
| readOnlyKw | AFXBoolKeyword |   | Read-only keyword. |
| mode | Int | AFXSELECTFILE_ANY | File selection mode. |
| patterns | String | * | File filter patterns. |
| patternIndexTgt | AFXIntTarget | None | Index used to select a file filter pattern when the dialog box is posted. |

### AFXFileSelectorDialog(owner, title, pathNameKw, readOnlyKw, mode=AFXSELECTFILE_ANY, patterns=*, patternIndexTgt=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor typically used to create a dialog box that is posted from another dialog box (e.g. from a "Select..." button); a keyword is used for the pathName. If the dialog box allows multiple selection, the pathName keyword contains comma-separated path names of all selected files.

| **Argument** | **Type** | **Default** | **Description** |
| owner | FXWindow |   | Owner |
| title | String |   | Dialog box title. |
| pathNameKw | AFXStringKeyword |   | Path name keyword. |
| readOnlyKw | AFXBoolKeyword |   | Read-only keyword. |
| mode | Int | AFXSELECTFILE_ANY | File selection mode. |
| patterns | String | * | File filter patterns. |
| patternIndexTgt | AFXIntTarget | None | Index used to select a file filter pattern when the dialog box is posted. |

### AFXFileSelectorDialog(form, title, pathNameTgt, readOnlyKw, mode=AFXSELECTFILE_ANY, patterns=*, patternIndexTgt=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor typically used to create a dialog box that is posted by a mode (e.g. by getFirstDialog); a target is used for the pathName. If the dialog box allows multiple selection, the pathName target contains comma-separated path names of all selected files.

| **Argument** | **Type** | **Default** | **Description** |
| form | AFXForm |   | Form. |
| title | String |   | Dialog box title. |
| pathNameTgt | AFXStringTarget |   | Path name target. |
| readOnlyKw | AFXBoolKeyword |   | Read-only keyword. |
| mode | Int | AFXSELECTFILE_ANY | File selection mode. |
| patterns | String | * | File filter patterns. |
| patternIndexTgt | AFXIntTarget | None | Index used to select a file filter pattern when the dialog box is posted. |

### AFXFileSelectorDialog(owner, title, pathNameTgt, readOnlyKw, mode=AFXSELECTFILE_ANY, patterns=*, patternIndexTgt=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor typically used to create a dialog box that is posted from another dialog box (e.g. from a "Select..." button); a target is used for the pathName. If the dialog box allows multiple selection, the pathName target contains comma-separated path names of all selected files.

| **Argument** | **Type** | **Default** | **Description** |
| owner | FXWindow |   | Owner |
| title | String |   | Dialog box title. |
| pathNameTgt | AFXStringTarget |   | Path name target. |
| readOnlyKw | AFXBoolKeyword |   | Read-only keyword. |
| mode | Int | AFXSELECTFILE_ANY | File selection mode. |
| patterns | String | * | File filter patterns. |
| patternIndexTgt | AFXIntTarget | None | Index used to select a file filter pattern when the dialog box is posted. |

### Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**File selection modes**

| **AFXSELECTFILE_ANY** | 

A single file, existing or not (to save to).

 |
| **AFXSELECTFILE_EXISTING** | 

An existing file (to load).

 |
| **AFXSELECTFILE_MULTIPLE** | 

Multiple existing files.

 |
| **AFXSELECTFILE\_MULTIPLE\_ALL** | 

Multiple existing files or directories.

 |
| **AFXSELECTFILE_DIRECTORY** | 

Existing directory.

 |
| **AFXSELECTFILE\_REMOTE\_HOST** | 

Enable opening files on a remote host.

