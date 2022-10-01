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
    The abqpy is built in Python 3 but the Python interpreter of Abaqus is Python 2, so you 
    must write codes that are compatiable with Python 2 and Python 3.

.. you can use it to run Abaqus fluently, it is a package to make Abaqus 
.. modeling, calculation, visualization easily. Using `abqpy`, you can simply build the Abaqus 
.. model, submit and monitor the job, and visualize the results in just one python script, you 
.. don't even need to open Abaqus the whole time.

Other links for this project
----------------------------

* Homepage: `abqpy.com <https://abqpy.com>`_
* GitHub repository: `github.com/haiiliin/abqpy <https://github.com/haiiliin/abqpy>`_
* PyPI: `pypi.org/project/abqpy <https://pypi.org/project/abqpy/>`_
* Anaconda: `anaconda.org/haiiliin/abqpy <https://anaconda.org/haiiliin/abqpy>`_
* Read the Docs: `readthedocs.org/projects/abqpy <https://readthedocs.org/projects/abqpy>`_


Documentation
-------------

.. toctree::
   :maxdepth: 1
   :caption: Contents

   getting_started
   tutorials
   templates
   user
   summary
   references

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
