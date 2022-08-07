from .ConstrainedSketchVertex import ConstrainedSketchVertex


class Spot(ConstrainedSketchVertex):
    def __init__(self, point: tuple[float, ...]):
        """This method creates a spot (construction point) located at the specified coordinates.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].sketches[name].Spot

        Parameters
        ----------
        point
            A pair of Floats specifying the coordinates of the construction point.

        Returns
        -------
        ConstrainedSketchVertex
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertex.ConstrainedSketchVertex` object (None if the spot cannot be created).
        """
        pass
