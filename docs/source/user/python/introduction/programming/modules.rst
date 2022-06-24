=====================
Functions and modules
=====================

When you start Python from a local window or from Abaqus/CAE, the Python interpreter is aware of a limited set of built-in functions. For example, try entering the following at the Python prompt:

.. code-block:: python

    >>> myName = 'Einstein'
    >>> len(myName)

Python returns the number 8, indicating the length of the string `myName`. The `len()` function is a built-in function and is always available when you are using Python. To see a list of the built-in functions provided by Python, type `dir(__builtins__)` at the Python prompt.

`dir(__builtins__)` is typed as dir(underscore underscorebuiltinsunderscore underscore). You have seen this underscore underscore notation already in Sequences.

In addition, you can look at the standard Python documentation on the official Python website (http:www.python.org) for a list of built-in functions. Built-in functions are described in the Built-in Functions section of the Python Library Reference.

Many functions, however, are not built-in; for example, most of the math functions, such as `sin()` and `cos()`, are not available when you start Python. Functions that are not built-in are defined in modules. Modules are a way of grouping functionality and are similar to a Fortran library of subroutines. For example, the following code could be the opening lines of a Python script. The code imports the Python module `sys` and uses the `argv` member of `sys` to print the command line arguments:

.. code-block:: python

    import sys
    for argument in sys.argv:
        print argument

You must first import the module to make its functions, names, and functionality available to the Python interpreter. Try the following:


.. code-block:: python

    >>> from math import *
    >>> x = pi/4.0
    >>> sin(x)
    0.707106781187

The first line imports all of the names from the math module. The second line uses `pi`, a float number defined in the math module. The third line refers to a `sin()` function. Python can use the `sin()` function because you imported it from the math module.

To import only the `sin()` function, you could have typed


.. code-block:: python

    >>> from math import sin

You need to import a module only once during a session. Once a module is imported, its functions, methods, and attributes are always available to you. You cannot unload a module after you import it.

To see a list of all the functions that come with the math module, look at the Miscellaneous Services section of the Python Library Reference. You can download public-domain modules, and you can create your own modules.

Python provides a second approach to importing modules. For example,


.. code-block:: python

    >>> import math
    >>> x = 22.0/(7.0 * 4.0)
    >>> math.sin(x)
    0.707330278085

The `import` approach shown above imports the module as a unit, and you must qualify the name of an object from the module. To access a function from the `math` module in our example, you must prepend the function with `math.`; the `math.` statement is said to qualify the `sin()` function.

What is the difference between the two approaches to importing modules? If two modules contain an object with the same name, Python cannot distinguish between the objects if you use the `from modulename import *` approach. If two objects have the same name, Python uses the object most recently imported. However, if you use the `import modulename` approach, modulename qualifies the name of the object and makes it unique.
