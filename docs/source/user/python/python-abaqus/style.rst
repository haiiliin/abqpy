==============================================
Abaqus Scripting Interface documentation style
==============================================

This section describes the style that is used to describe Abaqus Scripting Interface commands. The commands are found in the :doc:`/references`. You may want to refer to the :doc:`/references` while you read this section and compare the style of a documented command with the descriptions provided here.

How the commands are ordered
----------------------------

The following list describes the order in which commands are documented in the :doc:`/references`:

Chapters are grouped alphabetically by functionality. In general, the functionality corresponds to the modules and toolsets that are found in Abaqus/CAE; for example, Amplitude commands, Animation commands, and Assembly commands.

Within each chapter the primary objects appear first and are followed by other objects in alphabetical order. For example, in Mesh commands the objects are listed in the following order:

- Assembly
- Part
- ElemType
- MeshEdge
- MeshElement
- MeshFace
- MeshNode
- MeshStats

Within each object description, the commands are listed in the following order:

- Constructors (in alphabetical order)
- Methods (in alphabetical order)
- Members

Some methods are not associated with an object and appear at the end of a chapter; for example, the `evaluateMaterial()` method appears at the end of :doc:`/reference/mdb/model/material` commands.

Access
------

The description of each object in the :doc:`/references` begins with a section that describes how you access an instance of the object. The import statements are provided for completeness. Abaqus/CAE imports all modules when you start a session, and you do not need to include the `import module name` statement in your scripts. However, you must import the Abaqus Scripting Interface Symbolic Constants with the following statement:

.. code-block:: python2

    from abaqusConstants import *

These should be the first statement in all your Abaqus Scripting Interface scripts.

The following is the access description for the Material object:

.. code-block:: python2
    
    import material
    mdb.models[name].materials[name]

The first line of the access description indicates the module that Abaqus/CAE imported to make this object, and its methods and members, available to your script.

The access description also specifies where instances of the object are located in the data model. In the previous example the second line indicates how your script can access Material objects from a particular model. You must qualify a material object, command, or member with the variable mdb, as described in Functions and modules. For example,

.. code-block:: python2
    
    mdb.models[crash].Material[steel]
    mdb.models[crash].materials[steel].Elastic(
        table=((30000000.0, 0.3), ))
    elasticityType = mdb.models[crash].materials[steel].elastic.type

Similarly, if you are reading from an output database, the following is the access description for the HistoryRegion object:

.. code-block:: python2
    
    import odbAccess
    session.odbs[name].steps[name].historyRegions[name]
    
The first line indicates that Abaqus/CAE imported the odbAccess module to make the Odb objects, methods, and members available to your Abaqus Scripting Interface script. The second line indicates how your script can access HistoryRegion objects from a particular step.

The Access description for the FieldOutput object is

.. code-block:: python2
    
    session.odbs[name].steps[name].frames[i].fieldOutputs[name]

The following statements show how you use the object described by this Access description:

.. code-block:: python2
    
    sideLoadStep = session.odbs['Forming loads'].steps['Side load']
    lastFrame = sideLoadStep.frames[-1]
    stressData = lastFrame.fieldOutputs['S']
    integrationPointData = stressData.getSubset(
        position=INTEGRATION_POINT)
    invariantsData = stressData.validInvariants

- The next to last line shows the getSubset method of the FieldOutput object.
- The last line shows the validInvariants member of the FieldOutput object.

Path
----

A method that creates an object is called a constructor. The Abaqus Scripting Interface uses the convention that constructors begin with an uppercase character. In contrast, methods that operate on an object begin with a lowercase character. The description of each constructor in the :doc:`/references` includes a path to the command. For example, the following describes the path to the Viewport constructor:

.. code-block:: python2
    
    session.Viewport

Some constructors include more than one path. For example, you can create a datum that is associated with either a Part object or the RootAssembly object, and each path is listed.

.. code-block:: python2
    
    mdb.models[name].parts[name].DatumAxisByCylFace
    mdb.models[name].rootAssembly.DatumAxisByCylFace

The path is not listed if the method is not a constructor.

If you are using the Abaqus Scripting Interface to read data from an output database, the objects exist when you open the output database, and you do not have to use constructors to create them. However, if you are creating or writing to an output database, you may need to use constructors to create new objects, such as part instances and steps. The documentation describes the path to the constructors that create objects in an output database.

For example, the Path description for the FieldOutput constructor is

.. code-block:: python2
    
    session.odbs[name].steps[name].frames[i].FieldOutput

The following statement creates a FieldOutput object:

.. code-block:: python2
    
    myFieldOutput = session.odbs[name].steps['Side load'].frames[-1].\
        FieldOutput(name='S', description='stress', 
        type=TENSOR_3D_FULL)

Arguments
---------

The ellipsis `(...)` in the command description indicates that the command takes one or more arguments. For example, the Viewport constructor takes arguments.

.. code-block:: python2
    
    Viewport(...)

In contrast, the `makeCurrent` method takes no arguments.

.. code-block:: python2
    
    makeCurrent()

Some arguments of a command are required, and some arguments are optional. In the :doc:`/references` the required arguments are listed first, followed by the optional arguments. If the argument is optional, the default value is provided. The default value is the value of an optional argument when you call a method and omit the argument.

The `setValues` method is a special case. All of the arguments to the `setValues` method are optional, but any argument that you omit retains its current value; Abaqus does not assign a default value to the argument.

Some objects have no constructors; Abaqus creates the objects for you. For such objects the documentation describes the initial value of an optional argument. The initial value given for the argument is the initial value assigned to the corresponding member when Abaqus creates the object. For example, the defaultViewportAnnotationOptions object has no constructor; Abaqus creates the defaultViewportAnnotationOptions object when you start a session. When you create a new viewport, the settings are copied from the current viewport.

You can use the `setValues` method to modify the value of a member; for example, to modify the value of the triad member of the defaultViewportAnnotationsOptions object. When you call session.

.. code-block:: python2

    defaultViewportAnnotationOptions.setValues(triad=OFF)

the value of the triad member is set to off. The other member values remain unchanged; this behavior is called "as is" behavior because the values remain "as is." The `setValuesInStep` method displays similar "as is" behavior.

Keyword and positional arguments are described in Creating functions. We recommend that you use keyword arguments since they can be supplied in any order and they make your scripts easier to read and debug; for example,

.. code-block:: python2
    
    newViewport = session.Viewport(name='myViewport', 
        origin=(10, 10), width=100, height=50)

If you choose not to use keywords, the arguments must be provided in the order in which they are documented.

.. code-block:: python2
    
    newViewport = session.Viewport('myViewport', 
        (10, 10), 100, 50)

You can use a combination of keyword and positional arguments. Keyword arguments can be supplied after positional arguments; however, positional arguments cannot be entered after keyword arguments. For example, you can use the following statement:

.. code-block:: python2
    
    newViewport = session.Viewport('myViewport', 
        (10, 10), width=100, height=50)

However, you cannot use the following statement:

.. code-block:: python2
    
    newViewport = session.Viewport(name='myViewport', 
        (10, 10), 100, 50)

You will find it easier to use keyword arguments so that you do not have to concern yourself with the positional requirements.

Return value
------------

All commands return a value. Many commands return the None object described in :ref:`python-none`. Constructors (methods that create an object) always return the object being created. The return value of a command can be assigned to a Python variable. For example, in the following statement the Viewport constructor returns a Viewport object, and the variable `newViewport` refers to this new object.

.. code-block:: python2
    
    newViewport = session.Viewport(name='myViewport', 
        origin=(10, 10), width=100, height=50)

You can use the object returned by a command in subsequent statements. For example, the `titlebar` member of a Viewport object is a Boolean specifying whether the viewport title bar is displayed and can have a value of either ON or OFF. The following statement tests the titlebar member of the new viewport created by the previous statement:

.. code-block:: python2
    
    if newViewport.titleBar:
        print 'The title bar will be displayed.'