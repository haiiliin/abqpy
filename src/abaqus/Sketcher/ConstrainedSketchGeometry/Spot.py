import typing

from .ConstrainedSketchGeometry import ConstrainedSketchGeometry
from ..._decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class Spot(ConstrainedSketchGeometry):
    @abaqus_method_doc
    def __init__(self, point: typing.Tuple[float, ...]):
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
        ...
