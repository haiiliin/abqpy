==============
Error handling
==============

When a script encounters unusual circumstances, Python allows you to modify the flow of control through the script and to take the necessary action. The action of signaling a problem during execution is called raising or throwing an exception. Recognizing the problem is called catching an exception. Taking appropriate action is called exception handling.

Python provides exception handling through the try and except commands. For example, the following statement attempts to open an existing file for reading:

.. code-block:: python

    >>> outputFile = open('foam.txt')

If the file does not exist, the statement fails, and Python displays the following error message:

.. code-block:: python

    >>> outputFile = open('foam.txt')
    Traceback (innermost last):
    File "<stdin>", line 1, in ?
    IOError: (2, 'No such file or directory')

If you use exception handling, you can catch the error, display a helpful message, and take the appropriate action. For example, a revised version of the code attempts to open the same file within a try statement. If an IOError error is encountered, the except statement catches the IOError exception and assigns the exception's value to the variable error.

.. code-block:: python

    >>> try:
    ...     outputFile = open('foam.txt')   
    ... except IOError,error:
    ...     print 'Exception trapped: ', error
    ...
    Exception trapped:  (2, 'No such file or directory')

You can raise your own exceptions by providing the error type and the error message to the raise statement. The following example script raises an exception and displays a message if the function myFunction encounters a problem.

.. code-block:: python

    def myFunction(x,y):

        if y == 0:
            raise ValueError, 'y argument cannot be zero'
        else:
            return x/y

    try:
        print myFunction(temperature, velocity)
    except ValueError, error:
        print error

Exception handling is discussed in more detail in Error handling in the :doc:`references`.