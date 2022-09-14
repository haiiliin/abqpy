from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ConstrainedSketchConstraint import ConstrainedSketchConstraint
from ..ConstrainedSketchGeometry.ConstrainedSketchGeometry import (
    ConstrainedSketchGeometry,
)


@abaqus_class_doc
class FixedConstraint(ConstrainedSketchConstraint):
    @abaqus_method_doc
    def __init__(self, entity: ConstrainedSketchGeometry):
        """This method creates a fixed constraint. This constraint applies to a
        ConstrainedSketchGeometry object or a ConstrainedSketchVertex object and constrains them to be fixed in
        space. Both the location and the shape of the sketch geometry is fixed.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].FixedConstraint

        Parameters
        ----------
        entity
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object or a ConstrainedSketchVertex object specifying the item to fix in
            space.

        Returns
        -------
        ConstrainedSketchConstraint
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint` object.

        """
        ...
