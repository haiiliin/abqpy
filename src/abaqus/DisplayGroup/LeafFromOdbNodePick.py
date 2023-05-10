from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import DEFAULT_MODEL, SymbolicConstant
from .Leaf import Leaf


@abaqus_class_doc
class LeafFromOdbNodePick(Leaf):
    """The LeafFromOdbNodePick object can be used whenever a Leaf object is expected as an argument. Leaf
    objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects,
    which are then used as arguments to DisplayGroup commands. The LeafFromOdbNodePick object is derived from
    the Leaf object.

    .. note::
        This object can be accessed by::

            import displayGroupOdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: Optional[SymbolicConstant] = None

    @abaqus_method_doc
    def __init__(self, nodePick: tuple):
        """This method creates a Leaf object from a tuple containing machine readable, compact strings defining
        the nodes picked for each part instance. Leaf objects specify the items in a display group.

        .. note::
            This function can be accessed by::

                LeafFromOdbNodePick

        Parameters
        ----------
        nodePick
            A sequence of tuples of the form [part name, entity count, machine readable pick
            strings].

        Returns
        -------
        LeafFromOdbNodePick
            A LeafFromOdbNodePick object.
        """
        super().__init__(DEFAULT_MODEL)
