from __future__ import annotations

from typing import Union, Optional, Sequence, overload

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Region import Region
from ..BasicGeometry.EdgeArray import EdgeArray
from ..BasicGeometry.Face import Face
from ..BasicGeometry.FaceArray import FaceArray
from ..Mesh.MeshElementArray import MeshElementArray
from ..Mesh.MeshNodeArray import MeshNodeArray
from ..UtilityAndView.SymbolicConstant import abaqusConstants as C
from ..UtilityAndView.abaqusConstants import SymbolicConstant, UNION


@abaqus_class_doc
class Surface(Region):
    """The Surface object stores surfaces selected from the assembly. A surface is comprised of
    geometric or discrete entities but not both. An instance of a Surface object is
    available from the **surface** member of the Assembly object.

    .. note::
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].allInternalSurfaces[name]
            mdb.models[name].parts[name].allSurfaces[name]
            mdb.models[name].parts[name].surfaces[name]
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].surfaces[name]
            mdb.models[name].rootAssembly.allInternalSurfaces[name]
            mdb.models[name].rootAssembly.allSurfaces[name]
            mdb.models[name].rootAssembly.instances[name].surfaces[name]
            mdb.models[name].rootAssembly.modelInstances[i].surfaces[name]
            mdb.models[name].rootAssembly.surfaces[name]
    """

    #: An :py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` object.
    edges: EdgeArray = EdgeArray([])

    #: A :py:class:`~abaqus.BasicGeometry.FaceArray.FaceArray` object.
    faces: FaceArray = FaceArray([])

    #: A :py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` object.
    elements: MeshElementArray = MeshElementArray([])

    #: A :py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` object.
    nodes: MeshNodeArray = MeshNodeArray([])

    #: A tuple of SymbolicConstants specifying the sides; for example, (SIDE1, SIDE2).
    sides: Optional[Sequence[SymbolicConstant]] = None

    #: A tuple of Ints specifying the instances. This member is not applicable for a Surface
    #: object on an output database.
    instances: Optional[int] = None

    @overload
    @abaqus_method_doc
    def __init__(
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
        **kwargs,
    ) -> None:
        """This method creates a surface from a sequence of objects in a model database. The
        surface will apply to the sides specified by the arguments.For example
        surface=mdb.models['Model-1'].parts['Part-1'].Surface(side1Faces=side1Faces,
        name='Surf-1')

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
        Surface
            A :py:class:`~abaqus.Region.Surface.Surface` object.
        """
        ...

    @overload
    @abaqus_method_doc
    def __init__(self, name: str, objectToCopy: Surface) -> None:
        """This method copies a surface from an existing surface.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].Surface
                mdb.models[name].rootAssembly.Surface

        Parameters
        ----------
        name
            A String specifying the name of the surface.
        objectToCopy
            A :py:class:`~abaqus.Region.Surface.Surface` object to be copied.

        Returns
        -------
        Surface
            A :py:class:`~abaqus.Region.Surface.Surface` object.
        """
        ...

    @abaqus_method_doc
    def __init__(self, *args, **kwargs) -> None:
        ...

    def SurfaceByBoolean(
        self,
        name: str,
        surfaces: Sequence[Surface],
        operation: Literal[C.UNION, C.INTERSECTION, C.DIFFERENCE] = UNION,
    ) -> Surface:
        """This method creates a surface by performing a boolean operation on two or more input
        surfaces.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].Surface
                mdb.models[name].rootAssembly.Surface

        Parameters
        ----------
        name
            A String specifying the repository key.
        surfaces
            A sequence of Surface objects.
        operation
            A SymbolicConstant specifying the boolean operation to perform. Possible values are
            UNION, INTERSECTION, and DIFFERENCE. The default value is UNION. Note that if DIFFERENCE
            is specified, the order of the given input surfaces is important; All surfaces specified
            after the first one are subtracted from the first one.

        Returns
        -------
        Surface
            A :py:class:`~abaqus.Region.Surface.Surface` object.
        """
        ...

    @abaqus_method_doc
    def SurfaceFromElsets(self, name: str, elementSetSeq: tuple) -> Surface:
        """This method creates a surface from a sequence of element sets in a model database.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].Surface
                mdb.models[name].rootAssembly.Surface

        Parameters
        ----------
        name
            A String specifying the repository key.
        elementSetSeq
            A sequence of element sets. For example,`elementSetSeq=((elset1, S1),(elset2, S2))`where
            `elset1=mdb.models[name].rootAssembly.sets['Clutch']` and `S1` and `S2` indicate the
            side of the element set.

        Returns
        -------
        Surface
            A :py:class:`~abaqus.Region.Surface.Surface` object.
        """
        ...
