import typing

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from ..BasicGeometry.Edge import Edge
from ..BasicGeometry.EdgeArray import EdgeArray
from ..BasicGeometry.Face import Face
from ..BasicGeometry.FaceArray import FaceArray
from ..Mesh.MeshEdge import MeshEdge
from ..Mesh.MeshElementArray import MeshElementArray
from ..Mesh.MeshFace import MeshFace


@abaqus_class_doc
class Skin:
    """The Skin object stores information on skin reinforcements created on entities.

    .. note:: 
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].skins[name]
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].skins[name]
            mdb.models[name].rootAssembly.instances[name].skins[name]
            mdb.models[name].rootAssembly.skins[name]
    """

    #: A :py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` object.
    elements: MeshElementArray = MeshElementArray([])

    #: An :py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` object.
    edges: EdgeArray = EdgeArray([])

    #: A :py:class:`~abaqus.BasicGeometry.FaceArray.FaceArray` object.
    faces: FaceArray = FaceArray([])

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        faces: typing.Tuple[Face, ...] = (),
        edges: typing.Tuple[Edge, ...] = (),
        elementFaces: typing.Tuple[MeshFace, ...] = (),
        elementEdges: typing.Tuple[MeshEdge, ...] = (),
    ):
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
            Applicable to three and two dimensional parts.
        edges
            A sequence of Edge objects specifying the edges on which skins should be created.
            Applicable to axisymmetric parts.
        elementFaces
            A sequence of MeshFace objects specifying the mesh faces on which skins should be
            created. Applicable to three and two dimensional parts.
        elementEdges
            A sequence of MeshEdge objects specifying the mesh edges on which skins should be
            created. Applicable to axisymmetric parts.

        Returns
        -------
        Skin
            A :py:class:`~abaqus.Region.Skin.Skin` object.
        """
        ...

    @abaqus_method_doc
    def EditSkin(
        self,
        name: str = "",
        faces: typing.Tuple[Face, ...] = (),
        edges: typing.Tuple[Edge, ...] = (),
        elementFaces: typing.Tuple[MeshFace, ...] = (),
        elementEdges: typing.Tuple[MeshEdge, ...] = (),
    ):
        """This method modifies underlying entities of the selected skin. At least one of the
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
            Applicable to three and two dimensional parts.
        edges
            A sequence of Edge objects specifying the edges on which skins should be created.
            Applicable to axisymmetric parts.
        elementFaces
            A sequence of MeshFace objects specifying the mesh faces on which skins should be
            created. Applicable to three and two dimensional parts.
        elementEdges
            A sequence of MeshEdge objects specifying the mesh edges on which skins should be
            created. Applicable to axisymmetric parts.

        Returns
        -------
        Skin
            A :py:class:`~abaqus.Region.Skin.Skin` object.
        """
        ...
