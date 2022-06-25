from .ConstrainedSketchGeometry import ConstrainedSketchGeometry


class Arc3Points(ConstrainedSketchGeometry):
    def __init__(
        self, point1: tuple[float], point2: tuple[float], point3: tuple[float]
    ):
        """This method constructs an arc using a two endpoints and an intermediate third point on
        the arc.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].sketches[name].Arc3Points

        Parameters
        ----------
        point1
            A pair of Floats specifying the first endpoint of the arc.
        point2
            A pair of Floats specifying the second endpoint of the arc.
        point3
            A pair of Floats specifying the third point on the arc.

        Returns
        -------
        ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object (None if the arc cannot be created).

        """
        pass
