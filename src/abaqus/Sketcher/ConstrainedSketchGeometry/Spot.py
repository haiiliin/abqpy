from typing import Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ConstrainedSketchGeometry import ConstrainedSketchGeometry


@abaqus_class_doc
class Spot(ConstrainedSketchGeometry):
    @abaqus_method_doc
    def __init__(self, point: Sequence[float]):
        """This method creates a spot construction point located at the specified coordinates. The
        spot is added to the vertex repository of the ConstrainedSketch object.

        .. note:: 
            This function can be accessed by::

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
        ...
