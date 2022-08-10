from abaqusConstants import *
from .Leaf import Leaf


class LeafFromPartInstance(Leaf):
    """The LeafFromPartInstance object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects
    are constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.
    The LeafFromPartInstance object is derived from the Leaf object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import displayGroupOdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: SymbolicConstant = None

    #: A sequence of Strings specifying the names of the part instances.
    partInstanceName: tuple

    def __init__(self, partInstanceName: tuple):
        """This method creates a Leaf object from a list of part instance names.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                LeafFromPartInstance

        Parameters
        ----------
        partInstanceName
            A sequence of Strings specifying the names of the part instances.

        Returns
        -------
        LeafFromPartInstance
            A :py:class:`~abaqus.DisplayGroup.LeafFromPartInstance.LeafFromPartInstance` object.
        """
        super().__init__(DEFAULT_MODEL)
        ...
