from abaqusConstants import *
from .Leaf import Leaf
from ..Datum.Datum import Datum


class LeafFromDatums(Leaf):
    """The LeafFromDatums object can be used whenever a Leaf object is expected as an argument.
    Leaf objects are used to specify the items in a display group. Leaf objects are
    constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.
    The LeafFromDatums object is derived from the Leaf object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import displayGroupMdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: SymbolicConstant = None

    def __init__(self, datumSeq: tuple[Datum]):
        """This method creates a Leaf object from a sequence of datum objects. Leaf objects specify
        the items in a display group.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                LeafFromDatums

        Parameters
        ----------
        datumSeq
            A sequence of datum objects.

        Returns
        -------
        LeafFromDatums
            A :py:class:`~abaqus.DisplayGroup.LeafFromDatums.LeafFromDatums` object.
        """
        super().__init__(DEFAULT_MODEL)
        pass
