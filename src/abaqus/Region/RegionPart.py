from __future__ import annotations

from typing import Optional, Sequence, Tuple, Union, overload

from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..BasicGeometry.Cell import Cell
from ..BasicGeometry.Edge import Edge
from ..BasicGeometry.Face import Face
from ..BasicGeometry.ReferencePoint import ReferencePoint
from ..BasicGeometry.Vertex import Vertex
from ..Mesh.MeshEdge import MeshEdge
from ..Mesh.MeshElement import MeshElement
from ..Mesh.MeshFace import MeshFace
from ..Mesh.MeshNode import MeshNode
from ..UtilityAndView.abaqusConstants import (
    DIFFERENCE,
    INTERSECTION,
    OVERWRITE,
    UNION,
    Boolean,
)
from .Region import Region
from .RegionPartBase import RegionPartBase
from .Set import Set
from .Skin import Skin
from .Stringer import Stringer
from .Surface import Surface


@abaqus_class_doc
class RegionPart(RegionPartBase):
    """The following commands operate on Part objects. For more information about the Part object, see Part
    object.

    .. note::
        This object can be accessed by::

            import regionToolset
    """

    @abaqus_method_doc
    def Surface(
        self,
        name: str,
        side1Faces: Union[Face, Sequence[Face], None] = None,
        side2Faces: Union[Face, Sequence[Face], None] = None,
        side12Faces: Union[Face, Sequence[Face], None] = None,
        end1Edges: Union[Face, Sequence[Face], None] = None,
        end2Edges: Union[Face, Sequence[Face], None] = None,
        circumEdges: Union[Face, Sequence[Face], None] = None,
        side1Edges: Union[Face, Sequence[Face], None] = None,
        side2Edges: Union[Face, Sequence[Face], None] = None,
        face1Elements: Union[Face, Sequence[Face], None] = None,
        face2Elements: Union[Face, Sequence[Face], None] = None,
        face3Elements: Union[Face, Sequence[Face], None] = None,
        face4Elements: Union[Face, Sequence[Face], None] = None,
        face5Elements: Union[Face, Sequence[Face], None] = None,
        face6Elements: Union[Face, Sequence[Face], None] = None,
        side1Elements: Union[Face, Sequence[Face], None] = None,
        side2Elements: Union[Face, Sequence[Face], None] = None,
        side12Elements: Union[Face, Sequence[Face], None] = None,
        end1Elements: Union[Face, Sequence[Face], None] = None,
        end2Elements: Union[Face, Sequence[Face], None] = None,
        circumElements: Union[Face, Sequence[Face], None] = None,
        **kwargs,
    ) -> Surface:
        """This method creates a surface from a sequence of objects in a model database. The surface will apply
        to the sides specified by the arguments.For example::

            surface=mdb.models['Model-1'].parts['Part-1'].Surface(side1Faces=side1Faces, name='Surf-1')

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].Surface
                mdb.models[name].rootAssembly.Surface

        Parameters
        ----------
        name
            A String specifying the repository key. The default value is an empty string.
        side1Elements
            A sequence of MeshElement objects (surface applies to SIDE1 of element).
            The default value is None.
        side2Elements
            A sequence of MeshElement objects (surface applies to SIDE2 of element).
            The default value is None.
        side12Elements
            A sequence of MeshElement objects (surface applies to both SIDE1 and SIDE2 of element).
            The default value is None.
        end1Elements
            A sequence of MeshElement objects (surface applies to END1 of element).
            The default value is None.
        end2Elements
            A sequence of MeshElement objects (surface applies to END2 of element).
            The default value is None.
        circumElements
            A sequence of MeshElement objects (surface applies to circumference of element).
            The default value is None.
        face1Elements
            A sequence of MeshElement objects (surface applies to FACE1 of element) or MeshFace objects.
            The default value is None.
        face2Elements
            A sequence of MeshElement objects (surface applies to FACE2 of element) or MeshFace objects.
            The default value is None.
        face3Elements
            A sequence of MeshElement objects (surface applies to FACE3 of element) or MeshFace objects.
            The default value is None.
        face4Elements
            A sequence of MeshElement objects (surface applies to FACE4 of element) or MeshFace objects.
            The default value is None.
        face5Elements
            A sequence of MeshElement objects (surface applies to FACE5 of element) or MeshFace objects.
            The default value is None.
        face6Elements
            A sequence of MeshElement objects (surface applies to FACE6 of element) or MeshFace objects.
            The default value is None.
        side1Faces
            A sequence of Face objects (surface applies to SIDE1 of face). The default value is None.
        side2Faces
            A sequence of Face objects (surface applies to SIDE2 of face). The default value is None.
        side12Faces
            A sequence of Face objects (surface applies to both SIDE1 and SIDE2 of face).
            The default value is None.
        side1Edges
            A sequence of Edge objects (surface applies to SIDE1 of edge). The default value is None.
        side2Edges
            A sequence of Edge objects (surface applies to SIDE2 of edge). The default value is None.
        end1Edges
            A sequence of Edge objects (surface applies to END1 of edge). The default value is None.
        end2Edges
            A sequence of Edge objects (surface applies to END2 of edge). The default value is None.
        circumEdges
            A sequence of Edge objects (surface applies circumferentially to edge).
            The default value is None.
        kwargs
            The required parameters for different conditions are:

            - On three-dimensional solid faces, you can use the following arguments:
              side1Faces, side2Faces

            - On three-dimensional shell faces, you can use the following arguments:
              side1Faces, side2Faces, side12Faces

            - On three-dimensional wire edges, you can use the following arguments:
              end1Edges, end2Edges, circumEdges

            - On three-dimensional or two-dimensional or axisymmetric edges, you can use the following arguments:
              side1Edges, side2Edges

            - On two-dimensional or axisymmetric shell elements, you can use the following arguments:
              face1Elements, face2Elements, face3Elements, face4Elements

            - On solid elements, you can use the following arguments:
              face1Elements, face2Elements, face3Elements, face4Elements, face5Elements, face6Elements

            - On three-dimensional shell elements, you can use the following arguments:
              side1Elements, side2Elements, side12Elements

            - On three-dimensional wire elements, you can use the following arguments:
              end1Elements, end2Elements, circumElements

            - On two-dimensional or axisymmetric wire elements, you can use the following arguments:
              side1Elements, side2Elements

        Returns
        -------
        surf: Surface
            A Surface object
        """
        surface = Surface(
            side1Faces,
            side2Faces,
            side12Faces,
            end1Edges,
            end2Edges,
            circumEdges,
            side1Edges,
            side2Edges,
            face1Elements,
            face2Elements,
            face3Elements,
            face4Elements,
            face5Elements,
            face6Elements,
            side1Elements,
            side2Elements,
            side12Elements,
            end1Elements,
            end2Elements,
            circumElements,
            name,
        )
        self.surfaces[name] = surface
        self.allSurfaces[name] = surface
        return surface

    @overload
    @abaqus_method_doc
    def Set(
        self,
        name: str,
        nodes: Optional[Sequence[MeshNode]] = None,
        elements: Optional[Sequence[MeshElement]] = None,
        region: Optional[Region] = None,
        vertices: Optional[Sequence[Vertex]] = None,
        edges: Optional[Sequence[Edge]] = None,
        faces: Optional[Union[Face, Sequence[Face]]] = None,
        cells: Optional[Union[Cell, Sequence[Cell]]] = None,
        xVertices: Optional[Sequence[Vertex]] = None,
        xEdges: Optional[Sequence[Edge]] = None,
        xFaces: Optional[Sequence[Face]] = None,
        referencePoints: Sequence[ReferencePoint] = (),
        skinFaces: Tuple[Tuple[str, Sequence[Face]], ...] = ...,
        skinEdges: Tuple[Tuple[str, Sequence[Edge]], ...] = ...,
        stringerEdges: Tuple[Tuple[str, Sequence[Edge]], ...] = ...,
    ) -> Set:
        """This method creates a set from a sequence of objects in a model database.

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
            A sequence of Face objects that exclude specific faces from the set. The default value
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
        set: Set
            A Set object
        """
        ...

    @overload
    @abaqus_method_doc
    def Set(self, name: str, objectToCopy: Set) -> Set:
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
        set: Set
            A Set object
        """
        ...

    @overload
    @abaqus_method_doc
    def Set(
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
    ) -> Set:
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
        set: Set
            A Set object
        """
        ...

    @abaqus_method_doc
    def Set(self, name, *args, **kwargs) -> Set:
        self.sets[name] = aSet = Set(name, *args, **kwargs)
        return aSet

    @abaqus_method_doc
    def Skin(
        self,
        name: str,
        faces: Sequence[Face] = (),
        edges: Sequence[Edge] = (),
        elementFaces: Sequence[MeshFace] = (),
        elementEdges: Sequence[MeshEdge] = (),
    ) -> Skin:
        """This method creates a skin from a sequence of objects in a model database. At least one of the
        optional arguments needs to be specified.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].Skin

        Parameters
        ----------
        name
            A String specifying the repository key. The default value is an empty string.
        faces
            A sequence of Face objects specifying the faces on which skins should be created.
            Applicable to three and two-dimensional parts.
        edges
            A sequence of Edge objects specifying the edges on which skins should be created.
            Applicable to axisymmetric parts.
        elementFaces
            A sequence of MeshFace objects specifying the mesh faces on which skins should be
            created. Applicable to three and two-dimensional parts.
        elementEdges
            A sequence of MeshEdge objects specifying the mesh edges on which skins should be
            created. Applicable to axisymmetric parts.

        Returns
        -------
        skin: Skin
            A Skin object
        """
        self.skins[name] = skin = Skin(name, faces, edges, elementFaces, elementEdges)
        return skin

    @abaqus_method_doc
    def EditSkin(
        self,
        name: str = "",
        faces: Sequence[Face] = (),
        edges: Sequence[Edge] = (),
        elementFaces: Sequence[MeshFace] = (),
        elementEdges: Sequence[MeshEdge] = (),
    ) -> Skin:
        """This method modifies underlying entities of the selected skin. At least one of the optional arguments
        needs to be specified.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].EditSkin

        Parameters
        ----------
        name
            A String specifying the repository key. The default value is an empty string.
        faces
            A sequence of Face objects specifying the faces on which skins should be created.
            Applicable to three and two-dimensional parts.
        edges
            A sequence of Edge objects specifying the edges on which skins should be created.
            Applicable to axisymmetric parts.
        elementFaces
            A sequence of MeshFace objects specifying the mesh faces on which skins should be
            created. Applicable to three and two-dimensional parts.
        elementEdges
            A sequence of MeshEdge objects specifying the mesh edges on which skins should be
            created. Applicable to axisymmetric parts.

        Returns
        -------
        skin: Skin
            A Skin object
        """
        self.skins[name] = skin = Skin(name, faces, edges, elementFaces, elementEdges)
        return skin

    @abaqus_method_doc
    def Stringer(
        self,
        name: str,
        edges: Sequence[Edge] = (),
        elementEdges: Sequence[MeshEdge] = (),
    ) -> Stringer:
        """This method creates a stringer from a sequence of objects in a model database. At least one of the
        optional arguments needs to be specified.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].Stringer

        Parameters
        ----------
        name
            A String specifying the repository key. The default value is an empty string.
        edges
            A sequence of Edge objects specifying the edges on which stringers should be created.
            Applicable to three and two-dimensional parts.
        elementEdges
            A sequence of MeshEdge objects specifying the mesh edges on which stringers should be
            created. Applicable to three and two-dimensional parts.

        Returns
        -------
        stringer: Stringer
            A Stringer object
        """
        self.stringers[name] = stringer = Stringer(name, edges, elementEdges)
        return stringer

    # The following methods was originally in the ``Set`` object page documentation
    # But it accessed only by ``Part`` and ``rootAssembly`` objetcs.

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
        """This method creates a set containing faces of the part marked with a specified color attribute.
        Third-party applications can assign color attributes to faces, and the color attribute can be imported
        into Abaqus from an ACIS file. You can use this method to create sets only on parts; however, you can
        access the sets from instances of the parts in the assembly.

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

        Returns
        -------
        Set
            A Set object.
        """
        ...

    @abaqus_method_doc
    def MapSetsFromOdb(self, odbPath: str, odbSets: str, partSets: str = "", method: str = OVERWRITE) -> Set:
        """This method creates sets based on mapping sets from element centroid locations in an Odb.

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
