from typing import Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ConstrainedSketchGeometry import ConstrainedSketchGeometry


@abaqus_class_doc
class ArcByStartEndTangent(ConstrainedSketchGeometry):
    @abaqus_method_doc
    def __init__(self, point1: Sequence[float], point2: Sequence[float], vector: tuple):
        """This method constructs an arc using two vertices. The Arc object is added to the
        geometry repository of the ConstrainedSketch object.

        .. note::
            This function can be accessed by::

                mdb.models[name].sketches[name].ArcByStartEndTangent

        Parameters
        ----------
        point1
            A pair of Floats specifying the first endpoint of the arc.
        point2
            A pair of Floats specifying the second endpoint of the arc.
        vector
            A sequence of two Floats specifying the start direction for constructing the arc.

        Returns
        -------
        ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object (None if the arc cannot be created).

        """
        ...
