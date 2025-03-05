# Environment Variables

The following environment variables can be used to configure the package.

```{envvar} ABAQUS_BAT_PATH

**Type: string**

The file path of the `abaqus` command line batch file (`.bat`). Only set this environment variable if `abaqus` is not
the default Abaqus command line executable. This variable is used by `abqpy` to run the Abaqus command line
procedure inside the Python interpreter environment where it is installed.
```

````{envvar} ABAQUS_COMMAND_OPTIONS

**Type: string of a Python dictionary**

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
strings, e.g.: `{'gui': True, 'database': 'file.odb'}`

The possible options are:

1. Using `abaqus cae` command line options (import `abaqus` module):

   ```python
   {
       "gui": bool,
       "database": "database-file",
       "replay": "replay-file",
       "recover": "journal-file",
       "startup": "startup-file",
       "envstartup": bool,
       "savedOptions": bool,
       "savedGuiPrefs": bool,
       "startupDialog": bool,
       "custom": "script-file",
       "guiTester": "GUI-script",
       "guiRecord": bool,
   }
   ```

2. Using `abaqus python` command line options (import `odbAccess` module):

   ```python
   {
       "sim": "sim_file_name",
       "log": "log_file_name",
   }
   ```

One advantage in using this alternative is to change the options at run time inside the code.

```{note}
The environment variable {envvar}`ABAQUS_COMMAND_OPTIONS` must be a valid string that can be parsed to a Python dictionary,
which means that you must use `True` or `False` for boolean options. However, in the following individual environment
variables, you can use `true`, `on`, `yes` or `1` (or capitalized ones since they are not case sensitive) to set the
boolean option to `True` and any other values to set it to `False`.
```
````

```{envvar} ABAQUS_CAE_DATABASE

**Type: string**

A shortcut to the {envvar}`ABAQUS_COMMAND_OPTIONS` environment variable to set the `database` option but has higher priority.
```

```{envvar} ABAQUS_CAE_REPLAY

**Type: string**

A shortcut to the {envvar}`ABAQUS_COMMAND_OPTIONS` environment variable to set the `replay` option but has higher priority.
```

```{envvar} ABAQUS_CAE_RECOVER

**Type: string**

A shortcut to the {envvar}`ABAQUS_COMMAND_OPTIONS` environment variable to set the `recover` option but has higher priority.
```

```{envvar} ABAQUS_CAE_STARTUP

**Type: string**

A shortcut to the {envvar}`ABAQUS_COMMAND_OPTIONS` environment variable to set the `startup` option but has higher priority.
```

```{envvar} ABAQUS_CAE_GUI

**Type: bool {true, false, on, off, yes, no, 1, 0}**

A shortcut to the {envvar}`ABAQUS_COMMAND_OPTIONS` environment variable to set the `gui` option but has higher priority.
```

```{envvar} ABAQUS_CAE_ENVSTARTUP

**Type: bool {true, false, on, off, yes, no, 1, 0}**

A shortcut to the {envvar}`ABAQUS_COMMAND_OPTIONS` environment variable to set the `envstartup` option but has higher priority.
```

```{envvar} ABAQUS_CAE_SAVED_OPTIONS

**Type: bool {true, false, on, off, yes, no, 1, 0}**

A shortcut to the {envvar}`ABAQUS_COMMAND_OPTIONS` environment variable to set the `savedOptions` option but has higher priority.
```

```{envvar} ABAQUS_CAE_SAVED_GUI_PREFS

**Type: bool {true, false, on, off, yes, no, 1, 0}**

A shortcut to the {envvar}`ABAQUS_COMMAND_OPTIONS` environment variable to set the `savedGuiPrefs` option but has higher priority.
```

```{envvar} ABAQUS_CAE_STARTUP_DIALOG

**Type: bool {true, false, on, off, yes, no, 1, 0}**

A shortcut to the {envvar}`ABAQUS_COMMAND_OPTIONS` environment variable to set the `startupDialog` option but has higher priority.
```

```{envvar} ABAQUS_CAE_CUSTOM

**Type: string**

A shortcut to the {envvar}`ABAQUS_COMMAND_OPTIONS` environment variable to set the `custom` option but has higher priority.
```

```{envvar} ABAQUS_CAE_GUI_TESTER

**Type: string**

A shortcut to the {envvar}`ABAQUS_COMMAND_OPTIONS` environment variable to set the `guiTester` option but has higher priority.
```

```{envvar} ABAQUS_CAE_GUI_RECORD

**Type: bool {true, false, on, off, yes, no, 1, 0}**

A shortcut to the {envvar}`ABAQUS_COMMAND_OPTIONS` environment variable to set the `guiRecord` option but has higher priority.
```

```{envvar} ABAQUS_PYTHON_SIM

**Type: string**

A shortcut to the {envvar}`ABAQUS_COMMAND_OPTIONS` environment variable to set the `sim` option but has higher priority.
```

```{envvar} ABAQUS_PYTHON_LOG

**Type: string**

A shortcut to the {envvar}`ABAQUS_COMMAND_OPTIONS` environment variable to set the `log` option but has higher priority.
```

```{envvar} ABQPY_DEBUG

**Type: bool {true, false, on, off, yes, no, 1, 0}**

Set this environment variable to `True` to enable debug mode in `abqpy`.
```

```{envvar} ABQPY_SKIP_ABAQUS

**Type: bool {true, false, on, off, yes, no, 1, 0}**

Set this environment variable to `True` to skip the Abaqus command line procedure execution.
```

```{envvar} ABQPY_MAKE_DOCS

**Type: bool {true, false, on, off, yes, no, 1, 0}**

This environment variable is set to true when the `abqpy` package is being used to generate the documentation.
```

```{envvar} ABQPY_CLI_TRACEBACK_LIMIT

**Type: int**

The maximum number of levels of the traceback (`sys.tracebacklimit`) to show in the command line interface. The default value is 0.
```

```{envvar} ABQPY_EXECUTION_METHOD

**Type: string {os, subprocess}**

Method to run the Abaqus command line procedure. The default method is `os` which uses the `os.system` function to run the command. The `subprocess` method uses the `subprocess.run` function to run the command.
```

## Example

The snippet bellow changes the default procedure options before calling
abaqus cae command procedure, at run time.

```python
import os

os.environ["ABAQUS_COMMAND_OPTIONS"] = str({"gui": True, "database": "file.odb"})

from abaqus import *

...
```

In this specific case, the procedure will use the graphical user interface (GUI mode)
and load a _database_ file, i.e., it will run the following command line.

```sh
abaqus cae script=script.py database=file.odb -- [args ...]
```

## Comments

<script
   type="text/javascript"
   src="https://utteranc.es/client.js"
   async="async"
   repo="haiiliin/abqpy"
   issue-term="pathname"
   theme="github-light"
   label="💬 comment"
   crossorigin="anonymous"
/>
