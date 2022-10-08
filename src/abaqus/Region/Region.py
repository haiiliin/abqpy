from typing import Optional, Union, Sequence, overload

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..BasicGeometry.Cell import Cell
from ..BasicGeometry.Edge import Edge
from ..BasicGeometry.Face import Face
from ..BasicGeometry.ReferencePoint import ReferencePoint
from ..BasicGeometry.Vertex import Vertex
from ..Mesh.MeshElement import MeshElement as Element
from ..Mesh.MeshNode import MeshNode as Node


@abaqus_class_doc
class Region:
    """The purpose of the Region object is to provide a link between an attribute and the
    geometric or discrete entities to which the attribute is applied. An attribute (Load,
    BC, IC, etc.) is applied to one or more Region objects; each Region object in turn is
    associated with a picked Set or Surface or with a named Set or Surface. The Region
    object provides a unified interface (or "façade") to data and functionality located at
    the Set or Surface.
    A script that applies an attribute to a picked Set or Surface requires the explicit
    creation of a Region object and will implicitly create a matching internal Set or
    Surface. Conversely, a script that applies an attribute to a named Set or Surface
    requires the explicit creation of that Set or Surface (see 39.4) and will implicitly
    create a region object.
    The reference between Region and Set/Surface is by name (user-provided or internal.) If
    the Set/Surface is suppressed, deleted, or renamed, the Region object will not be able
    to find the associated Set/Surface, and will communicate that to the attribute, but will
    not be affected otherwise. If a Set/Surface with the same name becomes available (only
    possible with user-provided names) the Region object will re-establish the connection.
    Another way of correcting this problem is to re-apply the attribute.
    Wherever a particular Load, BC, IC, etc. command accepts a named set or a named surface,
    that command will also accept a Region object. For example::
    
        myRegion = regionToolset.Region(edges=edges1)
        mdb.models['Model-1'].DisplacementBC(name='BC-1'
            createStepName='Initial', region=myRegion, u1=SET
            u2=SET)
        myRegion = regionToolset.Region(elements=e[1:100])
        p = mdb.models['mirror'].parts['COLLAR_MIRROR-1']
        p.SectionAssignment(region=myRegion, sectionName='Section-1')
    
    Abaqus does not provide a regions repository; as an alternative, you should assign a
    variable to a Region object and refer to the variable. The lifecycle of a Region object
    is similar to the lifecycle of a Leaf object used by display groups; as a result, you
    should use a Region object immediately after you create it. The contents of a Region
    object are not intended to survive regeneration. If you use an out-of-date Region
    object, the script is unlikely to function correctly.
    Querying an attribute's Region will return a Region tuple. The contents of the tuple are
    the set name followed by the owners of the set and three flags expressed as integers.
    The flags indicate the region space, the type of region and the whether the region is an
    internal set.

    .. note:: 
        This object can be accessed by::

            import regionToolset
    """

    @overload
    @abaqus_method_doc
    def __init__(
        self,
        elements: Optional[Sequence[Element]] = None,
        nodes: Optional[Sequence[Node]] = None,
        vertices: Optional[Sequence[Vertex]] = None,
        edges: Optional[Sequence[Edge]] = None,
        faces: Optional[Sequence[Face]] = None,
        cells: Optional[Sequence[Cell]] = None,
        referencePoints: Optional[Sequence[ReferencePoint]] = (),
        xVertices: Optional[Sequence[Vertex]] = None,
        xEdges: Optional[Sequence[Vertex]] = None,
        xFaces: Optional[Sequence[Vertex]] = None,
        skinFaces: tuple = ...,
        skinEdges: tuple = ...,
        stringerEdges: tuple = ...,
    ):
        """This command creates a set-like region. For example
        myRegion = regionToolset.Region(vertices=v[2:4]
            edges=e[4:5]+e[6:9])
        The arguments are the same as the arguments to the Set method, except for the **name**
        argument.
        In most cases, the constructor will be called with only one argument of sequences. The
        arguments **xVertices**, **xEdges**, and **xFaces** are used to exclude lower-dimension
        entities and to provide finer control on the content of the region. For example, the
        following statement defines a region enclosing a square face but without two of its
        edges:
        region = regionToolset.Region(faces=f[3:4], xEdges=e[1:3])

        .. note:: 
            This function can be accessed by::

                Region

        Parameters
        ----------
        elements
            A sequence of Element objects. The default value is None.
        nodes
            A sequence of Node objects. The default value is None.
        vertices
            A sequence of ConstrainedSketchVertex objects. The default value is None.
        edges
            A sequence of Edge objects. The default value is None.
        faces
            A sequence of Face objects. The default value is None.
        cells
            A sequence of Cell objects. The default value is None.
        referencePoints
            A sequence of ReferencePoint objects. The default value is an empty sequence.
        xVertices
            A sequence of ConstrainedSketchVertex objects that excludes specific vertices from the region. The
            default value is None.
        xEdges
            A sequence of ConstrainedSketchVertex objects that excludes specific edges from the region. The default
            value is None.
        xFaces
            A sequence of ConstrainedSketchVertex objects that excludes specific faces from the region. The default
            value is None.
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
        Region
            A :py:class:`~abaqus.Region.Region.Region` object.
        """
        ...

    @overload
    @abaqus_method_doc
    def __init__(
        self,
        side1Faces: Union[Face, Sequence[Face], None] = None,
        side2Faces: Union[Face, Sequence[Face], None] = None,
        side12Faces: Union[Face, Sequence[Face], None] = None,
        side1Edges: Union[Edge, Sequence[Edge], None] = None,
        side2Edges: Union[Edge, Sequence[Edge], None] = None,
        end1Edges: Union[Edge, Sequence[Edge], None] = None,
        end2Edges: Union[Edge, Sequence[Edge], None] = None,
        circumEdges: Union[Edge, Sequence[Edge], None] = None,
        face1Elements: Union[Element, Sequence[Element], None] = None,
        face2Elements: Union[Element, Sequence[Element], None] = None,
        face3Elements: Union[Element, Sequence[Element], None] = None,
        face4Elements: Union[Element, Sequence[Element], None] = None,
        face5Elements: Union[Element, Sequence[Element], None] = None,
        face6Elements: Union[Element, Sequence[Element], None] = None,
        side1Elements: Union[Element, Sequence[Element], None] = None,
        side2Elements: Union[Element, Sequence[Element], None] = None,
        side12Elements: Union[Element, Sequence[Element], None] = None,
        end1Elements: Union[Element, Sequence[Element], None] = None,
        end2Elements: Union[Element, Sequence[Element], None] = None,
        circumElements: Union[Element, Sequence[Element], None] = None,
    ):
        """This command creates a surface-like region. For example
        myRegion = regionToolset.Region(side1Faces=f[12:14])
        The arguments are the same as the arguments to the Surface method, except for the **name**
        argument.

        .. note:: 
            This function can be accessed by::

                Region

        Parameters
        ----------
        side1Faces
            A sequence of Face objects (surface applies to SIDE1 of face). The default value is
            None.
        side2Faces
            A sequence of Face objects (surface applies to SIDE2 of face). The default value is
            None.
        side12Faces
            A sequence of Face objects (surface applies to both SIDE1 and SIDE2 of face). The
            default value is None.
        side1Edges
            A sequence of Edge objects (surface applies to SIDE1 of edge). The default value is
            None.
        side2Edges
            A sequence of Edge objects (surface applies to SIDE2 of edge). The default value is
            None.
        end1Edges
            A sequence of Edge objects (surface applies to END1 of edge). The default value is None.
        end2Edges
            A sequence of Edge objects (surface applies to END2 of edge). The default value is None.
        circumEdges
            A sequence of Edge objects (surface applies circumferentially to edge). The default
            value is None.
        face1Elements
            A sequence of Element objects (surface applies to FACE1 of element). The default value
            is None.
        face2Elements
            A sequence of Element objects (surface applies to FACE2 of element). The default value
            is None.
        face3Elements
            A sequence of Element objects (surface applies to FACE3 of element). The default value
            is None.
        face4Elements
            A sequence of Element objects (surface applies to FACE4 of element). The default value
            is None.
        face5Elements
            A sequence of Element objects (surface applies to FACE5 of element). The default value
            is None.
        face6Elements
            A sequence of Element objects (surface applies to FACE6 of element). The default value
            is None.
        side1Elements
            A sequence of Element objects (surface applies to SIDE1 of element). The default value
            is None.
        side2Elements
            A sequence of Element objects (surface applies to SIDE2 of element). The default value
            is None.
        side12Elements
            A sequence of Element objects (surface applies to both SIDE1 and SIDE2 of element). The
            default value is None.
        end1Elements
            A sequence of Element objects (surface applies to END1 of element). The default value is
            None.
        end2Elements
            A sequence of Element objects (surface applies to END2 of element). The default value is
            None.
        circumElements
            A sequence of Element objects (surface applies to circumference of element). The default
            value is None.

        Returns
        -------
        Region
            A :py:class:`~abaqus.Region.Region.Region` object.
        """
        ...

    def __init__(self, *args, **kwargs):
        ...
