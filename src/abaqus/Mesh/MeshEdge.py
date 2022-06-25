from .MeshElementArray import MeshElementArray


class MeshEdge:
    """The MeshEdge object refers to an element edge. It has no constructor or members. A
    MeshEdge object can be accessed via a MeshEdgeArray or a repository on a part or part
    instance.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import part
            mdb.models[name].parts[name].elemEdges[i]
            mdb.models[name].parts[name].elementEdges[i]
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].elemEdges[i]
            mdb.models[name].rootAssembly.allInstances[name].elementEdges[i]
            mdb.models[name].rootAssembly.instances[name].elemEdges[i]
            mdb.models[name].rootAssembly.instances[name].elementEdges[i]
    """

    def getElements(self):
        """This method returns a tuple of elements that share the element edge.

        Returns
        -------
        tuple[MeshElement, ...]
            A tuple of :py:class:`~abaqus.Mesh.MeshElement.MeshElement` objects.
        """
        pass

    def getElementsViaTopology(self, domain: MeshElementArray = MeshElementArray([])):
        """This method returns an array of MeshElement objects that are obtained by recursively
        finding adjacent elements via topology.

        Parameters
        ----------
        domain
            A :py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` object specifying the domain to include in the search. By default,
            all elements in the mesh are included.

        Returns
        -------
        MeshElementArray
            A :py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` object, which is a sequence of MeshElement objects.
        """
        pass

    def getNodesViaTopology(self, domain: MeshElementArray = MeshElementArray([])):
        """This method returns an array of MeshNode objects that lie along element edges
        topologically in line with the element edge.

        Parameters
        ----------
        domain
            A :py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` object specifying the domain to include in the search. By default,
            all elements in the mesh are included.

        Returns
        -------
        MeshNodeArray
            A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object, which is a sequence of MeshNode objects.
        """
        pass

    def getElemFaces(self):
        """This method returns a tuple of unique MeshFace objects that share the element edge.

        Returns
        -------
        tuple[MeshFace, ...]
            A tuple of :py:class:`~abaqus.Mesh.MeshFace.MeshFace` objects.
        """
        pass

    def getNodes(self):
        """This method returns a tuple of nodes on the element edge.

        Returns
        -------
        tuple[MeshNode, ...]
            A tuple of :py:class:`~abaqus.Mesh.MeshNode.MeshNode` objects.
        """
        pass
