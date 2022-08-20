import typing

from .ConstrainedSketchVertex import ConstrainedSketchVertex
from ..._decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class Spot(ConstrainedSketchVertex):
    @abaqus_method_doc
    def __init__(self, point: typing.Tuple[float, ...]):
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
        ...
