==============================================================
Object-oriented programming and the Abaqus Scripting Interface
==============================================================

You should now be familiar with some of the concepts behind object-oriented programming, such as objects, constructors, methods, and members. This section describes how object-oriented programming relates to the Abaqus Scripting Interface and summarizes some of the terminology.

The Abaqus Scripting Interface and methods
------------------------------------------

Most Abaqus Scripting Interface commands are methods. For example,

.. code-block:: python2
    
    session.viewports['Viewport-1'].setValues(width=50)

In this example `setValues()` is a method of the Viewport object.

A constructor is a method that creates an object. By convention, all constructor names and all objects start with an uppercase character in the Abaqus Scripting Interface. The name of a constructor is usually the same as the name of the type of object it creates. In the following example `Viewport` is a constructor that creates a Viewport object called `myViewport`:

.. code-block:: python2
    
    myViewport = session.Viewport(name='newViewport',
        width=100,height=100)

Some objects do not have a constructor. The object is created as a member of another object when the first object is created. For example, Abaqus creates the vertices of a part when you create a part's geometry, and the coordinates of the vertices are stored as Vertex objects. The Vertex objects are members of the Part object. The following statement prints the coordinates of the first vertex of a part:

.. code-block:: python2
    
    print
    mdb.models['Model-1'].parts['Part-1'].vertices[0].pointOn

The standard Python statement `object.__methods__` lists all the methods of an object. For example, the following statement lists all the methods of a Viewport object:

.. code-block:: python2
    
    session.viewports['myViewport'].__methods__ 

See the :doc:`/references` for a description of each method of the Abaqus Scripting Interface objects.

The Abaqus Scripting Interface and members
------------------------------------------

An object has members as well as methods. A member can be thought of as a property of an object. For example, `width` is a member of the Viewport object. The following statements show how you access a member of an object:

.. code-block:: python2
    
    >>> myWidth = session.viewports['myViewport'].width
    >>> print 'Viewport width =', myWidth Viewport width = 100.0

The standard Python statement `object.__members__` lists all the members of an object. For example, the following statement lists all the members of a Viewport object:

.. code-block:: python2
    
    session.viewports['myViewport'].__members__

The values of members are specific to each instance of the object. For example, the value of the `width` member of a Viewport object is specific to each viewport.

Members of an Abaqus object are read-only; consequently, you cannot change their value with a simple assignment statement. You use the `setValues()` method to change the value of a member. For example, the `setValues()` statement in the following script changes the thickness of a shell section:

.. code-block:: python2
    
    >>> import section 
    >>> shellSection = mdb.models['Model-1'].HomogeneousShellSection(
            name='Steel Shell', thickness=1.0, material='Steel') 
    >>> print 'Original shell section thickness = ' \ 
            , shellSection.thickness
    Original shell section thickness =  1.0 
    >>> shellSection.setValues(thickness=2.0)
    >>> print 'Final shell section thickness = ' \
            , shellSection.thickness
    Final shell section thickness =  2.0

You cannot use assignment to change the value of the Shell object.

.. code-block:: python2
    
    >>> myShell.thickness = 2.0  
    TypeError: readonly Attribute 

The following statements illustrate the use of constructors, methods, and members:

.. code-block:: python2
    
    >>> # Create a Section object 
    >>> mySection = mdb.models['Model-1'].HomogeneousSolidSection(
            name='solidSteel', material='Steel', thickness=1.0)  
    >>> # Display the type of the object 
    >>> print 'Section type = ', type(mySection) 
    Section type = <type 'HomogeneousSolidSection'> 
    >>> # List the members of the object
    >>> print 'Members of the section are:' , mySection.__members__ 
    Members of the section are: ['category', 'dimension', 
    'layout', 'material', 'name',
    'thickness']  
    >>> # List the methods of the object 
    >>> print 'Methods of the section are: ', mySection.__methods__ 
    Methods of the section are:  ['setValues']
    >>> # Print the value of each member in a nice format 
    >>> for member in mySection.__members__:
        ...     
        print 'mySection.%s = %s' % (member, 
            getattr(mySection, member))
    mySection.category = SOLID  
    mySection.dimension = THREE_DIM  
    mySection.layout = HOMOGENEOUS  
    mySection.material = Steel  
    mySection.name = solidSteel  
    mySection.thickness = 1.0

You use the `Access` description provided with each object in the :doc:`/references` to determine how you access the object. You append a method or member to this description when you are writing a script. Similarly, you use the `Path` description provided with each constructor in the :doc:`/references` to determine the path to the constructor.

Object-oriented programming and the Abaqus Scripting Interface - a summary
--------------------------------------------------------------------------

After you create an object, you then use methods of the objects to enter or to modify the data associated with the object. For example, you use the `addNodes` and `addElements` methods of the Part object to add nodes and elements, respectively. Similarly, you use the `addData` method of the `FieldOutput` object to add field output data.

The following list summarizes some of the concepts behind object-oriented programming and how they relate to the Abaqus Scripting Interface:

- An object encapsulates some data and functions that are used to manipulate those data.

- The data encapsulated by an object are called the members of the object.

- The functions that manipulate the data are called methods.

- The Abaqus Scripting Interface uses the convention that the name of a type of object begins with an uppercase character; for example, a Viewport object.

- A method that creates an object is called a constructor. The Abaqus Scripting Interface uses the convention that constructors begin with an uppercase character. In contrast, methods that operate on an object begin with a lowercase character.

- After you create an object, you then use methods of the object to enter or to modify the data associated with the object. For example, if you are creating an output database, you first create an Odb object. You then use the `addNodes` and `addElements` methods of the Part object to add nodes and elements, respectively. Similarly, you use the `addData` method of the `FieldOutput` object to add field output data to the output database.

- You use the `Access` description provided with each object in the :doc:`/references` to determine how you access the object. You append a method or a member to this description when you are writing a script.

- You use the `Path` description provided with each constructor in the :doc:`/references` to determine the path to the constructor.

- You use the `setValues()` method to modify the members of an Abaqus Scripting Interface object.

.. code-block:: python2
    
    session.viewports['Side view'].setValues(origin=(20,20))
