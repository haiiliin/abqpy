from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import DEFAULT_MODEL, SymbolicConstant
from .Leaf import Leaf


@abaqus_class_doc
class LeafFromModelNodeLabels(Leaf):
    """The LeafFromModelNodeLabels object can be used whenever a Leaf object is expected as an argument. Leaf
    objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects,
    which are then used as arguments to DisplayGroup commands. The LeafFromModelNodeLabels object is derived
    from the Leaf object.

    .. note::
        This object can be accessed by::

            import displayGroupOdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: Optional[SymbolicConstant] = None

    #: A sequence of Strings specifying expressions that denote node labels per part instance
    #: in the model. Each part instance node expression is a sequence of a String specifying
    #: the part instance name and a sequence of node expressions; for example,
    #: `(('partInstance1',(1,'7','3:15;3'),), ('partInstance2','8'),))`. The node expressions
    #: can be any of the following:An Int specifying a single node label; for example, `1`.A
    #: String specifying a single node label; for example, `'7'`.A String specifying a sequence
    #: of node labels; for example, `'3:5'` and `'3:15:3'`.
    nodeLabels: tuple

    @abaqus_method_doc
    def __init__(self, nodeLabels: tuple):
        """This method creates a Leaf object from a sequence of node labels spanning several part instances.

        .. note::
            This function can be accessed by::

                LeafFromModelNodeLabels

        Parameters
        ----------
        nodeLabels
            A sequence of Strings specifying expressions that denote node labels per part instance
            in the model. Each part instance node expression is a sequence of a String specifying
            the part instance name and a sequence of node expressions; for example,
            `(('partInstance1',(1,'7','3:15;3'),), ('partInstance2','8'),))`. The node expressions
            can be any of the following:An Int specifying a single node label; for example, `1`.A
            String specifying a single node label; for example, `'7'`.A String specifying a sequence
            of node labels; for example, `'3:5'` and `'3:15:3'`.

        Returns
        -------
        LeafFromModelNodeLabels
            A LeafFromModelNodeLabels object.
        """
        super().__init__(DEFAULT_MODEL)
