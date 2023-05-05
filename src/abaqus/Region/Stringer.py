from typing import Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..BasicGeometry.Edge import Edge
from ..BasicGeometry.EdgeArray import EdgeArray
from ..Mesh.MeshEdge import MeshEdge
from ..Mesh.MeshElementArray import MeshElementArray


@abaqus_class_doc
class Stringer:
    """The Stringer object stores information on stringer reinforcements created on entities.

    .. note::
        This object can be accessed by::

            import part
            mdb.models[name].parts[name].stringers[name]
            import assembly
            mdb.models[name].rootAssembly.allInstances[name].stringers[name]
            mdb.models[name].rootAssembly.instances[name].stringers[name]
            mdb.models[name].rootAssembly.stringers[name]
    """

    #: A MeshElementArray object.
    elements: MeshElementArray = MeshElementArray([])

    #: An EdgeArray object.
    edges: EdgeArray = EdgeArray([])

    @abaqus_method_doc
    def __init__(self, name: str, edges: Sequence[Edge] = (), elementEdges: Sequence[MeshEdge] = ()):
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
            Applicable to three and two dimensional parts.
        elementEdges
            A sequence of MeshEdge objects specifying the mesh edges on which stringers should be
            created. Applicable to three and two dimensional parts.

        Returns
        -------
        Stringer
            A Stringer object.
        """
        ...

    @abaqus_method_doc
    def EditStringer(self, name: str, edges: Sequence[Edge] = (), elementEdges: Sequence[MeshEdge] = ()):
        """This method modifies underlying entities of the selected stringer. At least one of the optional
        arguments needs to be specified.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].Stringer

        Parameters
        ----------
        name
            A String specifying the repository key. The default value is an empty string.
        edges
            A sequence of Edge objects specifying the edges on which stringers should be created.
            Applicable to three and two dimensional parts.
        elementEdges
            A sequence of MeshEdge objects specifying the mesh edges on which stringers should be
            created. Applicable to three and two dimensional parts.

        Returns
        -------
        Stringer
            A Stringer object.
        """
        ...
