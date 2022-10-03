=============================
Writing to an output database
=============================

You can write your own data to an output database, and you can use Abaqus/CAE to view the data. Writing to an output database is very similar to reading from an output database. When you open an existing database, the Odb object contains all the objects found in the output database, such as instances, steps, and field output data. In contrast, when you are writing to a new output database, these objects do not exist. As a result you must use a constructor to create the objects. For example, you use the Part constructor to create a Part object, the Instance constructor to create an OdbInstance object, and the Step constructor to create an OdbStep object.

After you create an object, you use methods of the objects to enter or modify the data associated with the object. For example, if you are creating an output database, you first create an Odb object. You then use the Part constructor to create a part. After creating the part, you use the addNodes and addElements methods of the Part object to add nodes and elements, respectively. Similarly, you use the addData method of the FieldOutput object to add field output data to the output database. After creating an output database, you should use the save method on the Odb object to save the output database.

The example script in :ref:`creating-an-output-database` also illustrates how you can write to an output database.

Creating a new output database
------------------------------

You use the Odb constructor to create a new, empty Odb object.

.. code-block:: cpp

    odb_Odb& odb = Odb("myData","derived data",
        "test problem", "testWrite.odb");

For a full description of the Odb command, see :py:class:`~abaqus.Odb.Odb.Odb` object. Abaqus creates the RootAssembly object when you create or open an output database.

You use the `save` method to `save` the output database.

.. code-block:: cpp

    odb.save();

For a full description of the save command, see :py:meth:`~abaqus.Odb.OdbBase.OdbBase.save`.

Writing model data
------------------

To define the geometry of your model, you first create the parts that are used by the model and then you add nodes and elements to the parts. You then define the assembly by creating instances of the parts. If the output database already contains results data, you should not change the geometry of the model. This is to ensure that the results remain synchronized with the model.

- **Part**

  If the part was created by Abaqus/CAE, the description of the native Abaqus/CAE geometry is stored in the model database, but it is not stored in the output database. A part is stored in an output database as a collection of nodes, elements, surfaces, and sets. You use the Part constructor to add a part to the Odb object. You can specify the type of the part; however, only DEFORMABLE_BODY is currently supported. For example,`
  
  .. code-block:: cpp

      odb_Part& part1 = odb.Part("part-1",
          odb_Enum::THREE_D, odb_Enum::DEFORMABLE_BODY);
  
  For a full description of the Part constructor, see :py:class:`~abaqus.Odb.OdbPart.OdbPart`. The new Part object is empty and does not contain geometry. After you create the Part object, you add nodes and elements.
  
  You use the addNodes method to add nodes by defining node labels and coordinates. You can also define an optional node set. For example,
  
  .. code-block:: cpp

    odb_SequenceInt nodeLabels;
    nodeLabels.append(1);
    nodeLabels.append(2);
    nodeLabels.append(3);
    nodeLabels.append(5);
    nodeLabels.append(7);
    nodeLabels.append(11);
    double c[6][3] = { {2.0, 1.0, 0.0},
                {1.0, 1.0, 0.0},
                {1.0, 0.0, 0.0},
                {2.0, 0.0, 0.0},
                {1.0, 0.0, 1.0},
                {2.0, 0.0, 1.0} };
    odb_SequenceSequenceFloat nodeCoor;
    for (int n=0; n<nodeLabels.size(); n++) {    
        odb_SequenceFloat loc;
        for (int i=0; i<3; i++)
        loc.append(c[n][i]);
        nodeCoor.append(loc);
    }
    part1.addNodes(nodeLabels, nodeCoor, "nodes_1");
      
  For a full description of the addNodes command, see :py:meth:`~abaqus.Odb.OdbPart.OdbPart.addNodes`. After you have created nodes, you can use the NodeSetFromNodeLabels constructor to create a node set from the node labels. For more information, see :py:meth:`~abaqus.Odb.OdbPart.OdbPart.NodeSetFromNodeLabels`. Similarly, you use the addElements method to add elements to the part using a sequence of element labels, element connectivity, and element type. You can also define an optional element set and an optional section category. For example,
  
  .. code-block:: cpp

    odb_SequenceInt elLabels;
    elLabels.append(9);
    elLabels.append(99);
    odb_SequenceSequenceInt connect;
    const int numNodePerEl = 4;
    int conn[2][numNodePerEl] = {{1, 2, 3, 5},
                    {5, 3, 7, 11}};  
    for (int e=0; e<elLabels.size(); e++) {
        odb_SequenceInt l;
        for (int i=0; i<numNodePerEl; i++)
        l.append(conn[e][i]);
        connect.append(l);
    }
    part1.addElements(elLabels, connect, "S4R",
                "s4_els", shellCat);
  
  For a full description of the addElements command, see :py:meth:`~abaqus.Odb.OdbPart.OdbPart.addElements`.

- **The RootAssembly object**

  The root assembly is created when you create the output database. You access the RootAssembly object using the same syntax as that used for reading from an output database.
  
  .. code-block:: cpp

      odb_Assembly& rootAssy = odb.rootAssembly();
  
  You can create both instances and regions on the RootAssembly object.

- **Part instances**

  You use the Instance constructor to create part instances of the parts you have already defined using the Part constructor. For example,
  
  .. code-block:: cpp

      odb_Instance& instanceA =
      odb.rootAssembly().Instance("part-1-1", part1);
  
  You can also supply an optional local coordinate system that specifies the rotation and translation of the part instance. You can add nodes and elements only to a part; you cannot add elements and nodes to a part instance. As a result, you should create the nodes and elements that define the geometry of a part before you instance the part. For a full description of the Instance command, see :py:class:`~abaqus.Odb.OdbInstance.OdbInstance`.

- **Regions**

  Region commands are used to create sets from element labels, node labels, and element faces. You can create a set on a part, part instance, or the root assembly. Node and element labels are unique within an instance but not within the assembly. As a result, a set on the root assembly requires the names of the part instances associated with the nodes and elements. You can also use region commands to create surfaces. For example,
  
  .. code-block:: cpp

    // An ElementSet on an instance  
    odb_SequenceInt eLabelsA(2);
    eLabelsA.append(9);
    eLabelsA.append(99);
    instanceA.ElementSet("elSetA", eLabelsA);
    
    // A NodeSet on the rootAssembly

    odb_SequenceSequenceInt nodeLabelsRA;
    odb_SequenceString namesRA;
    namesRA.append("part-1-1");
    odb_SequenceInt nodeLabelsRA_A;
    nodeLabelsRA_A.append(5);
    nodeLabelsRA_A.append(11);
    nodeLabelsRA.append(nodeLabelsRA_A);
    const odb_Set& nSetRA = rootAssy.NodeSet("nodeSetRA",
                        namesRA, nodeLabelsRA);  
  
  The region commands are described in :doc:`/reference/mdb/model/part_assembly/region`.

- **Materials**

  You use the Material object to list material properties.Materials are stored in the materials repository under the Odb object. 
  
  Materials are stored in the materials repository under the Odb object.

  Extend the Material commands available to the Odb object using the following statement:
  
  .. code-block:: cpp

    odb_MaterialApi materialApi;
    odb.extendApi(odb_Enum::odb_MATERIAL,materialApi); 
  
  To create an isotropic elastic material, with a Young's modulus of 12000.0 and an effective Poisson's ratio of 0.3 in the output database:
  
  .. code-block:: cpp

    odb_String materialName("Elastic Material");
    odb_Material& material = materialApi.Material(materialName);
    odb_SequenceSequenceFloat myTable;
    odb_SequenceFloat myData;
    myData.append(12000.0); myData.append(0.3);
    myTable.append(myData);
    odb_String type("ISOTROPIC");
    material.Elastic(myTable,type); 

  For more information, see :doc:`/reference/mdb/model/material`.

- **Sections**

  You use the Section object to create sections and profiles.Sections are stored in the sections repository under the Odb object.
  
  Sections are stored in the sections repository under the Odb object.

  Extend the API commands available to the Odb object using the following statement:
  
  .. code-block:: cpp

    odb_SectionApi sectionApi;
    odb.extendApi(odb_Enum::odb_SECTION, 
                  sectionApi);

  The following code creates a homogeneous solid section object. A Material object must be present before creating a Section object. An exception is thrown if the material does not exist.
  
  .. code-block:: cpp

    odb_String sectionName("Homogeneous Solid Section");
    float thickness = 2.0;
    odb_HomogeneousSolidSection& mySection = 
        sectionApi.HomogeneousSolidSection( sectionName, 
                                            materialName, 
                                            thickness);

  To create a circular beam profile object in the output database:
  
  .. code-block:: cpp

    odb_String profileName("Circular Profile");
    float radius = 10.00;
    sectionApi.CircularProfile(profileName, radius);

- **Section assignments**

  You use the SectionAssignment object to assign sections and their associated material properties to regions of the model. SectionAssignment objects are members of the Odb object. For a full description of the assignSection method, see :py:meth:`~abaqus.Odb.OdbInstance.OdbInstance.assignSection`.
  
  All Elements in an Abaqus analysis need to be associated with section and material properties. Section assignments provide the relationship between elements in an Instance object and their section properties. The section properties include the associated material name. To create an element set and assign a section:
  
  .. code-block:: cpp
    
    odb_SequenceInt setLabels; 
    setLabels.append(1);
    setLabels.append(2);
    elsetName = "Material 1";
    odb_Set& elset = instance.ElementSet(elsetName,setLabels);
    // section assignment on instance
    instance.assignSection(elset,section);

Writing results data
--------------------

To write results data to the output database, you first create the Step objects that correspond to each step of the analysis. If you are writing field output data, you also create the Frame objects that will contain the field data. History output data are associated with Step objects.

- **Steps**
  
  You use the Step constructor to create a results step for time, frequency, or modal domain results. For example,

  .. code-block:: cpp
    
    odb_Step& step1 = odb.Step("s1",
       "Perturbation Step", odb_Enum::TIME);
    odb_Step& step2 = odb.Step("sT",
        "Time domain analysis", odb_Enum::TIME, 1.0);
    odb_Step& step3 = odb.Step("sF",
        "Frequency analysis", odb_Enum::FREQUENCY, 123.4);

  The `Step` constructor has an optional previousStepName argument that specifies the step after which this step must be inserted in the steps repository. For a full description of the Step command, see :py:class:`~abaqus.Step.Step.Step`.

- **Frames**
  
  You use the Frame constructor to create a frame for field output. For example,

  .. code-block:: cpp
    
    odb_Frame frameOne = step2.Frame(1, 0.3, "first frame");

  For a full description of the Frame command, see :py:class:`~abaqus.Odb.OdbFrame.OdbFrame`.

Writing field output data
-------------------------

A FieldOutput object contains a cloud of data values (e.g., stress tensors at each integration point for all elements). Each data value has a location, type, and value. You add field output data to a Frame object by first creating a FieldOutput object using the FieldOutput constructor and then adding data to the FieldOutput object using the `addData` method. For example,

.. code-block:: cpp

    // vector
    odb_SequenceString vectorCompLabels;
    vectorCompLabels.append("1");
    vectorCompLabels.append("2");
    vectorCompLabels.append("3");
    odb_SequenceInvariant vectorInvar;
    vectorInvar.append(odb_Enum::MAGNITUDE);
    odb_FieldOutput& vectorField = frameOne.FieldOutput("U",
                    "displacement vector", 
                                    odb_Enum::VECTOR,
                    vectorCompLabels, vectorInvar);
    
    odb_SequenceInt labels2;
    labels2.append(3);
    labels2.append(5);
    odb_SequenceSequenceFloat vecDat;
    odb_SequenceFloat v1;
    v1.append(1.1); v1.append(1.2); v1.append(1.3);
    vecDat.append(v1);
    odb_SequenceFloat v2;
    v2.append(2.1); v2.append(2.2); v2.append(2.3);
    vecDat.append(v2);
    
    vectorField.addData(odb_Enum::NODAL, instanceA, 
                        labels2, vecDat);

For a full description of the FieldOutput constructor, see :py:class:`~abaqus.Odb.FieldOutput.FieldOutput`.

The **type** argument to the FieldOutput constructor describes the type of the data—tensor, vector, or scalar. The properties of the different tensor types are:

- Full tensor

  A tensor that has six components and three principal values. Full three-dimensional rotation of the tensor is possible.

- Three-dimensional surface tensor

  A tensor that has only three in-plane components and two principal values. Full three-dimensional rotation of the tensor components is possible.

- Three-dimensional planar tensor

  A tensor that has three in-plane components, one out-of-plane component, and three principal values. Full three-dimensional rotation of the tensor components is possible.

- Two-dimensional surface tensor

  A tensor that has only three in-plane components and two principal values. Only in-plane rotation of the tensor components is possible.

- Two-dimensional planar tensor

  A tensor that has three in-plane components, one out-of-plane component, and three principal values. Only in-plane rotation of the tensor components is possible.

The valid components and invariants for the different data types are given in Table 1.

+--------------------+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Data type          | Components              | Invariants                                                                                                                                    |
+====================+=========================+===============================================================================================================================================+
| SCALAR             |                         |                                                                                                                                               |
+--------------------+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| VECTOR             | 1, 2, 3                 | MAGNITUDE                                                                                                                                     |
+--------------------+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| TENSOR_3D_FULL     | 11, 22, 33, 12, 13, 23  | MISES, TRESCA, PRESS, INV3, MAX_PRINCIPAL, MID_PRINCIPAL, MIN_PRINCIPAL                                                                       |
+--------------------+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| TENSOR_3D_SURFACE  | 11, 22, 12              | MAX_PRINCIPAL, MIN_PRINCIPAL, MAX_INPLANE_PRINCIPAL, MIN_INPLANE_PRINCIPAL                                                                    |
+--------------------+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| TENSOR_3D_PLANAR   | 11, 22, 33, 12          | MISES, TRESCA, PRESS, INV3, MAX_PRINCIPAL, MID_PRINCIPAL, MIN_PRINCIPAL, MAX_INPLANE_PRINCIPAL, MIN_INPLANE_PRINCIPAL, OUTOFPLANE_PRINCIPAL   |
+--------------------+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| TENSOR_2D_SURFACE  | 11, 22, 12              | MAX_PRINCIPAL, MIN_PRINCIPAL, MAX_INPLANE_PRINCIPAL, MIN_INPLANE_PRINCIPAL                                                                    |
+--------------------+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| TENSOR_2D_PLANAR   | 11, 22, 33, 12          | MISES, TRESCA, PRESS, INV3, MAX_PRINCIPAL, MID_PRINCIPAL, MIN_PRINCIPAL, MAX_INPLANE_PRINCIPAL, MIN_INPLANE_PRINCIPAL, OUTOFPLANE_PRINCIPAL   |
+--------------------+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+


For example, the following statements add element data to the FieldOutput object:

.. code-block:: cpp

    odb_SequenceString tensorCompLabels;
    tensorCompLabels.append("s11");
    tensorCompLabels.append("s22");
    tensorCompLabels.append("s33");
    tensorCompLabels.append("s12");
    tensorCompLabels.append("s13");
    tensorCompLabels.append("s23");
    odb_SequenceInvariant tensorInvar;
    tensorInvar.append(odb_Enum::MISES);
    tensorInvar.append(odb_Enum::TRESCA);
    tensorInvar.append(odb_Enum::MAX_PRINCIPAL);
    tensorInvar.append(odb_Enum::MID_PRINCIPAL);
    tensorInvar.append(odb_Enum::MIN_PRINCIPAL);
    
    odb_FieldOutput& tensorField = frameOne.FieldOutput("S",
                    "stress tensor", 
                                    odb_Enum::TENSOR_3D_FULL,
                    tensorCompLabels, tensorInvar);
    
    odb_SequenceInt tensorLabels;
    tensorLabels.append(9);
    tensorLabels.append(99);
    
    odb_SequenceSequenceFloat tensorDat;
    odb_SequenceFloat t1;
    t1.append(1.0); t1.append(2.0); t1.append(3.0);
    t1.append(0.0); t1.append(0.0); t1.append(0.0);
    odb_SequenceFloat t2;
    t2.append(120.0); t2.append(-55.0); t2.append(-85.0);
    t2.append(-55.0); t2.append(-75.0); t2.append(33.0);
    tensorDat.append(t1);
    tensorDat.append(t2);
    
    tensorField.addData(odb_Enum::CENTROID, instanceA, tensorLabels,
                tensorDat, topShell);

For a full description of the `addData` command, see :py:meth:`~abaqus.Odb.FieldOutput.FieldOutput.addData`.

As a convenience, **localCoordSystem** can be a single transform or a list of transforms. If **localCoordSystem** is a single transform, it applies to all values. If **localCoordSystem** is a list of transforms, the number of items in the list must match the number of data values.

Default display properties
--------------------------

The previous examples show how you can use commands to set the default field variable and deformed field variable. Abaqus/CAE uses the default field variable setting to determine the variable to display in a contour plot; for example, stress. Similarly, the default deformed field variable determines the variable that distinguishes a deformed plot from an undeformed plot. Typically, you will use displacement for the default deformed field variable; you cannot specify an invariant or a component. The default variable settings apply for each frame in the step. For example, the following statements use the deformation 'U' as the default setting for both field variable and deformed field variable settings during a particular step:

.. code-block:: cpp

    step1.setDefaultField(tensorField);
    step1.setDefaultDeformedField(vectorField);
 
You can set a different default field variable and deformed field variable for different steps.

Writing history output data
---------------------------

History output is output defined for a single point or for values calculated for a portion of the model as a whole, such as energy. Depending on the type of output expected, the historyRegions repository contains data from one of the following:

- a node
- an element, or a location in an element
- a region

.. note::
    History data from an analysis cannot contain multiple points.

The output from all history requests that relate to a specified point is collected in one HistoryRegion object. You use the HistoryPoint constructor to create the point. For example,

.. code-block:: cpp

    db_HistoryPoint hPoint1(instanceA.elements(0));

For a full description of the HistoryPoint command, see :py:class:`~abaqus.Odb.HistoryPoint.HistoryPoint`.

You then use the HistoryRegion constructor to create a HistoryRegion object:

.. code-block:: cpp

    odb_HistoryRegion& hr1 = step1.HistoryRegion("ElHist",
                              "output at element", hPoint1);

For a full description of the HistoryRegion command, see :py:class:`~abaqus.Odb.HistoryRegion.HistoryRegion`.

You use the HistoryOutput constructor to add variables to the HistoryRegion object.

.. code-block:: cpp

    odb_HistoryRegion& hr1 = step1.HistoryRegion("ElHist",
                              "output at element", hPoint1);

Each HistoryOutput object contains a sequence of (**frameValue**, **value**) sequences. The HistoryOutput object has a method (addData) for adding data. Each data item is a sequence of (**frameValue**, **value**). In a time domain analysis (**domain** = TIME) the sequence is (**stepTime**, **value**). In a frequency domain analysis (**domain** = FREQUENCY) the sequence is (**frequency**, **value**). In a modal domain analysis (**domain** = MODAL) the sequence is (**mode**, **value**).

You add the data values as time and data tuples. The number of data items must correspond to the number of time items. For example,


.. code-block:: cpp

    ho1.addData(0.001, 0.1);
  
    // or using two sequences

    odb_SequenceFloat timeData;
    odb_SequenceFloat values;
    timeData.append(0.001);
    values.append(0.1);
    ho1.addData(timeData, values);
    
    // or using a sequence of sequences
    odb_SequenceSequenceFloat s11;
    odb_SequenceFloat value1;
    value1.append(0.001);
    value1.append(0.1);
    s11.append(value1);
    ho1.addData(s11);
