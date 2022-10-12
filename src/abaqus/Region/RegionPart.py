from __future__ import annotations

from typing import Optional, Union, overload, Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Region import Region
from .RegionPartBase import RegionPartBase
from .Set import Set
from .Skin import Skin
from .Stringer import Stringer
from .Surface import Surface
from ..BasicGeometry.Cell import Cell
from ..BasicGeometry.Edge import Edge
from ..BasicGeometry.Face import Face
from ..BasicGeometry.ReferencePoint import ReferencePoint
from ..BasicGeometry.Vertex import Vertex
from ..Mesh.MeshEdge import MeshEdge
from ..Mesh.MeshElement import MeshElement
from ..Mesh.MeshFace import MeshFace
from ..Mesh.MeshNode import MeshNode


@abaqus_class_doc
class RegionPart(RegionPartBase):
    """The following commands operate on Part objects. For more information about the Part
    object, see Part object.

    .. note:: 
        This object can be accessed by::

            import regionToolset
    """

    @abaqus_method_doc
    def Surface(
        self,
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
        name: str = "",
        **kwargs
    ) -> Surface:
        """This method creates a surface from a sequence of objects in a model database. The
        surface will apply to the sides specified by the arguments.For example::

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
            A :py:class:`~abaqus.Region.Surface.Surface` object
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
        skinFaces: tuple = ...,
        skinEdges: tuple = ...,
        stringerEdges: tuple = ...,
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
            A :py:class:`~abaqus.Region.Region.Region` object specifying other objects to be included in the set. The default value is
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
            A :py:class:`~abaqus.Region.Set.Set` object
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
            A :py:class:`~abaqus.Region.Set.Set` object to be copied.

        Returns
        -------
        set: Set
            A :py:class:`~abaqus.Region.Set.Set` object
        """
        ...

    @abaqus_method_doc
    def Set(self, name, *args, **kwargs) -> Set:
        """This method creates a set from a sequence of objects in a model database.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].Set
                mdb.models[name].rootAssembly.Set

        Parameters
        ----------
        name

        Returns
        -------
        set: Set
            A :py:class:`~abaqus.Region.Set.Set` object
        """
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
        """This method creates a skin from a sequence of objects in a model database. At least one
        of the optional arguments needs to be specified.

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
            A :py:class:`~abaqus.Region.Skin.Skin` object
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
        """This method modifies underlying entities of the selected skin. At least one of the
        optional arguments needs to be specified.

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
            A :py:class:`~abaqus.Region.Skin.Skin` object
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
        """This method creates a stringer from a sequence of objects in a model database. At least
        one of the optional arguments needs to be specified.

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
            A :py:class:`~abaqus.Region.Stringer.Stringer` object
        """
        self.stringers[name] = stringer = Stringer(name, edges, elementEdges)
        return stringer
