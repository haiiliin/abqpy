This class is responsible for providing some high-level GUI control methods.

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-afxapp.png)

### AFXApp(appName=Abaqus/CAE, vendorName=SIMULIA, productName='', majorNumber=-1, minorNumber=-1, updateNumber=-1, prerelease=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Constructor.

| **Argument** | **Type** | **Default** | **Description** |
| appName | String | Abaqus/CAE | Application registry key. |
| vendorName | String | SIMULIA | Vendor registry key. |
| productName | String | '' | Product name. |
| majorNumber | Int | -1 | Version number. |
| minorNumber | Int | -1 | Release number. |
| updateNumber | Int | -1 | Update number. |
| prerelease | Bool | False | Official/Prerelease flag. |

### create()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Creates windows for the application.

Reimplemented from FXApp.

### getAFXMainWindow()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns a pointer to the AFXMainWindow.

### getBasePrerelease()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the base product is a prerelease.

### getBaseProductName()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the base product name.

### getBaseVersionNumbers(majorNumber, minorNumber, updateNumber)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the base product's major, minor, and update numbers.

| **Argument** | **Type** | **Default** | **Description** |
| majorNumber | Int |   | Version number. |
| minorNumber | Int |   | Release number. |
| updateNumber | Int |   | Update number. |

### getKernelInitializationCommand()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the command string that will be issued upon application startup.

### getPrerelease()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if this is a prerelease.

### getProductName()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the product name.

### getVersionNumbers()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns the major, minor, and update numbers.

### init(argc, argv)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Initializes the application and connects to the kernel.

| **Argument** | **Type** | **Default** | **Description** |
| argc | Int |   |   |
| argv | String |   |   |

### isLocked()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the GUI is locked or False if otherwise.

Reimplemented from FXApp.

### isProductCAE()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the base product is Abaqus/CAE.

### isProductViewer()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the base product is Abaqus/Viewer.

### isLearningEdition()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True if the base product is a learning edition.

### lock()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Locks the GUI (normally used during command and mode processing).

### run()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Runs the main application event loop until stop() is called,.

Reimplemented from FXApp.

### runUntil(condition)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Run an event loop till some flag becomes non-zero.

Reimplemented from FXApp.

| **Argument** | **Type** | **Default** | **Description** |
| condition | Int |   |   |

### unlock()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Unlocks the GUI.

### Class flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Message ID's.**

| **ID\_QUERY\_GUILOCK** | 

Used to query whether the GUI is locked.

 |
| **ID\_SHOW\_HOURGLASS** | 

Used to change the cursor.

 |