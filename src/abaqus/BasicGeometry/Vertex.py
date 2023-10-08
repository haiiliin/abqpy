from __future__ import annotations

from typing import TYPE_CHECKING

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Mesh.MeshElement import MeshElement
from ..Mesh.MeshNode import MeshNode
from ..UtilityAndView.abaqusConstants import OFF, Boolean

if TYPE_CHECKING:  # to avoid circular imports
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
    index: int

    #: A Boolean specifying whether the vertex belongs to the reference representation of the
    #: Part or Instance.
    isReferenceRep: Boolean = OFF

    #: A tuple of Floats specifying the **X** -, **Y** -, and **Z** -coordinates of the vertex.
    pointOn: tuple[float, float, float]

    #: A tuple of Floats specifying the name of the feature that created this vertex.
    featureName: tuple[float, ...]

    #: A tuple of Floats specifying the name of the part instance for this vertex (if
    #: applicable).
    instanceName: tuple[float, ...]

    def getEdges(self) -> tuple[int]:
        """This method returns a sequence consisting of the edge ids of the edges which share this vertex.

        Returns
        -------
        tuple[int]
            A tuple of integers.
        """
        return (0,)

    def getNodes(self) -> MeshNodeArray:
        """This method returns an array of node objects that are associated with the vertex.

        Returns
        -------
        MeshNodeArray
            A MeshNodeArray object which is a sequence of MeshNode objects.
        """
        return MeshNodeArray([MeshNode((0.0, 0.0, 0.0))])

    def getElements(self) -> MeshElementArray:
        """This method returns an array of element objects that are associated with the vertex.

        Returns
        -------
        MeshElementArray
            A MeshElementArray object which is a sequence of MeshElement objects.
        """
        return MeshElementArray([MeshElement()])
