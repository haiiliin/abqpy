=================
Python data types
=================

Python includes the following built-in data types:

Integer
-------

To create variables called i and j that refer to integer objects, type the following at the Python prompt:

.. code-block:: python

    >>> i = 20
    >>> j = 64

An integer is based on a C long and can be compared to a Fortran integer\*4 or \*8. For extremely large integer values, you should declare a long integer. The size of a long integer is essentially unlimited. The L at the end of the number indicates that it is a long integer.

.. code-block:: python

    >>> nodes = 2000000L
    >>> bigNumber = 120L**21

Use int(*n*) to convert a variable to an integer; use long(*n*) to convert a variable to a long integer.

.. code-block:: python
    
    >>> load  = 279.86
    >>> iLoad = int(load)
    >>> iLoad
    279
    >>> a = 2
    >>> b = 64
    >>> bigNumber = long(a)**b
    >>> print 'bigNumber = ', bigNumber
    bigNumber = 18446744073709551616


.. note::

    All Abaqus Scripting Interface object types begin with an uppercase character; for example, a Part or a Viewport. An integer is another kind of object and follows the same convention. The Abaqus Scripting Interface refers to an integer object as an Int. Similarly, the Abaqus Scripting Interface refers to a floating-point object as a Float.

Float
-----

Floats represent floating-point numbers or real numbers. You can use exponential notation for floats.

.. code-block:: python
    
    >>> pi   = 22.0/7.0
    >>> r    = 2.345e-6
    >>> area = pi * r * r
    >>> print 'Area = ', area
    Area =  1.728265e-11

A float is based on a C double and can be compared to a Fortran real\*8. Use float(**n**) to convert a variable to a float.

Complex
-------

Complex numbers use the j notation to indicate the imaginary part of the number. Python provides methods to manipulate complex numbers. The conjugate method calculates the conjugate of a complex number.

.. code-block:: python
    
    >>> a = 2 + 4j
    >>> a.conjugate()
    (2-4j)

A complex number has two members, the real member and the imaginary member.

.. code-block:: python
    
    >>> a = 2 + 4j
    >>> a.real
    2.0
    >>> a.imag
    4.0

Python provides complex math functions to operate on complex variables. You need to import the cmath module to use the complex square root function.

.. code-block:: python
    
    >>> import cmath
    >>> y = 3 + 4j
    >>> print cmath.sqrt(y)
    (2+1j)

Remember, functions of a type are called methods; data of a type are called members. In our example conjugate is a method of a complex type; a.real refers to the real member of a complex type.

Sequences
---------

Sequences include strings, lists, tuples, and arrays. Sequences are described in :doc:`sequences` and :doc:`sequence-operations`.