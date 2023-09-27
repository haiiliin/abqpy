Application Object

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fxapp.png)

### FXApp(name=Application, vendor=FoxDefault)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Copyright notice of library.

Construct application object; the name and vendor strings are used as keys into the registry database for this application's settings

| **Argument** | **Type** | **Default** | **Description** |
| name | String | Application |   |
| vendor | String | FoxDefault |   |

### addChore(tgt, sel)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Add a idle processing message to be sent to target object when the system becomes idle, i.e. there are no events to be processed.

| **Argument** | **Type** | **Default** | **Description** |
| tgt | FXObject |   |   |
| sel | Int |   |   |

### addInput(fd, mode, tgt, sel)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Add a file descriptor fd to be watched for activity as determined by mode, where mode is a bitwise OR (INPUT\_READ, INPUT\_WRITE, INPUT\_EXCEPT). A message of type SEL\_IO\_READ, SEL\_IO\_WRITE, or SEL\_IO_EXCEPT will be sent to the target when the specified activity is detected on the file descriptor.

On Windows, a Win32 event, not a file descriptor, must be specified. The client code for this interface must be platform-dependent. See addSocket below for a portable interface. CAE

| **Argument** | **Type** | **Default** | **Description** |
| fd | FXInputHandle |   |   |
| mode | Int |   |   |
| tgt | FXObject |   |   |
| sel | Int |   |   |

### addSocket(sd, mode, tgt, sel)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

CAE Add a socket descriptor sd to be watched for activity as determined by mode, where mode is a bitwise OR (INPUT\_READ, INPUT\_WRITE, INPUT\_EXCEPT). A message of type SEL\_IO\_READ, SEL\_IO\_WRITE, or SEL\_IO_EXCEPT will be sent to the target when the specified activity is detected on the socket descriptor.

This is identical to addInput on Unix. It behaves the same on Windows.

| **Argument** | **Type** | **Default** | **Description** |
| sd | SOCKET |   |   |
| mode | Int |   |   |
| tgt | FXObject |   |   |
| sel | Int |   |   |

### addTimeout(ms, tgt, sel)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Add timeout message to be sent to target object in ms milliseconds; the timer fires only once after the interval expires.

| **Argument** | **Type** | **Default** | **Description** |
| ms | Int |   |   |
| tgt | FXObject |   |   |
| sel | Int |   |   |

### beep()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Beep.

### beginWaitCursor()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Begin of wait-cursor block; wait-cursor blocks may be nested.

### create()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Create application's windows.

Reimplemented in AFXApp.

### endWaitCursor()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

End of wait-cursor block.

### forceRefresh()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Force GUI refresh.

### getAppName()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get application name.

### getBorderColor()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Obtain default colors.

### getMainWindow()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get main window, if any.

### getMonoVisual()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get monochrome visual.

### getNormalFont()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default font.

### getRoot()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get root Window.

### getTypingSpeed()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Obtain application-wide settings.

### init(argc, argv, connect=True)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Initialize application. Parses and removes common command line arguments, reads the registry. Finally, if connect is True, it opens the display.

| **Argument** | **Type** | **Default** | **Description** |
| argc | Int |   |   |
| argv | String |   |   |
| connect | Bool | True |   |

### peekEvent()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Peek to determine if there's an event.

### refresh()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Schedule a refresh.

### removeChore(c)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Remove idle processing message.

| **Argument** | **Type** | **Default** | **Description** |
| c | FXChore |   |   |

### removeInput(fd, mode)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Remove input message and target object for the specified file descriptor and mode, which is a bitwise OR of (INPUT\_READ, INPUT\_WRITE, INPUT_EXCEPT).

| **Argument** | **Type** | **Default** | **Description** |
| fd | FXInputHandle |   |   |
| mode | Int |   |   |

### removeSocket(sd, mode)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

CAE Remove input message and target object for the specified socket descriptor and mode, which is a bitwise OR of (INPUT\_READ, INPUT\_WRITE, INPUT_EXCEPT).

| **Argument** | **Type** | **Default** | **Description** |
| sd | SOCKET |   |   |
| mode | Int |   |   |

### removeTimeout(t)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Remove timeout, returns NULL.

| **Argument** | **Type** | **Default** | **Description** |
| t | FXTimer |   |   |

### repaint()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Paint all windows marked for repainting. On return all the applications windows have been painted.

### run()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Run the main application event loop until stop() is called, and return the exit code passed as argument to stop().

Reimplemented in AFXApp.

### runOneEvent()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Perform one event dispatch.

### runUntil(condition)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Run an event loop till some flag becomes non-zero.

Reimplemented in AFXApp.

| **Argument** | **Type** | **Default** | **Description** |
| condition | Int |   |   |

### runWhileEvents(window=None)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Run event loop while there are events are available in the queue. Returns 1 when all events in the queue have been handled, and 0 when the event loop was terminated due to stop() or stopModal(). Except for the modal window and its children, user input to all windows is blocked; if the modal window is NULL all user input is blocked.

| **Argument** | **Type** | **Default** | **Description** |
| window | FXWindow | None |   |

### setBorderColor(color)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change default colors.

| **Argument** | **Type** | **Default** | **Description** |
| color | FXColor |   |   |

### setNormalFont(font)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change default font.

| **Argument** | **Type** | **Default** | **Description** |
| font | FXFont |   |   |

### setTypingSpeed(speed)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change application-wide settings.

| **Argument** | **Type** | **Default** | **Description** |
| speed | Int |   |   |

### stop(value=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Terminate the outermost event loop, and all inner modal loops; All more deeper nested event loops will be terminated with code equal to 0, while the outermost event loop will return code equal to value.

| **Argument** | **Type** | **Default** | **Description** |
| value | Int | 0 |   |

###   
Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

### 

**Messages applications understand.**

| **ID_QUIT** | 

Terminate the application normally.

 |
| **ID_DUMP** | 

Dump the current widget tree.

 |

###   
Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

### 

**File input modes for addInput**

| **INPUT_NONE** | 

Inactive.

 |
| **INPUT_READ** | 

Read input fd.

 |
| **INPUT_WRITE** | 

Write input fd.

 |
| **INPUT_EXCEPT** | 

Except input fd.

 |

### 

**All ways of being modal**

| **MODAL\_FOR\_NONE** | 

Non modal event loop (dispatch normally).

 |
| **MODAL\_FOR\_WINDOW** | 

Modal dialog (beep if outside of modal dialog).

 |
| **MODAL\_FOR\_POPUP** | 

Modal for popup (always dispatch to popup).

 |

### 

**Default cursors provided by the application**

| **DEF\_ARROW\_CURSOR** | 

Arrow cursor.

 |
| **DEF\_RARROW\_CURSOR** | 

Reverse arrow cursor.

 |
| **DEF\_TEXT\_CURSOR** | 

Text cursor.

 |
| **DEF\_HSPLIT\_CURSOR** | 

Horizontal split cursor.

 |
| **DEF\_VSPLIT\_CURSOR** | 

Vertical split cursor.

 |
| **DEF\_XSPLIT\_CURSOR** | 

Cross split cursor.

 |
| **DEF\_SWATCH\_CURSOR** | 

Color swatch drag cursor.

 |
| **DEF\_MOVE\_CURSOR** | 

Move cursor.

 |
| **DEF\_DRAGH\_CURSOR** | 

Resize horizontal edge.

 |
| **DEF\_DRAGV\_CURSOR** | 

Resize vertical edge.

 |
| **DEF\_DRAGTL\_CURSOR** | 

Resize upper-leftcorner.

 |
| **DEF\_DRAGBR\_CURSOR** | 

Resize bottom-right corner.

 |
| **DEF\_DRAGTR\_CURSOR** | 

Resize upper-right corner.

 |
| **DEF\_DRAGBL\_CURSOR** | 

Resize bottom-left corner.

 |
| **DEF\_DNDSTOP\_CURSOR** | 

Drag and drop stop.

 |
| **DEF\_DNDCOPY\_CURSOR** | 

Drag and drop copy.

 |
| **DEF\_DNDMOVE\_CURSOR** | 

Drag and drop move.

 |
| **DEF\_DNDLINK\_CURSOR** | 

Drag and drop link.

 |
| **DEF\_CROSSHAIR\_CURSOR** | 

Cross hair cursor.

 |
| **DEF\_CORNERNE\_CURSOR** | 

North-east cursor.

 |
| **DEF\_CORNERNW\_CURSOR** | 

North-west cursor.

 |
| **DEF\_CORNERSE\_CURSOR** | 

South-east cursor.

 |
| **DEF\_CORNERSW\_CURSOR** | 

South-west cursor.

 |
| **DEF\_ROTATE\_CURSOR** | 

Rotate cursor.

 |