===================
Sequence operations
===================

Python provides a set of tools that allow you to operate on a sequence.

Slicing
-------

Sequences can be divided into smaller sequences. This operation is called slicing. The expression sequence[m:n] returns a copy of sequence from m to n−1. The default value for m is zero; the default value for n is the length of the sequence.

.. code-block:: python

    >>> myList = [0,1,2,3,4]
    >>> myList[1:4]
    [1, 2, 3]
    >>> myString ='linear load'
    >>> myString[7:]
    'load'
    >>> myString[:6]
    'linear'

Repeat a sequence
-----------------

.. code-block:: python

    >>> x=(1,2)
    >>> x*2
    (1, 2, 1, 2)
    >>> s = 'Hoop Stress'
    >>> s*2
    >>> 'Hoop StressHoop Stress'

Determine the length of a sequence
----------------------------------


.. code-block:: python

    >>> myString ='linear load'
    >>> len(myString)
    11
    >>> myList = [0,1,2,3,4]
    >>> len(myList)
    5

Concatenate sequences
---------------------

.. code-block:: python

    >>> a = [0,1]
    >>> b = [9,8]
    >>> a + b
    [0, 1, 9, 8]
    >>> test = 'wing34'
    >>> fileExtension = '.odb'
    >>> test+fileExtension
    'wing34.odb'

Range
-----

The `range()` function generates a list containing a sequence of integers. You can use the `range()` function to control iterative loops. The arguments to range are start (the starting value), end (the ending value plus one), and step (the step between each value). The start and step arguments are optional; the default start argument is 0, and the default step argument is 1. The arguments must be integers.

.. code-block:: python

    >>> range(2,8)
    [2, 3, 4, 5, 6, 7]
    >>> range(4)
    [0, 1, 2, 3]
    >>> range(1,8,2)
    [1, 3, 5, 7]

Convert a sequence type
-----------------------

Convert a sequence to a list or a tuple.

.. code-block:: python

    >>> myString='noise'
    >>> myList = list(myString) #Convert a string to a list.
    >>> myList[0] = 'p'
    >>> myList
    ['p', 'o', 'i', 's', 'e']
    >>> myTuple = tuple(myString) #Convert a string to a tuple.
    >>> print myTuple
    ('n', 'o', 'i', 's', 'e')