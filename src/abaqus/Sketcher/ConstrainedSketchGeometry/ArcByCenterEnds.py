from typing import Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from typing_extensions import Literal

from .ConstrainedSketchGeometry import ConstrainedSketchGeometry
<<<<<<< HEAD
=======
from ...UtilityAndView.abaqusConstants import abaqusConstants as C
>>>>>>> 9cc45e87 ([typing]: Including remaining `Literal` in all modules (#3004))


@abaqus_class_doc
class ArcByCenterEnds(ConstrainedSketchGeometry):
    @abaqus_method_doc
    def __init__(
        center: Sequence[float],
        point1: Sequence[float],
        point2: Sequence[float],
<<<<<<< HEAD
=======
        direction: Literal[C.COUNTERCLOCKWISE, C.CLOCKWISE],
>>>>>>> 9cc45e87 ([typing]: Including remaining `Literal` in all modules (#3004))
    ):
        """This method constructs an arc using a center point and two vertices. The Arc object is
        added to the geometry repository of the ConstrainedSketch object. The arc is created in
        a clockwise fashion from **point1** to **point2**.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].ArcByCenterEnds

        Parameters
        ----------
        center
            A pair of Floats specifying the center point of the arc.
        point1
            A pair of Floats specifying the first endpoint of the arc.
        point2
            A pair of Floats specifying the second endpoint of the arc.

        Returns
        -------
        ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object (None if the arc cannot be created).

        Raises
        ------
        If incompatible data are given, the second endpoint is ignored.

        """
        ...
