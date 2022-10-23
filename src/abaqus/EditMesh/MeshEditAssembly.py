from typing_extensions import Literal
from typing import overload, Optional, Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..Assembly.AssemblyBase import AssemblyBase
from ..Datum.DatumCsys import DatumCsys
from ..Mesh.MeshElement import MeshElement
from ..Mesh.MeshNode import MeshNode
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import Boolean, OFF, ON, OUTWARD


@abaqus_class_doc
class MeshEditAssembly(AssemblyBase):
    """An :py:class:`~abaqus.Assembly.Assembly.Assembly` object is a container for instances of parts. The Assembly object has no
    constructor command. Abaqus creates the **rootAssembly** member when a Model object is
    created.

    .. note:: 
        This object can be accessed by::

            import assembly
            mdb.models[name].rootAssembly
    """

    @abaqus_method_doc
    def collapseMeshEdge(self, edge: str, collapseMethod: Literal[C.FORWARD, C.REVERSE, C.AVERAGE]):
        """This method collapses an edge of a quadrilateral or triangular element of a part
        instance.

        Parameters
        ----------
        edge
            A single MeshEdge object specifying the element edge to collapse.
        collapseMethod
            A SymbolicConstant specifying the method used to collapse the edge. Possible values are
            FORWARD, REVERSE, and AVERAGE.
        """
        ...

    @abaqus_method_doc
    def combineElement(self, elements: tuple):
        """This method combines two triangular elements of a part instance.

        Parameters
        ----------
        elements
            A sequence of triangular MeshElement objects specifying the elements to combine.
        """
        ...

    @abaqus_method_doc
    def deleteElement(
        self, elements: Sequence[MeshElement], deleteUnreferencedNodes: Boolean = OFF
    ):
        """This method deletes the given elements from a part instance. The elements must have been
        generated using the bottom-up meshing technique.

        Parameters
        ----------
        elements
            A sequence of MeshElement objects or a Set object containing elements.
        deleteUnreferencedNodes
            A Boolean specifying whether to delete all those associated nodes that become
            unreferenced after the given elements are deleted. The default value is OFF.
        """
        ...

    @abaqus_method_doc
    def projectNode(self, nodes: Sequence[MeshNode], projectionReference: str):
        """This method projects the given nodes of a part instance onto a mesh entity, geometric
        entity, or a datum object.

        Parameters
        ----------
        nodes
            A sequence of MeshNode objects to be projected.
        projectionReference
            An object specifying the target for the node projection operation. The
            **projectionReference** can be any one of the following objects: MeshNode, MeshEdge,
            MeshFace, ConstrainedSketchVertex, Edge, Face, DatumPoint, DatumAxis, or DatumPlane.
        """
        ...

    @abaqus_method_doc
    def editNode(
        self,
        nodes: Sequence[MeshNode],
        coordinate1: Optional[float] = None,
        coordinate2: Optional[float] = None,
        coordinate3: Optional[float] = None,
        coordinates: Sequence[float] = (),
        offset1: Optional[float] = None,
        offset2: Optional[float] = None,
        offset3: Optional[float] = None,
        localCsys: Optional[DatumCsys] = None,
        projectToGeometry: Boolean = ON,
    ):
        """This method changes the coordinates of the given nodes on a part instance.

        Parameters
        ----------
        nodes
            A sequence of MeshNode objects or a Set object containing nodes.
        coordinate1
            A Float specifying the value of the first coordinate. If **coordinate1** and **offset1** are
            unspecified, the existing value does not change.
        coordinate2
            A Float specifying the value of the second coordinate. If **coordinate2** and **offset2**
            are unspecified, the existing value does not change.
        coordinate3
            A Float specifying the value of the third coordinate. If **coordinate3** and **offset3** are
            unspecified, the existing value does not change.
        coordinates
            A sequence of three-dimensional coordinate tuples specifying the coordinates for each of
            the given nodes. When specified, the number of coordinate tuples must match the number
            of given nodes, and be ordered to correspond to the given nodes in **ascending order**
            according to index. Furthermore, **coordinate1**, **coordinate2**, **coordinate3**, **offset1**,
            **offset2**, or **offset3** may not be specified.
        offset1
            A Float specifying an offset to apply to the value of the first coordinate of the
            specified nodes.
        offset2
            A Float specifying an offset to apply to the value of the second coordinate of the
            specified nodes.
        offset3
            A Float specifying an offset to apply to the value of the third coordinate of the
            specified nodes.
        localCsys
            A :py:class:`~abaqus.Datum.DatumCsys.DatumCsys` object specifying the local coordinate system. If unspecified, the global
            coordinate system will be used.
        projectToGeometry
            A Boolean specifying whether to project nodes back to their original geometry. For
            example, if a node is on a face, this method first positions the node at the new
            location and then projects it back to the original face. The default value is ON.

        Raises
        ------
        A coordinate and an offset may not both be specified for the same coordinate component
        """
        ...

    @overload
    @abaqus_method_doc
    def mergeNodes(
        self,
        nodes: Sequence[MeshNode],
        tolerance: Optional[float] = None,
        removeDuplicateElements: Boolean = True,
    ):
        """Merge the nodes of a part instance. The nodes must have been generated using the
        bottom-up meshing technique.

        Parameters
        ----------
        nodes
            A sequence of MeshNode objects specifying the nodes to merge.
        tolerance
            A Float specifying the maximum distance between nodes that will be merged to a single
            node. The location of the new node is the average position of the merged nodes. The
            default value is 10-6.
        removeDuplicateElements
            A Boolean specifying whether elements with the same connectivity after the merge will
            merged into a single element. The default value is True.
        """
        ...

    @overload
    @abaqus_method_doc
    def mergeNodes(
        self, node1: MeshNode, node2: MeshNode, removeDuplicateElements: Boolean = True
    ):
        """Merge two nodes of a part instance. At least one of the two nodes must have been
        generated using the bottom-up meshing technique.

        Parameters
        ----------
        node1
            A :py:class:`~abaqus.Mesh.MeshNode.MeshNode` object specifying the first node to merge.
        node2
            A :py:class:`~abaqus.Mesh.MeshNode.MeshNode` object specifying the second node to merge.
        removeDuplicateElements
            A Boolean specifying whether elements with the same connectivity after the merge will
            merged into a single element. The default value is True.
        """
        ...

    @abaqus_method_doc
    def mergeNodes(self, *args, **kwargs):
        ...

    def splitElement(self, elements: tuple):
        """This method splits quadrilateral elements into triangular elements.

        Parameters
        ----------
        elements
            A sequence of quadrilateral MeshElement objects specifying the elements to split. Each
            quadrilateral element is split into two triangular elements by the shorter diagonal.
        """
        ...

    @abaqus_method_doc
    def splitMeshEdge(self, edge: str, parameter: float = 0):
        """This method splits an edge of a quadrilateral or triangular element of a part instance.

        Parameters
        ----------
        edge
            A single MeshEdge object specifying the element edge to split.
        parameter
            A Float specifying the normalized distance along the **edge** at which to split. Possible
            values are 0.0 << **parameter** << 1.0. The default value is 0.5.
        """
        ...

    @abaqus_method_doc
    def swapMeshEdge(self, edge: str):
        """This method swaps the diagonal of two adjacent triangular elements of a part instance.

        Parameters
        ----------
        edge
            A single MeshEdge object specifying the element edge to swap.
        """
        ...

    @abaqus_method_doc
    def generateMeshByOffset(
        self,
        region: Region,
        meshType: str,
        totalThickness: float,
        distanceBetweenLayers: float,
        numLayers: int,
        offsetDirection: str = OUTWARD,
        initialOffset: float = 0.0,
        shareNodes: str = False,
        deleteBaseElements: Boolean = False,
        constantThicknessCorners: Boolean = False,
        extendElementSets: Boolean = False,
    ):
        """This method generates a solid or shell mesh from an orphan mesh surface by generating
        layers of elements that propagate out normal to the surface boundary.

        Parameters
        ----------
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the domain to be offset.
        meshType
            A Symbolic Constant specifying the type of mesh to be generated. Possible values are
            SOLID or SHELL.
        totalThickness
            A Float specifying the total thickness of the solid layers. This argument applies only
            when **meshType** = SOLID.
        distanceBetweenLayers
            A Float specifying the distance between shell layers. This argument applies only when
            **meshType** = SHELL.
        numLayers
            An Int specifying the number of element layers to be generated.
        offsetDirection
            A Symbolic Constant specifying the direction of the offset. This argument is required
            only when the given region relates to a shell mesh. Possible values are OUTWARD, INWARD,
            and BOTH. The default value is OUTWARD.
        initialOffset
            A Float specifying the magnitude of the initial offset. The default value is zero.
        shareNodes
            Boolean specifying whether the first layer of nodes should be shared with nodes on the
            base surface. The default value is False.
        deleteBaseElements
            A Boolean specifying whether to delete the shell elements after the offset layers are
            generated. The default value is False. This argument applies only when **meshType** = SHELL.
        constantThicknessCorners
            A Boolean specifying whether to use element-based thickness or nodal-based thickness.
            The default value is False.
        extendElementSets
            A Boolean specifying whether existing element sets that include base elements will be
            extended to include corresponding offset elements. The default value is False.
        """
        ...

    @abaqus_method_doc
    def redoMeshEdit(self):
        """This method executes the edit mesh or the bottom-up meshing operation most recently
        undone by the undoMeshEdit method on an assembly. A redo action must be currently
        available for the assembly. This implies that the user must have executed the
        undoMeshEdit method on the assembly and that the user has not subsequently executed any
        further edit mesh commands on the assembly. It also implies that the user provided a
        sufficient cache allowance to store the undo operation.
        """
        ...

    @abaqus_method_doc
    def undoMeshEdit(self):
        """This method undoes the most recent edit mesh or the bottom-up meshing operation on an
        assembly and restores the mesh on the affected part instance to its previous state. An
        edit mesh undo action must be available for the assembly. This implies that prior to
        executing an edit mesh command on the assembly, the user enabled edit mesh undo with a
        sufficient cache allowance to store the edit mesh operation.
        """
        ...
