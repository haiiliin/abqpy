from __future__ import annotations

from typing import Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ...UtilityAndView.abaqusConstants import OFF, Boolean
from ..ConstrainedSketchVertex.ConstrainedSketchVertex import ConstrainedSketchVertex
from .ConstrainedSketchDimension import ConstrainedSketchDimension


@abaqus_class_doc
class DistanceDimension(ConstrainedSketchDimension):
    @abaqus_method_doc
    def __init__(
        self,
        entity1: ConstrainedSketchVertex,
        entity2: ConstrainedSketchVertex,
        textPoint: Sequence[float],
        value: float | None = None,
        reference: Boolean = OFF,
    ):
        """This method constructs a ConstrainedSketchDimension object between two ConstrainedSketchGeometry, or
        aConstrainedSketchVertex and ConstrainedSketchGeometry object. A distance dimension specifies the
        shortest distance between two entities.

        .. note::
            This function can be accessed by::

                mdb.models[name].sketches[name].DistanceDimension

        Parameters
        ----------
        entity1
            A ConstrainedSketchVertex object or ConstrainedSketchGeometry object.
        entity2
            A ConstrainedSketchVertex object or ConstrainedSketchGeometry object.

            .. versionchanged:: 2017
                The ``vertex2`` argument was renamed to ``entity2``.
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
            A ConstrainedSketchDimension object (None if the dimension cannot be created).
        """
        ...
