from abaqusConstants import *
from .Leaf import Leaf
from ..Region.Surface import Surface


class LeafFromMeshSurfaceSets(Leaf):
    """The LeafFromMeshSurfaceSets object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects
    are constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.
    The LeafFromMeshSurfaceSets object is derived from the Leaf object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import displayGroupMdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: SymbolicConstant = None

    def __init__(self, surfaceSets: tuple[Surface]):
        """This method creates a Leaf object from a sequence of surface sets.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                LeafFromMeshSurfaceSets

        Parameters
        ----------
        surfaceSets
            A sequence of Surface objects.

        Returns
        -------
        LeafFromMeshSurfaceSets
            A :py:class:`~abaqus.DisplayGroup.LeafFromMeshSurfaceSets.LeafFromMeshSurfaceSets` object.
        """
        super().__init__(DEFAULT_MODEL)
        pass
