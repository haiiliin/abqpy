# Object-oriented basics

You need to understand some of the fundamentals of object-oriented programming to understand the terms used in this guide. The following is a brief introduction to the basic concepts behind object-oriented programming.

Traditional procedural languages, such as Fortran and C, are based around functions or subroutines that perform actions. A typical example is a subroutine that calculates the geometric center of a planar part given the coordinates of each vertex.

In contrast, object-oriented programming languages, such as Python and C++, are based around objects. An object encapsulates some data and functions that are used to manipulate those data. The data encapsulated by an object are called the members of the object. The functions that manipulate the data are called methods.

An object can be modeled from a real-world object, such as a tire; or an object can be modeled from something more abstract, such as an array of nodes. For example, the data (or members) encapsulated by a tire object are its diameter, width, aspect ratio, and price. The functions or methods encapsulated by the tire object calculate how the tire deforms under load and how it wears during use. Members and methods can be shared by more than one type of object; for example, a shock absorber has a price member and a deformation method.

Classes are an important concept in object-oriented programming. Classes are defined by the programmer, and a class defines members and the methods that operate on those members. An object is an instance of a class. An object inherits the members and methods of the class from which it was instanced. You should read a Python text book for a thorough discussion of classes, abstract base classes, and inheritance.
