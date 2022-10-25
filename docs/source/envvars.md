# System Environment Variables

## `ABAQUS_BAT_PATH`

In order to use Abaqus command to execute the Python script and submit the job, you need to tell
`abqpy` where the Abaqus command located. Usually, Abaqus command locates in a directory like this:

```sh
C:/SIMULIA/Commands/abaqus.bat
```

You can add the directory `C:/SIMULIA/Commands` to the system environment variable `Path`, or you can create a new
system variable named `ABAQUS_BAT_PATH`, and set the value to the file path of the Abaqus command, i.e.,
`C:/SIMULIA/Commands/abaqus.bat`.

## `ABAQUS_COMMAND_OPTIONS`

The default execution procedure invoked by `abqpy` inside the Python interpreter
environment where it is installed is to run one of the two following command lines:

1. When there is a `import abaqus` or `from abaqus import ...` statement:

   ```sh
   abaqus cae noGUI=script.py -- [args ...]
   ```

2. When there is a `import odbAccess` or `from odbAccess import ...` statement:

   ```sh
   abaqus python script.py [args ...]
   ```

However, there are other execution procedures that can be run with the `abaqus`
command and also another options that could be passed to these commands. To define
these procedures and options you can create a new system environment variable
named `ABAQUS_COMMAND_OPTIONS`, and set a **dictionary** to this variable with the
options you want to use. The values of the dictionary keys would be booleans or
strings, e.g.: `{'noGUI':True, 'database':'file.odb'}`

The possible options are:

1. Using `abaqus cae` command line options (import `abaqus` module):

   ```python
   {
       'noGUI': bool,
       'database': 'database-file',
       'replay': 'replay-file',
       'recover': 'journal-file',
       'startup': 'startup-file',
       'noenvstartup': bool,
       'noSavedOptions': bool,
       'noSavedGuiPrefs': bool,
       'noStartupDialog': bool,
       'custom': 'script-file',
       'guiTester': 'GUI-script',
       'guiRecord': bool,
       'guiNoRecord': bool,
   }
   ```

2. Using `abaqus python` command line options (import `odbAccess` module):

   ```python
   {
       'sim': 'sim_file_name',
       'log': 'log_file_name',
   }
   ```

One advantage in using this alternative is to change the options at run time inside the code.

## Example

The snippet bellow changes the default procedure options before calling
abaqus cae command procedure, at run time.

```python
import os
os.environ['ABAQUS_COMMAND_OPTIONS'] = str({'noGUI': False, 'database':'file.odb'})

from abaqus import *
...
```

In this specific case, the procedure will use the graphical user interface (GUI mode)
and load a *database* file, i.e., it will run the following command line.

```sh
abaqus cae script=script.py database=file.odb -- [args ...]
```
