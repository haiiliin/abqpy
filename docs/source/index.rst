.. abqpy documentation master file, created by
   sphinx-quickstart on Thu Jan 20 15:04:03 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

abqpy documentation
======================

Type hints for Abaqus/Python scripting.

`abqpy` is a Python package providing type hints for Python scripting of Abaqus, you can 
use it to write you Python script of Abaqus fluently, even without doing anything in Abaqus. 
It also provides some simple APIs to execute the Abaqus commands so that you can run your 
Python script to build the model, submit the job and extract the output data in just one 
Python script, even without opening the Abaqus/CAE.

.. note::
    The abqpy is built in Python 3 but the Python interpreter of Abaqus is Python 2, so you must write codes that are compatiable with Python 2 and Python 3.

.. you can use it to run Abaqus fluently, it is a package to make Abaqus 
.. modeling, calculation, visualization easily. Using `abqpy`, you can simply build the Abaqus 
.. model, submit and monitor the job, and visualize the results in just one python script, you 
.. don't even need to open Abaqus the whole time.

Other links for this project
----------------------------

* GitHub repository: `github.com/haiiliin/abqpy <https://github.com/haiiliin/abqpy>`_
* PyPI: `pypi.org/project/abqpy <https://pypi.org/project/abqpy/>`_
* Anaconda: `anaconda.org/haiiliin/abqpy <https://anaconda.org/haiiliin/abqpy>`_
* Read the Docs: `readthedocs.org/projects/abqpy <https://readthedocs.org/projects/abqpy>`_

Quick Start
-----------

Installation
~~~~~~~~~~~~

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
    python setup.py install

Write your Abaqus/Python script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After installing the `abqpy` package, you can start writing your own Abaqus/Python script
to build your model. You can refer
`abqpy/examples at main · haiiliin/abqpy <https://github.com/haiiliin/abqpy/tree/main/examples>`_
for some tests of the script, for more detailed documentation, please check
`abqpy documentation <https://haiiliin.com/abqpy/>`_.

Setup your Abaqus Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to use Abaqus command to execute the Python script and submit the job, you need to tell
`abqpy` where the Abaqus command is located. Usually, Abaqus command locates in a directory like this:

.. code-block:: sh

   C:/SIMULIA/Commands/abaqus.bat

You can add the directory `C:/SIMULIA/Commands` to the system environment variable `Path`, or you can create a new
system variable named `ABAQUS_BAT_PATH`, and set the value to the file path of the Abaqus command, i.e.,
`C:/SIMULIA/Commands/abaqus.bat`.

Run your Abaqus/Python script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now you can just run your Abaqus/Python script using your own Python interpreter that `abqpy` is installed.

- Create an Abaqus Model

.. image:: images/model-code.*
    :width: 100%
    :align: center
    :alt: Create an Abaqus Model

- Extract Output Data

.. image:: images/output-code.*
    :width: 100%
    :align: center
    :alt: Extract Output Data

What next?
----------

You may wonder how does this package work, 
you can go :doc:`/getting_started` for more detailed introduction and go
:doc:`/tutorials` for a simple tutorial. For more documentation about 
Abaqus/Python scripting, please check :doc:`/summary` for a list of 
descriptions of objects and methods of Abaqus models, check :doc:`/references` 
for more detailed API references.

Documentation
-------------

.. toctree::
   :maxdepth: 1
   :caption: Contents

   getting_started
   tutorials
   user
   summary
   references

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
