from __future__ import annotations

from abqpy.decorators import abaqus_class_doc

from ..UtilityAndView.abaqusConstants import DEFAULT_MODEL, SymbolicConstant
from .DisplayGroupArray import DisplayGroupArray
from .Leaf import Leaf


@abaqus_class_doc
class LeafFromDisplayGroup(Leaf):
    """The LeafFromDisplayGroup object can be used whenever a Leaf object is expected as an argument. Leaf
    objects are used to specify the items in a display group. Leaf objects are constructed as temporary objects,
    which are then used as arguments to DisplayGroup commands.The LeafFromDisplayGroup object is derived from
    the Leaf object.

    .. note::
        This object can be accessed by::

            import displayGroupMdbToolset
            import displayGroupOdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: SymbolicConstant

    #: A DisplayGroupArray object.
    displayGroup: DisplayGroupArray

    def __init__(self, displayGroup: DisplayGroupArray):
        """This method creates a Leaf object from a sequence of Display Group objects.

        .. note::
            This function can be accessed by::

                LeafFromDisplayGroup

        Parameters
        ----------
        displayGroup
            A DisplayGroupArray object.

        Returns
        -------
        LeafFromDisplayGroup
            A LeafFromDisplayGroup object.
        """
        super().__init__(DEFAULT_MODEL)
