from typing import Union, List, Tuple

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc
from .ConstrainedSketchGeometry import ConstrainedSketchGeometry
from ...UtilityAndView.abaqusConstants import Boolean


@abaqus_class_doc
class ConstrainedSketchGeometryArray(List[ConstrainedSketchGeometry]):
    """The ConstrainedSketchGeometryArray is a sequence of ConstrainedSketchGeometry objects.

    .. note:: 
        This object can be accessed by::

            import sketch
            mdb.models[name].sketches[name].geometry[i]
    """

    @abaqus_method_doc
    def findAt(self, coordinates: Tuple[float, float], printWarning: Boolean = True) -> ConstrainedSketchGeometry:
        """This method returns the ConstrainedSketchGeometry object located at the given
        coordinates.

        Parameters
        ----------
        coordinates
            A sequence of Floats specifying the **X**- and **Y**-coordinates of the object to find.
        printWarning
            A Boolean specifying whether a message is to be printed to the CLI if no entity is found
            at the specified location. The default value is True.

        Returns
        -------
        ConstrainedSketchGeometry
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry` object.
        """
        return ConstrainedSketchGeometry()
