from typing_extensions import Literal

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..UtilityAndView.abaqusConstants import SymbolicConstant
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class Leaf:
    """Leaf objects are used to specify the items in a display group. Leaf objects are constructed as temporary
    objects, which are then used as arguments to DisplayGroup commands. Leaf objects have similarities to Set
    objects; however, Leaf objects are evaluated when the DisplayGroup expression is evaluated, and they can
    have SymbolicConstant values (which are also evaluated when the DisplayGroup expression is evaluated).

    .. note::
        This object can be accessed by::

            import displayGroupMdbToolset
            import displayGroupOdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: SymbolicConstant

    @abaqus_method_doc
    def __init__(self, leafType: Literal[C.ALL_ELEMENTS, C.ALL_SURFACES, C.EMPTY_LEAF, C.DEFAULT_MODEL, C.ALL_NODES]):
        """This method creates a Leaf object.

        .. note::
            This function can be accessed by::

                Leaf

        Parameters
        ----------
        leafType
            A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
            DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.

        Returns
        -------
        Leaf
            A Leaf object.
        """
        ...
