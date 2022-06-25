class ConstrainedSketchVertex:
    """The ConstrainedSketchVertex object stores the vertex position.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import sketch
            mdb.models[name].sketches[name].vertices[i]
            mdb.models[name].sketches[name].vertices[i][i]
    """

    #: A tuple of Floats specifying the*X*-, **Y**-, and **Z**-coordinates of the sketch vertex.
    coords: float = None

    def Spot(self, point: tuple[float]):
        """This method creates a spot (construction point) located at the specified coordinates.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

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
        pass
