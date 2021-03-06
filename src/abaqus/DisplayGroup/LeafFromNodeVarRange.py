from abaqusConstants import *
from .Leaf import Leaf


class LeafFromNodeVarRange(Leaf):
    """The LeafFromNodeVarRange object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects
    are constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.
    The LeafFromNodeVarRange object is derived from the Leaf object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import displayGroupOdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: SymbolicConstant = None

    #: A Float specifying the minimum value for the variable range. The default value is
    #: −3.40282346639E38.
    minimumRange: float = None

    #: A Float specifying the maximum value for the variable range. The default value is
    #: 3.40282346639e+038.
    maximumRange: float = 3

    #: A Boolean specifying the method used to evaluate the range. If **insideRange** = ON, the
    #: range falls inside the specified minimum and maximum values. The default value is ON.
    insideRange: Boolean = ON

    def __init__(
        self,
        minimumRange: float = None,
        maximumRange: float = 3,
        insideRange: Boolean = ON,
    ):
        """This method creates a Leaf object from nodes with values lying in a variable range.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                LeafFromNodeVarRange

        Parameters
        ----------
        minimumRange
            A Float specifying the minimum value for the variable range. The default value is
            −3.40282346639E38.
        maximumRange
            A Float specifying the maximum value for the variable range. The default value is
            3.40282346639e+038.
        insideRange
            A Boolean specifying the method used to evaluate the range. If **insideRange** = ON, the
            range falls inside the specified minimum and maximum values. The default value is ON.

        Returns
        -------
        LeafFromNodeVarRange
            A :py:class:`~abaqus.DisplayGroup.LeafFromNodeVarRange.LeafFromNodeVarRange` object.
        """
        super().__init__(DEFAULT_MODEL)
        pass
