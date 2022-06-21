from .ConstrainedSketchVertex import ConstrainedSketchVertex


class Spot(ConstrainedSketchVertex):
    def __init__(self, point: tuple[float]):
        """This method creates a spot (construction point) located at the specified coordinates.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].sketches[name].Spot

        Parameters
        ----------
        point
            A pair of Floats specifying the coordinates of the construction point.

        Returns
        -------
        A ConstrainedSketchVertex object (None if the spot cannot be created).
        """
        pass
