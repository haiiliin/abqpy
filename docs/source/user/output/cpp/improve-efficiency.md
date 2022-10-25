# Improving the efficiency of your scripts

If you are accessing large amounts of data from an output database, you should be aware of potential inefficiencies in your script and techniques that will help to speed up your scripts.

## Creating objects to hold loop counters

A program can spend a large proportion of its computation time executing statements inside loops. As a result, you can make your scripts more efficient if you consider how Abaqus computes the next value of a loop counter each time the loop is executed. If possible, you should create an integer or a sequence object to hold the value of a loop counter. If you use a value derived from an Abaqus object, the time taken to calculate the next value can slow your program significantly.

The following example uses the number of nodes in a part instance to determine the range of a loop counter:

```cpp
const odb_SequenceNode& nodeSequence = myInstance.nodes();
for (int i=0; i < nodeSequence.size() ; i++){
  const odb_Node& myNode = nodeSequence[i];
  nodeLabel = myNode.label();
}
```

You can make the program more efficient if you create an object to hold the value of the number of nodes.

```cpp
const odb_SequenceNode& nodeSequence = myInstance.nodes();
int numNodes = nodeSequence.size();
for (int i=0; i < numNodes; i++){
  const odb_Node& myNode = nodeSequence[i];
  nodeLabel = myNode.label();
}
```

You can use this technique only if the maximum value of the loop counter remains fixed for the duration of the loop.

## Creating objects to hold temporary variables

To improve the efficiency of scripts that access an output database, you should create objects that will be used to hold temporary variables that are accessed multiple times while the program is executing. For example, if the program accesses the temporary variable while inside a loop that is executed many times, creating an object to hold the variable will speed up your program significantly.

The following example examines the von Mises stress in each element during a particular frame of field output. If the stress is greater than a certain maximum value, the program prints the strain components for the element.

```cpp
odb_FieldOutputRepository& fieldRep = frame1.fieldOutputs();
odb_FieldOutput& stressField = fieldRep.get("S");
odb_FieldOutput& strainField = fieldRep.get("LE");
const odb_SequenceFieldValue& seqStressVal =
    stressField.values();
int numFV = seqStressVal.size();
int strainComp = 0;
for (int loc=0; loc < numFV; loc++) {
    const odb_FieldValue stressVal = seqStressVal[loc];
    if (stressVal.mises() > stressCap) {
        cout << "Element label = " << stressVal.elementLabel()
            << endl;
        cout << "Integration Point = "
            << stressVal.integrationPoint() << endl;
        const odb_SequenceFieldValue& seqStrainVal =
                strainField.values();
        const odb_FieldValue strainVal = seqStrainVal[loc];
        const float* const data = strainVal.data(strainComp);
        cout << " LE : ";
        for (int comp=0; comp < strainComp; comp++)
            cout << data[comp];
        cout << endl;
    }
}
```

In this example every time the script calls the strainField.values method, Abaqus must reconstruct the sequence of FieldValue objects. This reconstruction could result in a significant performance degradation, particularly for a large model.

A slight change in the program greatly improves its performance, as shown in the following example:

```cpp
odb_FieldOutputRepository& fieldRep =
    frame1.fieldOutputs();
odb_FieldOutput& stressField = fieldRep.get("S");
odb_FieldOutput& strainField = fieldRep.get("LE");
const odb_SequenceFieldValue& seqStressVal =
    stressField.values();
const odb_SequenceFieldValue& seqStrainVal =
    strainField.values();
int numFV = seqStressVal.size();
int strainComp = 0;
for (int loc=0; loc < numFV; loc++) {
    const odb_FieldValue stressVal = seqStressVal[loc];
    if (stressVal.mises() > stressCap) {
        cout << "Element label = " << stressVal.elementLabel()
            << endl;
        cout << "Integration Point = "
            << stressVal.integrationPoint() << endl;
        const odb_FieldValue strainVal = seqStrainVal[loc];
        const float* data = strainVal.data(strainComp);
        cout << " LE : ";
        for (int comp = 0; comp < strainComp; comp++)
            cout << data[comp];
        cout << endl;
    }
}
```

Similarly, if you expect to retrieve more than one frame from an output database, you should create a temporary variable that holds the entire frame repository. You can then provide the logic to retrieve the desired frames from the repository and avoid recreating the repository each time. For example, executing the following statements could be very slow:

```cpp
int numFrames = step1.frames().size();
for (int n=0; n < numFrames; n++)
    odb_Frame& frame = step1.frames()[n];
```

Creating a temporary variable to hold the frame repository provides the same functionality and speeds up the process:

```cpp
odb_SequenceFrame& frameRepository = step1.frames();
int numFrames = frameRepository.size();
for (int n=0; n < numFrames; n++)
    odb_Frame& frame = frameRepository[n];
```

Such a potential loss of performance will not be a problem when accessing a load case frame. Accessing a load case frame does not result in the creation of a frame repository and, thus, does not suffer from a corresponding loss of performance.

## Using references to objects

Many functions return a reference to an object rather than an object. Returning a reference is much more efficient because it avoids unnecessary memory operations. To maintain the efficiency of references, you should use the reference itself. You should not assign the reference to a new object, since assigning the reference to a new object creates a copy of the object that is denoted by the reference and invokes potentially expensive copy constructors. For example,

```cpp
odb_Instance instance = odb.rootAssembly().instances()
                            ["PART-1-1"];
const odb_SequenceNode nodeSequence = myInstance.nodes();
```

In the above case a copy of the nodeSequence object has to be created in memory.

Many of the methods in the Abaqus Scripting Interface that provide access to an output database return a reference to an object rather than the object itself. It is much more efficient to modify the previous example to specify the returned type to be a reference:

```cpp
odb_Instance& instance = odb.rootAssembly().instances()["PART-1-1"];
const odb_SequenceNode& nodeSequence = myInstance.nodes();
```

In this case no new object is created and no copy constructors are called.
