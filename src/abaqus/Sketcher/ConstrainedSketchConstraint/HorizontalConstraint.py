from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ConstrainedSketchConstraint import ConstrainedSketchConstraint
from ..ConstrainedSketchGeometry.ConstrainedSketchGeometry import (
    ConstrainedSketchGeometry,
)


@abaqus_class_doc
class HorizontalConstraint(ConstrainedSketchConstraint):
    @abaqus_method_doc
    def __init__(self, entity: ConstrainedSketchGeometry):
        """This method creates a horizontal constraint. This constraint applies to a line and
        constrains it to be horizontal.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].HorizontalConstraint

        Parameters
        ----------
        entity
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object specifying the line to constrain.

        Returns
        -------
        ConstrainedSketchConstraint
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint` object.

        """
        ...
