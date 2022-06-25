from abaqusConstants import *
from .Leaf import Leaf


class LeafFromSurfaceSets(Leaf):
    """The LeafFromSurfaceSets object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects
    are constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.
    The LeafFromSurfaceSets object is derived from the Leaf object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import displayGroupOdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: SymbolicConstant = None

    #: A sequence of Strings specifying surface sets, or a String specifying a single surface
    #: set.
    surfaceSets: tuple

    def __init__(self, surfaceSets: tuple):
        """This method creates a Leaf object from a sequence of surface sets.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                LeafFromSurfaceSets

        Parameters
        ----------
        surfaceSets
            A sequence of Strings specifying surface sets, or a String specifying a single surface
            set.

        Returns
        -------
        LeafFromSurfaceSets
            A :py:class:`~abaqus.DisplayGroup.LeafFromSurfaceSets.LeafFromSurfaceSets` object.
        """
        super().__init__(DEFAULT_MODEL)
        pass
