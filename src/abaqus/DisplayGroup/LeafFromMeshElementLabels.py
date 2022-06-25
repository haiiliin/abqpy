from abaqusConstants import *
from .Leaf import Leaf
from ..Mesh.MeshElement import MeshElement


class LeafFromMeshElementLabels(Leaf):
    """The LeafFromMeshElementLabels object can be used whenever a Leaf object is expected as
    an argument. Leaf objects are used to specify the items in a display group. Leaf objects
    are constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.
    The LeafFromMeshElementLabels object is derived from the Leaf object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import displayGroupMdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: SymbolicConstant = None

    def __init__(self, elementSeq: tuple[MeshElement]):
        """This method creates a Leaf object from a sequence of mesh element objects. Leaf objects
        specify the items in a display group.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                LeafFromMeshElementLabels

        Parameters
        ----------
        elementSeq
            A sequence of MeshElement objects specifying elements.

        Returns
        -------
        LeafFromMeshElementLabels
            A :py:class:`~abaqus.DisplayGroup.LeafFromMeshElementLabels.LeafFromMeshElementLabels` object.
        """
        super().__init__(DEFAULT_MODEL)
        pass
