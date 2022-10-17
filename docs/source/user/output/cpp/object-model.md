# How the object model for the output database relates to commands

You need to understand the object model for the output database both to read data from it and to write data to it. An object model describes the relationship between objects. The object model for the Abaqus/CAE model is described in {doc}`/user/python/use-scripts/object-model`.

For example, consider the object model for field output data shown in {numref}`odb-overview-nls-1` The Odb object at the top of the figure is created when you issue the command to open or create an output database. As you move down the object model, an OdbStep object is a member of the Odb object; similarly, a Frame object is a member of the OdbStep object. The FieldOutput object has two members—fieldValue and fieldLocation.

(odb-overview-nls-1)=

```{figure} /images/odb-overview-nls.png
:align: center
:width: 100%

The output database object model.
```

The object model translates directly to the structure of an Abaqus C++ API command. For example, the following command refers to a Frame object in the sequence of frames contained in an OdbStep object:

```cpp
odb.steps()["10 hz"].frames(3);
```

Similarly, the following command refers to the sequence of field data contained in a FieldOutput object.

```cpp
odb.steps()["10 hz"].frames.get(3).
    fieldOutputs()["U"].values(47);
```

You use commands to access objects by stepping through the hierarchy of objects in the object model. The `Access`, `Path`, and `Prototype` descriptions in {doc}`/reference/odb` describe the interface definition of the command. The interface definition of the command reflects the hierarchy of objects in the object model.
