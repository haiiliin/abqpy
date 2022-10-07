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

Other links for this project
----------------------------

* Websitte: https://abqpy.com
* GitHub repository: https://github.com/haiiliin/abqpy
* PyPI: https://pypi.org/project/abqpy
* Anaconda: https://anaconda.org/haiiliin/abqpy
* Bug report: https://github.com/haiiliin/abqpy/issues


Documentation
-------------

.. toctree::
   :maxdepth: 1
   :caption: Contents

   getting_started
   tutorials
   user
   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
