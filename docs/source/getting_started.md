# Getting Started

## Introduction

`abqpy` is a Python package providing type hints for Python scripting of Abaqus, you can
use it to write you Python script of Abaqus fluently, even without doing anything in Abaqus.
It also provides some simple APIs to execute the Abaqus commands so that you can run your
Python script to build the model, submit the job and extract the output data in just one
Python script, even without opening the Abaqus/CAE.

## Installation

Make sure <a href="https://www.python.org/downloads/"> <img src="https://img.shields.io/badge/Python-3.7%2B-brightgreen" align=center /> </a> and 
<a href="https://www.3ds.com/products-services/simulia/products/abaqus/"> <img src="https://img.shields.io/badge/Abaqus-2016%2B-brightgreen" align=center /> </a>
are installed on your computer before installing `abqpy`. 

You can install `abqpy` with the following commands.

```{eval-rst}
.. tab-set::

    .. tab-item:: Install with pip

        .. parsed-literal::

            :version-major:`pip install abqpy==|abqpy|.*`  # recommended
            :version:`pip install abqpy==|abqpy|`
            pip install abqpy

    .. tab-item:: Install from source

        .. parsed-literal::

            :version-major:`pip install git+https://github.com/haiiliin/abqpy@|abqpy|`

    .. tab-item:: Install with jupyter notebook support

        .. code-block:: sh

            pip install abqpy[jupyter]

.. note::

    You are recommended to install the corresponding version of Abaqus and `abqpy` to avoid any compatibility issues.
```

### Two Python interpreters

Before we go any further, it is necessary for us to understand two Python interpreters.

When we use the Abaqus/CAE graphical user interface (GUI) to create a model and to visualize
the results, commands are issued internally by Abaqus/CAE after every operation. These
commands reflect the geometry you created along with the options and settings you selected
from each dialog box. The GUI generates commands in an object-oriented programming language
called Python. The commands issued by the GUI are sent to the Abaqus/CAE kernel. The kernel
interprets the commands and uses the options and settings to create an internal representation
of our model. The kernel is the brains behind Abaqus/CAE. The GUI is the interface between the
user and the kernel.

In a word, Abaqus use Python language to interact with the Abaqus kernel, everything that can
be done in Abaqus/CAE, can also be done using Python script. Abaqus has already installed a
Python interpreter so that Abaqus/CAE can use it to interact with the Abaqus kernel.

For some reasons, we cannot directly use the Python interpreter inside Abaqus to build an
Abaqus model. But fortunately, we can use the commands provided by Abaqus to access it. i.e.

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

Usually, we can use the noGUI-file or script-file to execute our Python script in Abaqus.

Another Python interpreter, is the Python interpreter installed by ourselves, where `abqpy`
is installed. `abqpy` provides a bridge to connect our Python script to Abaqus Python
interpreter, it provides type hints for Python scripting for Abaqus, enabling us to write a
Abaqus Python script quickly.

## How does this package work?

`abqpy` is just a package to provide type hints for Abaqus/Python scripting, it is installed outside Abaqus/Python
environment, you can use `abqpy` to write your Abaqus/Python scripts, and run the scripts inside Abaqus on your own.
However, with the help of Abaqus command, an easier way can be achieved: **you can actually run the script using your
own Python interpreter without opening Abaqus**, which is achieved via the **abaqus** command like this:

```sh
abaqus cae noGUI=script.py
```

The secret is hided in the {py:func}`~abqpy.abaqus.run` function:

```python
def run(cae = True):
    abaqus = os.environ.get("ABAQUS_BAT_PATH", "abaqus")

    filePath = os.path.abspath(__main__.__file__)
    args = " ".join(sys.argv[1:])

    if cae:
        os.system(f"{abaqus} cae noGUI={filePath} -- {args}")
    else:
        os.system(f"{abaqus} python {filePath} {args}")
    sys.exit(0)
```

In this package, the {py:mod}`~abaqus` module is reimplemented to automatically call this function. If you import this module in the top of your
script (i.e., `from abaqus import *`), your Python interpreter (not Abaqus Python interpreter) will call this function and use the
**abaqus** command to submit the script to Abaqus. After it is submitted to Abaqus, {py:func}`~abqpy.abaqus.run`
will exit the interpreter, because the script will already run in Abaqus Python interpreter.

In the output script, we might not want to always use the {py:mod}`~abaqus` module, because it needs the Abaqus/CAE kernel (and its license).
Instead, we use the module {py:mod}`~odbAccess` (i.e., `from odbAccess import *`), which requires only the Abaqus Python interpreter.
Then, another similar **abaqus** command line is needed:

```sh
abaqus python script.py
```

So, the {py:mod}`~odbAccess` module is also reimplemented to call the {py:func}`~abqpy.abaqus.run` function with the argument `cae = False`.

In summary, the {py:func}`~abqpy.abaqus.run` function will be called when you import one of the two modules ({py:mod}`~abaqus` or {py:mod}`~odbAccess`). It will pass the argument `cae = True`
in {py:mod}`~abaqus` module and `cae = False` in {py:mod}`~odbAccess` module.
Therefore, if you want to run your Python script in Abaqus Python environment, please make sure to import one of these modules
on the top of your script.

## Write your Abaqus/Python script

After installing the `abqpy` package, you can start writing your own Abaqus/Python script
to build your model. You can refer
[abqpy/examples at main · haiiliin/abqpy](https://github.com/haiiliin/abqpy/tree/main/examples)
for some script examples. Or you may go {doc}`/tutorials` for a simple tutorial. For more documentation about
Abaqus/Python scripting, please check {doc}`/reference/index` for more detailed API references.

## Setup your Abaqus Environment

Make sure the `abaqus` command is available in the command line (i.e., you can run `abaqus` in the command line), otherwise,
add a new system variable named `ABAQUS_BAT_PATH`, and set the value to the file path of the Abaqus command, for example,
`C:/SIMULIA/Commands/abaqus.bat`.

## Run your Abaqus/Python script

Now you can just run your Abaqus/Python script using your own Python interpreter that `abqpy` is installed.

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
