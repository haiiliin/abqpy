from typing import Tuple

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ConstrainedSketchGeometry import ConstrainedSketchGeometry


@abaqus_class_doc
class CircleByCenterPerimeter(ConstrainedSketchGeometry):
    @abaqus_method_doc
    def __init__(self, center: Tuple[float, ...], point1: Tuple[float, ...]):
        """This method constructs a circle using a center point and a point on the perimeter. The
        circle is added to the geometry repository of the ConstrainedSketch object.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].CircleByCenterPerimeter

        Parameters
        ----------
        center
            A pair of Floats specifying the center point of the circle.
        point1
            A pair of Floats specifying a point on the perimeter of the circle.

        Returns
        -------
        ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object (None if the circle cannot be created).

        """
        ...
