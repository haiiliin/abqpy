from typing import Optional
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Leaf import Leaf
from ..Part.Part import Part
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class LeafFromPartNodeLabels(Leaf):
    """The LeafFromPartNodeLabels object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects
    are constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.
    The LeafFromPartNodeLabels object is derived from the Leaf object.

    .. note:: 
        This object can be accessed by::

            import displayGroupMdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: Optional[SymbolicConstant] = None

    @abaqus_method_doc
    def __init__(self, part: Part, nodeLabels: tuple):
        """This method creates a Leaf object from a sequence of Strings specifying node labels.
        Leaf objects specify the items in a display group.

        .. note:: 
            This function can be accessed by::

                LeafFromPartNodeLabels

        Parameters
        ----------
        part
            A :py:class:`~abaqus.Part.Part.Part` object.
        nodeLabels
            A sequence of Strings specifying node labels.

        Returns
        -------
        LeafFromPartNodeLabels
            A :py:class:`~abaqus.DisplayGroup.LeafFromPartNodeLabels.LeafFromPartNodeLabels` object.
        """
        super().__init__(DEFAULT_MODEL)
