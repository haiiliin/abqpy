from typing import Tuple

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ConstrainedSketchGeometry import ConstrainedSketchGeometry


@abaqus_class_doc
class EllipseByCenterPerimeter(ConstrainedSketchGeometry):
    @abaqus_method_doc
    def __init__(
        self, center: Tuple[float, ...], axisPoint1: Tuple[float, ...], axisPoint2: Tuple[float, ...]
    ):
        """This method constructs an ellipse using a center point, a major axis point, and a minor
        axis point. The ellipse is added to the geometry repository of the ConstrainedSketch
        object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].EllipseByCenterPerimeter

        Parameters
        ----------
        center
            A pair of Floats specifying the center point of the ellipse.
        axisPoint1
            A pair of Floats specifying the major or minor axis point of the ellipse.
        axisPoint2
            A pair of Floats specifying the minor or major axis point of the ellipse.

        Returns
        -------
        ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object (None if the ellipse cannot be created).

        """
        ...
