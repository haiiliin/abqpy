import typing

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ConstrainedSketchDimension import ConstrainedSketchDimension
from ..ConstrainedSketchVertex.ConstrainedSketchVertex import ConstrainedSketchVertex
from ...UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class VerticalDimension(ConstrainedSketchDimension):
    @abaqus_method_doc
    def __init__(
        self,
        vertex1: ConstrainedSketchVertex,
        vertex2: ConstrainedSketchVertex,
        textPoint: typing.Tuple[float, ...],
        value: typing.Optional[float] = None,
        reference: Boolean = OFF,
    ):
        """This method constructs a ConstrainedSketchDimension between two vertices. A vertical
        dimension controls the vertical distance along the **Y**-axis between two vertices.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].VerticalDimension

        Parameters
        ----------
        vertex1
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertex.ConstrainedSketchVertex` object specifying the first endpoint.
        vertex2
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertex.ConstrainedSketchVertex` object specifying the second endpoint.
        textPoint
            A pair of Floats specifying the location of the dimension text.
        value
            A Float specifying the angle between the two lines.
        reference
            A Boolean specifying whether the created dimension enforces the above value or if it
            simply measures the angle between two lines.

        Returns
        -------
        ConstrainedSketchDimension
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimension.ConstrainedSketchDimension` object (None if the dimension cannot be created).

        """
        ...
