=============================
Variable names and assignment
=============================

The expression

.. code-block:: python

    >>> myName = 'Einstein'

creates a variable called `myName` that refers to a String object.

To see the value of a variable or expression, simply type the variable name or the expression at the Python prompt, and press **Enter**. For example,

.. code-block:: python

    >>> myName = 'Einstein'
    >>> myName
    'Einstein'
    >>> 3.0 / 4.0
    0.75
    >>> x = 3.0 / 4.0
    >>> x
    0.75

Python creates a variable when you assign a value to it. Python provides several forms of the assignment statement; for example,

.. code-block:: python

    >>> myName = 'Einstein'
    >>> myName, yourName = 'Einstein', 'Newton'
    >>> myName = yourName = 'Einstein'

The second line assigns the string 'Einstein' to the variable myName and assigns the string 'Newton' to the variable yourName. The third line assigns the string 'Einstein' to both myName and yourName.

The following naming rules apply:

- Variable names must start with a letter or an underscore character and can contain any number of letters, digits, or underscores. load_3 and _frictionStep are legal variable names; 3load, load_3$, and $frictionStep are not legal names. There is no limit on the length of a variable name.
- Some words are reserved and cannot be used to name a variable; for example, print, while, return, and class.
- Python is case sensitive. A variable named Load is different from a variable named load.

When you assign a variable in a Python program, the variable refers to a Python object, but the variable is not an object itself. For example, the expression numSpokes=3 creates a variable that refers to an integer object; however, numSpokes is not an object. You can change the object to which a variable refers. numSpokes can refer to a real number on one line, an integer on the next line, and a viewport on the next line.

The first example script in :doc:`/user/about/examples/create-part` created a model using the following statement:

.. code-block:: python

    myModel = mdb.Model(name='Model A')

The constructor `mdb.Model(name='Model A')` creates an instance of a model, and this instance is a Python object. The object created is `mdb.models['Model A']`, and the variable myModel refers to this object.

An object always has a type. In our example the type of `mdb.models['Model A']` is Model. An object's type cannot be changed. The type defines the data encapsulated by an object—its members—and the functions that can manipulate those data—its methods. Unlike most programming languages, you do not need to declare the type of a variable before you use it. Python determines the type when the assignment statement is executed. The Abaqus Scripting Interface uses the term object to refer to a specific Abaqus type as well as to an instance of that type; for example, a Model object refers to a Model type and to an instance of a Model type.