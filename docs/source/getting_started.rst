===============
Getting Started
===============


Introduction
------------

`abqpy` is a Python package providing type hints for Python scripting of Abaqus, you can 
use it to write you Python script of Abaqus fluently, even without doing anything in Abaqus. 
It also provides some simple APIs to execute the Abaqus commands so that you can run your 
Python script to build the model, submit the job and extract the output data in just one 
Python script, even without opening the Abaqus/CAE. 

Installation
------------

`abqpy` supports Python 3.7 or a later version. If you are using Python 3.6 or an earlier version, please upgrade to Python 3.7
or a later version.

.. grid:: 1 2 2 2
    :gutter: 4

    .. grid-item-card::

        Working with conda?
        ^^^^^^^^^^^^^^^^^^^

        `abqpy` can be installed via conda from `anaconda <https://anaconda.org/haiiliin/abqpy>`_.

        ++++

        .. code-block:: bash

            conda install -c haiiliin abqpy

    .. grid-item-card::

        Prefer pip?
        ^^^^^^^^^^^

        abqpy can also be installed via pip from `PyPI <https://pypi.org/project/abqpy>`__.

        ++++

        .. code-block:: bash

            pip install abqpy

    .. grid-item-card::
        :columns: 12

        Install from source?
        ^^^^^^^^^^^^^^^^^^^^

        You can also install `abqpy` from source:

        ++++

        .. code-block:: bash

            pip install git+https://github.com/haiiliin/abqpy@main

    .. grid-item-card::

        Install a specific version
        ^^^^^^^^^^^^^^^^^^^^^^^^^^

        You can specify the version number when installing `abqpy`, for example:

        ++++

        .. code-block:: bash

            pip install abqpy==2022.3.14
            pip install abqpy==2022.*
            conda install -c haiiliin abqpy=2022.3.14

    .. grid-item-card::

        Optional dependencies
        ^^^^^^^^^^^^^^^^^^^^^

        If you want to use the Jupyter notebook to write your Abaqus/Python scripts, use
        the following command:

        ++++

        .. code-block:: bash

            pip install abqpy[jupyter]


Two Python interpreters
~~~~~~~~~~~~~~~~~~~~~~~

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

.. code-block:: sh
    
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


Usually, we can use the noGUI-file or script-file to execute our Python script in Abaqus.

Another Python interpreter, is the Python interpreter installed by ourselves, where `abqpy` 
is installed. `abqpy` provides a bridge to connect our Python script to Abaqus Python 
interpreter, it provides type hints for Python scripting for Abaqus, enabling us to write a 
Abaqus Python script quickly.


How does this package work?
---------------------------

`abqpy` is just a package to provide type hints for Abaqus/Python scripting, it is installed outside Abaqus/Python
environment, you can use `abqpy` to write your Abaqus/Python scripts, and run the scripts inside Abaqus on your own.
However, with the help of Abaqus command, an easier way can be achieved: **you can actually run the script using your
own Python interpreter without opening Abaqus**, which is achieved via the **abaqus** command like this:

.. code-block:: sh

    abaqus cae noGUI=script.py

The secret is hided in the :py:meth:`~abqpy.abaqus.run` function:

.. autolink-concat:: off
.. code-block:: python

    def run():
        abaqus = 'abaqus'
        if 'ABAQUS_BAT_PATH' in os.environ.keys():
            abaqus = os.environ['ABAQUS_BAT_PATH']

        filePath = os.path.abspath(__main__.__file__)
        args = " ".join(sys.argv[1:])

        os.system(f"{abaqus} cae noGUI={filePath} -- {args}")
        
        sys.exit(0)

In this package, the :py:mod:`~abaqus` module is reimplemented to automatically call this function. If you import this module in the top of your
script (i.e., ``from abaqus import *``), your Python interpreter (not Abaqus Python interpreter) will call this function and use the
**abaqus** command to submit the script to Abaqus. After it is submitted to Abaqus, :py:meth:`~abqpy.abaqus.run`
will exit the interpreter, because the script will already run in Abaqus Python interpreter.

In the output script, we might not want to always use the :py:mod:`~abaqus` module, because it needs the Abaqus/CAE kernel (and its license).
Instead, we use the module :py:mod:`~odbAccess` (i.e., ``from odbAccess import *``), which requires only the Abaqus Python interpreter.
Then, another similar **abaqus** command line is needed:

.. code-block:: sh

    abaqus python script.py

So, the :py:mod:`~odbAccess` module is also reimplemented to call the :py:meth:`~abqpy.abaqus.run` function, and the actual implementation of this function is similar to:

.. autolink-skip:: section
.. code-block:: python

    def run(cae = True):
        abaqus = 'abaqus'
        if 'ABAQUS_BAT_PATH' in os.environ.keys():
            abaqus = os.environ['ABAQUS_BAT_PATH']

        filePath = os.path.abspath(__main__.__file__)
        args = " ".join(sys.argv[1:])

        if cae:
            os.system(f"{abaqus} cae noGUI={filePath} -- {args}")
        else:
            os.system(f"{abaqus} python {filePath} {args}")
        sys.exit(0)

In summary: this function will be called when you import one of the two modules (:py:mod:`~abaqus` or :py:mod:`~odbAccess`). It will pass the argument ``cae = True`` 
in :py:mod:`~abaqus` module and ``cae = False`` in :py:mod:`~odbAccess` module.
Therefore, if you want to run your Python script in Abaqus Python environment, please make sure to import one of these modules
on the top of your script.

Write your Abaqus/Python script
-------------------------------

After installing the `abqpy` package, you can start writing your own Abaqus/Python script
to build your model. You can refer
`abqpy/examples at main · haiiliin/abqpy <https://github.com/haiiliin/abqpy/tree/main/examples>`_
for some tests of the script, for more detailed documentation, please check
`abqpy documentation <https://haiiliin.com/abqpy/>`_.

Setup your Abaqus Environment
-----------------------------

In order to use Abaqus command to execute the Python script and submit the job, you need to tell
`abqpy` where the Abaqus command is located. Usually, Abaqus command locates in a directory like this:

.. code-block:: sh

   C:/SIMULIA/Commands/abaqus.bat

You can add the directory `C:/SIMULIA/Commands` to the system environment variable `Path`, or you can create a new
system variable named `ABAQUS_BAT_PATH`, and set the value to the file path of the Abaqus command, i.e.,
`C:/SIMULIA/Commands/abaqus.bat`.

Run your Abaqus/Python script
-----------------------------

Now you can just run your Abaqus/Python script using your own Python interpreter that `abqpy` is installed.

- Create an Abaqus Model

  .. image:: images/model-code.gif
      :width: 100%
      :align: center
      :alt: Create an Abaqus Model

- Extract Output Data

  .. image:: images/output-code.gif
      :width: 100%
      :align: center
      :alt: Extract Output Data

What next?
----------

You may wonder how does this package work, 
you can go :doc:`/getting_started` for more detailed introduction and go
:doc:`/tutorials` for a simple tutorial. For more documentation about 
Abaqus/Python scripting, please check :doc:`/references` 
for more detailed API references.
