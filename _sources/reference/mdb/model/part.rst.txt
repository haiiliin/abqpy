====
Part
====

Features in Abaqus/CAE include Parts, Datums, Partitions, and Assembly operations. Part commands create Feature objects on only the Part object. The commands that create Feature objects on only the rootAssembly object are described in Assembly commands. The commands that create Feature objects on both the Part and the rootAssembly objects are described in Feature commands.


Create parts
------------

.. autoclass:: abaqus.Part.PartModel.PartModel
    :noindex:
    :members:

.. autoclass:: abaqus.Part.PartBase.PartBase
    :noindex:
    :members:

Object features
---------------

Part
~~~~

.. autoclass:: abaqus.Part.Part.Part
    :members:
    :inherited-members:

    .. autoclasstoc::

PartBase
~~~~~~~~

.. autoclass:: abaqus.Part.Partbase.PartBase
    :members:

    .. autoclasstoc::

MeshEditPart
~~~~~~~~~~~~

.. autoclass:: abaqus.EditMesh.MeshEditPart.MeshEditPart
    :members:

    .. autoclasstoc::

MeshPart
~~~~~~~~

.. autoclass:: abaqus.Mesh.MeshPart.MeshPart
    :members:

    .. autoclasstoc::

PropertyPart
~~~~~~~~~~~~

.. autoclass:: abaqus.Property.PropertyPart.PropertyPart
    :members:

    .. autoclasstoc::

RegionPart
~~~~~~~~~~

.. autoclass:: abaqus.Region.RegionPart.RegionPart
    :members:

    .. autoclasstoc::

AcisFile
~~~~~~~~

.. autoclass:: abaqus.Part.AcisFile.AcisFile
    :members:

    .. autoclasstoc::

AcisMdb
~~~~~~~

.. autoclass:: abaqus.Part.AcisMdb.AcisMdb
    :members:

    .. autoclasstoc::

Feature
~~~~~~~

.. autoclass:: abaqus.Part.Feature.Feature
    :members:

    .. autoclasstoc::