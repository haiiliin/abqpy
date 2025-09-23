# Getting Started

## Introduction

`abqpy` is a Python package that provides type hints for Abaqus Python scripting. You can
use it to write your Abaqus Python scripts fluently.
It also provides simple APIs to execute Abaqus commands, enabling you to build models,
submit jobs, and extract output data in a single Python script, all without opening Abaqus/CAE.

## Installation

Make sure <a href="https://www.python.org/downloads/"> <img src="https://img.shields.io/badge/Python-3.8%2B-brightgreen" align=center /> </a> and
<a href="https://www.3ds.com/products-services/simulia/products/abaqus/"> <img src="https://img.shields.io/badge/Abaqus-2016%2B-brightgreen" align=center /> </a>
are installed on your computer before installing `abqpy`.

You can install `abqpy` with the following commands.

````{tab} pip
```{code-block} shell
pip install -U abqpy==2017.*
pip install -U abqpy2017
```
````

````{tab} conda
```{code-block} shell
conda install conda-forge::abqpy=2017
```
````

````{tab} Source
```{code-block} shell
pip install git+https://github.com/haiiliin/abqpy@2017
```
````

````{tab} Jupyter
```{code-block} shell
pip install -U abqpy[jupyter]==2017.*
pip install -U abqpy2017[jupyter]
pip install ipynbname nbconvert
```
````

```{warning}
Do not install abqpy in Abaqus's built-in Python interpreter, as it may cause the
Abaqus Python interpreter to crash and you may not be able to open Abaqus/CAE anymore.
```

```{note}
It is recommended to install the corresponding version of Abaqus and `abqpy` to avoid any compatibility issues.
```

## Two Python interpreters

Before proceeding, it's important to understand the concept of two different Python interpreters.

When you use the Abaqus/CAE graphical user interface (GUI) to create a model and visualize
results, Abaqus/CAE internally issues commands after every operation. These
commands reflect the geometry you created along with the options and settings you selected
from each dialog box. The GUI generates commands in the Python programming language.
The commands issued by the GUI are sent to the Abaqus/CAE kernel, which
interprets the commands and uses the options and settings to create an internal representation
of your model. The kernel is the computational engine behind Abaqus/CAE, while the GUI serves as the interface between you
and the kernel.

In summary, Abaqus uses the Python language to interact with the Abaqus kernel. Everything that can
be done in Abaqus/CAE can also be accomplished using Python scripts. Abaqus comes with a
Python interpreter that enables Abaqus/CAE to interact with the Abaqus kernel.

For various reasons, we cannot directly use the Python interpreter inside Abaqus to build an
Abaqus model independently. However, we can access it using commands provided by Abaqus:

```sh
abaqus cae
    [database=database-file]
    [replay=replay-file]
    [recover=journal-file]
    [startup=startup-file]
    [script=script-file]
    [noGUI=noGUI-file]
    [noenvstartup]
    [noSavedOptions]
    [noSavedGuiPrefs]
    [noStartupDialog]
    [custom=script-file]
    [guiTester=GUI-script]
    [guiRecord]
    [guiNoRecord]
```

Typically, we can use the `noGUI-file` or `script-file` options to execute your Python script in Abaqus.

The second Python interpreter is the one you install yourself, where `abqpy`
is installed. `abqpy` provides a bridge connecting your Python script to the Abaqus Python
interpreter. It provides type hints for Abaqus Python scripting, enabling you to write
Abaqus Python scripts efficiently.

## How does this package work?

`abqpy` is a package that provides type hints for Abaqus Python scripting. It is installed outside the Abaqus Python
environment. You can use `abqpy` to write your Abaqus Python scripts and then run those scripts inside Abaqus manually.
However, with the help of Abaqus commands, there's an easier approach: **you can actually run the script using your
own Python interpreter without opening Abaqus**. This is achieved via the **abaqus** command like this:

```sh
abaqus cae noGUI=script.py
```

The mechanism is implemented in the {py:func}`~abqpy.run.run` function.  
In this package, the {py:mod}`~abaqus` module is reimplemented to automatically call this function. When you import this module at the top of your
script (i.e., `from abaqus import *`), your Python interpreter (not the Abaqus Python interpreter) will call this function and use the
**abaqus** command to submit the script to Abaqus. After the script is submitted to Abaqus, {py:func}`~abqpy.run.run`
will exit the interpreter, because the script will already be running in the Abaqus Python interpreter.

In output scripts, you might not always want to use the {py:mod}`~abaqus` module, since it requires the Abaqus/CAE kernel (and its license).
Instead, you can use the {py:mod}`~odbAccess` module (i.e., `from odbAccess import *`), which only requires the Abaqus Python interpreter.
For this, a different **abaqus** command line is needed:

```sh
abaqus python script.py
```

So, the {py:mod}`~odbAccess` module is also reimplemented to call the {py:func}`~abqpy.run.run` function with the argument `cae = False`.

In summary, the {py:func}`~abqpy.run.run` function is called when you import either of the two modules ({py:mod}`~abaqus` or {py:mod}`~odbAccess`). It passes the argument `cae = True`
for the {py:mod}`~abaqus` module and `cae = False` for the {py:mod}`~odbAccess` module.
Therefore, if you want to run your Python script in the Abaqus Python environment, make sure to import one of these modules
at the top of your script.

## Write your Abaqus Python script

After installing the `abqpy` package, you can start writing your own Abaqus Python scripts
to build your models. You can refer to the
[abqpy/examples at main · haiiliin/abqpy](https://github.com/haiiliin/abqpy/tree/main/examples)
repository for script examples. Alternatively, you can check out {doc}`/tutorials` for a simple tutorial. For more detailed documentation about
Abaqus Python scripting, please see {doc}`/reference/index` for comprehensive API references.

## Set up your Abaqus environment

Ensure the `abaqus` command is available in the command line (i.e., you can run `abaqus` from the command line). If not,
add a new system environment variable named `ABAQUS_BAT_PATH` and set its value to the file path of the Abaqus command. For example:
`C:/SIMULIA/Commands/abaqus.bat`.

## Run your Abaqus Python script

Now you can run your Abaqus Python script using the following methods:

- Open Abaqus/CAE and click **Run Script** in the menu bar, then select your script file. This is the most common way to
  run a Python script in Abaqus/CAE.
- Use the `abaqus` command in the command line:
  ```sh
  abaqus cae script=script.py
  ```
  See [here](https://help.3ds.com/2017/English/DSSIMULIA_Established/SIMACAEEXCRefMap/simaexc-c-caeproc.htm?contextscope=all)
  for more information about the `abaqus` command.
- Use the `abqpy` command in the command line:
  ```sh
  [python -m] abqpy cae script.py
  ```
  The advantage of using the `abqpy` command instead of the `abaqus` command directly is that you can customize the
  default Python launch command. See {doc}`cli` for more information about the `abqpy` command.
- Use the Python 3 interpreter to run the script directly:
  ```sh
  python script.py
  ```
  This is the most convenient way to run the script. It is equivalent to the `abqpy` command with some default
  predefined arguments.
- Use the {py:obj}`abqpy.cli.abaqus` object (an {py:obj}`abqpy.cli.AbqpyCLI` object) to run the script:

  ```python
  from abqpy.cli import abaqus

  abaqus.cae(script="script.py")
  ```

  The {py:obj}`abqpy.cli.abaqus` object is used for the `abqpy` command. You can call the methods in this
  object directly to run the script. This method is convenient when you want to call the Abaqus Python script from another
  Python script, since typing annotations are provided for the methods. You can check the docstring of the methods for
  more information.

```{warning}
`abqpy` does not support debugging, since Abaqus does not provide a debugger for Python scripting outside Abaqus/CAE.
If you run the script in debug mode, it will be opened in Abaqus PDE where you can debug it.
```

- Create an Abaqus Model

  ```{image} images/model-code.*
  :align: center
  :alt: Create an Abaqus Model
  :width: 100%
  ```

- Extract Output Data

  ```{image} images/output-code.*
  :align: center
  :alt: Extract Output Data
  :width: 100%
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
