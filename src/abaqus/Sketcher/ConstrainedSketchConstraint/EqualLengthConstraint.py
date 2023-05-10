from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..ConstrainedSketchGeometry.ConstrainedSketchGeometry import (
    ConstrainedSketchGeometry,
)
from .ConstrainedSketchConstraint import ConstrainedSketchConstraint


@abaqus_class_doc
class EqualLengthConstraint(ConstrainedSketchConstraint):
    @abaqus_method_doc
    def __init__(self, entity1: ConstrainedSketchGeometry, entity2: ConstrainedSketchGeometry):
        """This method creates an equal length constraint. This constraint applies to lines and constrains them
        such that their lengths are equal.

        .. note::
            This function can be accessed by::

                mdb.models[name].sketches[name].EqualLengthConstraint

        Parameters
        ----------
        entity1
            A ConstrainedSketchGeometry object specifying the first line.
        entity2
            A ConstrainedSketchGeometry object specifying the second line.

        Returns
        -------
        ConstrainedSketchConstraint
            A ConstrainedSketchConstraint object.
        """
        ...
