==================
Using dictionaries
==================

Dictionaries are a powerful tool in Python. A dictionary maps a variable to a set of data, much like a real dictionary maps a word to its definition, its pronunciation, and its synonyms. Dictionaries are similar to lists in that they are not homogeneous and can contain objects of any type. To access an object in a list, you provide the integer index that specifies the position of the object in the list. For example,

.. code-block:: python

    >>> myList = [6,2,9]
    >>> myList[1]
    2

In contrast, you access an object in a dictionary through its key, which can be a string, an integer, or any type of immutable Python object. There is no implicit order to the keys in a dictionary. In most cases you will assign a string to the dictionary key. The key then becomes a more intuitive way to access the elements in a dictionary. You use square brackets and the dictionary key to access a particular object. For example,

.. code-block:: python

    >>> myPart = {}  #Create an empty dictionary
    >>> myPart['size'] = 3.0
    >>> myPart['material'] = 'Steel'
    >>> myPart['color'] = 'Red'
    >>> myPart['number'] = 667

You can add dictionary keys at any time.

.. code-block:: python

    >>> myPart['weight'] = 376.0
    >>> myPart['cost'] = 10.34

You use the key to access an item in a dictionary.

.. code-block:: python

    >>> costOverWeight = myPart['cost'] / myPart['weight']
    >>> costOverWeight
    0.0275
    >>> description = myPart['color'] + myPart['material']
    >>> description
    'RedSteel'

Dictionaries are not sequences, and you cannot apply sequence methods such as slicing and concatenating to dictionaries. Dictionaries have their own methods. The following statement lists the methods of the dictionary myPart.

.. code-block:: python

    >>> myPart.__methods__
    ['clear', 'copy', 'get', 'has_key', 'items', 'keys', 
    'update', 'values']

The `keys()` method returns a list of the dictionary keys.

.. code-block:: python

    >>> myPart.keys()
    ['size', 'weight', 'number', 'material', 'cost', 'color']

The `values()` method returns a list of the values of each entry in the dictionary.

.. code-block:: python

    >>> myPart.values()
    [3.0, 376.0, 667, 'Steel', 10.34, 'Red']

The `items()` method returns a list of tuples. Each tuple contains the key and its value.

.. code-block:: python

    >>> myPart.items() 
    [('size', 3.0), ('number', 667),   ('material', 'Steel'),
    ('color', 'Red'),   ('weight', 376.0), ('cost', 10.34),]

You use the `has_key()` method to see if a key exists. A return value of 1 indicates the key exists in the dictionary. A return value of 0 indicates the key does not exist.

.. code-block:: python

    >>> myPart.has_key('color')
    1

Python's del statement allows you to delete a variable.

.. code-block:: python

    >>> del myPart

You can also use del to delete an item from a dictionary.

.. code-block:: python

    >>> del myPart['color']
    >>> myPart.has_key('color')
    0

You can use the `keys()`, `values()`, or `items()` methods to loop through a dictionary. In the following example, `items()` returns two values; the first is assigned to property, and the second is assigned to setting.

.. code-block:: python

    >>> for property, setting in myPart.items():
    ...     print property, setting
    ... 
    size 3.0
    weight 376.0
    number 667
    material Steel
    cost 10.34