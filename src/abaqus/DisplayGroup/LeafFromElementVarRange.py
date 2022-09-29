from typing import Optional
from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .Leaf import Leaf
from ..UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class LeafFromElementVarRange(Leaf):
    """The LeafFromElementVarRange object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects
    are constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.
    The LeafFromElementVarRange object is derived from the Leaf object.

    .. note:: 
        This object can be accessed by::

            import displayGroupOdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: Optional[SymbolicConstant] = None

    #: A Float specifying the minimum value for the variable range. The default value is
    #: −3.40282346639E38.
    minimumRange: Optional[float] = None

    #: A Float specifying the maximum value for the variable range. The default value is
    #: 3.40282346639e+038.
    maximumRange: float = 3

    #: A Boolean specifying the method used to evaluate the range. If **insideRange** = ON, the
    #: range falls inside the specified minimum and maximum values. The default value is ON.
    insideRange: Boolean = ON

    @abaqus_method_doc
    def __init__(
        self,
        minimumRange: Optional[float] = None,
        maximumRange: float = 3,
        insideRange: Boolean = ON,
    ):
        """This method creates a Leaf object from elements with values lying in a variable range.

        .. note:: 
            This function can be accessed by::

                LeafFromElementVarRange

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
        LeafFromElementVarRange
            A :py:class:`~abaqus.DisplayGroup.LeafFromElementVarRange.LeafFromElementVarRange` object.
        """
        super().__init__(DEFAULT_MODEL)
