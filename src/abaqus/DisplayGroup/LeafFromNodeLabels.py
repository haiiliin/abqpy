from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Leaf import Leaf
from ..UtilityAndView.abaqusConstants import DEFAULT_MODEL, SymbolicConstant


@abaqus_class_doc
class LeafFromNodeLabels(Leaf):
    """The LeafFromNodeLabels object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects
    are constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.
    The LeafFromNodeLabels object is derived from the Leaf object.

    .. note::
        This object can be accessed by::

            import displayGroupOdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: Optional[SymbolicConstant] = None

    #: A String specifying the name of the part instance to which **nodeLabels** refers.
    partInstanceName: str

    #: A sequence of Strings specifying expressions that denote node labels. The expression can
    #: be any of the following:An Int specifying a single node label; for example, `1`.A String
    #: specifying a single node label; for example, `'7'`.A String specifying a sequence of
    #: node labels; for example, `'3:5'` and `'3:15:3'`.
    nodeLabels: tuple

    @abaqus_method_doc
    def __init__(self, partInstanceName: str, nodeLabels: tuple):
        """This method creates a Leaf object from a sequence of node labels that belong to a single
        part instance.

        .. note::
            This function can be accessed by::

                LeafFromNodeLabels

        Parameters
        ----------
        partInstanceName
            A String specifying the name of the part instance to which **nodeLabels** refers.
        nodeLabels
            A sequence of Strings specifying expressions that denote node labels. The expression can
            be any of the following:An Int specifying a single node label; for example, `1`.A String
            specifying a single node label; for example, `'7'`.A String specifying a sequence of
            node labels; for example, `'3:5'` and `'3:15:3'`.

        Returns
        -------
        LeafFromNodeLabels
            A LeafFromNodeLabels object.
        """
        super().__init__(DEFAULT_MODEL)
