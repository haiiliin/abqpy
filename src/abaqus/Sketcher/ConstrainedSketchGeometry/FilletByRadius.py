from typing import Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ConstrainedSketchGeometry import ConstrainedSketchGeometry


@abaqus_class_doc
class FilletByRadius(ConstrainedSketchGeometry):
    @abaqus_method_doc
    def __init__(
        self,
        radius: float,
        curve1: "ConstrainedSketchGeometry",
        nearPoint1: Sequence[float],
        curve2: "ConstrainedSketchGeometry",
        nearPoint2: Sequence[float],
    ):
        """This method constructs a fillet arc of a given radius between two curves. The fillet is
        added to the geometry repository of the ConstrainedSketch object.

        .. note::
            This function can be accessed by::

                mdb.models[name].sketches[name].FilletByRadius

        Parameters
        ----------
        radius
            A Float specifying the radius of the fillet arc. Possible values are Floats > 0.
        curve1
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object specifying the first curve.
        nearPoint1
            A pair of Floats specifying a point on the sketch near where the user wishes the fillet
            to intersect with **curve1**. This point does not need to be on*curve1*; it is used as a
            hint to draw the fillet.
        curve2
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object specifying the second curve.
        nearPoint2
            A pair of Floats specifying a point on the sketch near where the user wishes the fillet
            to intersect with **curve2**. This point does not need to be on **curve2**; it is used as a
            hint to draw the fillet.

        Returns
        -------
        ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object (None if the fillet cannot be created).

        Raises
        ------
        Range Error: cannot construct the Fillet specified
            If the radius given cannot be used to create a fillet between the two curves given.
        """
        ...
