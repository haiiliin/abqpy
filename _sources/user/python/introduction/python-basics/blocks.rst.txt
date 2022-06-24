==============
Control blocks
==============

Python does not use a special character, such as }, to signify the end of a control block such as an if statement. Instead, Python uses indentation to indicate the end of a control block. You define the indentation that governs a block. When your script returns to the original indentation, the block ends. For example,


.. code-block:: python

    max = 5
    i = 0
    while i <= max:
        square = i**2
        cube = i**3
        print i, square, cube
        i = i + 1
    print 'Loop completed'

When you are using the Python interpreter from the Abaqus/CAE command line interface or if you are running Python from a local Linux or Windows window, the prompt changes to the "..."" characters to indicate that you are in a block controlled by indentation.

if, elif, and else
------------------

.. code-block:: python

    >>> load = 10
    >>> if load > 6.75:
    ...     print 'Reached critical load'
    ... elif load < 2.75:  
    ...     print 'Minimal load'
    ... else:
    ...     print 'Typical load'

while
-----

.. code-block:: python

    >>> load   = 10
    >>> length = 3
    >>> while load < 1E4:
    ...     load = load * length
    ...     print load
    Use `break` to break out of a loop.

    >>> while 1:
    ...     x = raw_input(Enter a number or 0 to quit:')
    ...     if x == '0':
    ...         break
    ...     else:
    ...         print x

Use `continue` to skip the rest of the loop and to go to the next iteration.

.. code-block:: python

    >>> load   = 10
    >>> length = -3
    >>> while load < 1E6:  #Continue jumps up here
    ...     load = load * length
    ...     if load < 0:
    ...         continue   #Do not print if negative
    ...     print load 

for
---

Use a sequence to control the start and the end of for loops. The `range()` function is an easy way to create a sequence.

.. code-block:: python

    >>> for i in range(5):
    ...     print i
    ...
    0 
    1
    2
    3
    4