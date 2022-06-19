from abaqusConstants import *


class Leaf:
    """Leaf objects are used to specify the items in a display group. Leaf objects are
    constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.
    Leaf objects have similarities to Set objects; however, Leaf objects are evaluated when
    the DisplayGroup expression is evaluated, and they can have SymbolicConstant values
    (which are also evaluated when the DisplayGroup expression is evaluated).

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import displayGroupMdbToolset
        import displayGroupOdbToolset
    """

    def __init__(self, leafType: SymbolicConstant):
        """This method creates a Leaf object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            Leaf

        Parameters
        ----------
        leafType
            A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
            DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.

        Returns
        -------
            A Leaf object.
        """
        pass
