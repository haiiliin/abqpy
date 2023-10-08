from __future__ import annotations

from typing import List

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from ...UtilityAndView.abaqusConstants import Boolean
from .ConstrainedSketchVertex import ConstrainedSketchVertex


@abaqus_class_doc
class ConstrainedSketchVertexArray(List[ConstrainedSketchVertex]):
    """The ConstrainedSketchVertexArray is a sequence of ConstrainedSketchVertex objects.

    .. note::
        This object can be accessed by::

            import sketch
            mdb.models[name].sketches[name].vertices[i]
    """

    def findAt(self, coordinates: tuple[float, float], printWarning: Boolean = True) -> ConstrainedSketchVertex:
        """This method returns the ConstrainedSketchVertex located at the given coordinates.

        Parameters
        ----------
        coordinates
            A sequence of Floats specifying the **X**  and **Y** coordinates of the object to find.
        printWarning
            A Boolean specifying whether a message is to be printed to the CLI if no entity is found
            at the specified location. The default value is True.

        Returns
        -------
        ConstrainedSketchVertex
            A ConstrainedSketchVertex object.
        """
        return ConstrainedSketchVertex()
