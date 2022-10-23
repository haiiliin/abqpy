from typing import Optional, Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class ConstrainedSketchVertex:
    """The ConstrainedSketchVertex object stores the vertex position.

    .. note::
        This object can be accessed by::

            import sketch
            mdb.models[name].sketches[name].vertices[i]
            mdb.models[name].sketches[name].vertices[i][i]
    """

    #: A tuple of Floats specifying the*X*-, **Y**-, and **Z**-coordinates of the sketch vertex.
    coords: Optional[float] = None

    @abaqus_method_doc
    def Spot(self, point: Sequence[float]):
        """This method creates a spot (construction point) located at the specified coordinates.

        .. note::
            This function can be accessed by::

                mdb.models[name].sketches[name].Spot

        Parameters
        ----------
        point
            A pair of Floats specifying the coordinates of the construction point.

        Returns
        -------
        ConstrainedSketchVertex
            A :py:class:`~abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertex.ConstrainedSketchVertex` object (None if the spot cannot be created).
        """
        ...
