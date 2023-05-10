from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import DEFAULT_MODEL, SymbolicConstant
from .Leaf import Leaf


@abaqus_class_doc
class LeafFromElementSets(Leaf):
    """The LeafFromElementSets object can be used whenever a Leaf object is expected as an argument. Leaf
    objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects,
    which are then used as arguments to DisplayGroup commands. The LeafFromElementSets object is derived from
    the Leaf object.

    .. note::
        This object can be accessed by::

            import displayGroupOdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: Optional[SymbolicConstant] = None

    #: A sequence of Strings specifying element sets or a String specifying a single element
    #: set.
    elementSets: tuple

    @abaqus_method_doc
    def __init__(self, elementSets: tuple):
        """This method creates a Leaf object from a sequence of element sets.

        .. note::
            This function can be accessed by::

                LeafFromElementSets

        Parameters
        ----------
        elementSets
            A sequence of Strings specifying element sets or a String specifying a single element
            set.

        Returns
        -------
        LeafFromElementSets
            A LeafFromElementSets object.
        """
        super().__init__(DEFAULT_MODEL)
