from __future__ import annotations

from typing import List, Sequence, Union

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
    def __init__(self, edges: List[MeshEdge]):
        """This method creates a MeshEdgeArray object.

        .. note:: 
            This function can be accessed by::

                mesh.MeshEdgeArray

        Parameters
        ----------
        edges
            A list of MeshEdge objects.

        Returns
        -------
        MeshEdgeArray
            A :py:class:`~abaqus.Mesh.MeshEdgeArray.MeshEdgeArray` object.
        """
        super().__init__()

    @abaqus_method_doc
    def getSequenceFromMask(self, mask: Union[str, Sequence[str]]) -> MeshEdgeArray:
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
