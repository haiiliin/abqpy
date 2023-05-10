from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import DEFAULT_MODEL, SymbolicConstant
from .Leaf import Leaf


@abaqus_class_doc
class LeafFromGeometry(Leaf):
    """The LeafFromGeometry object can be used whenever a Leaf object is expected as an argument. Leaf objects
    are used to specify the items in a display group. Leaf objects are constructed as temporary objects, which
    are then used as arguments to DisplayGroup commands. The LeafFromGeometry object is derived from the Leaf
    object.

    .. note::
        This object can be accessed by::

            import displayGroupMdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: Optional[SymbolicConstant] = None

    @abaqus_method_doc
    def __init__(self, edgeSeq: tuple = (), faceSeq: tuple = (), cellSeq: tuple = ()):
        """This method creates a Leaf object from a sequence of edge, face and cell geometry objects. Any
        combination of edge, face or cell arguments is allowed however the arguments must specify at least one
        object--it is not permissible to create an empty leaf.

        .. note::
            This function can be accessed by::

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
            A LeafFromGeometry object.

        Raises
        ------
        Cannot define empty leaf
            If at least one of the sequences is not passed to this method.
        """
        super().__init__(DEFAULT_MODEL)
