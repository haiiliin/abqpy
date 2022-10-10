====
Part
====

Features in Abaqus/CAE include Parts, Datums, Partitions, and Assembly operations. Part commands create Feature objects on only the Part object. The commands that create Feature objects on only the rootAssembly object are described in Assembly commands. The commands that create Feature objects on both the Part and the rootAssembly objects are described in Feature commands.

Create parts
------------

.. autoclass:: abaqus.Part.PartModel.PartModel
    :noindex:

    .. autoclasstoc::

.. autoclass:: abaqus.Part.PartBase.PartBase
    :noindex:
    :members: PartFromBooleanCut, PartFromBooleanMerge, PartFromExtrude2DMesh, PartFromGeometryFile, PartFromInstanceMesh, PartFromMesh, PartFromMeshMirror, PartFromNodesAndElements, PartFromOdb, PartFromSection3DMeshByPlane, PartFromSubstructure, Part2DGeomFrom2DMesh, PartFromSubstructure
    :special-members: __init__

    .. autoclasstoc::

.. autoclass:: abaqus.Part.PartFeature.PartFeature
    :members:
    :special-members: __init__
    :noindex:

    .. autoclasstoc::

.. This is a comment ro supress the warning "(ERROR/3) Document may not end with a transition."
