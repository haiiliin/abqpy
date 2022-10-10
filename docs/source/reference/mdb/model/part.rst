====
Part
====

Features in Abaqus/CAE include Parts, Datums, Partitions, and Assembly operations. Part commands create Feature objects on only the Part object. The commands that create Feature objects on only the rootAssembly object are described in Assembly commands. The commands that create Feature objects on both the Part and the rootAssembly objects are described in Feature commands.


Create parts
------------

.. autoclass:: abaqus.Part.PartModel.PartModel
    :members:
    :special-members: __init__

.. autoclass:: abaqus.Part.PartBase.PartBase
    :members:
    :special-members: __init__

Object features
---------------

Part
~~~~

.. autoclass:: abaqus.Part.Part.Part
    :members:
    :special-members: __init__
    :inherited-members:

    .. autoclasstoc::

PartFeature
~~~~~~~~~~~

.. autoclass:: abaqus.Part.PartFeature.PartFeature
    :members:
    :special-members: __init__

    .. autoclasstoc::

MeshEditPart
~~~~~~~~~~~~

.. autoclass:: abaqus.EditMesh.MeshEditPart.MeshEditPart
    :members:
    :special-members: __init__
    :noindex:

    .. autoclasstoc::

MeshPart
~~~~~~~~

.. autoclass:: abaqus.Mesh.MeshPart.MeshPart
    :members:
    :special-members: __init__
    :noindex:

    .. autoclasstoc::

PropertyPart
~~~~~~~~~~~~

.. autoclass:: abaqus.Property.PropertyPart.PropertyPart
    :members:
    :special-members: __init__
    :noindex:

    .. autoclasstoc::

RegionPart
~~~~~~~~~~

.. autoclass:: abaqus.Region.RegionPart.RegionPart
    :members:
    :special-members: __init__
    :noindex:

    .. autoclasstoc::

AcisFile
~~~~~~~~

.. autoclass:: abaqus.Part.AcisFile.AcisFile
    :members:
    :special-members: __init__

    .. autoclasstoc::

AcisMdb
~~~~~~~

.. autoclass:: abaqus.Part.AcisMdb.AcisMdb
    :members:
    :special-members: __init__
    :noindex:

    .. autoclasstoc::

.. This is a comment ro supress the warning "(ERROR/3) Document may not end with a transition."
