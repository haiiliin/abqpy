# The basics of Python

The following sections introduce you to the basics of the Python language.

## Variable names and assignment

The expression

```python2
>>> myName = 'Einstein'
```

creates a variable called `myName` that refers to a String object.

To see the value of a variable or expression, simply type the variable name or the expression at the Python prompt, and press **Enter**. For example,

```python2
>>> myName = 'Einstein'
>>> myName
'Einstein'
>>> 3.0 / 4.0
0.75
>>> x = 3.0 / 4.0
>>> x
0.75
```

Python creates a variable when you assign a value to it. Python provides several forms of the assignment statement; for example,

```python2
>>> myName = 'Einstein'
>>> myName, yourName = 'Einstein', 'Newton'
>>> myName = yourName = 'Einstein'
```

The second line assigns the string 'Einstein' to the variable myName and assigns the string 'Newton' to the variable yourName. The third line assigns the string 'Einstein' to both myName and yourName.

The following naming rules apply:

- Variable names must start with a letter or an underscore character and can contain any number of letters, digits, or underscores. load_3 and \_frictionStep are legal variable names; 3load, load_3\$, and \$frictionStep are not legal names. There is no limit on the length of a variable name.
- Some words are reserved and cannot be used to name a variable; for example, print, while, return, and class.
- Python is case sensitive. A variable named Load is different from a variable named load.

When you assign a variable in a Python program, the variable refers to a Python object, but the variable is not an object itself. For example, the expression numSpokes=3 creates a variable that refers to an integer object; however, numSpokes is not an object. You can change the object to which a variable refers. numSpokes can refer to a real number on one line, an integer on the next line, and a viewport on the next line.

The first example script in {doc}`/user/about/examples/create-part` created a model using the following statement:

```python2
myModel = mdb.Model(name='Model A')
```

The constructor `mdb.Model(name='Model A')` creates an instance of a model, and this instance is a Python object. The object created is `mdb.models['Model A']`, and the variable myModel refers to this object.

An object always has a type. In our example the type of `mdb.models['Model A']` is Model. An object's type cannot be changed. The type defines the data encapsulated by an object—its members—and the functions that can manipulate those data—its methods. Unlike most programming languages, you do not need to declare the type of a variable before you use it. Python determines the type when the assignment statement is executed. The Abaqus Scripting Interface uses the term object to refer to a specific Abaqus type as well as to an instance of that type; for example, a Model object refers to a Model type and to an instance of a Model type.

(python-data-types)=

## Python data types

Python includes the following built-in data types:

### Integer

To create variables called i and j that refer to integer objects, type the following at the Python prompt:

```python2
>>> i = 20
>>> j = 64
```

An integer is based on a C long and can be compared to a Fortran integer\*4 or \*8. For extremely large integer values, you should declare a long integer. The size of a long integer is essentially unlimited. The L at the end of the number indicates that it is a long integer.

```python2
>>> nodes = 2000000L
>>> bigNumber = 120L**21
```

Use int(*n*) to convert a variable to an integer; use long(*n*) to convert a variable to a long integer.

```python2
>>> load  = 279.86
>>> iLoad = int(load)
>>> iLoad
279
>>> a = 2
>>> b = 64
>>> bigNumber = long(a)**b
>>> print 'bigNumber = ', bigNumber
bigNumber = 18446744073709551616
```

:::{note}
All Abaqus Scripting Interface object types begin with an uppercase character; for example, a Part or a Viewport. An integer is another kind of object and follows the same convention. The Abaqus Scripting Interface refers to an integer object as an Int. Similarly, the Abaqus Scripting Interface refers to a floating-point object as a Float.
:::

### Float

Floats represent floating-point numbers or real numbers. You can use exponential notation for floats.

```python2
>>> pi   = 22.0/7.0
>>> r    = 2.345e-6
>>> area = pi * r * r
>>> print 'Area = ', area
Area =  1.728265e-11
```

A float is based on a C double and can be compared to a Fortran real\*8. Use float(**n**) to convert a variable to a float.

### Complex

Complex numbers use the j notation to indicate the imaginary part of the number. Python provides methods to manipulate complex numbers. The conjugate method calculates the conjugate of a complex number.

```python2
>>> a = 2 + 4j
>>> a.conjugate()
(2-4j)
```

A complex number has two members, the real member and the imaginary member.

```python2
>>> a = 2 + 4j
>>> a.real
2.0
>>> a.imag
4.0
```

Python provides complex math functions to operate on complex variables. You need to import the cmath module to use the complex square root function.

```python2
>>> import cmath
>>> y = 3 + 4j
>>> print cmath.sqrt(y)
(2+1j)
```

Remember, functions of a type are called methods; data of a type are called members. In our example conjugate is a method of a complex type; a.real refers to the real member of a complex type.

### Sequences

Sequences include strings, lists, tuples, and arrays. Sequences are described in [sequences] and [sequence operations].

## Determining the type of a variable

You use the `type()` function to return the type of the object to which a variable refers.

```python2
>>> a = 2.375
>>> type(a)
<type 'float'>
>>> a = 1
>>> type(a)
<type 'int'>
>>> a = 'chamfer'
>>> type(a)
<type 'string'>
```

(sequences-1)=

## Sequences

Sequences are important and powerful data types in Python. A sequence is an object containing a series of objects. There are three types of built-in sequences in Python—list, tuple, and string. In addition, imported modules allow you to use arrays in your scripts. The following table describes the characteristics of list, tuple, string, and array sequences.

- Mutable: Elements can be added, changed, and removed.
- Homogeneous: Elements must be of the same type.
- Methods: The type has methods that can be used to manipulate the sequence; for example, `sort()`, `reverse()`.
- Syntax: The syntax used to create the sequence.

### List

Lists are mutable heterogeneous sequences (anything that can be modified is called mutable). A list can be a sequence of strings, integers, floats, or any combination of these. In fact, a list can contain any type of object; for example,

```python2
>>> myIntegerList = [7,6,5,4]
>>> myFloatList  = [7.1,6.5,5.3,4.8]
```

You can refer to individual items from a sequence using the index of the item. Indices start at zero. Negative indices count backward from the end of a sequence.

```python2
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
```

Lists are heterogeneous, which means they can contain objects of different type.

```python2
>>> myList=[1,2.5,'steel']
```

A list can contain other lists.

```python2
>>> myList=[[0,1,2],[3,4,5],[6,7,8]]
>>> myList[0]
[0, 1, 2]
>>> myList[2]
[6,7,8]
```

`myList[1][2]` refers to the third item in the second list. Remember, indices start at zero.

```python2
>>> myList[1][2]
5
```

Python has built-in methods that allow you to operate on the items in a sequence.

```python2
>>> myList
[1, 9, 3]
>>> myList.append(33)
>>> myList
[1, 9, 3, 33]
>>> myList.remove(9)
>>> myList
[1, 3, 33]
```

The following are some additional built-in methods that operate on lists:

- `count()`

  Return the number of times a value appears in the list.

  ```python2
  >>> myList = [0,1,2,1,2,3,2,3,4,3,4,5]
  >>> myList.count(2)
  3
  ```

- `index()`

  Return the index indicating the first time an item appears in the list.

  ```python2
  >>> myList.index(5)
  11
  >>> myList.index(4)
  8
  ```

- `insert()`

  Insert a new element into a list at a specified location.

  ```python2
  >>> myList.insert(2,22)
  >>> myList
  [0, 1, 22, 2, 1, 2, 3, 2, 3, 4, 3, 4, 5]
  ```

- `reverse()`

  Reverse the elements in a list.

  ```python2
  >>> myList.reverse()
  >>> myList
  [5, 4, 3, 4, 3, 2, 3, 2, 1, 2, 22, 1, 0]
  ```

- `sort()`

  Sort the elements in a list.

  ```python2
  >>> myList.sort()
  >>> myList
  [0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 22]
  ```

### Tuple

Tuples are very similar to lists; however, they are immutable heterogeneous sequences, which means that you cannot change them after you create them. You can think of a tuple as a list that cannot be modified. Tuples have no methods; you cannot append items to a tuple, and you cannot modify or delete the items in a tuple. The following statement creates an empty tuple:

```python2
myTuple = ()
```

The following statement creates a tuple with one element:

```python2
myTuple = (5.675,)
```

You can use the `tuple()` function to convert a list or a string to a tuple.

```python2
>>> myList = [1, 2, "stress", 4.67]
>>> myTuple = tuple(myList)
>>> print myTuple
(1, 2, 'stress', 4.67)
>>> myString = 'Failure mode'
>>> myTuple = tuple(myString)
>>> print myTuple
('F', 'a', 'i', 'l', 'u', 'r', 'e', ' ', 'm', 'o', 'd', 'e')
```

The following statements create a tuple and then try to change the value of an item in the tuple. An `AttributeError` error message is generated because a tuple is immutable.

```
>>> myTuple = (1,2,3,4,5)
>>> type(myTuple)
<type 'tuple'>
>>> myTuple[2]=3
Traceback (innermost last):
File "", line 1, in ?
AttributeError: __setitem__
```

### String

Strings are immutable sequences of characters. Strings are defined by single or double quotation marks. You can use the + operator to concatenate two strings and create a third string; for example,

```python2
>>> odbString = "Symbol plot from "
>>> odb = 'load1.odb'
>>> annotationString = odbString + odb
>>> print annotationString
Symbol plot from load1.odb
```

:::{note}
You can also use the + operator to concatenate tuples and lists.
:::

Python provides a set of functions that operate on strings.

```python2
>>> annotationString
'Symbol plot from load1.odb'
>>> annotationString.upper()
'SYMBOL PLOT FROM LOAD1.ODB'
>>> annotationString.split()
['Symbol', 'plot', 'from', 'load1.odb']
```

As with all sequences, you use negative indices to index backward from the end of a string.

```python2
>>> axis_label = 'maxstrain'
>>> axis_label[-1]
'n'
```

Use the built-in str function to convert an object to a string.

```python2
>>> myList = [8, 9, 10]
>>> str(myList)
'[8, 9, 10]'
```

Look at the standard Python documentation on the official Python website (<https://www.python.org>) for a list of common string operations. String functions are described in the String Services section of the Python Library Reference.

### Array

Arrays are mutable homogeneous sequences. The numpy module allows you to create and operate on multidimensional arrays. Python determines the type of elements in the array; you do not have to declare the type when you create the array. For more information about the numpy module, see <https://numpy.org>.

```python2
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
```

(sequence-operations)=

## Sequence operations

Python provides a set of tools that allow you to operate on a sequence.

### Slicing

Sequences can be divided into smaller sequences. This operation is called slicing. The expression sequence\[m:n\] returns a copy of sequence from m to n−1. The default value for m is zero; the default value for n is the length of the sequence.

```python2
>>> myList = [0,1,2,3,4]
>>> myList[1:4]
[1, 2, 3]
>>> myString ='linear load'
>>> myString[7:]
'load'
>>> myString[:6]
'linear'
```

### Repeat a sequence

```python2
>>> x=(1,2)
>>> x*2
(1, 2, 1, 2)
>>> s = 'Hoop Stress'
>>> s*2
>>> 'Hoop StressHoop Stress'
```

### Determine the length of a sequence

```python2
>>> myString ='linear load'
>>> len(myString)
11
>>> myList = [0,1,2,3,4]
>>> len(myList)
5
```

### Concatenate sequences

```python2
>>> a = [0,1]
>>> b = [9,8]
>>> a + b
[0, 1, 9, 8]
>>> test = 'wing34'
>>> fileExtension = '.odb'
>>> test+fileExtension
'wing34.odb'
```

### Range

The `range()` function generates a list containing a sequence of integers. You can use the `range()` function to control iterative loops. The arguments to range are start (the starting value), end (the ending value plus one), and step (the step between each value). The start and step arguments are optional; the default start argument is 0, and the default step argument is 1. The arguments must be integers.

```python2
>>> range(2,8)
[2, 3, 4, 5, 6, 7]
>>> range(4)
[0, 1, 2, 3]
>>> range(1,8,2)
[1, 3, 5, 7]
```

### Convert a sequence type

Convert a sequence to a list or a tuple.

```python2
>>> myString='noise'
>>> myList = list(myString) #Convert a string to a list.
>>> myList[0] = 'p'
>>> myList
['p', 'o', 'i', 's', 'e']
>>> myTuple = tuple(myString) #Convert a string to a tuple.
>>> print myTuple
('n', 'o', 'i', 's', 'e')
```

(python-none)=

## Python None

Python defines a special object called the None object or Python None that represents an empty value. The None object is returned by functions and methods that do not have a return value. The None object has no value and prints as None. For example

```python2
>>> a = [1, 3, 7, 5]
>>> print a.sort()
None
>>> import sys
>>> x = sys.path.append('.')
>>> print x
None
```

## Continuation lines and comments

You can continue a statement on the following line if you break the statement between a set of (), {}, or \[\] delimiters. For example, look at the tuple that was used in {doc}`/user/about/examples/create-part` to assign the coordinates of the vertices to a variable:

```python2
xyCoordsOuter = ((-10, 30), (10, 30), (40, -30),
    (30, -30), (20, -10), (-20, -10),
    (-30, -30), (-40, -30), (-10, 30))
```

If a statement breaks at any other place, you must include a \\ character at the end of the line to indicate that it is continued on the next line. For example,

```python2
distance = mdb.models['Model-1'].parts['housing'].\
    getDistance(entity1=node1, entity2=node2)
```

When you are running Python from a local Linux or Windows window, the prompt changes to the . . . characters to indicate that you are on a continuation line.
Comments in a Python script begin with the # character and continue to the end of the line.

```python2
>>> # Define material constants
>>> modulus = 1e6 # Define Young's modulus
```

## Printing variables using formatted output

Python provides a print function that displays the value of a variable. For example,

```python2
>>> freq = 22.0/7.0
>>> x = 7.234
>>> print 'Vibration frequency = ', freq
Vibration frequency =  3.14285714286
>>> print 'Vibration frequency = ', freq, 'Displacement = ', x
Vibration frequency =  3.14285714286 Displacement = 7.234
```

The string modulus operator % allows you to format your output. The %s operator in the following example converts the variables to strings.

```python2
>>> print 'Vibration frequency = %s Displacement = %s' % (freq, x)
Vibration frequency = 3.14285714286 Displacement = 7.234
```

The `%f` operator specifies floating point notation and indicates the total number of characters to print and the number of decimal places.

```python2
>>> print 'Vibration frequency = %6.2f Displacement = %6.2f' % (freq, x)
Vibration frequency =   3.14 Displacement =   7.23
```

The `%E` operator specifies scientific notation and indicates the number of decimal places.

```python2
>>> print 'Vibration frequency = %.6E Displacement = %.2E' % (freq, x)
Vibration frequency = 3.142857E+00 Displacement = 7.23E+00
```

The following list includes some additional useful printing operators.
The `+` flag indicates that a number should include a sign.

The `\\n` escape sequence inserts a new line.

The `\\t` escape sequence inserts a tab character.

For example,

```python2
>>> print 'Vibration frequency = %+.6E\nDisplacement = %+.2E' % (freq, x)
Vibration frequency = +3.142857E+00
Displacement = +7.23E+00
```

## Control blocks

Python does not use a special character, such as }, to signify the end of a control block such as an if statement. Instead, Python uses indentation to indicate the end of a control block. You define the indentation that governs a block. When your script returns to the original indentation, the block ends. For example,

```python2
max = 5
i = 0
while i <= max:
    square = i**2
    cube = i**3
    print i, square, cube
    i = i + 1
print 'Loop completed'
```

When you are using the Python interpreter from the Abaqus/CAE command line interface or if you are running Python from a local Linux or Windows window, the prompt changes to the "..."" characters to indicate that you are in a block controlled by indentation.

### if, elif, and else

```python2
>>> load = 10
>>> if load > 6.75:
...     print 'Reached critical load'
... elif load < 2.75:
...     print 'Minimal load'
... else:
...     print 'Typical load'
```

### while

```python2
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
```

Use `continue` to skip the rest of the loop and to go to the next iteration.

```python2
>>> load   = 10
>>> length = -3
>>> while load < 1E6:  #Continue jumps up here
...     load = load * length
...     if load < 0:
...         continue   #Do not print if negative
...     print load
```

### for

Use a sequence to control the start and the end of for loops. The `range()` function is an easy way to create a sequence.

```python2
>>> for i in range(5):
...     print i
...
0
1
2
3
4
```
