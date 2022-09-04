======================
Programming techniques
======================

The following sections introduce you to some of the techniques you will need to program with Python.

.. _creating-functions:

Creating functions
------------------

You can define your own functions in Python. A function is like a subroutine in Fortran. You can pass arguments into a function, it performs the operation, and it can return one or more values. For example, the following function returns the distance of a point from the origin. The def statement starts a function definition.

.. code-block:: python2

    def distance(x, y):
        a = x**2 + y**2     
        return  a ** 0.5
    
You supply the arguments to a function in parentheses; for example,

.. code-block:: python2

    >>> distance(4.7, 9.1)
    10.2420701033

You can assign the return value to a variable:

.. code-block:: python2

    >>> d = distance(4.7, 9.1)
    >>> print d
    10.2420701033

One of the methods provided by Abaqus uses as many as 50 arguments. Some of the arguments are required by the method; others are optional, and Abaqus provides an initial or default value. Fortunately, you can call a function or a method without providing every optional argument if you use Python's keyword arguments. A keyword specifies the argument that you are providing. Keyword arguments also make your scripts more readable. For example, the following defines a function called calculateCylinderVolume:


.. code-block:: python2

    >>> from math import *
    >>> def calculateCylinderVolume(radius,height):
    ...     volume = pi * radius**2 * height
    ...     return volume 

You can call the function with the following line:

.. code-block:: python2

    >>> volume = calculateCylinderVolume(3.2,27.5)

Here the arguments are called positional arguments because you are relying on their position in the function call to determine the variable to which they are assigned in the function—radius followed by height.

The following is the same statement using keyword arguments:

.. code-block:: python2

    >>> volume = calculateCylinderVolume(radius=3.2, height=27.5)

Keyword arguments make your code more readable. In addition, if you use keyword arguments, you can enter the arguments in any order.

.. code-block:: python2

    >>> volume = calculateCylinderVolume(height=27.5, radius=3.2)

You can define default values for an argument in a function definition. For example, the following sets the default value of radius to 0.5 and the default value of height to 1.0:

.. code-block:: python2

    >>> from math import *
    >>> def calculateCylinderVolume(radius=0.5,height=1.0):
    ...     volume = pi * radius * radius * height
    ...     return volume 

You can now call the function without providing all the arguments. The function assigns the default value to any missing arguments.

.. code-block:: python2

    >>> volume = calculateCylinderVolume(height=27.5)

It is good programming practice to use a documentation string that indicates the purpose of a function and the arguments expected. A documentation string appears at the top of a function and is delimited by triple quotes """. You can use the __doc__ method to obtain the documentation string from a function while running the Python interpreter. For example,

.. code-block:: python2

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

.. code-block:: python2

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

.. code-block:: python2

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

.. _using-dictionaries:

Using dictionaries
------------------

Dictionaries are a powerful tool in Python. A dictionary maps a variable to a set of data, much like a real dictionary maps a word to its definition, its pronunciation, and its synonyms. Dictionaries are similar to lists in that they are not homogeneous and can contain objects of any type. To access an object in a list, you provide the integer index that specifies the position of the object in the list. For example,

.. code-block:: python2

    >>> myList = [6,2,9]
    >>> myList[1]
    2

In contrast, you access an object in a dictionary through its key, which can be a string, an integer, or any type of immutable Python object. There is no implicit order to the keys in a dictionary. In most cases you will assign a string to the dictionary key. The key then becomes a more intuitive way to access the elements in a dictionary. You use square brackets and the dictionary key to access a particular object. For example,

.. code-block:: python2

    >>> myPart = {}  #Create an empty dictionary
    >>> myPart['size'] = 3.0
    >>> myPart['material'] = 'Steel'
    >>> myPart['color'] = 'Red'
    >>> myPart['number'] = 667

You can add dictionary keys at any time.

.. code-block:: python2

    >>> myPart['weight'] = 376.0
    >>> myPart['cost'] = 10.34

You use the key to access an item in a dictionary.

.. code-block:: python2

    >>> costOverWeight = myPart['cost'] / myPart['weight']
    >>> costOverWeight
    0.0275
    >>> description = myPart['color'] + myPart['material']
    >>> description
    'RedSteel'

Dictionaries are not sequences, and you cannot apply sequence methods such as slicing and concatenating to dictionaries. Dictionaries have their own methods. The following statement lists the methods of the dictionary myPart.

.. code-block:: python2

    >>> myPart.__methods__
    ['clear', 'copy', 'get', 'has_key', 'items', 'keys', 
    'update', 'values']

The `keys()` method returns a list of the dictionary keys.

.. code-block:: python2

    >>> myPart.keys()
    ['size', 'weight', 'number', 'material', 'cost', 'color']

The `values()` method returns a list of the values of each entry in the dictionary.

.. code-block:: python2

    >>> myPart.values()
    [3.0, 376.0, 667, 'Steel', 10.34, 'Red']

The `items()` method returns a list of tuples. Each tuple contains the key and its value.

.. code-block:: python2

    >>> myPart.items() 
    [('size', 3.0), ('number', 667),   ('material', 'Steel'),
    ('color', 'Red'),   ('weight', 376.0), ('cost', 10.34),]

You use the `has_key()` method to see if a key exists. A return value of 1 indicates the key exists in the dictionary. A return value of 0 indicates the key does not exist.

.. code-block:: python2

    >>> myPart.has_key('color')
    1

Python's del statement allows you to delete a variable.

.. code-block:: python2

    >>> del myPart

You can also use del to delete an item from a dictionary.

.. code-block:: python2

    >>> del myPart['color']
    >>> myPart.has_key('color')
    0

You can use the `keys()`, `values()`, or `items()` methods to loop through a dictionary. In the following example, `items()` returns two values; the first is assigned to property, and the second is assigned to setting.

.. code-block:: python2

    >>> for property, setting in myPart.items():
    ...     print property, setting
    ... 
    size 3.0
    weight 376.0
    number 667
    material Steel
    cost 10.34

Reading and writing from files
------------------------------

Many of the file commands are built-in Python commands. You do not have to import a module to use file commands. You use the open() function to create a file.

.. code-block:: python2

    >>> myInputFile  = open('crash_test/fender.txt','r')
    >>> myOutputFile = open('peak_deflection.txt','w+')

The first line opens an existing file in the crash_test directory called fender.txt. The file is opened in read-only mode; myInputFile is a variable that refers to a file object. The second line creates and opens a new file object in the local directory called peak_deflection.txt. This file is opened in read and write mode.

Use the `__methods__` technique that we saw earlier to see the methods of a file object.

.. code-block:: python2

    >>> myOutputFile = open('peak_deflection.txt','w')
    >>> myOutputFile.__methods__
    ['close', 'fileno', 'flush', 'isatty', 'read', 
    'readinto', 'readline', 'readlines', 'seek', 'tell', 
    'truncate', 'write', 'writelines']

The `readline()` method reads a single line from a file into a string, including the new line character that terminates the string. The `readlines()` method reads all the lines in a file into a list. The `write()` function writes a string to a file. Look at the standard Python documentation on the official Python website (https://www.python.org) for a description of functions that operate on files. File objects are described in the Built-in Types section of the Python Library Reference.

The following example reads each line of a text file and changes the line to uppercase characters:

.. code-block:: python2

    # Read-only is the default access mode

    >>> inputFile  = open('foam.txt') 

    # You must declare write access

    >>> outputFile = open('upper.txt','w')
    >>> lines = inputFile.readlines()
    >>> for line in lines:
    ...     newLine = line.upper()
    ...     outputFile.write(newLine)
    ...
    >>> inputFile.close()
    >>> outputFile.close()

The first line opens the input file; you do not need the `'r'` because read-only is the default access mode. The next line opens a new file to which you will write. You read the lines in the input file into a list. Finally, you enter a loop that converts each line to uppercase characters and writes the result to the output file. The final two lines close the files.

.. _error-handling:

Error handling
--------------

When a script encounters unusual circumstances, Python allows you to modify the flow of control through the script and to take the necessary action. The action of signaling a problem during execution is called raising or throwing an exception. Recognizing the problem is called catching an exception. Taking appropriate action is called exception handling.

Python provides exception handling through the try and except commands. For example, the following statement attempts to open an existing file for reading:

.. code-block:: python2

    >>> outputFile = open('foam.txt')

If the file does not exist, the statement fails, and Python displays the following error message:

.. autolink-skip:: section
.. code-block::

    >>> outputFile = open('foam.txt')
    Traceback (innermost last):
    File "<stdin>", line 1, in ?
    IOError: (2, 'No such file or directory')

If you use exception handling, you can catch the error, display a helpful message, and take the appropriate action. For example, a revised version of the code attempts to open the same file within a try statement. If an IOError error is encountered, the except statement catches the IOError exception and assigns the exception's value to the variable error.

.. code-block::

    >>> try:
    ...     outputFile = open('foam.txt')   
    ... except IOError,error:
    ...     print 'Exception trapped: ', error
    ...
    Exception trapped:  (2, 'No such file or directory')

You can raise your own exceptions by providing the error type and the error message to the raise statement. The following example script raises an exception and displays a message if the function myFunction encounters a problem.

.. code-block:: python2

    def myFunction(x,y):

        if y == 0:
            raise ValueError, 'y argument cannot be zero'
        else:
            return x/y

    try:
        print myFunction(temperature, velocity)
    except ValueError, error:
        print error

Exception handling is discussed in more detail in Error handling in the :doc:`/references`.

.. _functions-and-modules:

Functions and modules
---------------------

When you start Python from a local window or from Abaqus/CAE, the Python interpreter is aware of a limited set of built-in functions. For example, try entering the following at the Python prompt:

.. code-block:: python2

    >>> myName = 'Einstein'
    >>> len(myName)

Python returns the number 8, indicating the length of the string `myName`. The `len()` function is a built-in function and is always available when you are using Python. To see a list of the built-in functions provided by Python, type `dir(__builtins__)` at the Python prompt.

`dir(__builtins__)` is typed as dir(underscore underscorebuiltinsunderscore underscore). You have seen this underscore underscore notation already in Sequences.

In addition, you can look at the standard Python documentation on the official Python website (http:www.python.org) for a list of built-in functions. Built-in functions are described in the Built-in Functions section of the Python Library Reference.

Many functions, however, are not built-in; for example, most of the math functions, such as `sin()` and `cos()`, are not available when you start Python. Functions that are not built-in are defined in modules. Modules are a way of grouping functionality and are similar to a Fortran library of subroutines. For example, the following code could be the opening lines of a Python script. The code imports the Python module `sys` and uses the `argv` member of `sys` to print the command line arguments:

.. code-block:: python2

    import sys
    for argument in sys.argv:
        print argument

You must first import the module to make its functions, names, and functionality available to the Python interpreter. Try the following:


.. code-block:: python2

    >>> from math import *
    >>> x = pi/4.0
    >>> sin(x)
    0.707106781187

The first line imports all of the names from the math module. The second line uses `pi`, a float number defined in the math module. The third line refers to a `sin()` function. Python can use the `sin()` function because you imported it from the math module.

To import only the `sin()` function, you could have typed


.. code-block:: python2

    >>> from math import sin

You need to import a module only once during a session. Once a module is imported, its functions, methods, and attributes are always available to you. You cannot unload a module after you import it.

To see a list of all the functions that come with the math module, look at the Miscellaneous Services section of the Python Library Reference. You can download public-domain modules, and you can create your own modules.

Python provides a second approach to importing modules. For example,


.. code-block:: python2

    >>> import math
    >>> x = 22.0/(7.0 * 4.0)
    >>> math.sin(x)
    0.707330278085

The `import` approach shown above imports the module as a unit, and you must qualify the name of an object from the module. To access a function from the `math` module in our example, you must prepend the function with `math.`; the `math.` statement is said to qualify the `sin()` function.

What is the difference between the two approaches to importing modules? If two modules contain an object with the same name, Python cannot distinguish between the objects if you use the `from modulename import *` approach. If two objects have the same name, Python uses the object most recently imported. However, if you use the `import modulename` approach, modulename qualifies the name of the object and makes it unique.

Writing your own modules
------------------------

You can create your own module containing a set of Python functions. You can import this module and make use of its functions. The name of the module to import is the same as the name of the file containing the functions without the `.py` file suffix.

For example, you can create a module called myUtilities by copying a modified version of the function that calculates the distance from a point to the origin into a file called myUtilities.py.

.. code-block:: python2

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

.. code-block:: python2

    import myUtilities

    distance = myUtilities.distance(30, 50)

You can use the `__doc__` method to obtain the documentation string from a module. For example,

.. code-block:: python2

    myUtilities.__doc__
    ' myUtilities - a module of mathematical functions'

A tool for finding bugs in your modules is provided with Abaqus. The tool is called pychecker. When you import a module, pychecker prints warnings for any problems it finds with the Python source code. For example,

.. code-block:: python2

    >>> from pychecker import checker
    >>> import myUtilities
    d:\users\smith\myUtilities.py:3: Imported module (sys) not used
    d:\users\smith\myUtilities.py:14: Local variable (a) not used
    d:\users\smith\myUtilities.py:18: No global (b) found

For more information about `pychecker`, see the official Python website (https://www.python.org)

If you import a module during an interactive session using the command line interface and then make changes to the module, Python will not recognize your changes until you reload the module; for example:

.. code-block:: python2

    import myModule
    maxStress = myModule.calculateStress(odb)

    # Edit myModule.py and modify the calculateStress method.

    reload(myModule)
    maxStress = myModule.calculateStress(odb)