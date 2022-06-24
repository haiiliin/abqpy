=========================================
Printing variables using formatted output
=========================================

Python provides a print function that displays the value of a variable. For example,

.. code-block:: python

    >>> freq = 22.0/7.0
    >>> x = 7.234
    >>> print 'Vibration frequency = ', freq
    Vibration frequency =  3.14285714286
    >>> print 'Vibration frequency = ', freq, 'Displacement = ', x
    Vibration frequency =  3.14285714286 Displacement = 7.234

The string modulus operator % allows you to format your output. The %s operator in the following example converts the variables to strings.

.. code-block:: python

    >>> print 'Vibration frequency = %s Displacement = %s' % (freq, x)
    Vibration frequency = 3.14285714286 Displacement = 7.234

The `%f` operator specifies floating point notation and indicates the total number of characters to print and the number of decimal places.

.. code-block:: python

    >>> print 'Vibration frequency = %6.2f Displacement = %6.2f' % (freq, x)
    Vibration frequency =   3.14 Displacement =   7.23

The `%E` operator specifies scientific notation and indicates the number of decimal places.

.. code-block:: python

    >>> print 'Vibration frequency = %.6E Displacement = %.2E' % (freq, x)
    Vibration frequency = 3.142857E+00 Displacement = 7.23E+00

The following list includes some additional useful printing operators.
The `+` flag indicates that a number should include a sign.

The `\\n` escape sequence inserts a new line.

The `\\t` escape sequence inserts a tab character.

For example,

.. code-block:: python

    >>> print 'Vibration frequency = %+.6E\nDisplacement = %+.2E' % (freq, x)
    Vibration frequency = +3.142857E+00
    Displacement = +7.23E+00