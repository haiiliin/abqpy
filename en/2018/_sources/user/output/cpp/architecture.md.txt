# The Abaqus C++ API architecture

This section describes the architecture of the Abaqus C++ interface to an output database. The output database is an object-oriented database, which means that the data are held by “objects” (C++ classes) that have certain behavior (C++ methods). The methods of an object in the database allow access to and manipulation of the data held by the object. The data members of an object can be either primitives (integer, floating point, string) or other objects.

## Class naming convention

All class names start with `odb_` to avoid possible name clashes. For example, the string class is named `odb_String`.

## Constructors

A constructor is a method that creates an object. The Abaqus C++ API uses the following three types of constructors:

- **Constructors for nonpersistent objects**

  Constructors for nonpersistent objects are the standard C++ constructors. For example,

  ```cpp
  odb_String partName("New_Part");
  ```

- **Constructors for persistent objects**

  You create a persistent object by calling a method on an existing Abaqus C++ API object. In Abaqus the convention is that the constructor method name corresponds to the name of the object created and that the first letter of the constructor name is capitalized. The object can be accessed using the return value of the constructor call or using a lowercase version of the method name. For example, a Frame object can be created using the following:

  ```cpp
  odb_Frame s1_writeFrame2 = step1.Frame(2, 1.3,
                 "frame 2 of step1 at time 1.3");
  ```

  The Frame object can be retrieved with the following:

  ```cpp
  odb_Frame& s1_readFrame2 = step1.frames(1);
  ```

- **Constructors for objects created in large quantities**

  For efficiency the constructors for objects that you create in large quantities, such as elements, nodes, and field values, do not follow the capitalized constructor name rule used for persistent objects. Nodes, elements, and field values are created using the `addNodes`, `addElements`, and `addData` methods, respectively. For example, you use the addNodes method to create and retrieve nodes:

  ```cpp
  part1.addNodes(nodeLabels, coordinates, nodeSetName);
  const odb_SequenceNode& nodeSeq = part1.nodes();

  odb_Node node1 = part1.nodes(1);
  ```

## Header files

To use a class in a C++ program, the relevant header files must be included. The naming convention followed is that the file name is the same as the name of the class declared in the header file. For example, the `odb_FieldValue` object is declared in the file `odb_FieldValue.h`. The file `odb_API.h` includes all the header files required to use the API. Other header files must be included to use some classes:

- To access material objects you must include the file `odb_MaterialTypes.h`.
- To access section objects you must include the file `odb_SectionTypes.h`.
