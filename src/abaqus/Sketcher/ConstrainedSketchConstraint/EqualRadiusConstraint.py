from .ConstrainedSketchConstraint import ConstrainedSketchConstraint
from ..ConstrainedSketchGeometry.ConstrainedSketchGeometry import (
    ConstrainedSketchGeometry,
)


class EqualRadiusConstraint(ConstrainedSketchConstraint):
    def __init__(self, entity1: ConstrainedSketchGeometry, entity2: str):
        """This method creates an equal radius constraint. This constraint applies to circles and
        arcs and constrains them such that their radii are equal.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].sketches[name].EqualRadiusConstraint

        Parameters
        ----------
        entity1
            A ConstrainedSketchGeometry object specifying the first arc or circle.
        entity2
            A ConstrainedSketchGeometry specifying the second arc or circle.

        Returns
        -------
            A ConstrainedSketchConstraint object.

        """
        pass
