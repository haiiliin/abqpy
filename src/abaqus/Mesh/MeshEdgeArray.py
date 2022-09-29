from typing import List

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .MeshEdge import MeshEdge


@abaqus_class_doc
class MeshEdgeArray(List[MeshEdge]):
    """The MeshEdgeArray is a sequence of MeshEdge objects.

    .. note:: 
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].elementEdges
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].elementEdges
            mdb.models[name].rootAssembly.instances[name].elementEdges
    """

    @abaqus_method_doc
    def __init__(self, elemEdges: List[MeshEdge]):
        """This method creates a MeshEdgeArray object.

        .. note:: 
            This function can be accessed by::

                mesh.MeshEdgeArray

        Parameters
        ----------
        elemEdges
            A list of MeshEdge objects.

            .. versionchanged:: 2022
                The argument `edges` was renamed to `elemEdges`.

        Returns
        -------
        MeshEdgeArray
            A :py:class:`~abaqus.Mesh.MeshEdgeArray.MeshEdgeArray` object.
        """
        super().__init__()

    @abaqus_method_doc
    def getSequenceFromMask(self, mask: str):
        """This method returns the objects in the MeshEdgeArray identified using the specified
        **mask**. When large number of objects are involved, this method is highly efficient.

        Parameters
        ----------
        mask
            A String specifying the object or objects.

        Returns
        -------
        MeshEdgeArray
            A :py:class:`~abaqus.Mesh.MeshEdgeArray.MeshEdgeArray` object.

        Raises
        ------
        Error: The mask results in an empty sequence
            An exception occurs if the resulting sequence is empty.
        """
        ...

    @abaqus_method_doc
    def getMask(self):
        """This method returns a string specifying the object or objects.

        Returns
        -------
        str
            A String specifying the object or objects.
        """
        ...
