from typing import Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ConstrainedSketchVertex import ConstrainedSketchVertex


@abaqus_class_doc
class Spot(ConstrainedSketchVertex):
    @abaqus_method_doc
    def __init__(self, point: Sequence[float]):
        """This method creates a spot (construction point) located at the specified coordinates.

        .. note:: 
            This function can be accessed by::

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
        ...
