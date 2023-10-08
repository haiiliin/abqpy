from abqpy.decorators import abaqus_class_doc


@abaqus_class_doc
class Transform:
    """The MakeSketchTransform method creates a Transform object. The Transform object has no direct
    constructor. A Transform object is a 4x3 matrix of Floats that represents the transformation from sketch
    coordinates to assembly coordinates or to part coordinates.

    .. note::
        This object can be accessed by::

            import part
            import assembly
    """

    def matrix(self):
        """This method returns the transformation matrix as a tuple of 12 Floats.

        Returns
        -------
        tuple[float, float, float, float, float, float, float, float, float, float, float, float]
            A tuple of 12 Floats.
        """
        ...
