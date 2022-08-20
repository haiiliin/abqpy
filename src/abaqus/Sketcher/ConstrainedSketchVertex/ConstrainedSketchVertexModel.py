import typing

from ..ConstrainedSketchBase import ConstrainedSketchBase
from ..._decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class ConstrainedSketchVertexModel(ConstrainedSketchBase):
    """A :py:class:`~abaqus.Sketcher.ConstrainedSketch.ConstrainedSketch` object contains the entities that are used to create a sketch. The
    objects include ConstrainedSketchGeometry objects contained in the ConstrainedSketchGeometry Repository,
    such as Line, Arc, and Spline. ConstrainedSketchVertex, ConstrainedSketchDimension, ConstrainedSketchConstraint, and ConstrainedSketchParameter objects are
    contained in their respective repositories.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import sketch
            mdb.models[name].sketches[name]
    """

    @abaqus_method_doc
    def Spot(self, point: typing.Tuple[float, ...]):
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
        vertex: ConstrainedSketchVertex
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertex.ConstrainedSketchVertex` object (None if the spot cannot be created)
        """
        ...
