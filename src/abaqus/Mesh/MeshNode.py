from typing import Optional, Tuple

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .MeshFace import MeshFace
from ..Datum.DatumCsys import DatumCsys


@abaqus_class_doc
class MeshNode:
    """The MeshNode object refers to a node of a native mesh or an orphan mesh. A MeshNode
    object can be accessed via a part or part instance using an index that refers to the
    internal numbering of the node repository. The index does not refer to the node label.

    .. note:: 
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].allInternalSets[name].nodes[i]
            mdb.models[name].parts[name].allInternalSurfaces[name].nodes[i]
            mdb.models[name].parts[name].allSets[name].nodes[i]
            mdb.models[name].parts[name].allSurfaces[name].nodes[i]
            mdb.models[name].parts[name].nodes[i]
            mdb.models[name].parts[name].retainedNodes[i]
            mdb.models[name].parts[name].sets[name].nodes[i]
            mdb.models[name].parts[name].surfaces[name].nodes[i]
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].nodes[i]
            mdb.models[name].rootAssembly.allInstances[name].sets[name].nodes[i]
            mdb.models[name].rootAssembly.allInstances[name].surfaces[name].nodes[i]
            mdb.models[name].rootAssembly.allInternalSets[name].nodes[i]
            mdb.models[name].rootAssembly.allInternalSurfaces[name].nodes[i]
            mdb.models[name].rootAssembly.allSets[name].nodes[i]
            mdb.models[name].rootAssembly.allSurfaces[name].nodes[i]
            mdb.models[name].rootAssembly.instances[name].nodes[i]
            mdb.models[name].rootAssembly.instances[name].sets[name].nodes[i]
            mdb.models[name].rootAssembly.instances[name].surfaces[name].nodes[i]
            mdb.models[name].rootAssembly.modelInstances[i].nodes[i]
            mdb.models[name].rootAssembly.modelInstances[i].sets[name].nodes[i]
            mdb.models[name].rootAssembly.modelInstances[i].surfaces[name].nodes[i]
            mdb.models[name].rootAssembly.nodes[i]
            mdb.models[name].rootAssembly.sets[name].nodes[i]
            mdb.models[name].rootAssembly.surfaces[name].nodes[i]
    """

    #: An Int specifying the node label.
    label: Optional[int] = None

    #: A String specifying the name of the part instance that owns this node.
    instanceName: str = ""

    #: A tuple of three Floats specifying the coordinates of the new node.
    coordinates: Tuple[float, float, float]

    @abaqus_method_doc
    def __init__(
        self,
        coordinates: Tuple[float, float, float],
        localCsys: Optional[DatumCsys] = None,
        label: Optional[int] = None,
    ) -> None:
        """This method creates a node on an orphan mesh part.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].Node

        Parameters
        ----------
        coordinates
            A sequence of three Floats specifying the coordinates of the new node.
        localCsys
            A :py:class:`~abaqus.Datum.DatumCsys.DatumCsys` object specifying the local coordinate system. If unspecified, the global
            coordinate system will be used.
        label
            An Int specifying the node label.

        Returns
        -------
        node: MeshNode
            A :py:class:`~abaqus.Mesh.MeshNode.MeshNode` object
        """
        ...

    @abaqus_method_doc
    def getElemEdges(self):
        """This method returns a tuple of element edge objects that share the node.

        Returns
        -------
        edges: Sequence[MeshEdge]
            A tuple of MeshEdge objects
        """
        ...

    @abaqus_method_doc
    def getElemFaces(self) -> Tuple[MeshFace, ...]:
        """This method returns a tuple of element face objects that share the node.

        Returns
        -------
        faces: Sequence[MeshFace]
            A tuple of MeshFace objects
        """
        ...

    @abaqus_method_doc
    def getElements(self):
        """This method returns a tuple of element objects that share the node.

        Returns
        -------
        elements: Sequence[MeshElement]
            A tuple of MeshElement objects
        """
        ...

    @abaqus_method_doc
    def getNodesByFeatureEdge(self, angle: float):
        """This method returns an array of mesh node objects that are obtained by recursively
        finding adjacent nodes along a feature edge that are at an angle of less than or equal
        to the specified face angle.

        Parameters
        ----------
        angle
            A float specifying the value of the face angle in degrees.

        Returns
        -------
        nodes: MeshNodeArray
            A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object, which is a sequence of MeshNode objects
        """
        ...

    @abaqus_method_doc
    def setValues(self, label: Optional[int] = None) -> None:
        """This method modifies the MeshNode object.

        Parameters
        ----------
        label
            An Int specifying the node label. This member may only be edited if the node belongs to
            an orphan mesh part. The specified label must be non-negative and must not be in use by
            any other node of the same part.

        Returns
        -------
            None
        """
        ...
