from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..ConstrainedSketchGeometry.ConstrainedSketchGeometry import (
    ConstrainedSketchGeometry,
)
from .ConstrainedSketchConstraint import ConstrainedSketchConstraint


@abaqus_class_doc
class CoincidentConstraint(ConstrainedSketchConstraint):
    @abaqus_method_doc
    def __init__(self, entity1: ConstrainedSketchGeometry, entity2: ConstrainedSketchGeometry):
        """This method creates a coincident constraint. This constraint applies to two vertices, to a vertex and
        a ConstrainedSketchGeometry object, or to two ConstrainedSketchGeometry objects of the same type and
        constrains them to be coincident.

        .. note::
            This function can be accessed by::

                mdb.models[name].sketches[name].CoincidentConstraint

        Parameters
        ----------
        entity1
            A ConstrainedSketchGeometry object or a ConstrainedSketchVertex object specifying the first object.
        entity2
            A ConstrainedSketchGeometry object or a ConstrainedSketchVertex object specifying the second object.

        Returns
        -------
        ConstrainedSketchConstraint
            A ConstrainedSketchConstraint object.
        """
        ...
