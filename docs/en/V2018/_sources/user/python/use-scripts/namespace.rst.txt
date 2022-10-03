=========
Namespace
=========

Namespace is an important concept for the Abaqus Scripting Interface programmer. A namespace can be thought of as a program execution environment, and namespaces are independent of each other. Namespaces prevent conflict between variable names. You can use the same variable name to refer to different objects in different name spaces. :numref:`acl-all-schematic-nls-2` illustrates how commands interact with the Abaqus/CAE kernel.

.. _acl-all-schematic-nls-2:
.. figure:: /images/acl-all-schematic-nls.png
    :width: 50%
    :align: center
    
    The Abaqus Scripting Interface and the Abaqus/CAE kernel.

Abaqus Scripting Interface commands are issued to the Python interpreter from either the GUI, the command line interface, or a script. Abaqus/CAE executes these commands in one of two namespaces.

- **Script namespace**

  Abaqus Scripting Interface commands issued from scripts and from the command line interface are executed in the script namespace. Commands issued from **File -> Run Script** are also executed in the script namespace. For example, if you enter the following statement from the command line interface to create a viewport:

  .. code-block:: python2

      myViewport = session.Viewport(name='newViewport', 
          width=100, height=100)

  the variable myViewport exists only in the script namespace. The name of the script namespace is main.

- **Journal namespace**

  Abaqus Scripting Interface commands issued by the GUI are executed in the journal namespace. For example, if you use the GUI to partition an edge, Abaqus/CAE writes the following statements to the replay file, abaqus.rpy:

  .. code-block:: python2

      p1 = mdb.models['Model A'].parts['Part 3D A']
      e = p1.edges
      edges =(e[23], )
      p1.PartitionEdgeByParam(edges=edges, parameter=0.5)
  
  The variables defined in the replay file (p1, e, and edges, in the above example) exist only in the journal namespace. Abaqus/CAE issues an exception if you attempt to refer to one of these variables from the script namespace. For example, the following statement was issued from the command line interface and tries to partition the same edge:

  .. code-block:: python2

      p1.PartitionEdgeByParam(edges=edges, parameter=0.75)
      NameError: p1

  The name of the journal namespace is journaling.

The statement `from abaqus import *` described in Executing scripts imports the mdb variable into the script namespace. You can then use the mdb variable in your scripts to access the objects in the object model. Although variables in one namespace are not visible to the other namespace, the object repositories are now available in both. As a result, an object created in one namespace can still be referred to in another namespace if you use its full path (`mdb.models['Model A']...`) and its repository key.

For example, although the variable `p1` in the above statement cannot be accessed from the script namespace, you can still use the command line interface to access the part to which `p1` referred.

.. code-block:: python2

    myPart = mdb.models['Model A'].parts['Part 3D A']

The model and part repositories are available in both the journal and script namespaces. You can also create your own variable `p1` from the command line interface or from a script.

.. code-block:: python2

    p1 = myPart

The variable `p1` in the script namespace is independent of the variable p1 in the journal namespace.