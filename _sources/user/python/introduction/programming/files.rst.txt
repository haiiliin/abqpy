==============================
Reading and writing from files
==============================

Many of the file commands are built-in Python commands. You do not have to import a module to use file commands. You use the open() function to create a file.

.. code-block:: python

    >>> myInputFile  = open('crash_test/fender.txt','r')
    >>> myOutputFile = open('peak_deflection.txt','w+')

The first line opens an existing file in the crash_test directory called fender.txt. The file is opened in read-only mode; myInputFile is a variable that refers to a file object. The second line creates and opens a new file object in the local directory called peak_deflection.txt. This file is opened in read and write mode.

Use the `__methods__` technique that we saw earlier to see the methods of a file object.

.. code-block:: python

    >>> myOutputFile = open('peak_deflection.txt','w')
    >>> myOutputFile.__methods__
    ['close', 'fileno', 'flush', 'isatty', 'read', 
    'readinto', 'readline', 'readlines', 'seek', 'tell', 
    'truncate', 'write', 'writelines']

The `readline()` method reads a single line from a file into a string, including the new line character that terminates the string. The `readlines()` method reads all the lines in a file into a list. The `write()` function writes a string to a file. Look at the standard Python documentation on the official Python website (https://www.python.org) for a description of functions that operate on files. File objects are described in the Built-in Types section of the Python Library Reference.

The following example reads each line of a text file and changes the line to uppercase characters:

.. code-block:: python

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