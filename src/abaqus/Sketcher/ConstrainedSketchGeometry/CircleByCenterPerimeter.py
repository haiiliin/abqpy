from .ConstrainedSketchGeometry import ConstrainedSketchGeometry


class CircleByCenterPerimeter(ConstrainedSketchGeometry):
    def __init__(self, center: tuple[float], point1: tuple[float]):
        """This method constructs a circle using a center point and a point on the perimeter. The
        circle is added to the geometry repository of the ConstrainedSketch object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

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
        pass
