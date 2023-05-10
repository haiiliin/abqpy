from typing import Optional, Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ...UtilityAndView.abaqusConstants import OFF, Boolean
from ..ConstrainedSketchVertex.ConstrainedSketchVertex import ConstrainedSketchVertex
from .ConstrainedSketchDimension import ConstrainedSketchDimension


@abaqus_class_doc
class ObliqueDimension(ConstrainedSketchDimension):
    @abaqus_method_doc
    def __init__(
        self,
        vertex1: ConstrainedSketchVertex,
        vertex2: ConstrainedSketchVertex,
        textPoint: Sequence[float],
        value: Optional[float] = None,
        reference: Boolean = OFF,
    ):
        """This method constructs a ConstrainedSketchDimension object between two vertices. An oblique dimension
        indicates the distance between two vertices.

        .. note::
            This function can be accessed by::

                mdb.models[name].sketches[name].ObliqueDimension

        Parameters
        ----------
        vertex1
            A ConstrainedSketchVertex object specifying the first endpoint.
        vertex2
            A ConstrainedSketchVertex object specifying the second endpoint.
        textPoint
            A pair of Floats specifying the location of the dimension text.
        value
            A Float specifying the distance between the two ConstrainedSketchVertex objects.
        reference
            A Boolean specifying whether the created dimension enforces the above value or if it
            simply measures the distance between the two vertices.

        Returns
        -------
        ConstrainedSketchDimension
            A ConstrainedSketchDimension object (None if the dimension cannot be created).
        """
        ...
