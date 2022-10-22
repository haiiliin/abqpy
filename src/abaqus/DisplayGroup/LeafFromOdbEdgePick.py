from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Leaf import Leaf
from ..UtilityAndView.abaqusConstants import DEFAULT_MODEL, SymbolicConstant


@abaqus_class_doc
class LeafFromOdbEdgePick(Leaf):
    """The LeafFromOdbEdgePick object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects
    are constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.
    The LeafFromOdbEdgePick object is derived from the Leaf object.

    .. note:: 
        This object can be accessed by::

            import displayGroupOdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: Optional[SymbolicConstant] = None

    @abaqus_method_doc
    def __init__(self, edgePick: tuple):
        """This method creates a Leaf object from a tuple containing machine readable, compact
        strings defining the edges picked for each part instance. Leaf objects specify the items
        in a display group.

        .. note:: 
            This function can be accessed by::

                LeafFromOdbEdgePick

        Parameters
        ----------
        edgePick
            A sequence of tuples of the form [part name, entity count, machine readable pick
            strings].

        Returns
        -------
        LeafFromOdbEdgePick
            A :py:class:`~abaqus.DisplayGroup.LeafFromOdbEdgePick.LeafFromOdbEdgePick` object.
        """
        super().__init__(DEFAULT_MODEL)
