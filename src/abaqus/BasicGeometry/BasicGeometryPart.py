from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .Edge import Edge
from .InterestingPoint import InterestingPoint
from ..Part.PartBase import PartBase
from ..UtilityAndView.abaqusConstants import abaqusConstants as C


@abaqus_class_doc
class BasicGeometryPart(PartBase):

    @abaqus_method_doc
    def InterestingPoint(
        self, edge: Edge, rule: Literal[C.MIDDLE, C.CENTER]
    ) -> InterestingPoint:
        """This method creates an interesting point along an edge. An InterestingPoint is a
        temporary object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].parts[name].InterestingPoint
                mdb.models[name].rootAssembly.instances[name].InterestingPoint

        Parameters
        ----------
        edge
            An :py:class:`~abaqus.BasicGeometry.Edge.Edge` object specifying the edge on which the interesting point is positioned.
        rule
            A SymbolicConstant specifying the position of the interesting point. Possible values are
            MIDDLE or CENTER.

        Returns
        -------
        InterestingPoint
            An :py:class:`~abaqus.BasicGeometry.InterestingPoint.InterestingPoint` object.

        """
        ...
        return InterestingPoint(edge, rule)
