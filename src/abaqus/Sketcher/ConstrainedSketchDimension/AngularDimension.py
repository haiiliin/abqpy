from typing import Optional, Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ConstrainedSketchDimension import ConstrainedSketchDimension
from ..ConstrainedSketchGeometry.ConstrainedSketchGeometry import (
    ConstrainedSketchGeometry,
)
from ...UtilityAndView.abaqusConstants import Boolean, OFF


@abaqus_class_doc
class AngularDimension(ConstrainedSketchDimension):
    @abaqus_method_doc
    def __init__(
        self,
        line1: ConstrainedSketchGeometry,
        line2: ConstrainedSketchGeometry,
        textPoint: Sequence[float],
        value: Optional[float] = None,
        reference: Boolean = OFF,
    ):
        """This method constructs a ConstrainedSketchDimension object between two
        ConstrainedSketchGeometry objects, with the given angle between them.

        .. note::
            This function can be accessed by::

                mdb.models[name].sketches[name].AngularDimension

        Parameters
        ----------
        line1
            A ConstrainedSketchGeometry object specifying the first line.
        line2
            A ConstrainedSketchGeometry object specifying the second line.
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
