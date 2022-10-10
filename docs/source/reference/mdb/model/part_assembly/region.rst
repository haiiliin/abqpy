======
Region
======

Region commands are used to create part and assembly sets or surfaces from elements, nodes, and geometry. For more information, see Specifying a region. Part and assembly objects have the following member, a repository of Set objects:

- sets

In turn, a Set object can contain any one of the following types:

- elements
- nodes
- geometry

A Set object can contain a number of entities of a single type (nodes, elements, or geometry) or a combination of node and element types. However, except for nodes and elements, a Set object cannot contain a combination of types.

The following are members of the Set object:

- nodes
- elements
- cells
- faces
- edges
- vertices
- referencePoints

Region commands are also used to create surfaces on the assembly. Surfaces are sets with additional sidedness information.

Part sets contain regions of a part. You can assign section definitions to a set created by selecting a region of a part. The part sets can be accessed from the instance; however, the section definition you assigned to a region is copied automatically to all instances of that part in the assembly.

Assembly sets contain regions of an assembly and are used by many commands that operate on the assembly. For example, you can apply a load or boundary condition to a set created by selecting a region of the assembly. Sets can include regions from multiple part instances.

Create regions for Part
-----------------------

.. autoclass:: abaqus.Region.RegionPart.RegionPart
    :members:
    :special-members:

Create regions for Assembly
---------------------------

.. autoclass:: abaqus.Region.RegionAssembly.RegionAssembly
    :members:
    :special-members:


Object features
---------------

Region features for Part
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Region.RegionPartBase.RegionPartBase
    :members:
    :special-members:

    .. autoclasstoc::

Region features for Assembly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: abaqus.Region.RegionAssemblyBase.RegionAssemblyBase
    :members:
    :special-members:

    .. autoclasstoc::

Region
~~~~~~

.. autoclass:: abaqus.Region.Region.Region
    :members:
    :special-members:

    .. autoclasstoc::

RegionArray
~~~~~~~~~~~

.. autoclass:: abaqus.Region.RegionArray.RegionArray
    :members:
    :special-members:

    .. autoclasstoc::

Set
~~~

.. autoclass:: abaqus.Region.Set.Set
    :members:
    :special-members:

    .. autoclasstoc::

Skin
~~~~

.. autoclass:: abaqus.Region.Skin.Skin
    :members:
    :special-members:

    .. autoclasstoc::

Stringer
~~~~~~~~

.. autoclass:: abaqus.Region.Stringer.Stringer
    :members:
    :special-members:

    .. autoclasstoc::

Surface
~~~~~~~

.. autoclass:: abaqus.Region.Surface.Surface
    :members:
    :special-members:

    .. autoclasstoc::

