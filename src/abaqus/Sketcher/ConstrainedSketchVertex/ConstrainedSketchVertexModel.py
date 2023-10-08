from __future__ import annotations

from typing import Sequence

from abqpy.decorators import abaqus_class_doc

from ..ConstrainedSketchBase import ConstrainedSketchBase
from .ConstrainedSketchVertex import ConstrainedSketchVertex


@abaqus_class_doc
class ConstrainedSketchVertexModel(ConstrainedSketchBase):
    """A ConstrainedSketch object contains the entities that are used to create a sketch. The objects include
    ConstrainedSketchGeometry objects contained in the ConstrainedSketchGeometry Repository, such as Line, Arc,
    and Spline. ConstrainedSketchVertex, ConstrainedSketchDimension, ConstrainedSketchConstraint, and
    ConstrainedSketchParameter objects are contained in their respective repositories.

    .. note::
        This object can be accessed by::

            import sketch
            mdb.models[name].sketches[name]
    """

    def Spot(self, point: Sequence[float]) -> ConstrainedSketchVertex:
        """This method creates a spot (construction point) located at the specified coordinates.

        .. note::
            This function can be accessed by::

                mdb.models[name].sketches[name].Spot

        Parameters
        ----------
        point
            A pair of Floats specifying the coordinates of the construction point.

        Returns
        -------
        vertex: ConstrainedSketchVertex
            A ConstrainedSketchVertex object (None if the spot cannot be created)
        """
        return ConstrainedSketchVertex()
