from typing import Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ConstrainedSketchGeometry import ConstrainedSketchGeometry


@abaqus_class_doc
class ConstructionLine(ConstrainedSketchGeometry):
    @abaqus_method_doc
    def __init__(self, point1: Sequence[float], point2: Sequence[float]):
        """This method creates an oblique construction line that runs between two given points.

        .. note::
            This function can be accessed by::

                mdb.models[name].sketches[name].ConstructionLine

        Parameters
        ----------
        point1
            A pair of Floats specifying the first endpoint.
        point2
            A pair of Floats specifying the second endpoint.

        Returns
        -------
        ConstrainedSketchGeometry
            A ConstrainedSketchGeometry object (None if the line cannot be created).
        """
        ...
