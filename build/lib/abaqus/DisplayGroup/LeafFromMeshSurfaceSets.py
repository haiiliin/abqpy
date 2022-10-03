from typing import Optional, Tuple

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Leaf import Leaf
from ..Region.Surface import Surface
from ..UtilityAndView.abaqusConstants import DEFAULT_MODEL, SymbolicConstant


@abaqus_class_doc
class LeafFromMeshSurfaceSets(Leaf):
    """The LeafFromMeshSurfaceSets object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects
    are constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.
    The LeafFromMeshSurfaceSets object is derived from the Leaf object.

    .. note:: 
        This object can be accessed by::

            import displayGroupMdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: Optional[SymbolicConstant] = None

    @abaqus_method_doc
    def __init__(self, surfaceSets: Tuple[Surface, ...]):
        """This method creates a Leaf object from a sequence of surface sets.

        .. note:: 
            This function can be accessed by::

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
