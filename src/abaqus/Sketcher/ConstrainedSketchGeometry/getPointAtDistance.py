from typing import Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ConstrainedSketchGeometry import ConstrainedSketchGeometry
from ...UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class getPointAtDistance(ConstrainedSketchGeometry):
    @abaqus_method_doc
    def __init__(self, point: Sequence[float], distance: str, percentage: Boolean = OFF):
        """This method returns a point offset along the given ConstrainedSketchGeometry from the
        given end by a specified arc length distance or a percentage of the total length of the
        ConstrainedSketchGeometry object.

        Parameters
        ----------
        point
            A pair of Floats specifying the point from which the distance is to be measured.
        distance
            A float specifying the arc length distance along the ConstrainedSketchGeometry from the
            **point** at which the required point is situated.
        percentage
            A Boolean that specifies if the **distance** is an absolute distance or is a fraction
            relative to the length of the ConstrainedSketchGeometry object.

        Returns
        -------
        Sequence[float]
            A pair of floats representing the point along the edge.

        """
        ...
