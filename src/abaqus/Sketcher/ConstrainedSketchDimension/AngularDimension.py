from abaqusConstants import *
from .ConstrainedSketchDimension import ConstrainedSketchDimension
from ..ConstrainedSketchGeometry.ConstrainedSketchGeometry import (
    ConstrainedSketchGeometry,
)


class AngularDimension(ConstrainedSketchDimension):
    def __init__(
        self,
        line1: ConstrainedSketchGeometry,
        line2: ConstrainedSketchGeometry,
        textPoint: tuple[float],
        value: float = None,
        reference: Boolean = OFF,
    ):
        """This method constructs a ConstrainedSketchDimension object between two
        ConstrainedSketchGeometry objects, with the given angle between them.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].sketches[name].AngularDimension

        Parameters
        ----------
        line1
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object specifying the first line.
        line2
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object specifying the second line.
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
        pass
