from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ConstrainedSketchConstraint import ConstrainedSketchConstraint
from ..ConstrainedSketchGeometry.ConstrainedSketchGeometry import (
    ConstrainedSketchGeometry,
)
from ...BasicGeometry.Vertex import Vertex


@abaqus_class_doc
class EqualDistanceConstraint(ConstrainedSketchConstraint):
    @abaqus_method_doc
    def __init__(
        self, entity1: str, entity2: ConstrainedSketchGeometry, midpoint: Vertex
    ):
        """This method creates an equal distance constraint. This constraint can be applied between
        a midpoint ConstrainedSketchVertex object and any other two ConstrainedSketchVertex objects or between a midpoint ConstrainedSketchVertex
        object and two ConstrainedSketchGeometry objects that are lines. The equal distance
        constraint forces the midpoint vertex to remain at an equal distance from the two other
        vertices or lines.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].EqualDistanceConstraint

        Parameters
        ----------
        entity1
            AConstrainedSketchGeometry object specifying the first line or ConstrainedSketchVertex object.
        entity2
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object specifying the second line or ConstrainedSketchVertex object.
        midpoint
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertex.ConstrainedSketchVertex` object specifying the vertex that will be positioned an equal distance from
            **entity1** and **entity2**.

        Returns
        -------
        ConstrainedSketchConstraint
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint` object.

        """
        ...
