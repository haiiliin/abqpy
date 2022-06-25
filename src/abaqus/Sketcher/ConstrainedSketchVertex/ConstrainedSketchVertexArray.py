from abaqusConstants import *


class ConstrainedSketchVertexArray:
    """The ConstrainedSketchVertexArray is a sequence of ConstrainedSketchVertex objects.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import sketch
            mdb.models[name].sketches[name].vertices[i]
    """

    def findAt(self, coordinates: tuple, printWarning: Boolean = True):
        """This method returns the ConstrainedSketchVertex located at the given coordinates.

        Parameters
        ----------
        coordinates
            A sequence of Floats specifying the **X**- and **Y**-coordinates of the object to find.
        printWarning
            A Boolean specifying whether a message is to be printed to the CLI if no entity is found
            at the specified location. The default value is True.

        Returns
        -------
        ConstrainedSketchVertex
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertex.ConstrainedSketchVertex` object.
        """
        pass
