from __future__ import annotations

from typing import overload, Optional, Sequence, Tuple

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Region import Region
from ..BasicGeometry.Cell import Cell
from ..BasicGeometry.CellArray import CellArray
from ..BasicGeometry.Edge import Edge
from ..BasicGeometry.EdgeArray import EdgeArray
from ..BasicGeometry.Face import Face
from ..BasicGeometry.FaceArray import FaceArray
from ..BasicGeometry.ReferencePoint import ReferencePoint
from ..BasicGeometry.ReferencePointArray import ReferencePointArray
from ..BasicGeometry.Vertex import Vertex
from ..BasicGeometry.VertexArray import VertexArray
from ..Mesh.MeshElement import MeshElement
from ..Mesh.MeshElementArray import MeshElementArray
from ..Mesh.MeshNode import MeshNode
from ..Mesh.MeshNodeArray import MeshNodeArray
from ..UtilityAndView.abaqusConstants import Boolean, OVERWRITE, UNION, INTERSECTION, DIFFERENCE


@abaqus_class_doc
class Set(Region):
    """If a set spans more than one part instance, the members **vertices**, **edges**, **faces**,
    **cells**, **elements**, or **nodes** return a sequence of all the queried
    vertices/edges/faces/cells/elements/nodes respectively for each part instance contained
    in the set. For example::

        assembly=mdb.models['Transmission'].rootAssembly
        clutchElements=assembly.instances['Clutch'].elements
        clutchSet=clutchElements[16:18]+clutchElements[78:80]
        housingElements=assembly.instances['Housing'].elements
        housingSet=housingElements[45:48]
        transmissionSet=assembly.Set(name='TransmissionSet', elements=(clutchSet, housingSet))
        len(transmissionSet.elements)=7
        transmissionSet.elements[0]=mdb.models['Transmission'].rootAssembly.instances['Clutch-1'].elements[16]
        transmissionSet.elements[6]=mdb.models['Transmission'].rootAssembly.instances['housing-'].elements[47]

    .. note::
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].allInternalSets[name]
            mdb.models[name].parts[name].allSets[name]
            mdb.models[name].parts[name].sets[name]
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].sets[name]
            mdb.models[name].rootAssembly.allInternalSets[name]
            mdb.models[name].rootAssembly.allSets[name]
            mdb.models[name].rootAssembly.instances[name].sets[name]
            mdb.models[name].rootAssembly.modelInstances[i].sets[name]
            mdb.models[name].rootAssembly.sets[name]
    """

    #: A MeshElementArray object.
    elements: MeshElementArray = MeshElementArray([])

    #: A MeshNodeArray object.
    nodes: MeshNodeArray = MeshNodeArray([])

    #: A VertexArray object.
    vertices: VertexArray = VertexArray([])

    #: An EdgeArray object.
    edges: EdgeArray = EdgeArray([])

    #: A FaceArray object.
    faces: FaceArray = FaceArray([])

    #: A CellArray object.
    cells: CellArray = CellArray([])

    #: A VertexArray object.
    xVertices: VertexArray = VertexArray([])

    #: An EdgeArray object.
    xEdges: EdgeArray = EdgeArray([])

    #: A FaceArray object.
    xFaces: FaceArray = FaceArray([])

    #: A ReferencePointArray object.
    referencePoints: ReferencePointArray = []

    @overload
    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        nodes: Optional[Sequence[MeshNode]] = None,
        elements: Optional[Sequence[MeshElement]] = None,
        region: Optional[Region] = None,
        vertices: Optional[Sequence[Vertex]] = None,
        edges: Optional[Sequence[Edge]] = None,
        faces: Optional[Sequence[Face]] = None,
        cells: Optional[Sequence[Cell]] = None,
        xVertices: Optional[Sequence[Vertex]] = None,
        xEdges: Optional[Sequence[Edge]] = None,
        xFaces: Optional[Sequence[Face]] = None,
        referencePoints: Sequence[ReferencePoint] = (),
        skinFaces: Tuple[Tuple[str, Sequence[Face]], ...] = ...,
        skinEdges: Tuple[Tuple[str, Sequence[Edge]], ...] = ...,
        stringerEdges: Tuple[Tuple[str, Sequence[Edge]], ...] = ...,
    ) -> None:
        """This method creates a set from a sequence of objects in a model database.

        At least one sequence argument must be provided - elements, nodes, vertices, edges,
        faces, cells, or referencePoints. The arguments xVertices, xEdges, and xFaces are
        used to exclude lower-dimension entities and to provide finer control on the
        content of the set. For example, the following statement defines a region enclosing
        a square face but without two of its edges::

            set = mdb.models['Model-1'].rootAssembly.Set(name='mySet', faces=f[3:4], xEdges=e[1:3])

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].Set
                mdb.models[name].rootAssembly.Set

        Parameters
        ----------
        name
            A String specifying the repository key.
        nodes
            A sequence of MeshNode objects. The default value is None.
        elements
            A sequence of MeshElement objects. The default value is None.
        region
            A Region object specifying other objects to be included in the set. The default value is
            None.
        vertices
            A sequence of ConstrainedSketchVertex objects. The default value is None.
        edges
            A sequence of Edge objects. The default value is None.
        faces
            A sequence of Face objects. The default value is None.
        cells
            A sequence of Cell objects. The default value is None.
        xVertices
            A sequence of ConstrainedSketchVertex objects that excludes specific vertices from the set. The default
            value is None.
        xEdges
            A sequence of Edge objects that excludes specific edges from the set. The default value
            is None.
        xFaces
            A sequence of Face objects that excludes specific faces from the set. The default value
            is None.
        referencePoints
            A sequence of ReferencePoint objects. The default value is an empty sequence.
        skinFaces
            A tuple of tuples specifying a skin name and the sequence of faces associated with this
            skin. Valid only for geometric regions on 3D and 2D parts.
        skinEdges
            A tuple of tuples specifying a skin name and the sequence of edges associated with this
            skin. Valid only for geometric regions on Axisymmetric parts.
        stringerEdges
            A tuple of tuples specifying a stringer name and the sequence of edges associated with
            this stringer. Valid only for geometric regions on 3D and 2D parts.

        Returns
        -------
        Set
            A Set object.
        """
        ...

    @overload
    @abaqus_method_doc
    def __init__(self, name: str, objectToCopy: Set) -> None:
        """This method copies a set from an existing set.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].Set
                mdb.models[name].rootAssembly.Set

        Parameters
        ----------
        name
            A String specifying the name of the set.
        objectToCopy
            A Set object to be copied.

        Returns
        -------
        Set
            A Set object.
        """
        ...

    @abaqus_method_doc
    def __init__(self, *args, **kwargs) -> None:
        ...

    def SetByBoolean(
        self, name: str, sets: Sequence[Set], operation: Literal[UNION, INTERSECTION, DIFFERENCE] = UNION
    ) -> Set:
        """This method creates a set by performing a boolean operation on two or more input sets.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].SetByBoolean
                mdb.models[name].rootAssembly.SetByBoolean

        Parameters
        ----------
        name
            A String specifying the repository key.
        sets
            A sequence of Set objects.
        operation
            A SymbolicConstant specifying the boolean operation to perform. Possible values are
            UNION, INTERSECTION, and DIFFERENCE. The default value is UNION. Note that if DIFFERENCE
            is specified, the order of the given input sets is important; All sets specified after
            the first one are subtracted from the first one.

        Returns
        -------
        Set
            A Set object.
        """
        ...

    @abaqus_method_doc
    def SetFromColor(self, name: str, color: tuple) -> Set:
        """This method creates a set containing faces of the part marked with a specified color
        attribute. Third-party applications can assign color attributes to faces, and the color
        attribute can be imported into Abaqus from an ACIS file. You can use this method to
        create sets only on parts; however, you can access the sets from instances of the parts
        in the assembly.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].SetFromColor

        Parameters
        ----------
        name
            A String specifying the repository key.
        color
            A sequence of three Ints specifying the RGB color. Values can range from 0 to 255. The
            first integer is for red, the second for green, and the third for blue. For example, a
            face colored in yellow is identified by:`color=(255,255,0)`

        Returns
        -------
        Set
            A Set object.
        """
        ...

    @abaqus_method_doc
    def SetFromElementLabels(self, name: str, elementLabels: Sequence[int]) -> Set:
        """This method creates a set from a sequence of element labels in a model database.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].SetFromElementLabels
                mdb.models[name].rootAssembly.SetFromElementLabels

        Parameters
        ----------
        name
            A String specifying the repository key.
        elementLabels
            A sequence of element labels. An element label is a sequence of Int element identifiers.
            For example, for a part::

                elementLabels=(2,3,5,7)

            For an assembly::

                elementLabels=(('Instance-1', (2,3,5,7)), ('Instance-2', (1,2,3)))`

        Returns
        -------
        Set
            A Set object.
        """
        ...

    @abaqus_method_doc
    def SetFromNodeLabels(self, name: str, nodeLabels: Sequence[int], unsorted: Boolean = False) -> Set:
        """This method creates a set from a sequence of node labels in a model database.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].SetFromNodeLabels
                mdb.models[name].rootAssembly.SetFromNodeLabels

        Parameters
        ----------
        name
            A String specifying the repository key.
        nodeLabels
            A sequence of node labels. A node label is a sequence of Int node identifiers. For
            example, for a part::

                nodeLabels=(2,3,5,7)

            For an assembly::

                nodeLabels=(('Instance-1', (2,3,5,7)), ('Instance-2', (1,2,3)))`

        unsorted
            A Boolean specifying whether the created set is unsorted. The default value is False.

            .. versionadded:: 2018
                The `unsorted` argument was added.

        Returns
        -------
        Set
            A Set object.
        """
        ...

    @abaqus_method_doc
    def MapSetsFromOdb(self, odbPath: str, odbSets: str, partSets: str = "", method: str = OVERWRITE) -> Set:
        """This method creates sets based on mapping sets from element centroid locations in an
        Odb.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].MapSetsFromOdb

        Parameters
        ----------
        odbPath
            A String specifying the path to the ODB containing the source sets.
        odbSets
            A list of names of sets on the ODB to map.
        partSets
            A list of names of sets to construct or use corresponding to the ODB sets.
        method
            An enum to specify OVERWRITE, APPEND, INTERSECT, or REMOVE. The default is OVERWRITE.

        Returns
        -------
        Set
            A Set object or a tuple of Set objects.
        """
        ...
