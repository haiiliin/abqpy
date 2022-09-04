=============================
Writing to an output database
=============================

You can write your own data to an output database, and you can use Abaqus/CAE to view the data. Writing to an output database is very similar to reading from an output database. When you open an existing database, the Odb object contains all the objects found in the output database, such as instances, steps, and field output data. In contrast, when you are writing to a new output database, these objects do not exist. As a result you must use a constructor to create the objects. For example, you use the Part constructor to create a Part object, the Instance constructor to create an OdbInstance object, and the Step constructor to create an OdbStep object.

After you create an object, you use methods of the objects to enter or modify the data associated with the object. For example, if you are creating an output database, you first create an Odb object. You then use the Part constructor to create a part. After creating the part, you use the addNodes and addElements methods of the Part object to add nodes and elements, respectively. Similarly, you use the addData method of the FieldOutput object to add field output data to the output database. After creating an output database, you should use the save method on the Odb object to save the output database.

The example script in :ref:`creating-an-output-database` also illustrates how you can write to an output database.

Creating a new output database
------------------------------

You use the Odb constructor to create a new, empty Odb object.

.. code-block:: python2

    odb = Odb(name='myData',
        analysisTitle='derived data',
        description='test problem',
        path='testWrite.odb')

For a full description of the Odb command, see :py:class:`~abaqus.Odb.Odb.Odb` object. Abaqus creates the RootAssembly object when you create or open an output database.

You use the `save` method to `save` the output database.

.. code-block:: python2

    odb.save()

For a full description of the save command, see :py:meth:`~abaqus.Odb.OdbBase.OdbBase.save`.

Writing model data
------------------

To define the geometry of your model, you first create the parts that are used by the model and then you add nodes and elements to the parts. You then define the assembly by creating instances of the parts. If the output database already contains results data, you should not change the geometry of the model. This is to ensure that the results remain synchronized with the model.

- **Part**

  If the part was created by Abaqus/CAE, the description of the native Abaqus/CAE geometry is stored in the model database, but it is not stored in the output database. A part is stored in an output database as a collection of nodes, elements, surfaces, and sets. You use the Part constructor to add a part to the Odb object. You can specify the type of the part; however, only DEFORMABLE_BODY is currently supported. For example,`
  
  .. code-block:: python2

      part1 = odb.Part(name='part-1', 
          embeddedSpace=THREE_D, type=DEFORMABLE_BODY)
  
  For a full description of the Part constructor, see :py:class:`~abaqus.Odb.OdbPart.OdbPart`. The new Part object is empty and does not contain geometry. After you create the Part object, you add nodes and elements.
  
  You use the addNodes method to add nodes by defining node labels and coordinates. You can also define an optional node set. For example,
  
  .. code-block:: python2

      nodeData = (  (1, 1,0,0),  (2, 2,0,0),  
                (3, 2,1,0.1),  (4, 1,1,0.1),  
                (5, 2,-1,-0.1),  (6, 1,-1,-0.1), ) 
      part1.addNodes(nodeData=nodeData, nodeSetName='nset-1') 
      
  For a full description of the addNodes command, see :py:meth:`~abaqus.Odb.OdbPart.OdbPart.addNodes`. After you have created nodes, you can use the NodeSetFromNodeLabels constructor to create a node set from the node labels. For more information, see :py:meth:`~abaqus.Odb.OdbPart.OdbPart.NodeSetFromNodeLabels`. Similarly, you use the addElements method to add elements to the part using a sequence of element labels, element connectivity, and element type. You can also define an optional element set and an optional section category. For example,
  
  .. code-block:: python2

      # Set up the section categories

      sCat = odb.SectionCategory(name='S5', 
          description='Five-Layered Shell')

      spBot = sCat.SectionPoint(number=1, 
          description='Bottom')
      spMid = sCat.SectionPoint(number=3, 
          description='Middle')
      spTop = sCat.SectionPoint(number=5, 
          description='Top')

      elementData = ((1, 1,2,3,4),
                  (2, 6,5,2,1),)
      part1.addElements(elementData=elementData, type='S4',
      elementSetName='eset-1', sectionCategory=sCat)
  
  For a full description of the addElements command, see :py:meth:`~abaqus.Odb.OdbPart.OdbPart.addElements`.

- **The RootAssembly object**

  The root assembly is created when you create the output database. You access the RootAssembly object using the same syntax as that used for reading from an output database.
  
  .. code-block:: python2

      odb.rootAssembly
  
  You can create both instances and regions on the RootAssembly object.

- **Part instances**

  You use the Instance constructor to create part instances of the parts you have already defined using the Part constructor. For example,
  
  .. code-block:: python2

      a = odb.rootAssembly 
      instance1 = a.Instance(name='part-1-1', object=part1)
  
  You can also supply an optional local coordinate system that specifies the rotation and translation of the part instance. You can add nodes and elements only to a part; you cannot add elements and nodes to a part instance. As a result, you should create the nodes and elements that define the geometry of a part before you instance the part. For a full description of the Instance command, see :py:class:`~abaqus.Odb.OdbInstance.OdbInstance`.

- **Regions**

  Region commands are used to create sets from element labels, node labels, and element faces. You can create a set on a part, part instance, or the root assembly. Node and element labels are unique within an instance but not within the assembly. As a result, a set on the root assembly requires the names of the part instances associated with the nodes and elements. You can also use region commands to create surfaces. For example,
  
  .. code-block:: python2

      # An element set on an instance
      eLabels = [9,99]
      elementSet = instance1.ElementSetFromElementLabels(
          name='elsetA',elementLabels=eLabels)
      # A node set on the rootAssembly
      nodeLabels = (5,11)
      instanceName = 'part-1-1'
      nodeSet = assembly.NodeSetFromNodeLabels(
          name='nodesetRA',((instanceName,nodeLabels),))
  
  The region commands are described in :doc:`/reference/mdb/model/part_assembly/region`.

- **Materials**

  You use the Material object to list material properties.Materials are stored in the materials repository under the Odb object.To create an isotropic elastic material, with a Young's modulus of 12000.0 and an effective Poisson's ratio of 0.3 in the output database:
  
  .. code-block:: python2

      materialName = "Elastic Material"
      material_1 = odb.Material(name=materialName)
      material_1.Elastic(type=ISOTROPIC,table=((12000,0.3),))
  
  For more information, see :doc:`/reference/mdb/model/material`.

- **Sections**

  You use the Section object to create sections and profiles.Sections are stored in the sections repository under the Odb object.The following code creates a homogeneous solid section object. A Material object must be present before creating a Section object. An exception is thrown if the material does not exist.
  
  .. code-block:: python2

      sectionName = 'Homogeneous Solid Section'
      mySection = odb.HomogeneousSolidSection( 
                        name = sectionName, 
                        material = materialName, 
                        thickness = 2.0)

  To create a circular beam profile object in the output database:
  
  .. code-block:: python2

      profileName = "Circular Profile"
      radius = 10.00
      odb.CircularProfile(name = profileName, r = radius)

- **Section assignments**

  You use the SectionAssignment object to assign sections and their associated material properties to regions of the model. SectionAssignment objects are members of the Odb object. For a full description of the assignSection method, see :py:meth:`~abaqus.Odb.OdbInstance.OdbInstance.assignSection`.
  
  All Elements in an Abaqus analysis need to be associated with section and material properties. Section assignments provide the relationship between elements in an Instance object and their section properties. The section properties include the associated material name. To create an element set and assign a section:
  
  .. code-block:: python2
    
      elLabels = (1,2)
      elset = instance.ElementSetFromElementLabels(
      name=materialName, elementLabels=elLabels)
      instance.assignSection(region=elset,section=section)
      
Writing results data
--------------------

To write results data to the output database, you first create the Step objects that correspond to each step of the analysis. If you are writing field output data, you also create the Frame objects that will contain the field data. History output data are associated with Step objects.

- **Steps**
  
  You use the Step constructor to create a results step for time, frequency, or modal domain results. For example,

  .. code-block:: python2
    
      step1 = odb.Step(name='step-1',  
          description='', domain=TIME, timePeriod=1.0)

  The `Step` constructor has an optional previousStepName argument that specifies the step after which this step must be inserted in the steps repository. For a full description of the Step command, see :py:class:`~abaqus.Step.Step.Step`.

- **Frames**
  
  You use the Frame constructor to create a frame for field output. For example,

  .. code-block:: python2
    
      frame1 = step1.Frame(incrementNumber=1, 
          frameValue=0.1, description='')

  For a full description of the Frame command, see :py:class:`~abaqus.Odb.OdbFrame.OdbFrame`.

Writing field output data
-------------------------

A FieldOutput object contains a cloud of data values (e.g., stress tensors at each integration point for all elements). Each data value has a location, type, and value. You add field output data to a Frame object by first creating a FieldOutput object using the FieldOutput constructor and then adding data to the FieldOutput object using the `addData` method. For example,

.. code-block:: python2

    # Create the part and the instance.
    
    part1 = odb.Part(name='part-1', 
        embeddedSpace=THREE_D, type=DEFORMABLE_BODY)
    a = odb.rootAssembly
    instance1 = a.Instance(name='part-1-1', object=part1)
    
    # Write nodal displacements
    
    uField = frame1.FieldOutput(name='U',
        description='Displacements', type=VECTOR)
    
    # Create the node labels.
    
    nodeLabelData = (1, 2, 3, 4, 5, 6)
    
    # Each set of data corresponds to a node label.
    
    dispData = ((1,2,3),
                (4,5,6),
                (7,8,9),
                (10,11,12),
                (13, 14, 15),
                (16,17,18))
    
    # Add nodal data to the FieldOutput object using the
    # node labels and the nodal data for this part instance.
    
    uField.addData(position=NODAL, instance=instance1,
        labels=nodeLabelData, data=dispData)
    
    # Make this the default deformed field for this step.
    
    step1.setDefaultDeformedField(uField)

For a full description of the FieldOutput constructor, see :py:class:`~abaqus.Odb.FieldOutput.FieldOutput`.

Default display properties
--------------------------

The previous examples show how you can use commands to set the default field variable and deformed field variable. Abaqus/CAE uses the default field variable setting to determine the variable to display in a contour plot; for example, stress. Similarly, the default deformed field variable determines the variable that distinguishes a deformed plot from an undeformed plot. Typically, you will use displacement for the default deformed field variable; you cannot specify an invariant or a component. The default variable settings apply for each frame in the step. For example, the following statements use the deformation 'U' as the default setting for both field variable and deformed field variable settings during a particular step:

.. code-block:: python2

    field=odb.steps['impact'].frames[1].fieldOutputs['U']
    odb.steps['impact'].setDefaultField(field)
    odb.steps['impact'].setDefaultDeformedField(field)

You can set a different default field variable and deformed field variable for different steps. You will need to use a loop to set the defaults for each step. For example,

.. code-block:: python2

    for step in odb.steps.values():
    step.setDefaultField(field)

Writing history output data
---------------------------

History output is output defined for a single point or for values calculated for a portion of the model as a whole, such as energy. Depending on the type of output expected, the historyRegions repository contains data from one of the following:

- a node
- an element, or a location in an element
- a region

.. note::
    History data from an analysis cannot contain multiple points.

The output from all history requests that relate to a specified point is collected in one HistoryRegion object. You use the HistoryPoint constructor to create the point. For example,

.. code-block:: python2

    point1 = HistoryPoint(element=instance1.elements[0])

For a full description of the HistoryPoint command, see :py:class:`~abaqus.Odb.HistoryPoint.HistoryPoint`.

You then use the HistoryRegion constructor to create a HistoryRegion object:

.. code-block:: python2

    step1 = odb.Step(name='step-1',  
        description='', domain=TIME, timePeriod=1.0)
    h1 = step1.HistoryRegion(name='my history',
        description='my stuff',point=point1)

For a full description of the HistoryRegion command, see :py:class:`~abaqus.Odb.HistoryRegion.HistoryRegion`.

You use the HistoryOutput constructor to add variables to the HistoryRegion object.

.. code-block:: python2

    h1_u1 = h1.HistoryOutput(name='U1',
        description='Displacement', type=SCALAR)
    h1_rf1 = h1.HistoryOutput(name='RF1',
        description='Reaction Force', type=SCALAR)


    # Similarly for Step 2

    step2 = odb.Step(name='step-2',  
        description='', domain=TIME, timePeriod=1.0)
    h2 = step2.HistoryRegion(name='my history',
        description='my stuff', point=point1)
    h2_u1 = h2.HistoryOutput(name='U1',
        description='Displacement', type=SCALAR)
    h2_rf1 = h2.HistoryOutput(name='RF1',
        description='Reaction Force', type=SCALAR)

Each HistoryOutput object contains a sequence of (**frameValue**, **value**) sequences. The HistoryOutput object has a method (addData) for adding data. Each data item is a sequence of (**frameValue**, **value**). In a time domain analysis (**domain** = TIME) the sequence is (**stepTime**, **value**). In a frequency domain analysis (**domain** = FREQUENCY) the sequence is (**frequency**, **value**). In a modal domain analysis (**domain** = MODAL) the sequence is (**mode**, **value**).

You add the data values as time and data tuples. The number of data items must correspond to the number of time items. For example,


.. code-block:: python2

    timeData = (0.0, 0.1, 0.3, 1.0)
    u1Data = (0.0, 0.0004, 0.0067, 0.0514)
    rf1Data = (27.456, 32.555, 8.967, 41.222)

    h1_u1.addData(frameValue=timeData, value=u1Data)
    h1_rf1.addData(frameValue=timeData, value=rf1Data)

    # similar for step2

    timeData = (1.2, 1.9, 3.0, 4.0)
    u1Data = (0.8, 0.9, 1.3, 1.5)
    rf1Data = (0.9, 1.1, 1.3, 1.5)

    h2_u1.addData(frameValue=timeData, value=u1Data)
    h2_rf1.addData(frameValue=timeData, value=rf1Data)
