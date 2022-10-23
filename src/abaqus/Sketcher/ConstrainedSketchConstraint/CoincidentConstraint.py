from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ConstrainedSketchConstraint import ConstrainedSketchConstraint
from ..ConstrainedSketchGeometry.ConstrainedSketchGeometry import (
    ConstrainedSketchGeometry,
)


@abaqus_class_doc
class CoincidentConstraint(ConstrainedSketchConstraint):
    @abaqus_method_doc
    def __init__(self, entity1: ConstrainedSketchGeometry, entity2: ConstrainedSketchGeometry):
        """This method creates a coincident constraint. This constraint applies to two vertices, to
        a vertex and a ConstrainedSketchGeometry object, or to two ConstrainedSketchGeometry
        objects of the same type and constrains them to be coincident.

        .. note::
            This function can be accessed by::

                mdb.models[name].sketches[name].CoincidentConstraint

        Parameters
        ----------
        entity1
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object or a ConstrainedSketchVertex object specifying the first object.
        entity2
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object or a ConstrainedSketchVertex object specifying the second object.

        Returns
        -------
        ConstrainedSketchConstraint
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint` object.

        """
        ...
