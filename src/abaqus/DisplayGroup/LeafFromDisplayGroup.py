from abaqusConstants import *
from .DisplayGroupArray import DisplayGroupArray
from .Leaf import Leaf


class LeafFromDisplayGroup(Leaf):
    """The LeafFromDisplayGroup object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects
    are constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.The LeafFromDisplayGroup object is derived from the Leaf object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import displayGroupMdbToolset
            import displayGroupOdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: SymbolicConstant = None

    #: A :py:class:`~abaqus.DisplayGroup.DisplayGroupArray.DisplayGroupArray` object.
    displayGroup: DisplayGroupArray

    def __init__(self, displayGroup: DisplayGroupArray):
        """This method creates a Leaf object from a sequence of Display Group objects.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                LeafFromDisplayGroup

        Parameters
        ----------
        displayGroup
            A :py:class:`~abaqus.DisplayGroup.DisplayGroupArray.DisplayGroupArray` object.

        Returns
        -------
        LeafFromDisplayGroup
            A :py:class:`~abaqus.DisplayGroup.LeafFromDisplayGroup.LeafFromDisplayGroup` object.
        """
        super().__init__(DEFAULT_MODEL)
        pass
