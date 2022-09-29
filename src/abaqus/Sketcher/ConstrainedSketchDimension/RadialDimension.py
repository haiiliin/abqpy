from typing import Optional, Tuple

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ConstrainedSketchDimension import ConstrainedSketchDimension
from ..ConstrainedSketchGeometry.ConstrainedSketchGeometry import (
    ConstrainedSketchGeometry,
)
from ...UtilityAndView.abaqusConstants import *


@abaqus_class_doc
class RadialDimension(ConstrainedSketchDimension):
    @abaqus_method_doc
    def __init__(
        self,
        curve: ConstrainedSketchGeometry,
        textPoint: Tuple[float, ...],
        value: Optional[float] = None,
        reference: Boolean = OFF,
        majorRadius: Optional[float] = None,
        minorRadius: Optional[float] = None,
    ):
        """This method constructs a ConstrainedSketchDimension object on a circular or elliptical
        arc. A radial dimension indicates the radius of an arc or circle or the major or minor
        radius of an ellipse.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].RadialDimension

        Parameters
        ----------
        curve
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object specifying the circular or elliptical arc.
        textPoint
            A pair of Floats specifying the location of the dimension text.
        value
            A Float specifying the radius of the arc, circle or ellipse.
        reference
            A Boolean specifying whether the created dimension enforces the above value or if it
            simply measures the angle between two lines.
        majorRadius
            A Float specifying the major Radius if **curve** is an ellipse. This is mutually exclusive
            with **value** and **minorRadius**.
        minorRadius
            A Float specifying the minor Radius if **curve** is an ellipse. This is mutually exclusive
            with **value** and **majorRadius**.

        Returns
        -------
        ConstrainedSketchDimension
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimension.ConstrainedSketchDimension` object (None if the dimension cannot be created).

        """
        ...
