from .MeshEdge import MeshEdge


class MeshEdgeArray(list[MeshEdge]):
    """The MeshEdgeArray is a sequence of MeshEdge objects.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import part
        mdb.models[name].parts[name].elementEdges
        import assembly
        mdb.models[name].rootAssembly.allInstances[name].elementEdges
        mdb.models[name].rootAssembly.instances[name].elementEdges
    """

    def __init__(self, elemEdges: list[MeshEdge]):
        """This method creates a MeshEdgeArray object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mesh.MeshEdgeArray

        Parameters
        ----------
        elemEdges
            A list of MeshEdge objects.

        Returns
        -------
            A MeshEdgeArray object.
        """
        super().__init__()

    def getSequenceFromMask(self, mask: str):
        """This method returns the objects in the MeshEdgeArray identified using the specified
        **mask**. When large number of objects are involved, this method is highly efficient.

        Parameters
        ----------
        mask
            A String specifying the object or objects.

        Returns
        -------
            A MeshEdgeArray object.

        Raises
        ------
        Error: The mask results in an empty sequence
            An exception occurs if the resulting sequence is empty.
        """
        pass

    def getMask(self):
        """This method returns a string specifying the object or objects.

        Returns
        -------
            A String specifying the object or objects.
        """
        pass
