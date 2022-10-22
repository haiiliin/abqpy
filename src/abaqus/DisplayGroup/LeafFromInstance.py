from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Leaf import Leaf
from ..Assembly.PartInstance import PartInstance
from ..UtilityAndView.abaqusConstants import DEFAULT_MODEL, SymbolicConstant


@abaqus_class_doc
class LeafFromInstance(Leaf):
    """The LeafFromInstance object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects
    are constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.
    The LeafFromInstance object is derived from the Leaf object.

    .. note:: 
        This object can be accessed by::

            import displayGroupMdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: Optional[SymbolicConstant] = None

    @abaqus_method_doc
    def __init__(self, instances: PartInstance):
        """This method creates a Leaf object from a sequence of part instance objects.

        .. note:: 
            This function can be accessed by::

                LeafFromInstance

        Parameters
        ----------
        instances
            A :py:class:`~abaqus.Assembly.PartInstance.PartInstance` object or a Sequence of PartInstance objects.

        Returns
        -------
        LeafFromInstance
            A :py:class:`~abaqus.DisplayGroup.LeafFromInstance.LeafFromInstance` object.

        Raises
        ------
        Cannot define empty leaf
            If an invalid argument is passed to this method.
        """
        super().__init__(DEFAULT_MODEL)
