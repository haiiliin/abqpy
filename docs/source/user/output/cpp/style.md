# Abaqus Scripting Interface documentation style

This section describes the style that is used to describe a command in the {doc}`/reference/index`. You may want to refer to the {doc}`/reference/index` while you read this section and compare the style of a documented command with the descriptions provided here.

The following list describes the order in which commands are documented in the {doc}`/reference/index`:

- Chapters are grouped alphabetically by functionality. In general, the functionality corresponds to the modules and toolsets that are found in Abaqus/CAE; for example, {doc}`/reference/session/animation`, and {doc}`/reference/mdb/model/part_assembly/assembly`.

- Within each chapter the primary objects appear first and are followed by other objects in alphabetical order. For example, in {doc}`/reference/mdb/model/mesh` the objects are listed in the following order:

  - Assembly
  - Part
  - ElemType
  - MeshEdge
  - MeshElement
  - MeshFace
  - MeshNode
  - MeshStats

- Within each object description, the commands are listed in the following order:
  \- Constructors (in alphabetical order)
  \- Methods (in alphabetical order)
  \- Members

- Some methods are not associated with an object and appear at the end of a chapter; for example, the {py:meth}`~abaqus.Material.evaluateMaterial` method appears at the end of {doc}`/reference/mdb/model/material`.

## Access

The description of each object in the {doc}`/reference/index` begins with a section that describes how you access an instance of the object.

The following is the access description for the Part object:

```cpp
odb.parts()[name]
```

The access description specifies where instances of the object are located in the data model. The Part object can accordingly be accessed as:

```cpp
odb_PartContainer partCon = odb.parts();
odb_Part part = partCon["PART-1-1"];
```

The Access description for the FieldOutput object is

```cpp
odb.steps()[name].frames(i).fieldOutputs()[name]
```

The following statements show how you use the object described by this `Access` description:

```cpp
odb_StepContainer stepCon = odb.steps();
odb_Step step = stepCon["Side load"];
odb_SequenceFrame frameSeq = step.frames();
odb_Frame lastFrame = frameSeq.Get( frameSeq.Size() -1 );
odb_FieldOutputContainer fieldCon = lastFrame.fieldOutputs();
odb_FieldOutput field= fieldCon["S"];

odb_FieldOutput iPointFieldData = field.getSubset(
    odb_Enum::INTEGRATION_POINT);

odb_SequenceInvariant myInvariants = field.validInvariants();
```

- The next to last line shows the getSubset method of the FieldOutput object.
- The last line shows the **validInvariants** member of the FieldOutput object.

## Path

A method that creates an object is called a constructor. The Abaqus C++ API uses the convention that constructors begin with an uppercase character. In contrast, methods that operate on an object begin with a lowercase character. The description of each constructor in the {doc}`/reference/index` includes a path to the command. For example, the following describes the path to the Part constructor:

```cpp
odb.Part
```

Some constructors include more than one path. For example, you can create a nodeSet that is associated with either a Part object or the RootAssembly object, and each path is listed.

```cpp
odb.parts()[name].NodeSet
odb.rootAssembly().NodeSet
```

The path is not listed if the method is not a constructor.

If you are using the Abaqus C++ API to read data from an output database, the objects exist when you open the output database, and you do not have to use constructors to create them. However, if you are creating or writing to an output database, you may need to use constructors to create new objects, such as part instances and steps. The documentation describes the path to the constructors that create objects in an output database.

For example, the Path description for the FieldOutput constructor is

```cpp
odb.steps()[name].frames(i).FieldOutput
```

The following statement creates a FieldOutput object:

```cpp
odb_StepContainer stepCon = odb.steps();
odb_Step step = stepCon["Side load"];
odb_SequenceFrame frameSeq = step.frames();
odb_Frame frame = frameSeq.Get( frameSeq.Size() -1 );
odb_FieldOutput& myFieldOutput = frame.FieldOutput("S",
    "stress", odb_Enum::TENSOR_3D_FULL);
```

## Prototype

{doc}`/reference/odb` contains a prototype section for each C++ command. The prototype provides the type returned by the command, the name of the command, and a list of all its arguments along with the type of each argument. Required arguments appear first in the list followed by default arguments along with their default value. For example, the Frame constructor is given as

```cpp
odb_Frame Frame(int incrementNumber, float frameValue,
        const odb_String& description="");
```

indicating that the **incrementNumber** and **frameValue** arguments are required, that the optional **description** argument has a default value of the empty string, and that the method returns a reference to the Frame object created.

## Return value

All commands return a value. Many commands return the value void. Constructors (methods that create an object) always return the object being created. The return value of a command can be assigned to a variable. For example, in the following statement the Odb constructor returns an Odb object, and the variable newOdb refers to this new object.

```cpp
odb_Odb newOdb& = Odb("new", "", "", fileName);
```

You can use the object returned by a command in subsequent statements. The following statement uses the output database created by the previous statement:

```cpp
odb_Part& part = newOdb.Part("PART-1-1",
    odb_Enum::THREE_D, odb_Enum::DEFORMABLE_BODY);
```

If an exception is raised while a statement is executing, the command does not return a value.
