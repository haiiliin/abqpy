========================
Writing your own modules
========================

You can create your own module containing a set of Python functions. You can import this module and make use of its functions. The name of the module to import is the same as the name of the file containing the functions without the `.py` file suffix.

For example, you can create a module called myUtilities by copying a modified version of the function that calculates the distance from a point to the origin into a file called myUtilities.py.

.. code-block:: python

    """ myUtilities - a module of mathematical functions"""

    import math
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def distance(x, y):
        """
        Prints distance from origin to (x, y).

        Takes two arguments, x and y. 
        """ 

        # Square the arguments and add them. 

        a = x**2 + y**2

        # Return the square root.

        return math.sqrt(a)

You must import the module to make use of the functions and constants that it contains.

.. code-block:: python

    import myUtilities

    distance = myUtilities.distance(30, 50)

You can use the `__doc__` method to obtain the documentation string from a module. For example,

.. code-block:: python

    myUtilities.__doc__
    ' myUtilities - a module of mathematical functions'

A tool for finding bugs in your modules is provided with Abaqus. The tool is called pychecker. When you import a module, pychecker prints warnings for any problems it finds with the Python source code. For example,

.. code-block:: python

    >>> from pychecker import checker
    >>> import myUtilities
    d:\users\smith\myUtilities.py:3: Imported module (sys) not used
    d:\users\smith\myUtilities.py:14: Local variable (a) not used
    d:\users\smith\myUtilities.py:18: No global (b) found

For more information about `pychecker`, see the official Python website (https://www.python.org)

If you import a module during an interactive session using the command line interface and then make changes to the module, Python will not recognize your changes until you reload the module; for example:

.. code-block:: python

    import myModule
    maxStress = myModule.calculateStress(odb)

    # Edit myModule.py and modify the calculateStress method.

    reload(myModule)
    maxStress = myModule.calculateStress(odb)