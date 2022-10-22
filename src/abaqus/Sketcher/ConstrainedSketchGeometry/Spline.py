from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .ConstrainedSketchGeometry import ConstrainedSketchGeometry
from ...UtilityAndView.abaqusConstants import Boolean


@abaqus_class_doc
class Spline(ConstrainedSketchGeometry):
    @abaqus_method_doc
    def __init__(self, points: tuple, constrainPoints: Boolean = True):
        """This method creates a spline curve running through a sequence of points.

        .. note:: 
            This function can be accessed by::

                mdb.models[name].sketches[name].Spline

        Parameters
        ----------
        points
            A sequence of pairs of Floats specifying the points through which the spline passes.
        constrainPoints
            A Boolean that determines whether the points given are to constrained to always remain
            on the __init__. The default is True. For a large sequence of **points**, significant
            performance gains may be achieved by setting the value to False.

        Returns
        -------
        ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object (None if the spline cannot be created).

        """
        ...
