from .ConstrainedSketchGeometry import ConstrainedSketchGeometry


class Spot(ConstrainedSketchGeometry):
    def __init__(self, point: tuple[float, ...]):
        """This method creates a spot construction point located at the specified coordinates. The
        spot is added to the vertex repository of the ConstrainedSketch object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].sketches[name].Spot

        Parameters
        ----------
        point
            A pair of Floats specifying the coordinates of the spot construction point.

        Returns
        -------
        ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object (None if the spot cannot be created).

        """
        pass
