from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ConstrainedSketchConstraint import ConstrainedSketchConstraint
from ..ConstrainedSketchGeometry.ConstrainedSketchGeometry import (
    ConstrainedSketchGeometry,
)


@abaqus_class_doc
class PerpendicularConstraint(ConstrainedSketchConstraint):
    @abaqus_method_doc
    def __init__(self, entity1: ConstrainedSketchGeometry, entity2: ConstrainedSketchGeometry):
        """This method creates a perpendicular constraint. This constraint applies to different
        types of ConstrainedSketchGeometry objects and constrains them to be perpendicular to
        each other.

        .. note::
            This function can be accessed by::

                mdb.models[name].sketches[name].PerpendicularConstraint

        Parameters
        ----------
        entity1
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object specifying the first object.
        entity2
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object specifying the second object.

        Returns
        -------
        ConstrainedSketchConstraint
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint` object.

        """
        ...
