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

.. autoclass:: abaqus.Part.PartBase.PartBase
    :members:

    .. autoclasstoc::

MeshEditPart
~~~~~~~~~~~~

.. autoclass:: abaqus.EditMesh.MeshEditPart.MeshEditPart
    :members:
    :noindex:

    .. autoclasstoc::

MeshPart
~~~~~~~~

.. autoclass:: abaqus.Mesh.MeshPart.MeshPart
    :members:
    :noindex:

    .. autoclasstoc::

PropertyPart
~~~~~~~~~~~~

.. autoclass:: abaqus.Property.PropertyPart.PropertyPart
    :members:
    :noindex:

    .. autoclasstoc::

RegionPart
~~~~~~~~~~

.. autoclass:: abaqus.Region.RegionPart.RegionPart
    :members:
    :noindex:

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
    :noindex:

    .. autoclasstoc::

PartFeature
~~~~~~~~~~~

.. autoclass:: abaqus.Part.PartFeature.PartFeature
    :members:

    .. autoclasstoc::