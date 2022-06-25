from .ConstrainedSketchConstraint import ConstrainedSketchConstraint
from ..ConstrainedSketchGeometry.ConstrainedSketchGeometry import (
    ConstrainedSketchGeometry,
)


class ParallelConstraint(ConstrainedSketchConstraint):
    def __init__(
        self, entity1: ConstrainedSketchGeometry, entity2: ConstrainedSketchGeometry
    ):
        """This method creates a parallel constraint. This constraint applies to lines and
        constrains them to be parallel.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].sketches[name].ParallelConstraint

        Parameters
        ----------
        entity1
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object specifying the first line.
        entity2
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object specifying the second line.

        Returns
        -------
        ConstrainedSketchConstraint
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint` object.

        """
        pass
