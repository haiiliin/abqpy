from typing import Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ConstrainedSketchGeometry import ConstrainedSketchGeometry


@abaqus_class_doc
class Arc3Points(ConstrainedSketchGeometry):
    @abaqus_method_doc
    def __init__(
        self, point1: Sequence[float], point2: Sequence[float], point3: Sequence[float]
    ):
        """This method constructs an arc using a two endpoints and an intermediate third point on
        the arc.

        .. note:: 
            This function can be accessed by::

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
        ...
