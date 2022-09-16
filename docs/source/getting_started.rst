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

The secret is hided in the :py:meth:`~abaqus.Mdb.Mdb.Mdb.saveAs` method:

.. autolink-concat:: off
.. code-block:: python

    def saveAs(self, pathName: str):
        abaqus = 'abaqus'
        if 'ABAQUS_BAT_PATH' in os.environ.keys():
            abaqus = os.environ['ABAQUS_BAT_PATH']

        filePath = os.path.abspath(sys.argv[0])
        args = " ".join(sys.argv[1:])

        os.system(f"{abaqus} cae noGUI={filePath} -- {args}")

In this package, the :py:meth:`~abaqus.Mdb.Mdb.Mdb.saveAs` method is reimplemented, if you call this method in your
script (i.e., `mdb.saveAs('model.cae')`), the Python interpreter (not Abaqus Python interpreter) will use the
**abaqus** command to submit this script to Abaqus, when it is submited to Abaqus, :py:meth:`~abaqus.Mdb.Mdb.Mdb.saveAs`
will be just a normal method to save the model because `abqpy` is not installed in Abaqus Python interpreter.

In the output script, we might not have to use the :py:meth:`~abaqus.Mdb.Mdb.Mdb.saveAs` method, then another similar
method :py:meth:`~abaqus.Session.Session.Session.openOdb` is also reimplemented:

.. autolink-skip:: section
.. code-block:: python

    def openOdb(self, name: str, *args, **kwargs):
        abaqus = 'abaqus'
        if 'ABAQUS_BAT_PATH' in os.environ.keys():
            abaqus = os.environ['ABAQUS_BAT_PATH']

        filePath = os.path.abspath(sys.argv[0])
        args = " ".join(sys.argv[1:])

        os.system(f"{abaqus} cae noGUI={filePath} -- {args}")

Therefore, if you want to run your Python script in Abaqus Python environment, please make sure to use these methods.

Installation
------------

`abqpy` supports Python 3.7 or a later version. If you are using Python 3.6 or an earlier version, please upgrade to Python 3.7
or a later version.

`abqpy` is uploaded to `PyPI <https://pypi.org/project/abqpy>`_, you can simply install 
it using pip:

.. code-block:: sh
    
    pip install abqpy

`abqpy` is also uploaded to `anaconda <https://anaconda.org/haiiliin/abqpy>`_, you can use 
`conda` to install it:

.. code-block:: sh

    conda install -c haiiliin abqpy

You may install the latest development version by cloning the 
`GitHub repository <https://github.com/haiiliin/abqpy>`_ and use `python` to install from 
the local directory:

.. code-block:: sh

    git clone https://github.com/haiiliin/abqpy.git
    cd abqpy
    pip install -r requirements.txt
    python setup.py install

Optional Requirements
~~~~~~~~~~~~~~~~~~~~~

If you want to use the Jupyter notebook to write your Abaqus/Python scripts, you need to install
`ipynbname`:

.. code-block:: sh

    pip install ipynbname

Install A Specific Version
--------------------------

You can specify the version number when installing `abqpy`, for example:

Using `pip`:

.. code-block:: sh

    pip install abqpy==2021.3.2

Using `conda`:

.. code-block:: sh

    conda install -c haiiliin abqpy=2021.3.2

A better way is to use * to match specific version:

.. code-block:: sh

    pip install abqpy==2021.*


Abaqus command
--------------

In order to use Abaqus command to execute the Python script and submit the job, you need to tell 
`abqpy` where the Abaqus command located. Usually, Abaqus command locates in a directory like this: 

.. code-block:: sh

    C:/SIMULIA/Commands/abaqus.bat

You can add the directory `C:/SIMULIA/Commands` to the system environment variable `Path`, or you can create a new
system variable named `ABAQUS_BAT_PATH`, and set the value to the file path of the Abaqus command, i.e.,
`C:/SIMULIA/Commands/abaqus.bat`.
