from abaqusConstants import *
from .ConstrainedSketchGeometry import ConstrainedSketchGeometry


class getPointAtDistance(ConstrainedSketchGeometry):
    
    def __init__(self, point: tuple[float, ...], distance: str, percentage: Boolean = OFF):
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
        tuple[float, ...]
            A pair of floats representing the point along the edge.

        """
        pass
