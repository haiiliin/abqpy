from abaqusConstants import *
from .Leaf import Leaf


class LeafFromGeometry(Leaf):
    """The LeafFromGeometry object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects
    are constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.
    The LeafFromGeometry object is derived from the Leaf object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import displayGroupMdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: SymbolicConstant = None

    def __init__(self, edgeSeq: tuple = (), faceSeq: tuple = (), cellSeq: tuple = ()):
        """This method creates a Leaf object from a sequence of edge, face and cell geometry
        objects. Any combination of edge, face or cell arguments is allowed however the
        arguments must specify at least one object--it is not permissible to create an empty
        leaf.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                LeafFromGeometry

        Parameters
        ----------
        edgeSeq
            A sequence of geometry edges.
        faceSeq
            A sequence of geometry faces.
        cellSeq
            A sequence of geometry cells.

        Returns
        -------
        LeafFromGeometry
            A :py:class:`~abaqus.DisplayGroup.LeafFromGeometry.LeafFromGeometry` object.

        Raises
        ------
        Cannot define empty leaf
            If at least one of the sequences is not passed to this method.
        """
        super().__init__(DEFAULT_MODEL)
        pass
