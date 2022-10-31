from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Edge import Edge
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class InterestingPoint:
    """Interesting points can be located at the following:

    - The middle of an edge.
    - The middle of an arc.
    - The center of an arc.

    An InterestingPoint object is a temporary object and cannot be accessed from the Mdb
    object.

    .. note::
        This object can be accessed by::

            import part
            import assembly
    """

    @abaqus_method_doc
    def __init__(self, edge: Edge, rule: Literal[C.MIDDLE, C.CENTER]):
        """This method creates an interesting point along an edge. An InterestingPoint is a
        temporary object.

        .. note::
            This function can be accessed by::

                mdb.models[name].parts[name].InterestingPoint
                mdb.models[name].rootAssembly.instances[name].InterestingPoint

        Parameters
        ----------
        edge
            An Edge object specifying the edge on which the interesting point is positioned.
        rule
            A SymbolicConstant specifying the position of the interesting point. Possible values are
            MIDDLE or CENTER.

        Returns
        -------
        InterestingPoint
            An InterestingPoint object.

        """
        ...
