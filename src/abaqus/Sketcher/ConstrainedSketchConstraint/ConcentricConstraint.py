from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ..ConstrainedSketchGeometry.ConstrainedSketchGeometry import (
    ConstrainedSketchGeometry,
)
from .ConstrainedSketchConstraint import ConstrainedSketchConstraint


@abaqus_class_doc
class ConcentricConstraint(ConstrainedSketchConstraint):
    @abaqus_method_doc
    def __init__(self, entity1: ConstrainedSketchGeometry, entity2: ConstrainedSketchGeometry):
        """This method creates a concentric constraint. This constraint applies to any combination of circles,
        arcs, ellipses, and points and constrains them to be concentric. A concentric constraint implies that
        the center of ConstrainedSketchGeometry objects coincide.

        .. note::
            This function can be accessed by::

                mdb.models[name].sketches[name].ConcentricConstraint

        Parameters
        ----------
        entity1
            A ConstrainedSketchGeometry object specifying the first arc, circle, ellipse, or sketch
            vertex.
        entity2
            A ConstrainedSketchGeometry object specifying the second arc, circle, ellipse, or sketch
            vertex.

        Returns
        -------
        ConstrainedSketchConstraint
            A ConstrainedSketchConstraint object.
        """
        ...
