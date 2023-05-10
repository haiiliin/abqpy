from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import DEFAULT_MODEL, SymbolicConstant
from .Leaf import Leaf


@abaqus_class_doc
class LeafFromInstanceNodeLabels(Leaf):
    """The LeafFromInstanceNodeLabels object can be used whenever a Leaf object is expected as an argument. Leaf
    objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects,
    which are then used as arguments to DisplayGroup commands. The LeafFromInstanceNodeLabels object is derived
    from the Leaf object.

    .. note::
        This object can be accessed by::

            import displayGroupMdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: Optional[SymbolicConstant] = None

    @abaqus_method_doc
    def __init__(self, nodeLabels: tuple):
        """This method creates a Leaf object from a sequence of Strings specifying the node labels. Leaf objects
        specify the items in a display group.

        .. note::
            This function can be accessed by::

                LeafFromInstanceNodeLabels

        Parameters
        ----------
        nodeLabels
            A sequence of sequences specifying node labels. Each inner sequence consists of a
            PartInstance object followed by a sequence of Strings specifying node labels.

        Returns
        -------
        LeafFromInstanceNodeLabels
            A LeafFromInstanceNodeLabels object.
        """
        super().__init__(DEFAULT_MODEL)
