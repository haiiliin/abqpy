=========
Sequences
=========

Sequences are important and powerful data types in Python. A sequence is an object containing a series of objects. There are three types of built-in sequences in Python—list, tuple, and string. In addition, imported modules allow you to use arrays in your scripts. The following table describes the characteristics of list, tuple, string, and array sequences.

- Mutable: Elements can be added, changed, and removed.
- Homogeneous: Elements must be of the same type.
- Methods: The type has methods that can be used to manipulate the sequence; for example, `sort()`, `reverse()`.
- Syntax: The syntax used to create the sequence.

List
----

Lists are mutable heterogeneous sequences (anything that can be modified is called mutable). A list can be a sequence of strings, integers, floats, or any combination of these. In fact, a list can contain any type of object; for example,

.. code-block:: python

    >>> myIntegerList = [7,6,5,4]
    >>> myFloatList  = [7.1,6.5,5.3,4.8]

You can refer to individual items from a sequence using the index of the item. Indices start at zero. Negative indices count backward from the end of a sequence.

.. code-block:: python

    >>> myList = [1,2,3]
    >>> myList[0]
    1
    >>> myList[1] = 9
    >>> myList
    [1, 9, 3]
    >>> myNewList = [1.0,2.0,myList]
    >>> myNewList
    [1.0, 2.0, [1, 9, 3]]
    >>> myNewList[-1]
    [1, 9, 3]

Lists are heterogeneous, which means they can contain objects of different type.

.. code-block:: python

    >>> myList=[1,2.5,'steel']

A list can contain other lists.

.. code-block:: python

    >>> myList=[[0,1,2],[3,4,5],[6,7,8]] 
    >>> myList[0]
    [0, 1, 2]
    >>> myList[2]
    [6,7,8]

`myList[1][2]` refers to the third item in the second list. Remember, indices start at zero.

.. code-block:: python

    >>> myList[1][2]
    5

Python has built-in methods that allow you to operate on the items in a sequence.

.. code-block:: python

    >>> myList
    [1, 9, 3]
    >>> myList.append(33)
    >>> myList
    [1, 9, 3, 33]
    >>> myList.remove(9)
    >>> myList
    [1, 3, 33]
    
The following are some additional built-in methods that operate on lists:

- `count()`
  
  Return the number of times a value appears in the list.

  .. code-block:: python

      >>> myList = [0,1,2,1,2,3,2,3,4,3,4,5]
      >>> myList.count(2)
      3

- `index()`
  
  Return the index indicating the first time an item appears in the list.

  .. code-block:: python

      >>> myList.index(5)
      11
      >>> myList.index(4)
      8

- `insert()`
  
  Insert a new element into a list at a specified location.

  .. code-block:: python

      >>> myList.insert(2,22)   
      >>> myList
      [0, 1, 22, 2, 1, 2, 3, 2, 3, 4, 3, 4, 5]
  
- `reverse()`
  
  Reverse the elements in a list.
  

  .. code-block:: python

      >>> myList.reverse()
      >>> myList
      [5, 4, 3, 4, 3, 2, 3, 2, 1, 2, 22, 1, 0]
  
- `sort()`
  
  Sort the elements in a list.

  .. code-block:: python
  
      >>> myList.sort()
      >>> myList
      [0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 22]

Tuple
-----

Tuples are very similar to lists; however, they are immutable heterogeneous sequences, which means that you cannot change them after you create them. You can think of a tuple as a list that cannot be modified. Tuples have no methods; you cannot append items to a tuple, and you cannot modify or delete the items in a tuple. The following statement creates an empty tuple:

.. code-block:: python

    myTuple = ()

The following statement creates a tuple with one element:

.. code-block:: python

    myTuple = (5.675,)

You can use the `tuple()` function to convert a list or a string to a tuple.

.. code-block:: python

    >>> myList = [1, 2, "stress", 4.67]
    >>> myTuple = tuple(myList)
    >>> print myTuple
    (1, 2, 'stress', 4.67)
    >>> myString = 'Failure mode'
    >>> myTuple = tuple(myString)
    >>> print myTuple
    ('F', 'a', 'i', 'l', 'u', 'r', 'e', ' ', 'm', 'o', 'd', 'e')

The following statements create a tuple and then try to change the value of an item in the tuple. An `AttributeError` error message is generated because a tuple is immutable.

.. code-block:: python

    >>> myTuple = (1,2,3,4,5)
    >>> type(myTuple)
    <type 'tuple'>
    >>> myTuple[2]=3
    Traceback (innermost last):
    File "", line 1, in ?
    AttributeError: __setitem__

String
------

Strings are immutable sequences of characters. Strings are defined by single or double quotation marks. You can use the + operator to concatenate two strings and create a third string; for example,

.. code-block:: python

    >>> odbString = "Symbol plot from "
    >>> odb = 'load1.odb'
    >>> annotationString = odbString + odb
    >>> print annotationString
    Symbol plot from load1.odb


.. note::

    You can also use the + operator to concatenate tuples and lists.

Python provides a set of functions that operate on strings.

.. code-block:: python

    >>> annotationString
    'Symbol plot from load1.odb'
    >>> annotationString.upper()
    'SYMBOL PLOT FROM LOAD1.ODB'
    >>> annotationString.split()
    ['Symbol', 'plot', 'from', 'load1.odb']
    
As with all sequences, you use negative indices to index backward from the end of a string.

.. code-block:: python

    >>> axis_label = 'maxstrain'
    >>> axis_label[-1]
    'n'

Use the built-in str function to convert an object to a string.

.. code-block:: python

    >>> myList = [8, 9, 10]
    >>> str(myList)
    '[8, 9, 10]'

Look at the standard Python documentation on the official Python website (https://www.python.org) for a list of common string operations. String functions are described in the String Services section of the Python Library Reference.

Array
-----

Arrays are mutable homogeneous sequences. The numpy module allows you to create and operate on multidimensional arrays. Python determines the type of elements in the array; you do not have to declare the type when you create the array. For more information about the numpy module, see https://numpy.org.

.. code-block:: python

    >>> from numpy import array
    >>> myIntegerArray = array([[1,2],[2,3],[3,4]])
    >>> myIntegerArray
    array([[1, 2], 
           [2, 3], 
           [3, 4]])
    >>> myRealArray =array([[1.0,2],[2,3],[3,4]])
    >>> myRealArray
    array([[1., 2.], 
           [2., 3.], 
           [3., 4.]])
    >>> myRealArray * myIntegerArray
    array([[  1.,   4.],
           [  4.,   9.],
           [  9.,  16.]])