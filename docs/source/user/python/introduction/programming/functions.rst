==================
Creating functions
==================

You can define your own functions in Python. A function is like a subroutine in Fortran. You can pass arguments into a function, it performs the operation, and it can return one or more values. For example, the following function returns the distance of a point from the origin. The def statement starts a function definition.

.. code-block:: python

    def distance(x, y):
        a = x**2 + y**2     
        return  a ** 0.5
    
You supply the arguments to a function in parentheses; for example,

.. code-block:: python

    >>> distance(4.7, 9.1)
    10.2420701033

You can assign the return value to a variable:

.. code-block:: python

    >>> d = distance(4.7, 9.1)
    >>> print d
    10.2420701033

One of the methods provided by Abaqus uses as many as 50 arguments. Some of the arguments are required by the method; others are optional, and Abaqus provides an initial or default value. Fortunately, you can call a function or a method without providing every optional argument if you use Python's keyword arguments. A keyword specifies the argument that you are providing. Keyword arguments also make your scripts more readable. For example, the following defines a function called calculateCylinderVolume:

.. code-block:: python

    >>> from math import *
    >>> def calculateCylinderVolume(radius,height):
    ...     volume = pi * radius**2 * height
    ...     return volume 

You can call the function with the following line:

.. code-block:: python

    >>> volume = calculateCylinderVolume(3.2,27.5)

Here the arguments are called positional arguments because you are relying on their position in the function call to determine the variable to which they are assigned in the function—radius followed by height.

The following is the same statement using keyword arguments:

.. code-block:: python

    >>> volume = calculateCylinderVolume(radius=3.2, height=27.5)

Keyword arguments make your code more readable. In addition, if you use keyword arguments, you can enter the arguments in any order.

.. code-block:: python

    >>> volume = calculateCylinderVolume(height=27.5, radius=3.2)

You can define default values for an argument in a function definition. For example, the following sets the default value of radius to 0.5 and the default value of height to 1.0:

.. code-block:: python

    >>> from math import *
    >>> def calculateCylinderVolume(radius=0.5,height=1.0):
    ...     volume = pi * radius * radius * height
    ...     return volume 

You can now call the function without providing all the arguments. The function assigns the default value to any missing arguments.

.. code-block:: python

    >>> volume = calculateCylinderVolume(height=27.5)

It is good programming practice to use a documentation string that indicates the purpose of a function and the arguments expected. A documentation string appears at the top of a function and is delimited by triple quotes """. You can use the __doc__ method to obtain the documentation string from a function while running the Python interpreter. For example,

.. code-block:: python

    >>>def calculateCylinderVolume(radius=0.5,height=1.0):
    ...     """
    ...     Calculates the volume of a cylinder.
    ...
    ...     Takes two optional arguments, radius (default=0.5)
    ...     and height (default=1.0).
    ...     """
    ...     from math import *
    ...     volume = pi * radius**2 * height
    ...     return volume
    ...
    >>> print calculateCylinderVolume.__doc__

    Calculates the volume of a cylinder.

    Takes two optional arguments, radius (default=0.5)
    and height (default=1.0). 

You can retrieve the documentation string for the methods in the Abaqus Scripting Interface. For example,

.. code-block:: python

    >>> mdb.Model.__doc__
    'Mdb.Model(name <, description, stefanBoltzmann, absoluteZero>) -> 
        This method creates a Model object.'

    >>> session.Viewport.__doc__
    'Session.Viewport(name <, origin, width, height, border, titleBar, 
        titleStyle, customTitleString>) 
        -> This method creates a Viewport object with the specified 
        origin and dimensions.'

The documentation string shows the name of each argument name and whether the argument is required or optional. The string also shows a brief description of the method.

You can use the sys module to retrieve command line arguments and pass them to a function. For example, the following script takes two arguments—the X- and Y-coordinates of a point—and calculates the distance from the point to the origin. The script uses the following modules:

The `sys` module to retrieve the command line arguments.

The `math` module to calculate the square root.

.. code-block:: python

    import sys, math
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def distance(x, y):
        """
        Prints distance from origin to (x, y).

        Takes two command line arguments, x and y. 
        """ 

        # Square the arguments and add them. 

        a = x**2 + y**2

        # Return the square root.

        return math.sqrt(a)

    # Retrieve the command line arguments and 
    # convert the strings to floating-point numbers.

    x = float(sys.argv[1]) 
    y = float(sys.argv[2]) 

    # Call the distance function.

    d = distance(x, y)

    # Print the result.

    print 'Distance to origin = ', d

To use this script, do the following:

Copy the statements into a file called `distance.py` in your local directory.

Type the following at the system prompt:

.. code-block:: sh

    abaqus python distance.py 30 40

Abaqus executes the script and prints the result.

.. code-block:: sh

    Distance to origin =  50.0