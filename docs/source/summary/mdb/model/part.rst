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

    .. autoclasstoc::
    :members: PartFromBooleanCut, PartFromBooleanMerge, PartFromExtrude2DMesh, PartFromGeometryFile, PartFromInstanceMesh, PartFromMesh, PartFromMeshMirror, PartFromNodesAndElements, PartFromOdb, PartFromSection3DMeshByPlane, PartFromSubstructure, Part2DGeomFrom2DMesh, PartFromSubstructure