========================================
Extending the Abaqus Scripting Interface
========================================

You can extend the functionality of the Abaqus Scripting Interface by writing your own modules that contain classes and functions to accomplish tasks that are not directly available in Abaqus. For example, you can write a function to print the names of all materials that have a density specified, or you can write a function that creates a contour plot using a custom set of contour plot options. Creating functions and modules in Python is described in :doc:`/user/python/introduction/python-basics/functions` and :doc:`/user/python/introduction/python-basics/modules`.

This section describes how you can extend the functionality of the Abaqus Scripting Interface.

Storing custom data in the model database or in other objects
-------------------------------------------------------------

If you extend the kernel functionality by writing your own classes and functions, you may want to store data required by those classes or functions in the Abaqus/CAE model database so the data are available the next time you open the database. To store custom kernel data in the Abaqus/CAE model database, you must make use of the `customKernel` module. The `customKernel` module augments the mdb object with a member called customData. When you save a model database, Abaqus/CAE also saves any data created below the customData object.

For example,

.. code-block:: python
    
    import customKernel 
    mdb = Mdb() 
    mdb.customData.myString = 'The width is ' 
    mdb.customData.myNumber = 58 
    mdb.saveAs('custom-test.cae')
    mdb.close()

If you start a new session and open the model database, `custom-test.cae`, you can refer to the variables that you saved. For example,

.. code-block:: python
    
    >>> import customKernel
    mdb = openMdb('custom-test.cae') 
    >>> print mdb.customData.myString, mdb.customData.myNumber
    The width is 58

You can store almost any type of Python object under `mdb.customData`; for example, strings, numbers, and Python classes. However, there are some restrictions; for example, you cannot store file objects. These restrictions are due to the fact that the Abaqus/CAE infrastructure uses Python’s `pickle` module to store the `customData` object in the model database. The `pickle` module allows the Python programmer to write a data structure to a file and then recreate that data structure when reading from the file. For details on the restrictions imposed by the `pickle` module, see the official Python website (https://www.python.org).

If your code creates a custom class and stores an instance of the class in the model database, the custom module that defined that custom class must be available for Python to unpickle the data when the database is subsequently opened. Consequently, if a user saves custom data to a model database and then passes that model database to another user, the other user must also have access to the custom modules that produced the custom data. Otherwise, they will not be able to load the custom data into their Abaqus/CAE session.

Abaqus/CAE does not keep track of changes made to the `customData` object. As a result, when the user quits a session, Abaqus/CAE will not prompt them to save their changes if they changed only objects under `customData`.

Interaction with the GUI
------------------------

In addition to providing a persistence mechanism, the `customKernel` module contains classes that provide the following capabilities:

Querying custom kernel data values from the GUI. From a GUI script you can access some attribute of your custom kernel object, just as you would from the kernel. For example,

.. code-block:: python
    
    print mdb.customData.myObject.name

Notification to the GUI when custom kernel data change. For example, you can have a manager dialog box that lists the objects in a repository. When the contents of the repository change, you can be notified and take the appropriate action to update the list of objects in the manager dialog box.

To make use of these features, you must derive your custom kernel objects from the classes listed in the following sections. For more details on GUI customization, see the `Abaqus GUI Toolkit Reference Guide <https://help.3ds.com/2021/english/dssimulia_established/SIMACAEGUIRefHtml/simagui-c-ov.htm?contextscope=all>`_.

CommandRegister class
---------------------

You can use the CommandRegister class to derive a general class that can be queried from the GUI. In addition, the class can notify the GUI when its contents change. For example,

.. code-block:: python
    
    class Block(CommandRegister): 

        def __init__(self, name, ...): 
            CommandRegister.__init__(self) 
            ...

If a query is registered by the GUI on an instance of this class, the GUI will be notified when a member of this instance is changed, added, or deleted, For more details on registering queries, see the `Abaqus GUI Toolkit Reference Guide <https://help.3ds.com/2021/english/dssimulia_established/SIMACAEGUIRefHtml/simagui-c-ov.htm?contextscope=all>`_.

If your object is to be stored in a repository (see below), the first argument to the constructor must be a string representing the name of the object. That string will automatically be assigned by the infrastructure to a member called name.

Repositories
------------

Repositories are containers that hold objects that are keyed by strings. It may be convenient to store your custom kernel objects in repositories, in the same way that Abaqus/CAE part objects are stored in the Parts repository.

The customData object is an instance of a `RepositorySupport` class, which provides a Repository method that allows you to create a repository as an attribute of the instance. For more information, see `RepositorySupport`. The arguments to the Repository method are the name of the repository and a constructor or a sequence of constructors. Those constructors must have name as their first argument, and the infrastructure will automatically assign that value to a member called name. Instances of these constructors will be stored in the repository. For more information, see Repository object.

Since repositories are designed to notify the GUI when their contents change, the objects placed inside them should be derived from either CommandRegister or `RepositorySupport` to extend this capability to its fullest.

The Abaqus Scripting Interface uses the following conventions:

The name of a repository is a plural noun with all lowercase letters.

A constructor is a capitalized noun (or a combination of capitalized nouns and adjectives).

The first argument to the constructor must be name.

For example, the Part constructor creates a part object and stores it in the parts repository. You can access the part object from the repository using the same name argument that you passed in with the Part constructor. In some cases, more than one constructor can create instances that are stored in the same repository. For example, the HomogeneousSolidSection and the HomogeneousShellSection constructors both create section objects that are stored in the sections repository. For more information, see Abstract base type. For example, the following script creates a blocks repository, and the Block constructor creates a block object in the blocks repository:

.. code-block:: python
    
    from customKernel import CommandRegister
    class Block(CommandRegister): 

        def __init__(self, name): 
            CommandRegister.__init__(self)

    mdb.customData.Repository('blocks', Block) 
    block = mdb.customData.Block(name='Block-1')
    print mdb.customData.blocks['Block-1'].name Block-1