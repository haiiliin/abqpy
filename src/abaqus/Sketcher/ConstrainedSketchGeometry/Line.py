from .ConstrainedSketchGeometry import ConstrainedSketchGeometry


class Line(ConstrainedSketchGeometry):
    def __init__(self, point1: tuple[float, ...], point2: tuple[float, ...]):
        """This method creates a line between two given points.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].sketches[name].Line

        Parameters
        ----------
        point1
            A pair of Floats specifying the first endpoint.
        point2
            A pair of Floats specifying the second endpoint.

        Returns
        -------
        ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object (None if the line cannot be created).

        """
        pass
