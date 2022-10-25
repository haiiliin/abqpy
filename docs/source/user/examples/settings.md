# Editing display preferences and GUI settings

You can use the Abaqus Scripting Interface to edit the abaqus_2021.gpr file, which includes settings that control many default display preferences and GUI settings in the Abaqus/CAE user interface. To enable editing of this file, you must import the caePrefsAccess module. This section describes the structure of the abaqus_2021.gpr file and provides an overview of customizing its settings; for more detailed information about the functions available in the caePrefsAccess module, see {doc}`/reference/kernel/cae_display_preferences`.

:::{warning}
Editing the `abaqus_2021.gpr` file is for experienced users only. Do not use the functions in the `caePrefsAccess` module unless you are comfortable with the Abaqus Scripting Interface and understand the structure of the `abaqus_2021.gpr` file. In addition, you should not have Abaqus/CAE running when you make changes to the graphical preferences file.
:::

You can retrieve the location of your `abaqus_2021.gpr` file using the `getGuiPrefsFileName` function. The file records default settings in two sections: display options reside in the `sessionOptions` section, and GUI settings reside in the `guiPreferences` section. Editing the options in one section does not have any effect on the options in the other section.

- **sessionOptions**

  The session options consist of the settings that you can save using the **File -> Save Display Options** menu option. In Abaqus/CAE you can save these options in the current directory or in your home directory.

  You can display and edit session options using the `openSessionOptions` function.

  ```python2
  > abaqus Python
  ...
  >>> import caePrefsAccess
  >>> sessionOptions = caePrefsAccess.openSessionOptions()
  >>> caePrefsAccess.printValuesList(sessionOptions)
  ...
  sessionOptions['session.animationOptions']\
      ['frameCounter']:[type:bool] True
  sessionOptions['session.animationOptions']\
      ['frameRate']:[type:int] 100
  sessionOptions['session.aviOptions']['compressionMethod']:\
      [type:SymbolicConstant] CODEC
  sessionOptions['session.aviOptions']['compressionQuality']:[type:int] 75
  ...
  ```

  The following statement changes the frame rate to 50. You should confirm that the data type you specify matches the type of the existing value.

  ```python2
  >>> sessionOptions['session.animationOptions']['frameRate'] = 50
  ```

  You can save the options you change to the original file by issuing the following command:

  ```python2
  >>> sessionOptions.save()
  ```

- **guiPreferences**

  The GUI preferences control many default behaviors in the Abaqus/CAE graphical interface, including size and location of the main window, size and location of the dialog boxes within Abaqus/CAE, and the number of recent files listed in the **Start Session** dialog box and in the **File** menu.

  Abaqus/CAE saves `guiPreferences` settings to your home directory when you exit the application. A separate `guiPreferences` record is stored in the preferences file for each display you use, so you must specify the **displayName** you want to modify when you open the `guiPreferences` settings. You can obtain a list of the available **displayName** settings by calling the `getDisplayNamesInGuiPreferences` function, and you can edit these settings by using the `openGuiPreferences` function and specifying the **displayName** of the settings that you want to modify.

  In the following example, the `openGuiPreferences` function is used to examine the **X** - and **Y** -location and the height and width of the following components of Abaqus/CAE:

  - **Select Font** dialog box
  - Abaqus/CAE main window
  - **Adaptivity Plotter** plug-in
  - **Amplitude Plotter** plug-in
  - **Create Weld** dialog box
  - **Copy Annotation** dialog box

  The sample statements follow:

  ```python2
  > abaqus Python
  ...
  >>> import caePrefsAccess
  >>> from caePrefsAccess import openGuiPreferences, CURRENT, HOME
  >>> from caePrefsAccess import getGuiPrefsFileName,
          getDisplayNamesInGuiPreferences
  >>> from caePrefsAccess import printValuesList
  >>> guiPrefsFileName = getGuiPrefsFileName()
  >>> dispNames = getDisplayNamesInGuiPreferences(guiPrefsFileName)
  >>> print dispNames
  ['preludesim']
  >>> displayName = dispNames[0]
  >>> guiPrefs = openGuiPreferences(displayName)
  >>> printValuesList(guiPrefs)
  ...
  guiPreferences['Abaqus/CAE']['Geometry']['AFXFontSelectorDialog text']:\
      [type:str] '617,298,281,350'
  guiPreferences['Abaqus/CAE']['Geometry']['AFXMainWindow']:[type:str] \
      '193,67,1036,831'
  guiPreferences['Abaqus/CAE']['Geometry']['AdaptivityPlotter']:[type:str] \
      '11,156,226,240'
  guiPreferences['Abaqus/CAE']['Geometry']['Amplitude Plotter']:[type:str] \
      '1105,189,312,290'
  guiPreferences['Abaqus/CAE']['Geometry']['CREATE_Weld']:[type:str] \
      '10,276,377,560'
  guiPreferences['Abaqus/CAE']['Geometry']['Copy MDB Annotation']:[type:str] \
      '122,273,160,79'
  ```

You can change the geometry of the Abaqus/CAE main window by issuing a command like the following:

```python2
>>> guiPrefs['Abaqus/CAE']['Geometry']['AFXMainWindow'] = '193,67,800,600'
```

You can save the GUI preferences you change to the original file by issuing the following command:

```python2
>>> guiPrefs.save()
```
