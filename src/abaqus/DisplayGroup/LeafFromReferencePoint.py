from abaqusConstants import *
from .Leaf import Leaf


class LeafFromReferencePoint(Leaf):
    """The LeafFromReferencePoint object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects
    are constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.
    The LeafFromReferencePoint object is derived from the Leaf object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import displayGroupMdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: SymbolicConstant = None

    def __init__(self, refPtSeq: tuple):
        """This method creates a Leaf object from a sequence of ReferencePoint objects.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                LeafFromReferencePoint

        Parameters
        ----------
        refPtSeq
            A sequence of Reference Point objects.

        Returns
        -------
        LeafFromReferencePoint
            A :py:class:`~abaqus.DisplayGroup.LeafFromReferencePoint.LeafFromReferencePoint` object.
        """
        super().__init__(DEFAULT_MODEL)
        pass
