import typing

from .Leaf import Leaf
from ..Mesh.MeshNode import MeshNode
from ..UtilityAndView.abaqusConstants import *
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class LeafFromMeshNodeLabels(Leaf):
    """The LeafFromMeshNodeLabels object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects
    are constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.
    The LeafFromMeshNodeLabels object is derived from the Leaf object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import displayGroupMdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: SymbolicConstant = None

    @abaqus_method_doc
    def __init__(self, nodeSeq: typing.Tuple[MeshNode, ...]):
        """This method creates a Leaf object from a sequence of mesh node objects. Leaf objects
        specify the items in a display group.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                LeafFromMeshNodeLabels

        Parameters
        ----------
        nodeSeq
            A sequence of MeshNode objects specifying nodes.

        Returns
        -------
        LeafFromMeshNodeLabels
            A :py:class:`~abaqus.DisplayGroup.LeafFromMeshNodeLabels.LeafFromMeshNodeLabels` object.
        """
        super().__init__(DEFAULT_MODEL)
