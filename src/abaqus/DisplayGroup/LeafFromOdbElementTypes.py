from __future__ import annotations

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import DEFAULT_MODEL, SymbolicConstant
from .Leaf import Leaf


@abaqus_class_doc
class LeafFromOdbElementTypes(Leaf):
    """The LeafFromOdbElementTypes object can be used whenever a Leaf object is expected as an argument. Leaf
    objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects,
    which are then used as arguments to DisplayGroup commands. The LeafFromOdbElementTypes object is derived
    from the Leaf object.

    .. note::
        This object can be accessed by::

            import displayGroupOdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: SymbolicConstant

    @abaqus_method_doc
    def __init__(self, elementTypes: tuple):
        """This method creates a Leaf object from a sequence of Strings specifying element names. Leaf objects
        specify the items in a display group.

        .. note::
            This function can be accessed by::

                LeafFromOdbElementTypes

        Parameters
        ----------
        elementTypes
            A sequence of Strings specifying element Types.

        Returns
        -------
        LeafFromOdbElementTypes
            A LeafFromOdbElementTypes object.
        """
        super().__init__(DEFAULT_MODEL)
