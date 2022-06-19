from abaqusConstants import *


class Vertex:
    """Vertices are point regions of geometry.

    Attributes
    ----------
    index: int
        An Int specifying the index of the ConstrainedSketchVertex in the VertexArray.
    isReferenceRep: Boolean
        A Boolean specifying whether the vertex belongs to the reference representation of the
        Part or Instance.
    pointOn: float
        A tuple of Floats specifying the **X** -, **Y** -, and **Z** -coordinates of the vertex.
    featureName: float
        A tuple of Floats specifying the name of the feature that created this vertex.
    instanceName: float
        A tuple of Floats specifying the name of the part instance for this vertex (if
        applicable).

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

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

    # An Int specifying the index of the ConstrainedSketchVertex in the VertexArray.
    index: int = None

    # A Boolean specifying whether the vertex belongs to the reference representation of the
    # Part or Instance.
    isReferenceRep: Boolean = OFF

    # A tuple of Floats specifying the **X** -, **Y** -, and **Z** -coordinates of the vertex.
    pointOn: float = None

    # A tuple of Floats specifying the name of the feature that created this vertex.
    featureName: float = None

    # A tuple of Floats specifying the name of the part instance for this vertex (if
    # applicable).
    instanceName: float = None

    def getEdges(self):
        """This method returns a sequence consisting of the edge ids of the edges which share this
        vertex.

        Returns
        -------
            A tuple of integers.

        """
        pass

    def getNodes(self):
        """This method returns an array of node objects that are associated with the vertex.

        Returns
        -------
            A MeshNodeArray object which is a sequence of MeshNode objects.

        """
        pass

    def getElements(self):
        """This method returns an array of element objects that are associated with the vertex.

        Returns
        -------
            A MeshElementArray object which is a sequence of MeshElement objects.

        """
        pass
