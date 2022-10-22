from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ConstrainedSketchConstraint import ConstrainedSketchConstraint
from ..ConstrainedSketchGeometry.ConstrainedSketchGeometry import (
    ConstrainedSketchGeometry,
)


@abaqus_class_doc
class VerticalConstraint(ConstrainedSketchConstraint):
    @abaqus_method_doc
    def __init__(self, entity: ConstrainedSketchGeometry):
        """This method creates a vertical constraint. This constraint applies to a line and
        constrains it to be vertical.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].VerticalConstraint

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
