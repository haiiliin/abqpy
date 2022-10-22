from __future__ import annotations

from typing import Optional, Tuple, TYPE_CHECKING

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import Boolean, OFF

if TYPE_CHECKING: # to avoid circular imports
    from ..Mesh.MeshElementArray import MeshElementArray
    from ..Mesh.MeshNodeArray import MeshNodeArray

@abaqus_class_doc
class Vertex:
    """Vertices are point regions of geometry.

    .. note:: 
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].allInternalSets[name].vertices[i]
            mdb.models[name].parts[name].allSets[name].vertices[i]
            mdb.models[name].parts[name].sets[name].vertices[i]
            mdb.models[name].parts[name].vertices[i]
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].sets[name].vertices[i]
            mdb.models[name].rootAssembly.allInstances[name].vertices[i]
            mdb.models[name].rootAssembly.allInternalSets[name].vertices[i]
            mdb.models[name].rootAssembly.allSets[name].vertices[i]
            mdb.models[name].rootAssembly.instances[name].sets[name].vertices[i]
            mdb.models[name].rootAssembly.instances[name].vertices[i]
            mdb.models[name].rootAssembly.modelInstances[i].sets[name].vertices[i]
            mdb.models[name].rootAssembly.modelInstances[i].vertices[i]
            mdb.models[name].rootAssembly.sets[name].vertices[i]
            mdb.models[name].rootAssembly.vertices[i]
    """

    #: An Int specifying the index of the ConstrainedSketchVertex in the VertexArray.
    index: Optional[int] = None

    #: A Boolean specifying whether the vertex belongs to the reference representation of the
    #: Part or Instance.
    isReferenceRep: Boolean = OFF

    #: A tuple of Floats specifying the **X** -, **Y** -, and **Z** -coordinates of the vertex.
    pointOn: Tuple[float, float, float]

    #: A tuple of Floats specifying the name of the feature that created this vertex.
    featureName: Optional[float] = None

    #: A tuple of Floats specifying the name of the part instance for this vertex (if
    #: applicable).
    instanceName: Optional[float] = None

    @abaqus_method_doc
    def getEdges(self) -> Tuple[int]:
        """This method returns a sequence consisting of the edge ids of the edges which share this
        vertex.

        Returns
        -------
        Tuple[int]
            A tuple of integers.

        """
        ...

    @abaqus_method_doc
    def getNodes(self) -> MeshNodeArray:
        """This method returns an array of node objects that are associated with the vertex.

        Returns
        -------
        MeshNodeArray
            A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object which is a sequence of MeshNode objects.

        """
        ...

    @abaqus_method_doc
    def getElements(self) -> MeshElementArray:
        """This method returns an array of element objects that are associated with the vertex.

        Returns
        -------
        MeshElementArray
            A :py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` object which is a sequence of MeshElement objects.

        """
        ...
