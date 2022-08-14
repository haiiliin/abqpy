import typing

from abaqusConstants import *
from .ConstrainedSketchGeometry import ConstrainedSketchGeometry


class ArcByCenterEnds(ConstrainedSketchGeometry):
    def __init__(
        self,
        center: typing.Tuple[float, ...],
        point1: typing.Tuple[float, ...],
        point2: typing.Tuple[float, ...],
        direction: SymbolicConstant,
    ):
        """This method constructs an arc using a center point and two vertices. The Arc object is
        added to the geometry repository of the ConstrainedSketch object. The arc is created in
        a clockwise fashion from **point1** to **point2**.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].sketches[name].ArcByCenterEnds

        Parameters
        ----------
        center
            A pair of Floats specifying the center point of the arc.
        point1
            A pair of Floats specifying the first endpoint of the arc.
        point2
            A pair of Floats specifying the second endpoint of the arc.
        direction
            A SymbolicConstant specifying the direction of the arc. Possible values are CLOCKWISE
            and COUNTERCLOCKWISE.

        Returns
        -------
        ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object (None if the arc cannot be created).

        Raises
        ------
        If incompatible data are given, the second endpoint is ignored.

        """
        ...
