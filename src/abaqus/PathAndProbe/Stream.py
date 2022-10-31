from abqpy.decorators import abaqus_class_doc, abaqus_method_doc


@abaqus_class_doc
class Stream:
    """TheStream object defines a set of streamlines in fluid mechanics.

    .. note::
        This object can be accessed by::

            import visualization
            session.streams[name]
    """

    @abaqus_method_doc
    def __init__(
        self,
        name: str,
        numPointsOnRake: str,
        pointA: tuple = (),
        pointB: tuple = (),
        path: str = "",
    ):
        """This method creates aStream object and places it in the streams repository.

        .. note::
            This function can be accessed by::

                session.Stream

        Parameters
        ----------
        name
            A string name for the stream.
        numPointsOnRake
            An integer specifying the number of points along the rake.
        pointA
            A tuple of 3 floats specifying the starting point of the rake. Alternatively, a string
            representation of the node selected in the viewport.
        pointB
            A tuple of 3 floats specifying the end point of the rake. Alternatively, a string
            representation of the node selected in the viewport.
        path
            APath object that specifies the rake.

        Returns
        -------
        Stream
            A Stream object.
        """
        ...
